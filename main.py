from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import random

app = FastAPI()

# Bot ka dimag (questions -> answers)
brain = {
    "hello": ["Hi! Kaise ho?", "Hello ji 👋", "Namaste 🙏"],
    "hi": ["Hi there!", "Hii 👋", "Arey Hii!"],
    "bye": ["Goodbye! Fir milte hain.", "Bye bye 👋", "Phir aana!"],
    "time": [f"Abhi time ho raha hai {datetime.now().strftime('%H:%M:%S')}"],
    "name": ["Mera naam Mini Bot hai 🤖", "Main Mini Bot hoon", "Mini Bot present!"],
    "how are you": ["Main theek hoon 😃, tum kaise ho?", "Mast chal raha hai! Aur tum?"],
    "love": ["Love ❤️ ek pyari feeling hai!", "Mujhe bhi tumse pyaar hai 😍"],
    "joke": ["Teacher: Tum late kyu aaye? \nStudent: Sir, exam dene aa raha tha, raste me exam hi mil gaya 😅",
             "Ek aadmi doctor ke paas gaya: 'Doctor sahab, mujhe bhoolne ki bimaari hai.' \nDoctor: 'Kab se?' \nAadmi: 'Kab se kya?' 😂"]
}

# Chat endpoint
@app.get("/chat")
def chat(q: str):
    q_lower = q.lower()
    reply = None
    
    # Brain se match karo
    for key in brain:
        if key in q_lower:
            reply = random.choice(brain[key])
            break
    
    # Agar samajh na aaye
    if not reply:
        reply = f"Mujhe samajh nahi aaya: {q}"
    
    return {"reply": reply}


# Chatbot UI
@app.get("/", response_class=HTMLResponse)
def home():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mini Bot 🤖</title>
        <style>
            body { font-family: Arial; background: #f0f0f0; }
            #chat { width: 300px; height: 400px; border: 1px solid #ccc; 
                    overflow-y: auto; background: #fff; margin: 20px auto; padding: 10px; }
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
                if (!msg) return;
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