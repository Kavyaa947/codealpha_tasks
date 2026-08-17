from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

try:
    # Use deep-translator's GoogleTranslator for lightweight translation.
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except Exception:
    TRANSLATOR_AVAILABLE = False


@app.route("/")
def index():
    """Render the main translation page."""
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    """Translate text using deep-translator GoogleTranslator."""
    request_data = request.get_json(silent=True)
    if not request_data:
        return jsonify({"error": "Invalid request data. Please try again."}), 400

    text = request_data.get("text", "").strip()
    source_lang = request_data.get("source_lang", "auto")
    target_lang = request_data.get("target_lang", "en")

    if not text:
        return jsonify({"error": "Please enter text to translate."}), 400
    if not target_lang:
        return jsonify({"error": "Please select a target language."}), 400

    if not TRANSLATOR_AVAILABLE:
        return jsonify({"error": "deep-translator is not installed. Please run 'pip install -r requirements.txt'."}), 500

    try:
        src = source_lang if source_lang else "auto"
        translator = GoogleTranslator(source=src, target=target_lang)
        translated_text = translator.translate(text)

        if not translated_text:
            return jsonify({"error": "Translation service returned an unexpected response."}), 502

        return jsonify({"translatedText": translated_text})

    except Exception as exc:
        return jsonify({"error": f"Translation failed: {exc}"}), 502


if __name__ == "__main__":
    app.run(debug=True, port=8000)
