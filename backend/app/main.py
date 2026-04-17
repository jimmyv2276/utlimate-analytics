from fastapi import FastAPI

app = FastAPI(title="Ulti Analytics API")

@app.get("/health")
def health():
    return {"status": "ok"}