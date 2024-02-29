from flask import Flask, request, jsonify,render_template,redirect
from flask_cors import CORS, cross_origin
import pandas as pd
from keras.models import load_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import whois

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

model = load_model('model_h5.h5')
data = pd.read_csv("D:\\BT\\data.csv")
data['label'].replace(['good','bad'], [0, 1], inplace = True )

X = data['url']
Y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, Y , test_size=0.3, stratify=data['label'], random_state=0)

tokenizer = Tokenizer(filters='', char_level=True, lower=False, oov_token=1)

tokenizer.fit_on_texts(X)

def process(url):
    tokenized_url = tokenizer.texts_to_sequences([url])

    sequence_length = 160

    final_url = pad_sequences(tokenized_url, padding='post', maxlen=sequence_length)

    res = model.predict(final_url)

    return "phishing" if res > 0.5 else "safe"

@app.route('/main', methods=["POST"])
def main():
    if request.method == 'POST':
        print("Received request:")
        print(request.data)
        print("Request Headers:")
        print(request.headers)
        current_url = request.data.decode("utf-8")
        print("Current URL received:", current_url)
        res = process(current_url)
        print(res)
        return jsonify(result=res)
    # Process the current URL as needed
    return "data received"
        # url = request.data.decode("utf-8")
        # return url

@app.route("/")
def input_url():
    return render_template("index.html")

# @app.route("/info", methods=['GET', 'POST'])
# def info():
#     link = request.data.decode("utf-8")
#     ll = 'https://www.kaggle.com/code/nareshbhat/heart-attack-prediction-using-different-ml-models'
#     try:
#         test = whois.whois(ll)

#         return test
#     except whois.parser.PywhoisError as e:
#         return f"Error: {str(e)}"

@app.route("/info", methods=['GET', 'POST'])
def info():
    link = request.data.decode("utf-8")
    ll = 'https://www.kaggle.com/code/nareshbhat/heart-attack-prediction-using-different-ml-models'
    try:
        test = whois.whois(ll)
        domain_name = test.domain_name
        server_name = test.name_servers[0] if test.name_servers else None
        dnssec = test.dnssec
        org = test.org
        country = test.country
        creation_date = test.creation_date
        registrar = test.registrar
        state = test.state
        return render_template(
                "index.html",
                domain_name=domain_name,
                server_name=server_name,
                dnssec=dnssec,
                org=org,
                country=country,
                creation_date=creation_date,
                registrar=registrar,
                state=state
                )
    except whois.parser.PywhoisError as e:
        return render_template("index.html", error_message=str(e))
    # if request.method == 'POST':
    #     print(request.headers)
    #     link = request.data.decode("utf-8")
    #     print("in info ",link)
    #     if link:
    #         try:
    #             test = whois.whois(link)
    #             domain_name = test.domain_name
    #             server_name = test.name_servers[0] if test.name_servers else None
    #             dnssec = test.dnssec
    #             org = test.org
    #             country = test.country
    #             creation_date = test.creation_date
    #             registrar = test.registrar
    #             state = test.state

    #             return render_template(
    #                 "index.html",
    #                 domain_name=domain_name,
    #                 server_name=server_name,
    #                 dnssec=dnssec,
    #                 org=org,
    #                 country=country,
    #                 creation_date=creation_date,
    #                 registrar=registrar,
    #                 state=state
    #             )
    #         except whois.parser.PywhoisError as e:
    #             return render_template("index.html", error_message=str(e))
    #     else:
    #         return "Enter a valid URL"
    # return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

# full working code below
# from flask import Flask, request, jsonify,render_template,redirect
# from flask_cors import CORS, cross_origin
# import pandas as pd
# from keras.models import load_model
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

# model = load_model('model_h5.h5')
# data = pd.read_csv("D:\\BT\\data.csv")
# data['label'].replace(['good','bad'], [0, 1], inplace = True )

# X = data['url']
# Y = data['label']

# X_train, X_test, y_train, y_test = train_test_split(X, Y , test_size=0.3, stratify=data['label'], random_state=0)

# tokenizer = Tokenizer(filters='', char_level=True, lower=False, oov_token=1)

# tokenizer.fit_on_texts(X)

# def process(url):
#     tokenized_url = tokenizer.texts_to_sequences([url])

#     sequence_length = 160

#     final_url = pad_sequences(tokenized_url, padding='post', maxlen=sequence_length)

#     res = model.predict(final_url)

#     if res > 0.5:
#         return "phishing"
#     else:
#         return "safe"

# @app.route('/', methods=["POST"])
# def main():
#     if request.method == 'POST':
#         print("Received request:")
#         print(request.data)
#         print("Request Headers:")
#         print(request.headers)
#         current_url = request.data.decode("utf-8")
#         print("Current URL received:", current_url)
#         res = process(current_url)
#         print(res)
#     # Process the current URL as needed
#     return "data received"
#         # url = request.data.decode("utf-8")
#         # return url


# if __name__ == '__main__':
#     app.run(debug=True)