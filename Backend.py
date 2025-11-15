from flask import Flask, render_template_string, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple rule-based chatbot logic
def get_bot_response(user_message):
    user_message = user_message.lower()

    if 'hello' in user_message or 'hi' in user_message:
        return "Hello! How can I help you today?"
    elif 'how are you' in user_message:
        return "I'm doing well, thanks! How about you?"
    elif 'bye' in user_message or 'goodbye' in user_message:
        return "Goodbye! Have a great day!"
    elif 'name' in user_message:
        return "I'm a simple chatbot built with Flask."
    elif 'weather' in user_message:
        return "I don’t have access to real-time weather, but it’s always sunny in code!"
    elif 'python' in user_message:
        return "Python is an awesome language!"
    else:
        return "I'm not sure how to respond to that, but I'm learning more every day!"

# MAIN API ROUTE FOR CHATBOT
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = get_bot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
