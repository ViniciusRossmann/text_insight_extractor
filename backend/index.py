import pickle
from flask import Flask, request, send_file, jsonify

model = pickle.load(open("./models/LogisticRegressionTextClassifier", 'rb'))
vectorizer = pickle.load(open("./models/vectorizer", 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "teste"

@app.route('/classifications', methods=['POST'])
def classify():
    data = request.get_json()

    print(data)
    
    if 'text' not in data:
        return jsonify({'erro': 'O campo "texto" é obrigatório'}), 400

    texto = data['text']
    linhas = texto.split('\n')
    
    text_vectorizer = vectorizer.transform(linhas)
    predictions = model.predict(text_vectorizer)
    
    resultado = {}
    for i, linha in enumerate(linhas, start=0):
        resultado[linha] = predictions[i]
    return jsonify(resultado)

if __name__ == "__main__":
    app.run()