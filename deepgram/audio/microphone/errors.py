# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT


# exceptions for microphone
class DeepgramMicrophoneError(Exception):
    """
    Exception raised for known errors related to Microphone library.

    Attributes:
        message (str): The error message describing the exception.
    """

    def __init__(self, message: str):
        """"Initializes a DeepgramMicrophoneError object with the given message.
        Parameters:
            - message (str): The error message to be stored in the object.
        Returns:
            - None: This function does not return any value.
        Processing Logic:
            - Set the name of the object to "DeepgramMicrophoneError".
            - Store the given message in the object.
            - This function is used to create a custom error object for DeepgramMicrophone errors.""""
        
        super().__init__(message)
        self.name = "DeepgramMicrophoneError"
        self.message = message

    def __str__(self):
        """This function returns a string representation of the object, containing the name and message attributes.
        Parameters:
            - self (object): The object to be converted to a string.
        Returns:
            - str: A string representation of the object, containing the name and message attributes.
        Processing Logic:
            - Concatenates the name and message attributes.
            - Uses f-strings for string formatting."""
        
        return f"{self.name}: {self.message}"
