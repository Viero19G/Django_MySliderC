import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credenciais.json", scope
    )

    gc = gspread.authorize(credentials)
    return gc