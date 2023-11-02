import pickle
import re
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from nltk import download
download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

model = pickle.load(open("./models/LogisticRegressionTextClassifier", 'rb'))
vectorizer = pickle.load(open("./models/vectorizer", 'rb'))

app = Flask(__name__)
CORS(app)

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.lower().split()
    words = [word for word in words if word not in stopwords.words('portuguese')]
    stemmer = SnowballStemmer('portuguese')
    words = [stemmer.stem(word) for word in words]
    return ' '.join(words)

@app.route('/', methods=['GET'])
def home():
    return "running"

@app.route('/classifications', methods=['POST'])
def classify():
    data = request.get_json()
    
    if 'text' not in data:
        return jsonify({'error': 'O campo "texto" é obrigatório'}), 400

    texto = data['text']
    linhas = texto.split('\n')
    linhas_processadas = [preprocess_text(item) for item in linhas]
    
    text_vectorizer = vectorizer.transform(linhas_processadas)
    predictions = model.predict(text_vectorizer)
    
    resultado = [{"text": linha, "classification": predictions[i]} for i, linha in enumerate(linhas) if linha]
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)