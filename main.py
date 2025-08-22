from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def webchat():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mini Bot 🤖</title>
        <style>
            body { font-family: Arial; background: #f0f0f0; }
            #chat { width: 300px; height: 400px; border: 1px solid #ccc; overflow-y: auto; background: #fff; margin: 20px auto; padding: 10px; }
            input { width: 240px; padding: 5px; }
            button { padding: 6px; }
        </style>
    </head>
    <body>
        <div align="center"><h2>Mini Bot 🤖</h2></div>
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
                let res = await fetch(window.location.origin + "/chat?q=" + encodeURIComponent(msg));
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


@app.get("/chat")
def chat(q: str):
    if "hello" in q.lower():
        return {"reply": "Hi! How are you?"}
    elif "bye" in q.lower():
        return {"reply": "Goodbye! Fir milte hain 🙂"}
    elif "name" in q.lower():
        return {"reply": "Mera naam Mini Bot hai 🤖"}
    else:
        return {"reply": f"Tumne bola: {q}"}