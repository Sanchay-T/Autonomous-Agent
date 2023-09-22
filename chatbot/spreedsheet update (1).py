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




with open('data.json', 'r') as file:
    data = json.load(file)

# Append the rows to the spreadsheet
for row in data:
    worksheet.append_row([row['Name'], row['Phone Number'], row['Summary'], row['Status']])