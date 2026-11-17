from fastapi import FastAPI

app = FastAPI(
    title="MedMailGuard",
    description="Система семантической классификации входящих писем медицинской организации",
    version="0.1.0"
)

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}
