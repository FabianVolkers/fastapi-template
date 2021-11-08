import pytest
from app.config import TestSettings as _TestSettings

from app.utils.feature_flags import (
    feature_flag, get_flag_status, get_return_value
)


def func_a(a):
    return a


def func_b(b: str) -> str:
    return b


@pytest.mark.parametrize("test_input,expected", [
    ({"f": "func_a"}, None),
    ({"f": "func_b"}, str),
    ({"f": "func_b", "o": int}, int)
])
def test__get_return_value(test_input, expected):
    if "o" in test_input:
        return_type = get_return_value(eval(test_input["f"]), test_input["o"])
    else:
        return_type = get_return_value(eval(test_input["f"]))

    assert return_type == expected


@pytest.fixture
def override_get_feature_flag_settings():
    class _TestFeatureFlagSettings(_TestSettings):
        flag_is_enabled: bool = True
        flag_is_disabled: bool = False
    settings = _TestFeatureFlagSettings()
    return settings


@pytest.mark.parametrize("test_input,expected", [
    ('flag_is_disabled', False),
    ('flag_does_not_exist', False),
    ("flag_is_enabled", True)
])
def test__get_flag_status(test_input, expected, override_get_feature_flag_settings):
    flag_enabled = get_flag_status(test_input, override_get_feature_flag_settings)

    assert flag_enabled == expected
