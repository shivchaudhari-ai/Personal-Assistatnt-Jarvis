
# 🤖 Jarvis – Python AI Voice Assistant

Jarvis is a personal voice-controlled assistant built in Python. It listens to your voice commands and performs various tasks like searching Wikipedia, opening websites, sending emails, telling jokes, getting weather updates, taking screenshots, and more.

## 🚀 Features

- 🎤 Speech Recognition using `speech_recognition`
- 🗣️ Text-to-Speech with `pyttsx3`
- 🌐 Wikipedia search
- 🌦️ Real-time weather updates using OpenWeatherMap API
- ✉️ Send emails via Gmail
- 📷 Take screenshots with `pyautogui`
- 😂 Jokes using `pyjokes`
- 🕒 Time announcements
- 🔗 Open websites like YouTube, Google, and Stack Overflow
- 🧠 Intelligent voice interaction loop

## 🛠️ Tech Stack

- Python 3.x
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [wikipedia](https://pypi.org/project/wikipedia/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [pyjokes](https://pypi.org/project/pyjokes/)
- [requests](https://pypi.org/project/requests/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)

## 📦 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App:**
   ```bash
   python jarvis.py
   ```

## 🔐 Important Notes

- Configure your Gmail credentials in the `send_email` function.
- Replace the placeholder in `get_weather()` with your OpenWeatherMap API key.
- Customize VS Code path or other commands as per your system.

## 📁 Directory Structure

```
jarvis-voice-assistant/
│
├── jarvis.py              # Main assistant script
├── requirements.txt       # Dependency list
├── screenshot.png         # Saved screenshots
└── README.md              # This file
```

## 💡 Future Ideas

- Add GUI with Tkinter or Streamlit
- Integrate with OpenAI for smarter conversations
- Add voice training/personalization

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ by Shivam Chaudhari**
