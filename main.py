from fastapi import FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from calculation import get_occurrence, calc_main_alter
import json


app = FastAPI()


@app.post("/multipoligon/intersection")
async def getInformation(info : Request):
    #try:
    req_info = await info.json()
    # req_info = dict(req_info)
    result = calc_main_alter(req_info['fields'], req_info['districts'])
    headers = {"X-Cat-Dog": "alone", "Content-Language": "en-en"}
    return JSONResponse(content=result, headers=headers)
    # except:
    #     raise HTTPException(status_code=422, detail="Unprocessable Entity")
    # 