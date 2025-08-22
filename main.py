from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API key environment se lega
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message")

    try:
        # GPT-3.5 se reply lena
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tum ek helpful chatbot ho jo Hindi aur English dono samajhta hai."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response["choices"][0]["message"]["content"]

    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)