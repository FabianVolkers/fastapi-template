from app.utils.feature_flags import feature_flag, get_flag_status, get_return_value


def test__get_return_value_no_type():
    def func(a):
        return a

    return_type = get_return_value(func)

    assert return_type is None


def test__get_return_value_with_type():
    def func(a: str) -> str:
        return a

    return_type = get_return_value(func)

    assert return_type == str


def test__get_return_value_with_override():
    def func(a: str) -> str:
        return a

    return_type = get_return_value(func, int)

    assert return_type == int
