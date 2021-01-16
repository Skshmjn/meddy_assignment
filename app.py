import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/news")
def news(query: str = None):
    if query:
        query = query.lower().strip()
    data = {}
    return data


@app.get("/")
def home():
    return {
        "CONNECTED": "YOU ARE CONNECTED TO NEWS AGGREGATOR"
    }


#
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
