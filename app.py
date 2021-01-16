import uvicorn
from fastapi import FastAPI, HTTPException

# local
from aggregator import aggregate_news

app = FastAPI()


@app.get("/news")
def news(query: str = None):
    if query:
        query = query.lower()

    data = aggregate_news(search_query=query)
    if not data:
        raise HTTPException(status_code=404, detail="Can not fetch news")
    return data


@app.get("/")
def home():
    return {
        "CONNECTED": "YOU ARE CONNECTED TO NEWS AGGREGATOR"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
