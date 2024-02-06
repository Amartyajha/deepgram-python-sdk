# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

# version
__version__ = "0.0.0"

import logging

import verboselogs

# utilities
from .audio import CHANNELS, CHUNK, LOGGING, RATE, Microphone

# onprem
# manage client responses
# manage
# read
# prerecorded
# live
# listen client
# entry point for the deepgram python sdk
from .client import (
    AnalyzeClient,
    AnalyzeOptions,
    AnalyzeResponse,
    AnalyzeSource,
    AnalyzeStreamSource,
    AsyncAnalyzeClient,
    AsyncAnalyzeResponse,
    AsyncLiveClient,
    AsyncManageClient,
    AsyncOnPremClient,
    AsyncPreRecordedClient,
    AsyncPrerecordedResponse,
    Balance,
    BalancesResponse,
    BufferSource,
    Deepgram,
    DeepgramClient,
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
    OnPremClient,
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
from .options import ClientOptionsFromEnv, DeepgramClientOptions
