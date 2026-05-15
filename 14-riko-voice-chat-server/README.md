# 🎙️ Riko — AI Voice Chat Server

A **real-time AI voice chat server** with Speech Recognition, LLM processing, and Text-to-Speech output.

## 📁 Files

| File | Description |
|------|-------------|
| `main_chat.py` | Main chat server — orchestrates ASR → LLM → TTS pipeline |
| `asr_push_to_talk.py` | Speech-to-Text (ASR) — push-to-talk voice input |
| `llm_scr.py` | LLM integration — processes text through language model |
| `sovits_ping.py` | Text-to-Speech using SoVITS voice synthesis |

## 🔄 Pipeline
```
🎤 Voice Input → ASR → LLM Processing → TTS Voice Output 🔊
```

## 💡 Concepts Used
- Async server architecture
- Speech Recognition (ASR)
- Large Language Model (LLM) integration
- Neural TTS (SoVITS)
- Pipeline / modular design

> 🌟 This is an advanced AI project implementing a full voice-to-voice AI conversation pipeline!
