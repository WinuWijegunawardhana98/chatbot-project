from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import process
from googletrans import Translator

app = Flask(__name__)

# Define a dictionary of responses (in English)
responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! How can I help?",
    "bye": "Goodbye! Have a great day!",
    "how are you": "I'm just a bot, but I'm doing well. How about you?",
    "thank you": "You're welcome! Anything else I can help with?",
    "help": "Sure! You can ask me about greetings, farewells, or general assistance.",
}

# Initialize the translator
translator = Translator()

def chatbot_response(user_input, lang="en"):
    # Use fuzzy matching to find the closest match
    closest_match, confidence = process.extractOne(user_input.lower(), responses.keys())
    
    # Define a threshold for confidence
    if confidence > 75:  # 75% match threshold
        response = responses[closest_match]
    else:
        response = "I'm sorry, I don't quite understand that. Can you rephrase?"
    
    # Translate response to the user's language if it's not English
    if lang != "en":
        response = translator.translate(response, dest=lang).text
    
    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message", "")
    user_lang = request.json.get("language", "en")  # Default to English
    bot_reply = chatbot_response(user_input, user_lang)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
