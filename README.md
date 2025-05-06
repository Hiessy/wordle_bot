# 🧠 Wordle Bot - Python + Selenium

This project is an automated bot that plays the New York Times Wordle using Selenium WebDriver and logic to interpret feedback from the game tiles.

## 🔧 Setup Instructions

### ✅ Requirements

- Python 3.8+
- Firefox browser
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) installed and added to your system's PATH
- `list` file (a space-separated list of valid 5-letter words)

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/your-username/wordle-bot.git
cd wordle-bot
```

### 2. 🐍 Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```
### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. 🏁 Run the Bot
```bash
python wordle_bot.py
```
## 📄 File Structure
```bash
wordle-bot/
├── wordle_bot.py        # Main script that runs the bot
├── bot.py               # Logic module for filtering guesses
├── list                 # A file containing space-separated 5-letter words
├── requirements.txt     # Python dependencies
└── README.md            # Setup guide
```
## 🧪 Notes
* The bot uses Firefox with Selenium. To use Chrome, replace webdriver.Firefox() with webdriver.Chrome() and install ChromeDriver.
* The first guess is hardcoded as ALIVE in wordle_bot.py, but you can change it.

## 🤖 Disclaimer
This project is for educational and fun automation purposes. Do not use it to cheat or violate any website's terms of service.