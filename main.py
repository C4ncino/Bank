from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from bank import Bank

app = Flask(__name__)
bank = Bank()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.json:
        if request.json['account'] != '':

            if bank.search_account(request.json['account']):
                account_item = bank.get_account(request.json['account'])
                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance()
                }), 201
            
            return jsonify({'error' : "Account Does not exists"})
        
        else:
            abort(404)
    else:
        abort(404)

@app.route('/new_account', methods=['GET'])
def new_account():
    account = bank.add_account()

    return jsonify({
        'account' : account.get_account(), 
        'balance': account.get_balance()
    })

@app.route('/menu', methods=['GET'])
def menu():
    account = request.args.get('account')
    message = request.args.get('message')
    action = request.args.get('action')

    return render_template('account_options.html', account = account, balance = bank[account], message = message, action = action)
    

@app.route('/deposit', methods=['POST'])
def deposit():
    if request.json:
        if request.json['account'] != '' and request.json['amount'] != '':

            account = request.json['account']
            amount = int(request.json['amount'])

            if bank.search_account(account):
                account_item = bank.get_account(account)
                account_item.deposit(amount)
                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance(),
                    'message': 'Depósito Realizado',
                    'action': 1
                })
            
            abort(404)
        
        else:
            abort(404)
    else:
        abort(404)

@app.route('/withdrawal', methods=['POST'])
def withdrawal():
    if request.json:
        if request.json['account'] != '' and request.json['amount'] != '':

            account = request.json['account']
            amount = int(request.json['amount'])

            if bank.search_account(account):
                account_item = bank.get_account(account)
                message = ""
            
                if not account_item.whitdrawal(amount): 
                    message = "No tienes tanto Pa, retira menos, No te endeudes"
                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance(),
                    'message': message,
                    'action': 2
                })    
            
            abort(404)
        
        else:
            abort(404)
    else:
        abort(404)

@app.route('/transfer', methods=['POST'])
def transfer():
    if request.json:
        if request.json['origin'] != '' and request.json['amount'] != '' and request.json['destiny']:

            origin = request.json['origin']
            destiny = request.json['destiny']
            amount = int(request.json['amount'])

            if bank.search_account(origin):
                account_item = bank.get_account(origin)
                message = ""
            
                if not bank.transfer(origin, destiny, amount):
                    message = "La cuenta destino no existe Pa o No tienes tanto"

                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance(),
                    'message': message,
                    'action': 3
                })    
            
            abort(404)
        
        else:
            abort(404)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
