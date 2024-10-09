# NextWordPrediction

This is a simple project to predict the next word in a sentence using  Long Short-Term Memory (LSTM) cells. The model is trained on a corpus of text data and then used to predict the next word in a sentence.


## Dataset and Code

- The dataset and code is provided in dataset&Code folder. The dataset is a text file containing a large corpus of text data. The code is a jupyter notebook that contains the code to train the model and save it.

## Model

- `nextWordModel.pkl` is the trained model that is used to predict the next word in a sentence.

- `tokenizer.pkl` is the tokenizer used to convert the text data into sequences of integers.

## How to use

1. Clone the repository

```bash

git clone https://github.com/vsatyakiran/NextWordPrediction.git

```

2. create a virtual environment and install the required packages

```bash
     
cd NextWordPrediction
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

3. Run the app

```bash

python app.py

```

4. Open the browser and go to http://127.0.0.1:5000/