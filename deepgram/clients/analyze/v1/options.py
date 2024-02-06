# Copyright 2024 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

import logging
from dataclasses import dataclass
from typing import List, Optional, TypedDict, Union

import verboselogs
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class AnalyzeOptions:
    """
    Contains all the options for the AnalyzeOptions.

    Reference:
    https://developers.deepgram.com/reference/text-intelligence-apis
    """

    callback: Optional[str] = None
    callback_method: Optional[str] = None
    custom_intent: Optional[Union[list, str]] = None
    custom_intent_mode: Optional[str] = None
    custom_topic: Optional[Union[list, str]] = None
    custom_topic_mode: Optional[str] = None
    intents: Optional[bool] = None
    language: Optional[str] = None
    sentiment: Optional[bool] = None
    summarize: Optional[bool] = None
    topics: Optional[bool] = None

    def __getitem__(self, key):
        _dict = self.to_dict()
        return _dict[key]

    def check(self):
        verboselogs.install()
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.StreamHandler())
        prev = logger.level
        logger.setLevel(logging.ERROR)

        # no op at the moment

        logger.setLevel(prev)

        return True
