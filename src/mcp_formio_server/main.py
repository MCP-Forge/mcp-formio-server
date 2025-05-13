from typing import Union, Any

from mcp.server.fastmcp import Context
from mcp.types import CallToolResult, TextContent

from config import mcp, AppContext
from exceptions import FormIOAPIException
from api.form import get_forms, post_form
from api.authentication import admin_login, user_login, register_user


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
