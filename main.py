@app.get("/chat")
def chat(q: str):
    q = q.lower().strip()

    if "hello" in q or "hi" in q:
        return {"reply": "Hi! Kaise ho?"}
    elif "bye" in q:
        return {"reply": "Goodbye! Fir milte hain."}
    elif "time" in q:
        from datetime import datetime
        return {"reply": f"Abhi ka time hai: {datetime.now().strftime('%H:%M:%S')}"}
    elif "name" in q:
        return {"reply": "Mera naam Mini Bot hai 🤖"}
    elif "love" in q:
        return {"reply": "Mujhe pyaar ki samajh nahi hai, par dosti pakki hai 💙"}
    elif "joke" in q:
        return {"reply": "Ek joke suno: Teacher: Tum late kyu aaye? Student: Sir ghadi hi ruk gayi thi! Teacher: Toh tumne ghadi kyu nahi chalayi? Student: Sir, ghadi to diwar pe lagi thi 😂"}
    elif "help" in q:
        return {"reply": "Main tumhari help karne ke liye yahan hoon. Bas apna sawal pucho ✅"}
    elif "weather" in q:
        return {"reply": "Mujhe abhi live weather nahi pata, lekin tum Google me search kar sakte ho ☁️"}
    else:
        return {"reply": f"Mujhe samajh nahi aaya: '{q}'"}