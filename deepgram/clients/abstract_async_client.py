# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

import json

import httpx

from ..options import DeepgramClientOptions
from .errors import DeepgramApiError, DeepgramError, DeepgramUnknownApiError
from .helpers import append_query_params


class AbstractAsyncRestClient:
    """
    An abstract base class for a RESTful HTTP client.

    This class provides common HTTP methods (GET, POST, PUT, PATCH, DELETE) for making asynchronous HTTP requests.
    It handles error responses and provides basic JSON parsing.

    Args:
        url (Dict[str, str]): The base URL for the RESTful API, including any path segments.
        headers (Optional[Dict[str, Any]]): Optional HTTP headers to include in requests.
        params (Optional[Dict[str, Any]]): Optional query parameters to include in requests.
        timeout (Optional[httpx.Timeout]): Optional timeout configuration for requests.

    Exceptions:
        DeepgramApiError: Raised for known API errors.
        DeepgramUnknownApiError: Raised for unknown API errors.
    """

    def __init__(self, config: DeepgramClientOptions):
        """"Initializes a DeepgramClient object with the provided configuration options.
        Parameters:
            - config (DeepgramClientOptions): An object containing the configuration options for the DeepgramClient.
        Returns:
            - None: This function does not return any value.
        Processing Logic:
            - Checks if the provided configuration options are not None.
            - Raises a DeepgramError if the configuration options are None.
            - Sets the config attribute of the DeepgramClient object to the provided configuration options.""""
        
        if config is None:
            raise DeepgramError("Config are required")
        self.config = config

    async def get(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Gets data from a specified URL using a GET request.
        Parameters:
            - url (str): The URL to make the GET request to.
            - options (dict): Optional parameters to include in the request.
            - addons (dict): Optional add-ons to include in the request.
            - timeout (int): Optional timeout for the request.
            - **kwargs: Optional keyword arguments to include in the request.
        Returns:
            - dict: The response data from the GET request.
        Processing Logic:
            - Makes a GET request to the specified URL.
            - Includes any optional parameters and add-ons in the request.
            - Sets a timeout for the request if specified.
            - Uses the headers from the config file for the request."""
        
        return await self._handle_request(
            "GET",
            url,
            params=options,
            addons=addons,
            timeout=timeout,
            headers=self.config.headers,
            **kwargs,
        )

    async def post(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Sends a POST request to the specified URL.
        Parameters:
            - url (str): The URL to send the request to.
            - options (dict): Optional. Additional parameters to include in the request.
            - addons (dict): Optional. Additional headers or options to include in the request.
            - timeout (int): Optional. The timeout in seconds for the request.
            - **kwargs: Optional. Additional keyword arguments to include in the request.
        Returns:
            - type: The response from the request.
        Processing Logic:
            - Sends a POST request using the specified URL.
            - Includes any additional parameters or headers specified in the options or addons parameters.
            - Sets a timeout for the request if specified.
            - Any additional keyword arguments are included in the request."""
        
        return await self._handle_request(
            "POST",
            url,
            params=options,
            addons=addons,
            timeout=timeout,
            headers=self.config.headers,
            **kwargs,
        )

    async def put(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Sends a PUT request to the specified URL with optional parameters and addons.
        Parameters:
            - url (str): The URL to send the request to.
            - options (dict): Optional parameters to include in the request.
            - addons (dict): Optional addons to include in the request.
            - timeout (int): Optional timeout for the request in seconds.
            - **kwargs: Additional keyword arguments to be passed to the request.
        Returns:
            - response (dict): The response from the request in JSON format.
        Processing Logic:
            - Sends a PUT request using the aiohttp library.
            - Adds the specified parameters and addons to the request.
            - Sets a timeout for the request if specified.
            - Uses the config headers for the request.
            - Returns the response in JSON format.
        Example:
            response = await put("https://example.com/api", options={"param1": "value1"}, addons={"addon1": "value1"}, timeout=10)
            print(response)
            # Output: {"status": 200, "message": "Success"}"""
        
        return await self._handle_request(
            "PUT",
            url,
            params=options,
            addons=addons,
            timeout=timeout,
            headers=self.config.headers,
            **kwargs,
        )

    async def patch(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """"Sends a PATCH request to the specified URL with optional parameters and addons, and returns the response."
        Parameters:
            - url (str): The URL to send the request to.
            - options (dict): Optional parameters to include in the request.
            - addons (dict): Optional addons to include in the request.
            - timeout (int): Optional timeout for the request.
            - **kwargs: Additional keyword arguments to be passed to the request.
        Returns:
            - Response: The response from the PATCH request.
        Processing Logic:
            - Uses the _handle_request method to handle the request.
            - Includes the PATCH method, URL, and optional parameters and addons.
            - Uses the config headers for the request.
            - Additional keyword arguments can be passed to the request."""
        
        return await self._handle_request(
            "PATCH",
            url,
            params=options,
            addons=addons,
            timeout=timeout,
            headers=self.config.headers,
            **kwargs,
        )

    async def delete(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Deletes data from a specified URL.
        Parameters:
            - url (str): The URL from which data will be deleted.
            - options (dict): Optional parameters to be passed in the request.
            - addons (dict): Optional additional parameters to be passed in the request.
            - timeout (int): Optional timeout for the request in seconds.
            - **kwargs: Optional keyword arguments to be passed in the request.
        Returns:
            - dict: A dictionary containing the response from the request.
        Processing Logic:
            - Makes a DELETE request to the specified URL.
            - Uses optional parameters and headers from the config.
            - Can also accept additional keyword arguments.
            - Returns a dictionary with the response data."""
        
        return await self._handle_request(
            "DELETE",
            url,
            params=options,
            addons=addons,
            timeout=timeout,
            headers=self.config.headers,
            **kwargs,
        )

    async def _handle_request(
        self, method, url, params, addons, timeout, headers, **kwargs
    ):
        """ DeepgramUnknownApiError(str(e), 500) from e
        This function handles an HTTP request to the specified URL with the given parameters, addons, timeout, and headers. It uses the httpx library to make the request and returns the response text. If an error occurs, it raises a DeepgramApiError or DeepgramUnknownApiError depending on the type of error.
        Parameters:
            - method (str): The HTTP method to use for the request.
            - url (str): The URL to make the request to.
            - params (dict): Optional query parameters to append to the URL.
            - addons (dict): Optional query parameters to append to the URL.
            - timeout (float): Optional timeout for the request in seconds.
            - headers (dict): Optional headers to include in the request.
            - **kwargs: Optional keyword arguments to pass to the httpx request.
        Returns:
            - str: The response text from the HTTP request.
        Processing Logic:
            - Appends query parameters to the URL if provided.
            - Sets a default timeout of 30 seconds for the request.
            - Uses the httpx library to make the request.
            - Handles HTTP errors and raises appropriate DeepgramApiError or DeepgramUnknownApiError.
            - If an unknown error occurs, raises a DeepgramUnknownApiError with a status code of 500."""
        
        new_url = url
        if params is not None:
            new_url = append_query_params(new_url, params)
        if addons is not None:
            new_url = append_query_params(new_url, addons)

        if timeout is None:
            timeout = httpx.Timeout(30.0, connect=10.0)

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.request(
                    method, new_url, headers=headers, **kwargs
                )
                response.raise_for_status()
                return response.text
        except httpx._exceptions.HTTPError as e:
            if isinstance(e, httpx.HTTPStatusError):
                status_code = e.response.status_code or 500
                try:
                    json_object = json.loads(e.response.text)
                    raise DeepgramApiError(
                        json_object.get("err_msg"), status_code, json.dumps(json_object)
                    ) from e
                except json.decoder.JSONDecodeError:
                    raise DeepgramUnknownApiError(e.response.text, status_code) from e
                except ValueError as e:
                    raise DeepgramUnknownApiError(e.response.text, status_code) from e
            else:
                raise
        except Exception as e:
            raise
