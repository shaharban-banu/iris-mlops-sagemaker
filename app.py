from fastapi import FastAPI,Request
import pickle
import json
import numpy as np
from pydantic import BaseModel

app=FastAPI()

with open("model.pkl","rb") as f:
    model=pickle.load(f)

CLASS_NAMES=["setosa","versicolor","virginica"]

class InputData(BaseModel):
    data:list

@app.get("/ping")
def ping():
    return {"status":"ok"}


@app.post("/invocations")
async def invoke(input_data:InputData):
    body= np.array(input_data.data)
    # data=json.loads(body.decode("utf-8"))
    # data=np.array(data)
    preds=model.predict(body)
    labels=[CLASS_NAMES[p] for p in preds]
    return {"prediction":labels}