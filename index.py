from typing import Optional
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, Request
from fastapi.responses  import RedirectResponse
from fastapi.responses import JSONResponse
from bins import mydict, get_bin_info
import re
from pydantic import BaseModel
import urllib

app = FastAPI(debug=True, 
              title="Bin lookup By Ayan.", 
              redoc_url=None,
              description=" Feel free to use. made by @Ay_4n.")




class UnicornException(Exception):
    def __init__(self, name: str,  message: str):
        self.name = name
        self.message = message


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={'success': False, "message": exc.message},
    )


@app.get("/bin/{bin1}")
async def bin(bin1):
    price = bin1
    if not price.isdigit():
        raise HTTPException(
            status_code=404, detail="Give me 6 digits Numbers.")
    elif len(price) < 6:
        raise HTTPException(
            status_code=404, detail="Give me 6 numbers atleast.")
    bin = price[:6]
    bin_data = get_bin_info(bin)
    if not bin_data:
        raise HTTPException(status_code=404, detail="Bin Not Found")
    return {
        'bin': bin,
        'bank': bin_data['bank_name'],
        'country_iso2': bin_data['iso'],
        'country': bin_data['country'],
        'flag': bin_data['flag'],
        'brand': bin_data['vendor'],
        'type': bin_data['type'],
        'level': bin_data['level'],
        'prepaid': bin_data['prepaid'],                                                                               
    }


@app.get("/")
async def start():
    return RedirectResponse("http://www.github.com/")

