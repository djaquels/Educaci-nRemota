from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
#from sqlalchemy.orm import Session
#from starlette.responses import RedirectResponse

#from . import models, schemas
#from .database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)

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
    return {
     "response":"ok"
    }


@app.get("/send/")
def audio_to_text():
    #process audio using wattson
    return records
