import pytest

from app.utils.feature_flags import feature_flag, get_flag_status, get_return_value


def func_a(a):
    return a


def func_b(b: str) -> str:
    return b


@pytest.mark.parametrize("test_input,expected", [
    ({"f" :"func_a"}, None), ({"f": "func_b"}, str), ({"f": "func_b", "o": int}, int)
])
def test__get_return_value(test_input, expected):
    if "o" in test_input:
        return_type = get_return_value(eval(test_input["f"]), test_input["o"])
    else:
        return_type = get_return_value(eval(test_input["f"]))

    assert return_type == expected
