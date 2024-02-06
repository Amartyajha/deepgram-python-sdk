# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

import json

import httpx

from ..options import DeepgramClientOptions
from .errors import DeepgramApiError, DeepgramError, DeepgramUnknownApiError
from .helpers import append_query_params


class AbstractSyncRestClient:
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
            - Check if the provided config is not None.
            - If config is None, raise a DeepgramError.
            - Set the config attribute of the DeepgramClient object to the provided config.
        """"
        
        if config is None:
            raise DeepgramError("Config are required")
        self.config = config

    def get(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Returns a response from a GET request to the specified URL with optional parameters and addons.
        Parameters:
            - url (str): The URL to make the GET request to.
            - options (dict): Optional parameters to include in the request.
            - addons (dict): Optional addons to include in the request.
            - timeout (int): Optional timeout for the request.
            - **kwargs: Optional keyword arguments to include in the request.
        Returns:
            - Response: The response from the GET request.
        Processing Logic:
            - Makes a GET request to the specified URL.
            - Includes optional parameters and addons in the request.
            - Uses the specified timeout for the request.
            - Includes any additional keyword arguments in the request."""
        
        return self._handle_request(
            "GET",
            url,
            params=options,
            addons=addons,
            headers=self.config.headers,
            timeout=timeout,
            **kwargs,
        )

    def post(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """"Send a POST request to the specified URL with optional parameters and addons. Returns the response from the request.
        Parameters:
            - url (str): The URL to send the request to.
            - options (dict): Optional parameters to include in the request.
            - addons (dict): Optional addons to include in the request.
            - timeout (int): Optional timeout for the request in seconds.
            - **kwargs: Additional keyword arguments to be passed to the request.
        Returns:
            - Response: The response from the request.
        Processing Logic:
            - Send a POST request with optional parameters and addons.
            - Use the specified URL and headers from the config.
            - Include an optional timeout for the request.
            - Additional keyword arguments can be passed to the request.
        Example:
            response = post("https://example.com/api", options={"key": "value"}, timeout=10)
            print(response.status_code) # prints the status code of the response."""
        
        return self._handle_request(
            "POST",
            url,
            params=options,
            addons=addons,
            headers=self.config.headers,
            timeout=timeout,
            **kwargs,
        )

    def put(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Sends a PUT request to the specified URL with optional parameters and addons.
        Parameters:
            - url (str): The URL to send the request to.
            - options (dict): Optional parameters to include in the request.
            - addons (dict): Optional addons to include in the request.
            - timeout (int): Optional timeout for the request in seconds.
            - **kwargs: Additional keyword arguments to be passed to the request.
        Returns:
            - dict: The response from the request.
        Processing Logic:
            - Uses the _handle_request method to handle the request.
            - Adds the headers from the config to the request.
            - Includes any additional keyword arguments in the request.
            - Returns the response from the request.
        Example:
            put("https://www.example.com/api", options={"param1": "value1", "param2": "value2"}, addons={"addon1": "value1"}, timeout=10, data={"key": "value"})
            # Sends a PUT request to https://www.example.com/api with parameters "param1" and "param2", addons "addon1", and a timeout of 10 seconds. Additional data is included in the request."""
        
        return self._handle_request(
            "PUT",
            url,
            params=options,
            addons=addons,
            headers=self.config.headers,
            timeout=timeout,
            **kwargs,
        )

    def patch(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Sends a PATCH request to the specified URL with optional parameters and addons.
        Parameters:
            - url (str): The URL to send the request to.
            - options (dict): Optional parameters to include in the request.
            - addons (dict): Optional addons to include in the request.
            - timeout (int): Optional timeout for the request in seconds.
            - **kwargs: Additional keyword arguments to pass to the request.
        Returns:
            - Response: The response from the PATCH request.
        Processing Logic:
            - Sends a PATCH request using the _handle_request method.
            - Includes the specified URL and optional parameters and addons.
            - Uses the config headers and optional timeout.
            - Additional keyword arguments can be passed in.
            - Returns the response from the PATCH request.
        Example:
            response = patch("https://example.com/api", options={"key": "value"}, timeout=10)
            print(response.status_code)
            # Output: 200"""
        
        return self._handle_request(
            "PATCH",
            url,
            params=options,
            addons=addons,
            headers=self.config.headers,
            timeout=timeout,
            **kwargs,
        )

    def delete(self, url: str, options=None, addons=None, timeout=None, **kwargs):
        """Deletes data from a specified URL.
        Parameters:
            - url (str): The URL to send the DELETE request to.
            - options (dict): Optional parameters to be included in the request.
            - addons (dict): Optional add-ons to be included in the request.
            - timeout (int): Optional timeout value for the request.
            - **kwargs: Additional keyword arguments to be passed to the request.
        Returns:
            - response (dict): A dictionary containing the response from the DELETE request.
        Processing Logic:
            - Sends a DELETE request to the specified URL.
            - Includes any optional parameters and add-ons in the request.
            - Uses the specified timeout value, if provided.
            - Any additional keyword arguments are passed to the request."""
        
        return self._handle_request(
            "DELETE",
            url,
            params=options,
            addons=addons,
            headers=self.config.headers,
            timeout=timeout,
            **kwargs,
        )

    def _handle_request(self, method, url, params, addons, headers, timeout, **kwargs):
        """"""
        
        new_url = url
        if params is not None:
            new_url = append_query_params(new_url, params)
        if addons is not None:
            new_url = append_query_params(new_url, addons)

        if timeout is None:
            timeout = httpx.Timeout(30.0, connect=10.0)

        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.request(method, new_url, headers=headers, **kwargs)
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
