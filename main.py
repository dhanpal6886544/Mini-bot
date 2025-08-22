from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    html_code = """
    <html>
      <head>
        <title>Mini Bot</title>
      </head>
      <body>
        <h2>Mini Bot</h2>
        <div id="chat"></div>
        <input type="text" id="msg" placeholder="Type a message">
        <button onclick="send()">Send</button>

        <script>
          async function send() {
            let msg = document.getElementById("msg").value;
            let res = await fetch("/chat?q=" + msg);
            let data = await res.json();
            document.getElementById("chat").innerHTML += "<b>You:</b> " + msg + "<br>";
            document.getElementById("chat").innerHTML += "<b>Bot:</b> " + data.reply + "<br>";
            document.getElementById("msg").value = "";
          }
        </script>
      </body>
    </html>
    """
    return HTMLResponse(content=html_code)

@app.get("/chat")
def chat(q: str):
    q = q.lower().strip()
    if "hello" in q or "hi" in q:
        return {"reply": "Hi! Kaise ho?"}
    elif "bye" in q:
        return {"reply": "Goodbye! Fir milte hain."}
    else:
        return {"reply": f"Tumne bola: {q}"}