from typing import Union, Any

from mcp.server.fastmcp import Context
from mcp.types import CallToolResult, TextContent

from mcp_formio_server.config import mcp, AppContext
from mcp_formio_server.exceptions import FormIOAPIException
from mcp_formio_server.api.form import get_forms, post_form
from mcp_formio_server.api.authentication import admin_login, user_login, register_user
from mcp_formio_server.api.submission import get_form_submissions, post_submission, get_submission
from mcp_formio_server.api.role import get_roles, post_role, update_role


@mcp.tool()
async def create_role(
    role_info: dict, token: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Create a new role in the FormIO system.

    This function allows you to create a new role by providing a JSON structure
    that defines the role's properties and permissions. The JSON structure is sent
    to the FormIO API which then creates and stores the role.

    Args:
        role_info (dict): The role definition in JSON format.
        token (str): The JWT token for authentication.

    Returns:
        Union[dict, CallToolResult]: The created role object on success,
        or a CallToolResult describing the error.
    """
    base_url = ctx.request_context.lifespan_context.formio_url

    try:
        data = await post_role(base_url, role_info, token)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def update_existing_role(
    role_id: str, role_info: dict, token: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Update an existing role in the FormIO system.

    This function allows you to update an existing role by providing the role ID
    and a JSON structure that defines the updated properties and permissions.
    The JSON structure is sent to the FormIO API which then updates the role.

    Args:
        role_id (str): The ID of the role to update.
        role_info (dict): The updated role definition in JSON format.
        token (str): The JWT token for authentication.

    Returns:
        Union[dict, CallToolResult]: The updated role object on success,
        or a CallToolResult describing the error.
    """
    base_url = ctx.request_context.lifespan_context.formio_url

    try:
        data = await update_role(base_url, role_id, role_info, token)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def get_roles_list(
    token: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Retrieve a list of roles from the FormIO API.

    This function fetches the roles available in the FormIO system. Roles are
    used to manage permissions and access control for users and groups within
    the FormIO platform.

    Args:
        token (str): The JWT token for authentication.

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the list of roles,
        or a CallToolResult if the request failed.
    """
    base_url = ctx.request_context.lifespan_context.formio_url

    try:
        data = await get_roles(base_url, token)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def create_form_submission(
    form_id: str, data: dict, token: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Create a new submission for a specific form in the FormIO system.

    This function allows you to create a submission by providing the form ID and
    the data to be submitted. The data should match the structure defined in the
    form's schema. The submission will be stored in the FormIO system.

    Args:
        form_id (str): The ID of the form to which the submission belongs.
        data (dict): The submission data in JSON format.
        token (str): The JWT token for authentication.

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the created submission,
        or a CallToolResult if the request failed.
    """
    base_url = ctx.request_context.lifespan_context.formio_url

    try:
        data = await post_submission(base_url, form_id, data, token)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def load_form_submission(
    form_id: str, submission_id: str, token: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Retrieve a specific submission from the FormIO API.

    This function allows you to fetch a specific submission for a given form by
    providing the form ID and submission ID. The retrieved submission data can
    be used for various purposes, such as displaying or processing the submitted
    information.

    Args:
        form_id (str): The ID of the form to which the submission belongs.
        submission_id (str): The ID of the submission to retrieve.
        token (str): The JWT token for authentication.

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the submission data,
        or a CallToolResult if the request failed.
    """
    base_url = ctx.request_context.lifespan_context.formio_url

    try:
        data = await get_submission(base_url, form_id, submission_id, token)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def get_paginated_form_submissions(
    form_id: str, limit: int, skip: int, token: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Retrieve a paginated list of submissions for a specific form from the FormIO API.

    This function allows you to fetch submissions for a specific form with pagination
    support. You can specify how many submissions to retrieve and how many to skip,
    which is useful for implementing paginated listings or navigating through large
    collections of submissions.

    Args:
        form_id (str): The ID of the form to which the submissions belong.
        limit (int): The maximum number of submissions to return.
        skip (int): The number of submissions to skip (offset).
        token (str): The JWT token for authentication.

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the list of submissions and the total count,
        or a CallToolResult if the request failed.
    """
    base_url = ctx.request_context.lifespan_context.formio_url

    try:
        data = await get_form_submissions(base_url, form_id, limit, skip, token)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def create_user(
    email: str, password: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Register a new user in the FormIO system.

    This function allows you to create a new user by providing an email and password.
    The user will be registered in the FormIO system and can then log in using the
    provided credentials.

    Args:
        email (str): The email for the new user.
        password (str): The password for the new user.

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the user information and JWT token,
        or a CallToolResult if the request failed.
    """
    base_url = ctx.request_context.lifespan_context.formio_url
    try:
        data = await register_user(base_url, email, password)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def authenticate_user(
    email: str, password: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Authenticate an user and retrieve a JWT token.

    This function sends a login request to the FormIO API and retrieves a JWT token
    for subsequent authenticated requests. The token is essential for accessing
    protected resources in the FormIO system.

    Args:
        email (str): The email for authentication.
        password (str): The password for authentication.

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the JWT token and user information,
        or a CallToolResult if the request failed.
    """
    base_url = ctx.request_context.lifespan_context.formio_url
    try:
        token = await user_login(base_url, email, password)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return token


@mcp.tool()
async def authenticate_admin(
    email: str, password: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Authenticate an admin and retrieve a JWT token.

    This function sends a login request to the FormIO API and retrieves a JWT token
    for subsequent authenticated requests. The token is essential for accessing
    protected resources in the FormIO system.

    Args:
        email (str): The email for authentication.
        password (str): The password for authentication.

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the JWT token and user information,
        or a CallToolResult if the request failed.
    """
    base_url = ctx.request_context.lifespan_context.formio_url
    try:
        token = await admin_login(base_url, email, password)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return token


@mcp.tool()
async def get_paginated_forms(
    limit: int, skip: int, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Retrieve a paginated list of forms from the FormIO API.
    This function fetches forms with pagination support, allowing you to specify
    how many forms to retrieve and how many to skip, which is useful for implementing
    paginated listings or navigating through large collections of forms.
    Args:
        limit (int): The maximum number of forms to return.
        skip (int): The number of forms to skip (offset).

    Returns:
        Union[dict, CallToolResult]: A dictionary containing the list of forms and the total count,
        or a CallToolResult describing the error.
    """
    api_url = ctx.request_context.lifespan_context.formio_url

    try:
        data = await get_forms(api_url, limit, skip)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return data


@mcp.tool()
async def create_form(
    data: dict, token: str, ctx: Context[Any, AppContext]
) -> Union[dict, CallToolResult]:
    """
    Create a new form in the FormIO system.

    This function allows you to create a form by providing a JSON structure that defines
    the form's components, layout, validation rules, and other properties. The JSON structure
    is sent to the FormIO API which then creates and stores the form.

    Args:
        data (dict): The form definition in JSON format, including components like:
            - Input fields (text, email, number, etc.)
            - Layout elements (columns, panels, tabs)
            - Validation rules
            - Submission settings
        token (str): The JWT token for authentication.

    Returns:
        Union[dict, CallToolResult]: The created form object on success,
        or a CallToolResult describing the error.
    """
    api_url = ctx.request_context.lifespan_context.formio_url

    try:
        form = await post_form(api_url, data, token)
    except FormIOAPIException as e:
        return CallToolResult(
            isError=True,
            content=[
                TextContent(type="text", text=f"FormIOAPIException API Error: {e}")
            ],
        )

    return form


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
