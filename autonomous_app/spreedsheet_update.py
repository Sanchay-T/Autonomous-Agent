import gspread
import json

from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
spreadsheet = client.open('Agent')
worksheet = spreadsheet.get_worksheet(0)

worksheet.update_cell(1, 1, 'Name')
worksheet.update_cell(1, 2, 'Phone Number')
worksheet.update_cell(1, 3, 'Summary')
worksheet.update_cell(1, 4, "Status")
worksheet.update_cell(1, 5, "Chat duration")
worksheet.update_cell(1, 6, "Chats interactions")


import os

def update_in_gsheets(botresponse):
    filepath = os.path.join("autonomous_app", "data.json")
    json_response = json.loads(botresponse)
    with open(filepath, 'w') as file:
        file.write(json_response)
    file.close()

    # Append the rows to the spreadsheet
    for row in json_response:
        worksheet.append_row([row['Name'], row['Phone Number'], row['Summary'], row['Status']])