# Copyright 2020 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests
import os

from mycroft.tts import TTS, TTSValidator
from mycroft.configuration import Configuration


class ElevenlabsTTSPlugin(TTS):
    def __init__(self, lang="en-us", config=None):
        if config is None:
            self.config = Configuration.get().get("tts", {}).get("elevenlabs", {})
        else:
            self.config = config
        super(ElevenlabsTTSPlugin, self).__init__(lang, self.config, ElevenlabsTTSValidator(self), 'mp3')
        self.url = "https://api.elevenlabs.io/v1/text-to-speech/" + self.config['voiceId'];
        self.type = 'mp3'

    def get_tts(self, sentence, mp3_file):
        headers = {"Content-Type": "application/json; charset=utf-8", "Accept": "audio/mpeg", "xi-api-key": self.config['apiKey']}
        response = requests.post(self.url, json={'text': sentence}, headers=headers)
        with open(mp3_file, 'wb') as f:
            f.write(response.content)
        return (mp3_file, None)  # No phonemes


class ElevenlabsTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(ElevenlabsTTSValidator, self).__init__(tts)

    def validate_dependencies(self):
        pass

    def validate_lang(self):
        # TODO
        pass

    def validate_connection(self):
        config = Configuration.get().get("tts", {}).get("elevenlabs", {})
        headers = {"Content-Type": "application/json; charset=utf-8","xi-api-key": config['apiKey']}
        response = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers)
        if not response.status_code == 200:
            raise ConnectionRefusedError

    def get_tts_class(self):
        return ElevenlabsTTSPlugin
