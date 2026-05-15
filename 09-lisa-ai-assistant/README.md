# 🤖 Lisa — AI Voice Assistant

A personal AI voice assistant built from scratch in Python.

## Features
- 🗣️ **Text-to-Speech (TTS)** — Lisa speaks back to you using `pyttsx3`
- 🎤 **Speech-to-Text (STT)** — Listens to your voice using `speech_recognition`
- 🧠 **Memory** — Saves conversations and context using JSON
- 💬 **Custom Responses** — Personalized assistant behavior

## Files

| File | Description |
|------|-------------|
| `lisa.py` | Main assistant — memory, responses, conversation logic |
| `voice/tts.py` | Text-to-Speech module |
| `voice/stt.py` | Speech-to-Text module |

## Requirements
```
pip install pyttsx3 speechrecognition
```

## Run
```bash
python lisa.py
```

> 🌟 Lisa is a personal project — a fully custom voice AI assistant built without any cloud APIs.
