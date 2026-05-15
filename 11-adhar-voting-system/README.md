# 🪪 Adhar — Aadhaar Card & Voting System

A Python project simulating India's **Aadhaar card system** with ID verification and a linked **Voting System**.

## 📁 Files

| File | Description |
|------|-------------|
| `adhar.py` | Core Aadhaar module — name/ID verification and correction |
| `gpchat.py` | Government portal interface — displays "GOVERNMENT OF INDIA" header, takes name & Aadhaar no., opens Aadhaar HTML card |
| `Voting System.py` | Full voting system — verifies Aadhaar ID before allowing vote, reads HTML Aadhaar card |
| `satyammodule.py` | Utility module with prime checker, number functions |

## 🔑 Features
- ✅ Aadhaar ID verification before any action
- ✅ Update name / ID with verification check
- ✅ Government of India styled interface with date display
- ✅ HTML Aadhaar card file integration
- ✅ Voting access gated by Aadhaar authentication

## 💡 Concepts Used
- Functions & modules (`import adhar`)
- File handling (read/write HTML)
- `webbrowser` module
- `datetime` module
- Input validation & conditionals

> 🌟 This is a real-world simulation of India's digital ID system built entirely in Python!
