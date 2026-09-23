from fastapi import FastAPI
from transformers import BertTokenizer , BertForMaskedLM
from pydantic import BaseModel , Field , StrictInt , StrictStr
import torch
app = FastAPI()

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")

class TextInput(BaseModel):
    text : StrictStr = Field(..., description="This is the text having missing value") 

@app.post("/get_missing_value")
def FindMaskedValue(state : TextInput):
    sentence = state.text.strip()
    inputs = tokenizer(sentence , return_tensors = "pt")
    outputs = model(**inputs)
    mask_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]
    predictions = outputs.logits[0 , mask_index].softmax(-1)
    top5 = torch.topk(predictions, 5 , dim=1)
    listwords = []
    for score , index in  zip(top5.values[0], top5.indices[0]):
        word = tokenizer.decode([index])
        listwords.append(word)
    corrected = sentence.replace("[MASK]", listwords[0])
    return {
        "Completed_Text" : corrected
    }
