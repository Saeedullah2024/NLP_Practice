import re
from fastapi import FastAPI
from pydantic import BaseModel , Field , StrictStr , StrictInt

app = FastAPI()

class contactinfo(BaseModel):
    text : StrictStr = Field(... , description="This is the Text to be Extracted Contact Information")
   
@app.post("/contact_info")
def extract_contact_info(state : contactinfo):
    text = state.text.strip()
    #Patterns
    
    pattern = r'(\d{11}|\d{4}-\d{7}|\+\d{10,11})'
    pattern_age = r'\(age\s+(\d+)\)'
    pattern_name = r'Born\s+(.+?)\s+\d{1,2}\s+[A-Za-z]+\s+\d{4}'
    pattern_birthplace = r'\(age\s+\d+\)\s+(.+?)(?:\s+and contact|$)'

    #Findings
    phoneno = re.findall(pattern , text)
    age = re.findall(pattern_age , text)
    name = re.findall(pattern_name , text)
    birthplace = re.findall(pattern_birthplace , text)
    #Adding
    phone = phone if phoneno else "Not found"
    age = age if age else "Not found"
    name = name if name else "Not found"
    birthplace = birthplace if birthplace else "Not found"

    #Returning
    return {
        "Extracted_Phone_Number" : phone,
        "Extracted_Name" : name,
        "Extracted_Age" : age,
        "Extracted_birthplace" : birthplace
    }

