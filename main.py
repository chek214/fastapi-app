from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return "root"

@app.get("/notes")
def get_notes():
    return "notes"

@app.get("/note/{note_id}")
def get_note(note_id):
    return "note " + note_id    

@app.post("/note")
def store_note():
    return "stored"

@app.delete("/note/{note_id}")
def delete_note():
    return "deleted"     

@app.put("/note/{note_id}")
def update_note():
    return "updated"                

