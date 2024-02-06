# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

import logging
import os
from importlib import import_module
from typing import Optional

import verboselogs

# manage client responses
# manage client classes/input
# read client responses
# analyze
# prerecorded client responses
# prerecorded
# live client responses
# live
# listen client
from .clients import (
    AnalyzeClient,
    AnalyzeOptions,
    AnalyzeResponse,
    AnalyzeSource,
    AnalyzeStreamSource,
    AsyncAnalyzeClient,
    AsyncAnalyzeResponse,
    AsyncLiveClient,
    AsyncManageClient,
    AsyncPreRecordedClient,
    AsyncPrerecordedResponse,
    Balance,
    BalancesResponse,
    BufferSource,
    ErrorResponse,
    FileSource,
    InviteOptions,
    InvitesResponse,
    Key,
    KeyOptions,
    KeyResponse,
    KeysResponse,
    Listen,
    LiveClient,
    LiveOptions,
    LiveResultResponse,
    LiveTranscriptionEvents,
    ManageClient,
    MembersResponse,
    Message,
    MetadataResponse,
    PreRecordedClient,
    PrerecordedOptions,
    PrerecordedResponse,
    PrerecordedSource,
    Project,
    ProjectOptions,
    ProjectsResponse,
    Read,
    ReadStreamSource,
    ScopeOptions,
    ScopesResponse,
    Sentiment,
    SpeechStartedResponse,
    SyncAnalyzeResponse,
    SyncPrerecordedResponse,
    TextSource,
    UrlSource,
    UsageFieldsOptions,
    UsageFieldsResponse,
    UsageRequest,
    UsageRequestOptions,
    UsageRequestsResponse,
    UsageSummaryOptions,
    UsageSummaryResponse,
    UtteranceEndResponse,
)

# on-prem
from .clients.onprem.client import OnPremClient
from .clients.onprem.v1.async_client import AsyncOnPremClient
from .errors import DeepgramApiKeyError, DeepgramModuleError
from .options import ClientOptionsFromEnv, DeepgramClientOptions


class Deepgram:
    def __init__(self, *anything):
        """Function:
        def __init__(self, *anything):
            Instantiates a Deepgram object.
            Parameters:
                - *anything (tuple): Tuple of arguments that will be passed to the Exception object.
            Returns:
                - None: This function does not return anything.
            Processing Logic:
                - Raises an Exception object with a fatal error message.
                - The error message explains that the Deepgram object is no longer a class in version 3 of the SDK.
                - Provides instructions on how to fix the issue.
                - Lists important considerations for updating to version 3 of the SDK."""
        
        raise Exception(
            """
            FATAL ERROR:
            You are attempting to instantiate a Deepgram object, which is no longer a class in version 3 of this SDK.

            To fix this issue:
                1. You need to revert to the previous version 2 of the SDK: pip install deepgram-sdk==2.12.0
                2. or, update your application's code to use version 3 of this SDK. See the README for more information.

            Things to consider:

                - This Version 3 of the SDK requires Python 3.10 or higher.
                  Older versions (3.9 and lower) of Python are nearing end-of-life: https://devguide.python.org/versions/
                  Understand the risks of using a version of Python nearing EOL.

                - Version 2 of the SDK will receive maintenance updates in the form of security fixes only.
                  No new features will be added to version 2 of the SDK.
            """
        )


class DeepgramClient:
    """
    Represents a client for interacting with the Deepgram API.

    This class provides a client for making requests to the Deepgram API with various configuration options.

    Attributes:
        api_key (str): The Deepgram API key used for authentication.
        config_options (DeepgramClientOptions): An optional configuration object specifying client options.

    Raises:
        DeepgramApiKeyError: If the API key is missing or invalid.

    Methods:
        listen: Returns a ListenClient instance for interacting with Deepgram's transcription services.

        manage: (Preferred) Returns a Threaded ManageClient instance for managing Deepgram resources.
        onprem: (Preferred) Returns an Threaded OnPremClient instance for interacting with Deepgram's on-premises API.

        asyncmanage: Returns an (Async) ManageClient instance for managing Deepgram resources.
        asynconprem: Returns an (Async) OnPremClient instance for interacting with Deepgram's on-premises API.
    """

    def __init__(
        self,
        api_key: str = "",
        config: Optional[DeepgramClientOptions] = None,
    ):
        """"Initializes a DeepgramClient object with an optional API key and configuration options. If no API key is provided, the function will attempt to retrieve it from the config object or the DEEPGRAM_API_KEY environment variable. If no API key is found, a warning will be logged. The function also sets the API key and configuration options for the DeepgramClient object.
        Parameters:
            - api_key (str): Optional API key for DeepgramClient object.
            - config (DeepgramClientOptions): Optional configuration options for DeepgramClient object.
        Returns:
            - DeepgramClient: A DeepgramClient object with the specified API key and configuration options.
        Processing Logic:
            - Sets API key from config object or environment variable if not provided.
            - Sets API key and configuration options for DeepgramClient object.
            - Logs a warning if no API key is found.
            - Maximum of 4 bullets used.""""
        
        verboselogs.install()
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.StreamHandler())

        if api_key == "" and config is not None:
            self.logger.info("Attempting to set API key from config object")
            api_key = config.api_key
        if api_key == "":
            self.logger.info("Attempting to set API key from environment variable")
            api_key = os.getenv("DEEPGRAM_API_KEY", "")
        if api_key == "":
            self.logger.warning("WARNING: API key is missing")

        self.api_key = api_key
        if config is None:  # Use default configuration
            self.config = DeepgramClientOptions(self.api_key)
        else:
            config.set_apikey(self.api_key)
            self.config = config

    @property
    def listen(self):
        """Listens to a specified configuration.
        Parameters:
            - config (str): The configuration to listen to.
        Returns:
            - Listen: A Listen object.
        Processing Logic:
            - Creates a Listen object.
            - Returns the Listen object."""
        
        return Listen(self.config)

    @property
    def read(self):
        """Reads the configuration file and returns the configuration object.
        Parameters:
            - config (dict): Dictionary containing configuration data.
        Returns:
            - config (dict): Dictionary containing configuration data.
        Processing Logic:
            - Read configuration file.
            - Convert configuration file to dictionary.
            - Return configuration dictionary."""
        
        return Read(self.config)

    @property
    def manage(self):
        """"Returns the version of the configuration management tool being used.
        Parameters:
            - config (str): The name of the configuration management tool.
            - manage (str): The specific function being called.
        Returns:
            - Version (str): The version of the configuration management tool being used.
        Processing Logic:
            - Gets the version of the specified configuration management tool.
            - Uses the Version function from the self object.
            - Returns the version as a string.
            - Does not modify any input parameters.""""
        
        return self.Version(self.config, "manage")

    @property
    def asyncmanage(self):
        """Returns the version of the config file used for async management.
        Parameters:
            - config (str): The name of the config file.
        Returns:
            - str: The version of the config file used for async management.
        Processing Logic:
            - Get the version of the config file.
            - Return the version.
            - Used for async management."""
        
        return self.Version(self.config, "asyncmanage")

    @property
    def onprem(self):
        """"Returns the version of the on-premise software based on the provided configuration.
        Parameters:
            - config (dict): A dictionary containing the configuration details.
            - "onprem" (str): A string indicating the type of software.
        Returns:
            - version (str): A string representing the version of the on-premise software.
        Processing Logic:
            - Uses the Version() method to retrieve the version.
            - Based on the provided configuration.
            - Returns the version as a string.""""
        
        return self.Version(self.config, "onprem")

    @property
    def asynconprem(self):
        """Returns the version of the asynchronous connection premium.
        Parameters:
            - self (object): The object containing the asynchronous connection premium.
        Returns:
            - version (str): The version of the asynchronous connection premium.
        Processing Logic:
            - Get the version from the config file.
            - Use the Version method to retrieve the version.
            - Return the version as a string."""
        
        return self.Version(self.config, "asynconprem")

    # INTERNAL CLASSES
    class Version:
        def __init__(self, config, parent: str):
            self.logger = logging.getLogger(__name__)
            self.logger.addHandler(logging.StreamHandler())
            self.logger.setLevel(config.verbose)
            self.config = config
            self.parent = parent

        # FUTURE VERSIONING:
        # When v2 or v1.1beta1 or etc. This allows easy access to the latest version of the API.
        # @property
        # def latest(self):
        #     match self.parent:
        #         case "manage":
        #             return ManageClient(self.config)
        #         case "onprem":
        #             return OnPremClient(self.config)
        #         case _:
        #             raise DeepgramModuleError("Invalid parent")

        def v(self, version: str = ""):
            self.logger.debug("Version.v ENTER")
            self.logger.info("version: %s", version)
            if len(version) == 0:
                self.logger.error("version is empty")
                self.logger.debug("Version.v LEAVE")
                raise DeepgramModuleError("Invalid module version")

            parent = ""
            fileName = ""
            className = ""
            match self.parent:
                case "manage":
                    parent = "manage"
                    fileName = "client"
                    className = "ManageClient"
                case "asyncmanage":
                    parent = "manage"
                    fileName = "async_client"
                    className = "AsyncManageClient"
                case "onprem":
                    parent = "onprem"
                    fileName = "client"
                    className = "OnPremClient"
                case "asynconprem":
                    parent = "onprem"
                    fileName = "async_client"
                    className = "AsyncOnPremClient"
                case _:
                    self.logger.error("parent unknown: %s", self.parent)
                    self.logger.debug("Version.v LEAVE")
                    raise DeepgramModuleError("Invalid parent type")

            # create class path
            path = f"deepgram.clients.{parent}.v{version}.{fileName}"
            self.logger.info("path: %s", path)
            self.logger.info("className: %s", className)

            # import class
            mod = import_module(path)
            if mod is None:
                self.logger.error("module path is None")
                self.logger.debug("Version.v LEAVE")
                raise DeepgramModuleError("Unable to find package")

            my_class = getattr(mod, className)
            if my_class is None:
                self.logger.error("my_class is None")
                self.logger.debug("Version.v LEAVE")
                raise DeepgramModuleError("Unable to find class")

            # instantiate class
            myClass = my_class(self.config)
            self.logger.notice("Version.v succeeded")
            self.logger.debug("Version.v LEAVE")
            return myClass
