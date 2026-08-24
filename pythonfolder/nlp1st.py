from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import sent_tokenize , word_tokenize
from nltk.corpus import stopwords
from fastapi import FastAPI
from pydantic import BaseModel , Field , StrictStr
from nltk.tag import pos_tag

app = FastAPI()

class Word(BaseModel):
    word : StrictStr = Field(... , description="This is the Word to be Lemmatize")
    
class Sentence(BaseModel):
    sentence : StrictStr = Field(..., description="This is the Sentence given")
    
class SentencePos(BaseModel):
    sentence : StrictStr = Field(..., description="This is the Text to be converted into Part of Speech")
    
@app.post("/word_lemmatize")
def word_into_stem(state : Word):
    word = WordNetLemmatizer()
    wordlem = word.lemmatize(state.word , pos='v')
    return {
        "Lemmatized_word" : wordlem
    }

@app.post("/sentence_stemmer")
def sentence_lemmatize(state : Sentence):
    stopwordlist = stopwords.words('english')
    sentence = state.sentence
    lemitizer = WordNetLemmatizer()
    sentences = sent_tokenize(sentence)
    for i in range(len(sentences)):
        words = word_tokenize(sentences[i])
        words = [lemitizer.lemmatize(word) for word in words if word not in stopwordlist]   
        sentences[i] = " ".join(words)
    return {
        "sentence_stemmed" : " ".join(sentences)
    }

@app.post("/sentence_pos")
def pos_fun(state : SentencePos):
    sentence = state.sentence
    stopwordList = stopwords.words('english')
    sentences = sent_tokenize(sentence)
    for i in range(len(sentences)):
        words = word_tokenize(sentences[i])
        words = [word for word in words if word not in stopwordList]
        postagsword = pos_tag(words)
        return {
            "Part_Of_Speech" : postagsword 
        }
