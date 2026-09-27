from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

sentence = "This is a sample sentence, showing off the stop words filtration."

tokens = word_tokenize(sentence)
#print(tokens) #This is list of tokens

stemmed = PorterStemmer()

print("This is the Stemmization")
for words in tokens:
    print(f"{words} -------- {stemmed.stem(words)}")

lemmitizer = WordNetLemmatizer()

#lemmization is the best
print("This is lemmization")
for words in tokens:
    print(f"{words} ------- {lemmitizer.lemmatize(words , pos='v')}")

# import nltk
# nltk.download('stopwords')
stopwordseng = stopwords.words("english")

print(f"{tokens} --- {pos_tag(tokens)}") #Pos tag want list of words