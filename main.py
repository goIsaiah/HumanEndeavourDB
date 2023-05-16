import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1DZPcFBd1BIfNPw6L297mNe91pCfsuJBOGePOGyIHa3E"

LIST = ["T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ",
        "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ",
        "BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BK", "BL"]


def main():
    credentials = None
    if os.path.exists("token.json"):  # if token used for authentication exists
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)  # load the token.json file
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:  # enters this if statement if the credentials are not valid
            credentials.refresh(Request())
        else:  # load credentials file
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json",
                  "w") as token:  # create the token.json file using the credentials.json file since it didn't exist before
            token.write(credentials.to_json())
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        input1 = str(input("Enter the row you want to edit: "))
        # TODO: Take row number from input1 and join it with the list values
        # TODO: Create for loop that will iterate through the list and update each cell in the row
        for x in LIST:
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Main!" + x + input1,
                                   valueInputOption="USER_ENTERED", body={"values": [["TRUE"]]}).execute()

    except HttpError as error:
        print(error)


if __name__ == "__main__":
    main()
