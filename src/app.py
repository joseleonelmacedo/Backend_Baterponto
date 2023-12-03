import os, json
from flask import Flask, jsonify, request

app = Flask(__name__)

users_database = os.path.join(os.path.dirname(__file__), 'database', 'users.txt')
registers_database = os.path.join(os.path.dirname(__file__), 'database', 'registers.txt')

def check_user_credentials(email, password):
    # Read the user data from the text file and check if the credentials match
    try:
        with open(users_database, 'r', encoding="utf-8") as file:
            for line in file:
                user_data = json.loads(line)
                if user_data.get("email") == email and user_data.get("password") == password:
                    return True

    except Exception as ex:
        print("Error on check_user_credentials: ", ex)
    return False

def get_users(email):
    # Read the user data from the text file and check if the credentials match
    users = []
    try:
        with open(registers_database, 'r', encoding="utf-8") as file:
            for line in file:
                user_data = json.loads(line)
                print("user_data > ", user_data)
                if user_data.get("email") == email:
                    users.append(user_data)

    except Exception as ex:
        print("Error on get_users: ", ex)

    return users

@app.route('/sidi_ponto/v1/cadastro', methods=['POST'])
def cadastro():
    data = json.loads(request.data)
    response = None

    if 'name' in data and 'email' in data and 'password' in data:
        user = {
            'name': data['name'],
            'email': data['email'],
            'password': data['password']
        }

        try:
            with open(users_database, 'a', encoding="utf-8") as json_file:
                json_file.write(json.dumps(user) + '\n')
            response = jsonify({'message': 'Usuário cadastrado com sucesso!', 'status_code': 200}), 200
            return response
        except Exception as ex:
            print("Error on cadastro: ", ex)

    response = jsonify({'message': 'Erro nome, email, or senha', 'status_code': 400}), 400
    return response


@app.route('/sidi_ponto/v1/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    response = None

    if 'email' in data and 'password' in data:
        email = data['email']
        password = data['password']

        # Check the user's credentials in the text file
        if check_user_credentials(email, password):
            response = jsonify({'message': 'Login successful!', 'status_code': 200, "email": email}), 200
            return response
        else:
            response = jsonify({'message': 'Invalid email or password', 'status_code': 401}), 401
            return response
    else:
        response = jsonify({'message': 'Missing email or password', 'status_code': 400}), 400
        return response


@app.route('/sidi_ponto/v1/criar', methods=['POST'])
def criar_ponto():
    data = json.loads(request.data)
    response = None

    if 'email' in data and 'date' in data and ('entries' in data or 'exits' in data):
        item = {
            'email': data['email'],
            'date': data['date'],
            'entries': data.get('entries', None),
            'exits': data.get('exits', None) 
        }

        try:
            with open(registers_database, 'a', encoding="utf-8") as json_file:
                json_file.write(json.dumps(item) + '\n')
            response = jsonify({'message': 'Ponto registradom com sucesso!', 'status_code': 200}), 200
            return response
        except Exception as ex:
            print("Error on cadastro: ", ex)

    response = jsonify({'message': 'Error ao bater o ponto. Verifique as informação e tente novamente.', 'status_code': 400}), 400
    return response


@app.route('/sidi_ponto/v1/listar', methods=['POST'])
def listar_ponto():
    data = json.loads(request.data)
    response = None

    if 'email' in data:
        try:
            users = get_users(data["email"])
            response = jsonify({'data': users, 'status_code': 200}), 200
            return response
        except Exception as ex:
            print("Error on listar_ponto: ", ex)

    response = jsonify({'message': 'Error ao recuperar ponto.', 'status_code': 400}), 400
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
