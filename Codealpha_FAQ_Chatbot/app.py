from flask import Flask, jsonify, render_template, request

from FAQ_Chatbot import FAQChatbot

app = Flask(__name__)
chatbot = FAQChatbot()


@app.route("/")
def index():
    """Render the chatbot homepage."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Accept a user's question and return the chatbot response."""
    try:
        data = request.get_json(silent=True) or {}
        question = data.get("question", "")

        if not isinstance(question, str) or not question.strip():
            return jsonify({"error": "Please enter a valid question."}), 400

        answer = chatbot.get_response(question)
        return jsonify({"answer": answer})

    except Exception as exc:
        return jsonify({"error": f"Something went wrong: {str(exc)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
