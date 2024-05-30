from flask import Flask,render_template,request,redirect

from utils.encrypt import encyptToMorse
from utils.decrypt import decryptFromMorse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET','POST'])
def encrypt():
    input_text = request.form.get('inputdata')
    if not input_text:
        return redirect('/')
    
    encrypted_text = encyptToMorse(input_text)

    data = {
        "operation": 'Encrypted',
        "original": input_text,
        "result" : encrypted_text
    }

    return render_template('result.html', data=data)

@app.route('/decrypt', methods=['GET','POST'])
def decrypt():
    input_text = request.form.get('inputdata')
    if not input_text:
        return redirect('/')
    
    decrypted_text = decryptFromMorse(input_text)

    data = {
        "operation": 'Decrypted',
        "original": input_text,
        "result" : decrypted_text
    }
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)