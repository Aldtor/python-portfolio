# 🤖 Lisa — AI Voice Assistant

A personal AI voice assistant built from scratch in Python.

## Features
- 🗣️ **Text-to-Speech (TTS)** — Lisa speaks back to you using `pyttsx3`
- 🎤 **Optional Speech-to-Text (STT)** — `voice/stt.py` uses Google's online Speech Recognition API; recorded microphone audio is sent to Google.
- 🧠 **Memory** — Saves assistant settings and style preferences locally in JSON
- 💬 **Custom Responses** — Personalized assistant behavior

## Files

| File | Description |
|------|-------------|
| `lisa.py` | Main CLI — typed input, local Ollama chat, and speech output |
| `voice/tts.py` | Text-to-Speech module |
| `voice/stt.py` | Optional Google-based speech-to-text helper (requires internet; sends audio to Google) |

## Requirements
```
pip install pyttsx3 speechrecognition
```

## Run
```bash
python lisa.py
```

> Privacy note: `lisa.py` currently reads typed input and uses Ollama locally by default. The separate `voice/stt.py` helper is not connected to the main loop; it calls `recognize_google`, which requires internet and sends recorded audio to Google. Do not use that helper for sensitive audio unless you are comfortable sharing it with Google.
