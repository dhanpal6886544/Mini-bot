from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/chat")
def chat(q: str):
    q = q.lower().strip()
    if "hello" in q or "hi" in q:
        return {"reply": "Hi! Kaise ho?"}
    elif "bye" in q:
        return {"reply": "Goodbye! Fir milte hain."}
    else:
        return {"reply": f"Tune bola: {q}"}
