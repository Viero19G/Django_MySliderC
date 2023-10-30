import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Caminho para o arquivo JSON de credenciais
    credentials_path = "credenciais.json"

   # Carregar as credenciais a partir do arquivo
    with open(credentials_path, "r") as json_file:
        credentials = json.load(json_file)

    # Autenticação usando as credenciais
    gc = gspread.authorize(credentials)

    return gc