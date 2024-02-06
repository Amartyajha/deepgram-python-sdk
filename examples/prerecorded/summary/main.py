# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

import logging
import os
from datetime import datetime, timedelta

import verboselogs
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    FileSource,
    PrerecordedOptions,
)

load_dotenv()

AUDIO_FILE = "CallCenterPhoneCall.mp3"


def main():
    try:
        # STEP 1 Create a Deepgram client using the API key in the environment variables
        # config = DeepgramClientOptions(
        #     verbose=logging.SPAM,
        # )
        # deepgram = DeepgramClient("", config)
        # OR use defaults
        deepgram = DeepgramClient()

        # STEP 2 Call the transcribe_file method on the prerecorded class
        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            utterances=True,
            punctuate=True,
            summarize="v2",
        )

        before = datetime.now()
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        after = datetime.now()

        print(response.to_json(indent=4))
        print("")
        difference = after - before
        print(f"time: {difference.seconds}")

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
