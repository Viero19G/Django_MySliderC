from google.oauth2 import service_account
from google.auth.transport import requests
from oauth2client.service_account import ServiceAccountCredentials
import gspread


def authenticate_google_sheets_token():
    # Caminho para o arquivo JSON de credenciais
    credenciais_json = "credenciais.json"
    try:
        # Carregue as credenciais OAuth 2 a partir de um arquivo JSON
        credentials = service_account.Credentials.from_service_account_file(
            credenciais_json,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )

        # Crie um token OAuth 2
        credentials.refresh(requests.Request())
        access_token = credentials.token

        return access_token
    except Exception as e:
        # Lidar com erros de autenticação
        print(f"Erro na obtenção do token OAuth 2: {str(e)}")
        return None


def authenticate_google_sheets():
    # Carregue as credenciais OAuth 2 a partir de um arquivo JSON
    credenciais_json = "credenciais.json"
    credentials = service_account.Credentials.from_service_account_file(
        credenciais_json,
        scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive.readonly']
    )
    # Autentique-se com o cliente gspread
    gc = gspread.authorize(credentials)

    # Obtenha um token de acesso
    credentials.refresh(requests.Request())
    access_token = credentials.token

    return credentials, access_token
