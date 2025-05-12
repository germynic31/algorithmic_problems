DEFAULT_MAX_USERS = 10


def validate_and_normalize(conf: dict):
    required_fields = ["app_name", "debug_mode", "allowed_origins"]
    for field in required_fields:
        if field not in conf:
            raise ValueError(f"Missing required field: {field}")

    result = conf.copy()

    result["app_name"] = str(conf["app_name"]).strip()
    if not result["app_name"]:
        raise ValueError("app_name cannot be empty")

    debug_mode = conf["debug_mode"]
    if isinstance(debug_mode, str):
        result["debug_mode"] = debug_mode.lower() == 'true'
    elif isinstance(debug_mode, bool):
        result["debug_mode"] = debug_mode
    else:
        raise ValueError("debug_mode must be string or boolean")

    max_users = conf.get("max_users", 10)
    try:
        max_users = int(max_users)
        if max_users <= 0:
            raise ValueError("max_users must be positive")
        result["max_users"] = max_users
    except (ValueError, TypeError):
        raise ValueError("max_users must be a positive integer")

    if not isinstance(conf["allowed_origins"], list):
        raise ValueError("allowed_origins must be a list")

    origins = []
    for origin in conf["allowed_origins"]:
        try:
            origins.append(str(origin).lower())
        except (TypeError, ValueError):
            raise ValueError("All origins must be strings")

    result["allowed_origins"] = list(set(origins))

    return result


def test_validate_and_normalize():
    input_conf = {
        "app_name": "  MyApp  ",
        "debug_mode": "true",
        "allowed_origins": [
            "HTTP://API.COM", "http://test.com", "http://api.com"
            ]
    }
    result = validate_and_normalize(input_conf)
    expected_result = {
        "app_name": "MyApp",
        "debug_mode": True,
        "max_users": 10,
        "allowed_origins": ["http://api.com", "http://test.com"]
    }
    assert result == expected_result, result


test_validate_and_normalize()
