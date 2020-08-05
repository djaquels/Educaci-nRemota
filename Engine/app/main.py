from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import spacy
import requests
subscription_key = "8a6603fc5be646b4a45843fd0473cfae" # free key
endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/search" #endpoint
# NLP 
nlp = spacy.load("en_core_web_sm")
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)




@app.get("/")
def main():
    return {"module":"engine"}


@app.get("/search/")
def show_records(text: str):
    #spacy calls
    doc = nlp(text)
    nouns = [chunk.text for chunk in doc.noun_chunks]
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    content = nouns[0:3] + verbs[0:3]
    result = {
        "most_used_phrases":content
    }
    query = " ".join(str(x) for x in content)
    try:
        mkt = 'en-US'
        params = { 'q': query, 'mkt': mkt }
        headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        print("\nHeaders:\n")
        print(response.headers)
        print("\nJSON Response:\n")
        data = response.json()
        data = data["webPages"]
        data = data["value"]
        links = []
        for link in data:
            links.append({link["url"]:link["snippet"]})
        result["data"] = links

    except Exception as ex:
        raise ex
    return result
