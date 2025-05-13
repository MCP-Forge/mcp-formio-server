from api.common import safe_request


async def admin_login(
    base_url: str, email: str, password: str
) -> dict:
    """
    Authenticate an admin and retrieve a JWT token.

    Args:
        base_url (str): The base URL of the FormIO API.
        email (str): The email for authentication.
        password (str): The password for authentication.

    Returns:
        dict: A dictionary containing the JWT token and user information.
    """
    url = f"{base_url}/admin/login"
    data = {
        "data": {
            "email": email,
            "password": password,
        }
    }
    data, headers = await safe_request("POST", url, json=data)
    token = headers.get("x-jwt-token")
    data["token"] = token
    return data


async def user_login(
    base_url: str, email: str, password: str
) -> dict:
    """
    Authenticate a user and retrieve a JWT token.

    Args:
        base_url (str): The base URL of the FormIO API.
        email (str): The email for authentication.
        password (str): The password for authentication.

    Returns:
        dict: A dictionary containing the JWT token and user information.
    """
    url = f"{base_url}/user/login"
    data = {
        "data": {
            "email": email,
            "password": password,
        }
    }
    data, headers = await safe_request("POST", url, json=data)
    token = headers.get("x-jwt-token")
    data["token"] = token
    return data


async def register_user(
    base_url: str, email: str, password: str
) -> dict:
    """
    Register a new user and retrieve a JWT token.

    Args:
        base_url (str): The base URL of the FormIO API.
        email (str): The email for authentication.
        password (str): The password for authentication.

    Returns:
        dict: A dictionary containing the JWT token and user information.
    """
    url = f"{base_url}/user/register"
    data = {
        "data": {
            "email": email,
            "password": password,
        }
    }
    data, headers = await safe_request("POST", url, json=data)
    token = headers.get("x-jwt-token")
    data["token"] = token
    return data
