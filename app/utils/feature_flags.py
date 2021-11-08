from functools import wraps
import logging
from typing import Any, get_type_hints

from app.dependencies import get_settings

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

        @wraps(func)
        def wrapper(*args, **kwargs):
            settings = get_settings()
            settings_var = f"flag_{flag_name}"

            return_val = get_return_value(func, disabled_return_val)

            try:
                flag_enabled = settings.dict()[settings_var]
            except KeyError:
                logger.debug(
                    f"Feature flag {flag_name} is not defined in settings"
                    )
                flag_enabled = False
            
            if flag_enabled:
                logger.info(f"Feature flag {flag_name} is enabled")
                return func(*args, **kwargs)
            else:
                logger.info(f"Feature flag {flag_name} is disabled")
                return return_val

        return wrapper

    return feature_flag_decorator


def get_return_value(func, override_return_value):
    if override_return_value:

        type_hints  = get_type_hints(func)

        if 'return' in type_hints:
            return type_hints['return']
        else:
            return None

def get_flag_status(flag_name):
    