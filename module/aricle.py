from pydantic import BaseModel
class Aricle(BaseModel):
    title:str=''
    image:str=''
    contents:str=''

    