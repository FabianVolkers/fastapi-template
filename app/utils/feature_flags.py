import logging
from functools import wraps
from typing import Any, get_type_hints

from app.config import Settings

logger = logging.getLogger(__name__)


def feature_flag(
    flag_name: str,
    disabled_return_val: Any = "no_override_passed"
):
    """Toggles the decorated function on or off depending on settings.

    Arguments:
    flag_name -- the feature flag name as defined in config.py without the
    'flag_'
    disabled_return_val -- the value returned by the function when disabled
    (default return value type hint | None)
    """
    def feature_flag_decorator(func):
        logger.debug(f"Evalutating feature flag {flag_name} for {func}")

        @wraps(func)
        def wrapper(*args, **kwargs):

            settings_var = f"flag_{flag_name}"

            return_val = get_return_value(func, disabled_return_val)

            flag_enabled = get_flag_status(settings_var)

            if flag_enabled:
                logger.info(f"Feature flag {flag_name} is enabled")
                return func(*args, **kwargs)
            else:
                logger.info(f"Feature flag {flag_name} is disabled")
                return return_val

        return wrapper

    return feature_flag_decorator


def get_return_value(func, override_return_value="no_override_passed"):
    if override_return_value == "no_override_passed":

        type_hints = get_type_hints(func)

        if 'return' in type_hints:
            return type_hints['return']
        else:
            return None

    else:
        return override_return_value


# def get_flag_status(flag_name: str, settings: Settings = get_settings())
# -> bool:
def get_flag_status(flag_name: str) -> bool:
    from app.dependencies import get_settings
    settings = get_settings()
    if flag_name in settings.dict():
        return settings.dict()[flag_name]
    else:
        logger.debug(
            f"Feature flag {flag_name} is not defined in settings"
        )
        return False
