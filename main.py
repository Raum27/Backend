from fastapi import FastAPI
from typing import Optional
from module.summarize_text import Sumary_text
from module.user import User
from storage.contents import get_all_contents,get_all_contents2
from sumarizer import gen_summarizer 
from storage import storage_ID as setid
import pandas as pd
app = FastAPI()


@app.get("/")
async def root():
    return {"Hello":"world"}


@app.get("/contents")  # for all contents 
async def send_aricle():
    contents =  get_all_contents()
    return contents


@app.get("/summarizer/")  # for summarizer text
async def gen_Text(text:Optional[str]=None): # query parameter
    word =''
    for i in gen_summarizer(text):
        word +=i
    data = Sumary_text(contents=word)
    return data

@app.post("/register")  # for login
async def register_route(ID:Optional[User]=None):
    setid.add_id(ID)
    print(setid.get_id())
    return True


@app.post("/login")  # for login
async def login_route(ID:Optional[User]=None):
    checklist=setid.get_id()
    print(checklist)
    for i in checklist:
        if i==ID:
            return {'status':True}
    return {'status':False}

@app.get("/Sepcontents")  # for login
async def test_route():
    return get_all_contents2()


# uvicorn main:app --host 192.168.1.226 --port 8000 --reload
# uvicorn main:app --port 8000 --reload 

if __name__ == "__main__":
     print("hello")