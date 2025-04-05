from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import time
import requests
import os
from dotenv import load_dotenv
from upload_data import update_s3, consume_data

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_KEY") 
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    ## AUTENTICAÇÃO BASICA ##
    if username == os.getenv("USERNAME_API") and password == os.getenv("PASSWORD_API"):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"erro": "Usuário ou senha inválidos!"}), 401

@app.route('/obesitydataset', methods=['GET'])
# @jwt_required()
def braindataset():
    try:
        consume_data.download_data()
        update_s3.insert_s3()
        return jsonify({"Concluido": "QO insert foi realizado no S3, favor verifique !!"})
    
    except Exception as e:
        return jsonify({"Falha": f"Erro: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)