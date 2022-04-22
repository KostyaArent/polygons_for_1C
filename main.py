from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from calculation import get_occurrence, calc_main


app = FastAPI()


@app.post("/")
async def getInformation(info : Request):
    req_info = await info.json()
    result = calc_main(req_info['fields'], req_info['districts'])
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "ru-ru"}
    return JSONResponse(content=result, headers=headers)