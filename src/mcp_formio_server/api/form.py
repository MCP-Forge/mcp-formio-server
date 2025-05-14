from mcp_formio_server.api.common import safe_request


async def get_forms(base_url: str, limit: int, skip: int) -> dict:
    """
    Retrieve a paginated list of forms from the FormIO API.
    This function fetches forms with pagination support, allowing you to specify
    how many forms to retrieve and how many to skip, which is useful for implementing
    paginated listings or navigating through large collections of forms.
    Args:
        base_url (str): The base URL of the FormIO API.
        limit (int): The maximum number of forms to return.
        skip (int): The number of forms to skip (offset).
    Returns:
        dict: A dictionary containing the list of forms and the total count.
    """

    url = f"{base_url}/form"
    params = {
        "type": "form",
        "limit": limit,
        "skip": skip,
    }
    forms, headers = await safe_request("GET", url, params=params)
    content_range = headers.get("Content-Range")
    total = content_range.split("/")[-1] if content_range else None
    data = {
        "forms": forms,
        "total": total,
    }
    return data


async def post_form(base_url: str, data: dict, token: str):
    url = f"{base_url}/form"
    params = {"type": "form"}
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    data, _ = await safe_request("POST", url, json=data, params=params, headers=headers)
    return data
