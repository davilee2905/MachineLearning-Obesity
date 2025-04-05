import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

def download_data():
    kaggle_json_path = r"C:\Users\Davi Lee\Documents\ML-Obesidade\kaggle.json"

    if os.path.exists(kaggle_json_path):
        with open(kaggle_json_path, 'r') as f:
            kaggle_creds = json.load(f)

        os.environ['KAGGLE_USERNAME'] = kaggle_creds['username']
        os.environ['KAGGLE_KEY'] = kaggle_creds['key']

        api = KaggleApi()
        api.authenticate()

        dataset = 'adeniranstephen/obesity-prediction-dataset'
        api.dataset_download_files(dataset, path='datasets', unzip=True)
        print("Dataset baixado com sucesso.")
    else:
        print(f"Arquivo {kaggle_json_path} não encontrado. Verifique o caminho e tente novamente.")