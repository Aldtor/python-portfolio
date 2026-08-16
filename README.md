# 🐍 Python Practice & Engineering Portfolio

<div align="center">

[![Python](https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Programs](https://img.shields.io/badge/Programs-200%2B%20Scripts-4B8BBE?style=for-the-badge)](https://github.com/Aldtor/python-portfolio)
[![Status](https://img.shields.io/badge/Status-Active%20Engineering%20Archive-brightgreen?style=for-the-badge)](https://github.com/Aldtor/python-portfolio)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

### **A Comprehensive Collection of 200+ Python Programs, Algorithms, Data Structures, CLI Systems, and AI Utilities**

*From core number theory, sorting algorithms, and custom data structure implementations to an Aadhaar ID voting simulation, local offline voice assistant, and automation tools.*

---

[Highlight Projects](#-highlight-projects) • [Directory Index](#-directory-index) • [Topics Covered](#-topics--concepts-mastered) • [Running Scripts](#-how-to-run) • [About](#-author)

</div>

---

## 📌 Overview

This repository documents my hands-on journey mastering Python through direct problem-solving, building from scratch, and avoiding black-box abstractions. It contains **over 200+ structured Python scripts**, covering fundamental algorithms, binary file processing, custom memory structures, automation pipelines, and standalone CLI utilities.

---

## 📂 Directory Index

| Folder | Module / Domain | Highlights & Focus | Count |
| :--- | :--- | :--- | :--- |
| [`01-number-programs`](./01-number-programs/) | 🔢 **Number Theory & Math** | Armstrong, Palindrome, Prime, Fibonacci, Spy, Niven, Magic, Strong numbers | 25+ |
| [`02-patterns-and-loops`](./02-patterns-and-loops/) | 🔷 **Patterns & Nested Loops** | Dynamic star pyramids, hollow diamonds, Pascal triangles, number matrices | 10+ |
| [`03-lists-and-arrays`](./03-lists-and-arrays/) | 📋 **Lists & Linear Sequences** | Sorting algorithms (Bubble, Insertion, Selection), binary search, matrix ops | 15+ |
| [`04-strings`](./04-strings/) | 🔤 **String Manipulation** | Anagram detection, substring parsers, cipher encoding, frequency maps | 10+ |
| [`05-dictionaries-and-tuples`](./05-dictionaries-and-tuples/) | 📦 **Dictionaries & Tuples** | Record indices, immutable tuple unpacking, nested hashmap lookups | 8+ |
| [`06-functions`](./06-functions/) | ⚙️ **Functions & Recursion** | Pure functions, lambda calculus, recursive algorithms, memoization | 15+ |
| [`07-file-handling`](./07-file-handling/) | 📁 **File I/O & Serialization** | Text streams, CSV parsers, binary record management with `pickle` | 8+ |
| [`08-stacks-and-queues`](./08-stacks-and-queues/) | 📚 **Data Structures** | Stack (LIFO) & Queue (FIFO) implementations with overflow/underflow logic | 6+ |
| [`09-lisa-ai-assistant`](./09-lisa-ai-assistant/) | 🤖 **Lisa AI Voice Assistant** | Local STT (`speech_recognition`) + TTS (`pyttsx3`) + conversation memory | 4 |
| [`10-practicals`](./10-practicals/) | 📝 **Formal Coursework** | Comprehensive laboratory exercises and academic practical challenges | 10 |
| [`11-adhar-voting-system`](./11-adhar-voting-system/) | 🪪 **Aadhaar ID & Voting CLI** | Full Aadhaar identity verification gate with electronic voting simulation | 4 |
| [`12-python-data-types-explorer`](./12-python-data-types-explorer/) | 🧠 **Mega Interactive Explorer** | 16KB monolithic interactive CLI demonstrating all Python data types | 2 |
| [`15-extra-programs`](./15-extra-programs/) | ➕ **Utilities & Automation** | Logic gates, terminal animations, date utilities, automation scripts | 15+ |

---

## ⭐ Highlight Projects

### 🪪 1. Aadhaar Card Verification & Electronic Voting System
A complete terminal-based authentication and electoral voting engine.
- **Identity Gating:** Simulates UIDAI Aadhaar ID validation prior to ballot access.
- **Security Check:** Prevents duplicate voting through unique ID token locks.
- **Data Persistence:** Stores candidate tallies and voter verification logs securely.
- 📁 *Path: [`11-adhar-voting-system/`](./11-adhar-voting-system/)*

### 🤖 2. Lisa — Personal AI Voice Assistant
A lightweight, offline-capable desktop voice assistant.
- **Speech Synthesis:** Offline text-to-speech engine powered by `pyttsx3`.
- **Audio Recognition:** Real-time microphone listening via `speech_recognition`.
- **Stateful Memory:** JSON-backed context storage for maintaining user preferences.
- 📁 *Path: [`09-lisa-ai-assistant/`](./09-lisa-ai-assistant/)*

### 🧠 3. Python Data Types Interactive Explorer
An educational CLI application that serves as a live sandbox for Python learners.
- Interactive navigation through arithmetic, bitwise operators, string manipulation, and list operations in real-time.
- 📁 *Path: [`12-python-data-types-explorer/`](./12-python-data-types-explorer/)*

---

## 📈 Topics & Concepts Mastered

- ✅ **Core Logic:** Flow control (`if/elif/else`), nested loops, pattern geometry, recursion.
- ✅ **Data Structures:** Custom Stack, Queue, Hash Tables, Matrix manipulations, Sorting & Searching.
- ✅ **File Systems:** Binary I/O, `pickle` serialization, text streaming, exception handling.
- ✅ **System Automation:** `os`, `sys`, `datetime`, `json`, `webbrowser` standard libraries.
- ✅ **Audio & Signal Processing:** Real-time speech recognition, voice synthesis pipelines.

---

## 💻 How to Run

### Prerequisites
- Python 3.8+ installed on your machine

### Clone and Execute
```bash
# Clone the repository
git clone https://github.com/Aldtor/python-portfolio.git
cd python-portfolio

# Run any standalone script (e.g. Number Programs)
python 01-number-programs/01_armstrong.py

# Run the Aadhaar Voting System
python 11-adhar-voting-system/main.py

# Run Lisa Voice Assistant (requires pyttsx3 & speech_recognition)
pip install pyttsx3 speechrecognition pyaudio
python 09-lisa-ai-assistant/main.py
```

---

## 👤 Author

**Satyam Kumar (Aldtor)**
- 🌐 Portfolio: [aldtor.vercel.app](https://aldtor.vercel.app)
- 🐙 GitHub: [@Aldtor](https://github.com/Aldtor)
- 💼 LinkedIn: [linkedin.com/in/aldtor](https://in.linkedin.com/in/aldtor)

---

<div align="center">
  <sub>Documenting the journey from foundational algorithms to robust software systems.</sub>
</div>
