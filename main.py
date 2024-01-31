from flask import Flask, render_template, request, redirect, url_for
from random import randint as ri

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    account = request.form['account']
    try:
        bank[account]
        
        return redirect(url_for('menu', account = account, message = "", action = 0))
    except:
        return render_template('not_valid.html')

@app.route('/new_account', methods=['GET'])
def new_account():
    account = ""

    for i in range(5):
        account += str(ri(0,9))
    
    bank[account] = 0
    
    return redirect(url_for('menu', account = account, message = "", action = 0))

@app.route('/menu', methods=['GET'])
def menu():
    account = request.args.get('account')
    message = request.args.get('message')
    action = request.args.get('action')

    return render_template('account_options.html', account = account, balance = bank[account], message = message, action = action)
    

@app.route('/deposit', methods=['POST'])
def deposit():
    account = request.form['account']
    amount = int(request.form['amount'])

    bank[account] += amount 
    message = "Depósito Realizado"
    
    return redirect(url_for('menu', account = account, message = message, action = 1))


@app.route('/withdrawal', methods=['POST'])
def withdrawal():
    account = request.form['account']
    amount = int(request.form['amount'])
    message = ""

    if bank[account] < amount:
        message = "No tienes tanto Pa, retira menos, No te endeudes"
    else:
        bank[account] -= amount 
    
    return redirect(url_for('menu', account = account, message = message, action = 2))

@app.route('/transfer', methods=['POST'])
def transfer():
    origin = request.form['origin']
    destiny = request.form['destiny']
    amount = int(request.form['amount'])
    message = ""
    
    try:
        bank[destiny]
        
        if bank[origin] < amount:
            message = "No tienes tanto Pa, retira menos, No te endeudes"
        else:
            bank[origin] -= amount
            bank[destiny] += amount
    except:
        message = "La cuenta destino no existe Pa"
    
    return redirect(url_for('menu', account = origin, message = message, action = 3))


if __name__ == '__main__':
    bank = {}
    app.run(debug=True)
