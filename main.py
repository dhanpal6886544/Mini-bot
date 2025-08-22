from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API key set karo
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]

    try:
        # GPT se response lo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # ya gpt-4 agar tumhare pass access hai
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response["choices"][0]["message"]["content"]

    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)