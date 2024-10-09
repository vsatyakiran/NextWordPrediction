import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from flask import Flask, request, jsonify, render_template
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open("nextWordModel.pkl", "rb"))
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
maxlen = 18


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    text = data.get('text', '')

    # Tokenize and pad the input text
    token_text = tokenizer.texts_to_sequences([text])[0]
    padded_token_text = pad_sequences([token_text], maxlen=maxlen+1, padding='pre')
    
    suggested_words = [text]


    for  _ in range(5):
        token_text = tokenizer.texts_to_sequences([suggested_words[-1]])[0]
        padded_token_text = pad_sequences([token_text],maxlen=19,padding='pre')
        pos = np.argmax(model.predict(padded_token_text))
        for word,index in tokenizer.word_index.items():
            if index == pos:
                    text = text + " " + word
                    suggested_words.append(text)
                    break
    return jsonify({'suggestions': suggested_words})

if __name__ == '__main__':
    app.run(debug=True)
