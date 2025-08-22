from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# OpenAI API key environment variable se
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    bot_reply = response.choices[0].text.strip()
    return {"reply": bot_reply}

if __name__ == "__main__":
    app.run(debug=True)