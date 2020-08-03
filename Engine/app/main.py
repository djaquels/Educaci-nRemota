from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import spacy


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


@app.get("/info/")
def show_records():
    #spacy calls
    return records
