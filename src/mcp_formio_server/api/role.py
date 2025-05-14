from api.common import safe_request


async def get_roles(base_url: str, token: str) -> dict:
    """
    Retrieve a list of roles from the FormIO API.

    Args:
        base_url (str): The base URL of the FormIO API.
        token (str): The JWT token for authentication.

    Returns:
        dict: A dictionary containing the list of roles.
    """
    url = f"{base_url}/role"
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    data, _ = await safe_request("GET", url, headers=headers)
    return data


async def post_role(
    base_url: str, role_info: dict, token: str
) -> dict:
    """
    Create a new role in the FormIO API.

    Args:
        base_url (str): The base URL of the FormIO API.
        role_info (dict): A dictionary containing the role information.
        token (str): The JWT token for authentication.

    Returns:
        dict: A dictionary containing the created role data.
    """
    url = f"{base_url}/role"
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    data, _ = await safe_request("POST", url, json=role_info, headers=headers)
    return data


async def update_role(
    base_url: str, role_id: str, role_info: dict, token: str
) -> dict:
    """
    Update an existing role in the FormIO API.

    Args:
        base_url (str): The base URL of the FormIO API.
        role_id (str): The ID of the role to update.
        role_info (dict): A dictionary containing the updated role information.
        token (str): The JWT token for authentication.

    Returns:
        dict: A dictionary containing the updated role data.
    """
    url = f"{base_url}/role/{role_id}"
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    data, _ = await safe_request("PUT", url, json=role_info, headers=headers)
    return data
        