from typing import Any

from httpx import AsyncClient, HTTPStatusError, RequestError

from exceptions import FormIOAPIException


async def safe_request(
    method: str,
    url: str,
    **kwargs: dict,
) -> tuple[Any, dict]:
    async with AsyncClient() as client:
        try:
            if method == "GET":
                response = await client.get(url, **kwargs)
            elif method == "POST":
                response = await client.post(url, **kwargs)
            else:
                raise ValueError(f"Unsupported method: {method}")

            response.raise_for_status()
            return response.json(), response.headers

        except HTTPStatusError as e:
            raise FormIOAPIException(
                f"API error {e.response.status_code} at {url}: {e.response.text}"
            ) from e

        except RequestError as e:
            raise FormIOAPIException(
                f"Network error during request to {url}: {str(e)}"
            ) from e

        except Exception as e:
            raise FormIOAPIException(
                f"Unexpected error during request to {url}: {str(e)}"
            ) from e
