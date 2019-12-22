## Sentiment Analysis using FastAPI
backend core app.

## get started

```shell
poetry install 
uvicorn main:app --reload
```
## Check it

Open your browser at http://localhost:8000/analysis/?q=I%20like%20your%20code .

You will see the JSON response as:

```json
{"sentence": "I like your code", "polarity": 0}
```
