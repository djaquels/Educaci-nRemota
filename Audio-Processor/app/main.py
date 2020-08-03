#from typing import List
import json
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
import threading
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('BNx3h9w6l_MZRViXbepF-egoyDc_5y92CJr8R3MKdiF0')
service = SpeechToTextV1(authenticator=authenticator)
service.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/57915824-77d0-45b8-b08b-515adbe01138')

print("Connected to Watson!")

models = service.list_models().get_result()
print(json.dumps(models, indent=2))

model = service.get_model('en-US_BroadbandModel').get_result()
print(json.dumps(model, indent=2))


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
    with open('/app/app/test.mp3','rb') as audio_file:
        return  service.recognize(
                audio=audio_file,
                content_type='audio/mp3',
                timestamps=True,
                word_confidence=True).get_result()
