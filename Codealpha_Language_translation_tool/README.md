# Language Translation Tool

A simple Python + Flask translation web app that uses the `deep-translator` library (no API key required).

## Features
- Enter text and select source and target languages
- Translate using `deep-translator` GoogleTranslator
- Copy translated text to the clipboard
- Text-to-speech for translated text
- Clear button and friendly error messages
- Responsive, modern interface for college project demonstration

## Project structure
- `app.py` – Flask backend and translation endpoint
- `templates/index.html` – frontend page
- `static/style.css` – CSS styles
- `static/script.js` – frontend JavaScript logic
- `requirements.txt` – Python dependencies
- `.env.example` – kept for compatibility (no API key required)

## Setup
1. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
2. Start the Flask application (runs on port 8000):
   ```powershell
   python app.py
   ```
3. Open your browser at:
   ```text
   http://127.0.0.1:8000
   ```

## Notes
- No API key, billing, or Docker required.
- `deep-translator` uses public translation endpoints and does not require a paid API key for GoogleTranslator.
- If translation fails, the app will return a clear error message.
