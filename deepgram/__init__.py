# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

# version
__version__ = '0.0.0'

# entry point for the deepgram python sdk
from .client import DeepgramClient
from .options import DeepgramClientOptions
from .errors import DeepgramError, DeepgramApiError, DeepgramUnknownApiError, DeepgramUnknownError

# live
from .clients.live.options import LiveOptions
from .clients.live.enums import LiveTranscriptionEvents

# prerecorded
from .clients.prerecorded.options import PrerecordedOptions

# manage
from .clients.manage.client import ManageClient
