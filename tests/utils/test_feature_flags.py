from unittest import mock

import pytest

from app.utils.feature_flags import (feature_flag, get_flag_status,
                                     get_return_value)
from tests.conftest import override_get_settings


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


@pytest.mark.parametrize("test_input,expected", [
    ('flag_is_disabled', False),
    ('flag_does_not_exist', False),
    ("flag_is_enabled", True)
])
def test__get_flag_status(test_input, expected):
    with mock.patch('app.dependencies.get_settings') as settings_mock:
        settings_mock.return_value = override_get_settings()

        from app.dependencies import get_settings

        flag_enabled = get_flag_status(test_input)

        get_settings.assert_called_once()

        assert flag_enabled == expected


@feature_flag("is_enabled")
def enabled_feature():
    return "This feature is enabled"


@feature_flag("is_disabled")
def disabled_feature():
    return "This feature is disabled"


@feature_flag("does_not_exist")
def undefined_feature():
    return "This feature flag is not defined"


@feature_flag("is_disabled")
def disabled_feature_typed() -> str:
    return "This feature is disabled and typed"


@feature_flag("is_disabled", int)
def disabled_feature_typed_override() -> str:
    return "egal"


@pytest.mark.parametrize("test_input,expected", [
    ("enabled_feature", "This feature is enabled"),
    ("disabled_feature", None),
    ("undefined_feature", None),
    ("disabled_feature_typed", str),
    ("disabled_feature_typed_override", int)
])
def test__feature_flag_decorator(test_input, expected):
    with mock.patch('app.dependencies.get_settings') as settings_mock:
        settings_mock.return_value = override_get_settings()

        from app.dependencies import get_settings

        return_value = eval(test_input)()

        get_settings.assert_called_once()

        assert return_value == expected
