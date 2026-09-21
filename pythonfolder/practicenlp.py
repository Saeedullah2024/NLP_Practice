import re
from fastapi import FastAPI
from pydantic import BaseModel , Field , StrictStr , StrictInt

app = FastAPI()

class contactinfo(BaseModel):
    text : StrictStr = Field(... , description="This is the Text to be Extracted Contact Information")
    phone : StrictInt = Field(... , description="This is the Phone Number to be Extracted")

@app.post("/contact_info")
def extract_contact_info(state : contactinfo):
    text = state.text 
    pattern = r'(\d{11}|\d{4}-\d{7}|\+\d{10,11})'
    phoneno = re.findall(pattern , text)
    state.phone = phoneno
    return {
        "Extracted_Phone_Number" : state.phone
    }
