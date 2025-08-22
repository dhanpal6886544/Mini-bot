from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random, datetime

app = FastAPI()

# Bot ka dimag (knowledge base)
def bot_brain(q: str) -> str:
    q = q.lower()

    # Greetings
    if "hello" in q or "hi" in q:
        return "Hi there! 😊 Kaise ho?"
    elif "bye" in q:
        return "Goodbye! Fir milte hain 👋"

    # Name
    elif "your name" in q:
        return "Mera naam Mini Bot 🤖 hai."

    # Time
    elif "time" in q:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Abhi ka time hai: {now} ⏰"

    # Date
    elif "date" in q:
        today = datetime.date.today().strftime("%d-%m-%Y")
        return f"Aaj ki date hai: {today} 📅"

    # Jokes
    elif "joke" in q:
        jokes = [
            "Teacher: Tum late kyu aaye? Student: Sir, sapne me cricket khel raha tha. Umpire out nahi kar raha tha isliye jag nahi paya. 😂",
            "Doctor: Tumhe kya problem hai? Patient: Mujhe sab kuch bhoolne ki bimari hai. Doctor: Kab se? Patient: Kab se kya? 🤔",
            "Ek aadmi restaurant gaya aur bola: 'Ek plate samosa dena, aur uske saath ek selfie bhi!' 🤳😂"
        ]
        return random.choice(jokes)

    # Study / GK
    elif "capital of india" in q:
        return "India ki capital New Delhi hai 🇮🇳"
    elif "prime minister" in q:
        return "Bharat ke Pradhan Mantri Narendra Modi ji hain."
    elif "2+2" in q:
        return "2 + 2 = 4 🔢"
    elif "earth" in q:
        return "Earth humara planet hai jo Suraj se 3rd number par hai 🌍"

    # Sports
    elif "cricket" in q:
        return "Mujhe bhi cricket pasand hai 🏏! Tumhe konsa player pasand hai?"
    elif "football" in q:
        return "Football duniya ka sabse popular game hai ⚽"

    # Motivation
    elif "motivate" in q or "inspire" in q:
        quotes = [
            "Hard work beats talent when talent doesn’t work hard. 💪",
            "Har din naya moka hai kuch naya karne ka! 🌟",
            "Jo sapne dekhte hain, wahi unhe poora karte hain 🚀"
        ]
        return random.choice(quotes)

    # Default fallback
    else:
        return f"Tumne bola: '{q}' — mujhe abhi ye samajhna nahi aaya 🤔"

# Chat API
@app.get("/chat")
def chat(q: str):
    reply = bot_brain(q)
    return {"reply": reply}

# Web UI
@app.get("/", response_class=HTMLResponse)
def home():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mini Bot 🤖</title>
        <style>
            body { font-family: Arial; background: #f0f0f0; }
            #chat { width: 320px; height: 400px; border: 1px solid #ccc; 
                    background: #fff; margin: 20px auto; padding: 10px; 
                    overflow-y: auto; }
            input { width: 240px; padding: 5px; }
            button { padding: 6px; }
        </style>
    </head>
    <body>
        <h2 align="center">Mini Bot 🤖</h2>
        <div id="chat"></div>
        <div align="center">
            <input id="msg" type="text" placeholder="Type a message...">
            <button onclick="sendMsg()">Send</button>
        </div>
        <script>
            async function sendMsg() {
                let msg = document.getElementById("msg").value;
                let chatBox = document.getElementById("chat");
                chatBox.innerHTML += "<b>You:</b> " + msg + "<br>";
                let res = await fetch(`/chat?q=${encodeURIComponent(msg)}`);
                let data = await res.json();
                chatBox.innerHTML += "<b>Bot:</b> " + data.reply + "<br>";
                document.getElementById("msg").value = "";
                chatBox.scrollTop = chatBox.scrollHeight;
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_code)