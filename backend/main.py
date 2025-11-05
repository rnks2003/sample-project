from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()

@app.get("/")
def service():
    return {'service': 'melanoma detection'}

@app.get("/ping")
def ping():
    return {'ok': True, 'timestamp': datetime.utcnow()}

@app.post("/predict")
def predict(request: dict):
    # Placeholder for prediction logic
    print(request)
    return {'diagnosis': 'benign', 'confidence': 0.95}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)