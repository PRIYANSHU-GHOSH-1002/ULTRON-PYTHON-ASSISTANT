ULTRON — Voice-Controlled Python Assistant

Ultron is a lightweight voice-controlled personal assistant built with Python. It listens for a wake word, processes spoken commands, responds using text-to-speech, and automates everyday actions such as opening websites and playing music through predefined commands.
The project focuses on speech-based automation and modular command handling without relying on AI.

🎙️ Features
Wake-word activation using "Ultron"
Speech-to-text command recognition
Text-to-speech responses
Opens commonly used websites through voice commands
Plays songs using a custom music library
Modular command-processing function
Simple fallback responses for unsupported commands
Continuous listening loop

🛠️ Technology Stack
Language: Python
Speech Recognition: SpeechRecognition
Text-to-Speech: pyttsx3
Browser Automation: Python webbrowser
Audio Input: Microphone via SpeechRecognition
Custom Module: music_lib

🧠 How It Works
Ultron follows a simple voice-command pipeline:

Microphone
    ↓
Speech Recognition
    ↓
Wake Word Detection
    ↓
Command Recognition
    ↓
Command Processing
    ↓
Action + Voice Response
The assistant continuously listens for the wake word "Ultron". Once detected, it activates and listens for the next command.

For example:

User: "Ultron"
Ultron: "INITIALIZING ULTRON"
User: "Open YouTube"
Ultron: "Aye aye sir"

→ YouTube opens in the browser
🎤 Supported Commands
Open Websites
Open Instagram
Open Insta
Open YouTube
Open YT
Open Google
Play Music
Play <song>
Songs are looked up from the custom music_lib module.

Unsupported Commands
If a command is not recognized, Ultron responds:
Negative sir

📁 Project Structure
ULTRON/
│
├── main.py
├── music_lib.py
└── README.md
main.py
Contains the main assistant logic, including:

Microphone input

Speech recognition
Wake-word detection
Command processing
Text-to-speech responses
Browser automation
music_lib.py

Stores predefined songs and their corresponding links used by the music command.

▶️ Running the Project
1. Clone the repository
git clone <your-repository-url>
cd ULTRON
2. Install dependencies
pip install SpeechRecognition pyttsx3
Depending on your system, you may also need the audio input dependency required by SpeechRecognition:

pip install PyAudio
3. Run Ultron
python main.py
You should see:

Listening...
Say:

Ultron
The assistant will activate and wait for your command.

🔧 Customization
Ultron is designed around a simple command-processing function, making it easy to add new commands.

Commands can be added inside:

def processcommand(c):
For example:

elif "open github" in c:
    speak("aye aye sir")
    webbrowser.open("https://github.com")
This allows the assistant to be extended with additional websites, utilities, scripts, and custom actions.

🚀 Future Improvements
Possible extensions include:
More voice commands
System-level automation
File and application management
Weather and connectivity utilities
Custom command configuration
Better error handling
Offline speech recognition
Plugin-based command modules
Voice-controlled productivity tools

📌 Project Type
Voice Assistant · Python Automation

👨‍💻 About
Ultron was built as a Python project to explore speech recognition, automation, modular programming, and human-computer interaction while keeping the system lightweight and independent of AI services.
