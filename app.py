from flask import Flask , render_template , request
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import pickle


app = Flask(__name__)
lemmatize = WordNetLemmatizer()
stop_word = set(stopwords.words("english"))


def load_model():
    global model , cv
    model = pickle.load(open("spam_ham_project.pkl" , "rb"))  
    cv = pickle.load(open("vectorized.pkl" , "rb")) 


def remove_punctuation(text):
    new_text = text
    import string
    for i in new_text:
        if i in string.punctuation:
            new_text = new_text.replace(i , "")
    return new_text
    
def lower(text):
    return str(text).lower()


def tokenize(text):
    return word_tokenize(text)

def remove_digits(ls):
    f_list = []
    for i in ls:
        if i.isalpha():
            f_list.append(i)
    return f_list


def remove_stopwords(ls):
    f_list = []
    for i in ls:
        if i not in stopwords.words("english"):
            f_list.append(i)
    return f_list


def lemmat(ls):
    f_list = []
    for i in ls:
        a = lemmatize.lemmatize(i , pos="v")
        f_list.append(a)
    return f_list 


def join_words(ls):
    return " ".join(ls)


def preprocess(text):
    text = remove_punctuation(text)
    text = lower(text)
    text = tokenize(text)
    text = remove_digits(text)
    text = remove_stopwords(text)
    text = lemmat(text)
    text = join_words(text)
    return text


def predict_message(msg):
    msg = preprocess(msg)
    v = cv.transform([msg])
    result = model.predict(v)[0]
    if result == "spam":
        return "SPAM MESSAGE"
    else:
        return "NORMAL MESSAGE"

@app.route("/" , methods = ["GET" , "POST"])
def home():
    result = ""

    if request.method == "POST":
        message = request.form.get("message")
        load_model()
        result = predict_message(message)
    return render_template("index.html"  , result = result)


if __name__ == "__main__":
    app.run(debug=True , port=5000)
