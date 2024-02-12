from flask import Flask, render_template, request, jsonify, abort
from flask_cors import CORS
from bank import Bank

app = Flask(__name__)
CORS(app)

bank = Bank()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.json:
        if request.json.get('account') != '':
            account = request.json['account']
            
            if bank.search_account(account):
                account_item = bank.get_account(account)
                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance(),
                    'success': True
                })
            
            abort(404)
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

@app.route('/get_accounts', methods=['GET'])
def menu():
    accounts = []

    for key, account in bank.get_accounts().items():
        accounts.append(
            {
                'account': account.get_account(),
                'balance': account.get_balance()
            }
        )

    return jsonify({'accounts': accounts})
    

@app.route('/deposit', methods=['POST'])
def deposit():
    if request.json:
        if request.json.get('account') != '' and request.json.get('amount'):

            account = request.json['account']
            amount = int(request.json['amount'])

            if bank.search_account(account):
                account_item = bank.get_account(account)
                account_item.deposit(amount)
                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance(),
                    'message': 'Depósito Realizado',
                    'success': True
                })
            
            abort(404)
        
        else:
            abort(404)
    else:
        abort(404)

@app.route('/withdrawal', methods=['POST'])
def withdrawal():
    if request.json:
        if request.json.get('account') != '' and request.json.get('amount'):

            account = request.json['account']
            amount = int(request.json['amount'])

            if bank.search_account(account):
                account_item = bank.get_account(account)
                message = ""
                success = True
            
                if not account_item.whitdrawal(amount): 
                    message = "No tienes tanto Pa, retira menos, No te endeudes"
                    success = False
                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance(),
                    'message': message,
                    'success': success
                })    
            
            abort(404)
        
        else:
            abort(404)
    else:
        abort(404)

@app.route('/transfer', methods=['POST'])
def transfer():
    if request.json:
        if request.json.get('origin') != '' and request.json.get('amount') and request.json.get('destiny') != '':

            origin = request.json['origin']
            destiny = request.json['destiny']
            amount = int(request.json['amount'])

            if bank.search_account(origin):
                account_item = bank.get_account(origin)
                message = ""
                success = True
            
                if not bank.transfer(origin, destiny, amount):
                    message = "La cuenta destino no existe Pa o No tienes tanto"
                    success = False
                
                return jsonify({
                    'account' : account_item.get_account(), 
                    'balance': account_item.get_balance(),
                    'message': message,
                    'success': success
                })    
            
            abort(404)
        
        else:
            abort(404)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
