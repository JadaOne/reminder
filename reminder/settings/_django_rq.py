from env_utils import get_bool, get_env, get_int  # noqa

RQ_QUEUES = {
    "default": {
        "HOST": get_env("RQ_HOST", "localhost"),
        "PORT": get_int("RQ_PORT", 6379),
        "DB": get_int("RQ_DB", 0),
        "PASSWORD": get_env("RQ_PASSWORD", ""),
        "DEFAULT_TIMEOUT": 360,
    },
    "high": {
        "HOST": get_env("RQ_HOST", "localhost"),
        "PORT": get_int("RQ_PORT", 6379),
        "DB": get_int("RQ_DB", 0),
        "PASSWORD": get_env("RQ_PASSWORD", ""),
        "DEFAULT_TIMEOUT": 360,
    },
    "low": {
        "HOST": get_env("RQ_HOST", "localhost"),
        "PORT": get_int("RQ_PORT", 6379),
        "DB": get_int("RQ_DB", 0),
        "PASSWORD": get_env("RQ_PASSWORD", ""),
        "DEFAULT_TIMEOUT": 360,
    },
}
