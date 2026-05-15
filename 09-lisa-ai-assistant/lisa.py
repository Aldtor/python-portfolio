import json
import os
import pyttsx3
import subprocess

ASSISTANT_NAME = "Lisa"
MEMORY_FILE = "memory.json"
MAX_STYLE = 0.6

# ------------------ MEMORY ------------------

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "assistant_name": ASSISTANT_NAME,
            "style_score": 0.2
        }
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

memory = load_memory()

# ------------------ VOICE ------------------

engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ------------------ STYLE ADAPTATION ------------------

def analyze_user_style(text):
    casual_markers = ["lol", "yeah", "nah", "ok", "okay"]
    return min(sum(0.05 for w in casual_markers if w in text.lower()), 0.1)

def update_style(text):
    delta = analyze_user_style(text)
    memory["style_score"] = min(memory["style_score"] + delta, MAX_STYLE)
    save_memory(memory)

# ------------------ COMMAND HANDLER ------------------

def handle_command(text):
    if "your name" in text.lower():
        return f"My name is {ASSISTANT_NAME}, sir."
    if "stop listening" in text.lower():
        speak("Understood, sir. I will stop.")
        exit()
    return None

# ------------------ AI CHAT ------------------

def ask_ai(user_text):
    style = memory["style_score"]

    if style < 0.3:
        tone = "polite and structured"
    else:
        tone = "friendly but respectful"

    system_prompt = f"""
You are {ASSISTANT_NAME}, a private offline voice assistant.
You are a friendly companion but always respectful.
You always address the user as sir.
You never change your name or role.
Your tone is {tone}.
"""

    prompt = system_prompt + f"\nUser: {user_text}\n{ASSISTANT_NAME}:"

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()

# ------------------ IDENTITY ENFORCEMENT ------------------

def enforce_identity(text):
    forbidden = ["assistant", "chatgpt", "ai model"]
    for word in forbidden:
        if word in text.lower():
            return f"I am {ASSISTANT_NAME}, sir."
    return text

# ------------------ MAIN LOOP ------------------

def main():
    speak(f"Hello sir. This is {ASSISTANT_NAME}. I am listening.")

    while True:
        user_text = input("You: ")  # replace with speech-to-text later

        update_style(user_text)

        command_response = handle_command(user_text)
        if command_response:
            speak(command_response)
            continue

        reply = ask_ai(user_text)
        reply = enforce_identity(reply)
        speak(reply)

if __name__ == "__main__":
    main()
