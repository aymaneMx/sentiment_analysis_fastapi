from fastapi import FastAPI
from textblob import TextBlob


app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Alive!"}


@app.get("/analysis/")
def analysis_result(q: str = None):
    if q:
        polarity = TextBlob(q).sentences[0].polarity
        return {"sentence": q, "polarity": polarity}
    else:
        return {"Error": "plz enter a sentence!"}
