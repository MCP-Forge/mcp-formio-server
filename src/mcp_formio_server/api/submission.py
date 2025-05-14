from api.common import safe_request


async def get_submission(
    base_url: str, form_id: str, submission_id: str, token: str
) -> dict:
    """
    Retrieve a specific submission from the FormIO API.

    Args:
        base_url (str): The base URL of the FormIO API.
        form_id (str): The ID of the form to which the submission belongs.
        submission_id (str): The ID of the submission to retrieve.
        token (str): The JWT token for authentication.

    Returns:
        dict: A dictionary containing the submission data.
    """
    url = f"{base_url}/form/{form_id}/submission/{submission_id}"
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    data, _ = await safe_request("GET", url, headers=headers)
    return data


async def get_form_submissions(
    base_url: str, form_id: str, limit: int, skip: int, token: str
) -> dict:
    """
    Retrieve a paginated list of submissions for a specific form from the FormIO API.

    Args:
        base_url (str): The base URL of the FormIO API.
        form_id (str): The ID of the form to which the submissions belong.
        limit (int): The maximum number of submissions to return.
        skip (int): The number of submissions to skip (offset).
        token (str): The JWT token for authentication.

    Returns:
        dict: A dictionary containing the list of submissions and the total count.
    """
    url = f"{base_url}/form/{form_id}/submission"
    params = {
        "limit": limit,
        "skip": skip,
    }
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    data, headers = await safe_request("GET", url, params=params, headers=headers)
    content_range = headers.get("Content-Range")
    total = content_range.split("/")[-1] if content_range else None
    data["total"] = total
    return data


async def post_submission(base_url: str, form_id: str, form_info: dict, token: str) -> dict:
    """
    Submit a new submission to the FormIO API.  
    This function allows you to create a new submission for a specific form.
    Args:
        base_url (str): The base URL of the FormIO API.
        form_id (str): The ID of the form to which the submission belongs.
        form_info (dict): The data for the new submission.
        token (str): The JWT token for authentication.
    Returns:
        dict: A dictionary containing the created submission data.
    """

    url = f"{base_url}/form/{form_id}/submission"
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    post_data = {
        "data": form_info,
    }
    data, _ = await safe_request("POST", url, json=post_data, headers=headers)
    return data


async def validate_submission(
    base_url: str, form_id: str, submission_id: str, token: str
) -> dict:
    """
    Validate a specific submission in the FormIO API.

    Args:
        base_url (str): The base URL of the FormIO API.
        form_id (str): The ID of the form to which the submission belongs.
        submission_id (str): The ID of the submission to validate.
        token (str): The JWT token for authentication.

    Returns:
        dict: A dictionary containing the validation result.
    """
    url = f"{base_url}/form/{form_id}/submission/{submission_id}/validate"
    headers = {
        "Content-Type": "application/json",
        "x-jwt-token": token,
    }
    data, _ = await safe_request("POST", url, headers=headers)
    return data
