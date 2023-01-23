### mycroft-tts-plugin-elevenlabs

This TTS service for Mycroft requires a subscription to [ElevenLabs](https://elevenlabs.io). It is not very robust, but works well.

Configuration parameters:

```json
"tts": {
    "module": "elevenlabs_tts",
    "elevenlabs": {
       "voiceId": "THE_ID_OF_THE_VOICE_YOU_WANT",
       "apiKey": "YOUR_ELEVENLABS_API_KEY"
    }
}
```
