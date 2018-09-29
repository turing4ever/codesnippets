import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('testgspread-2e1000ac98bd.json', scope)
gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("test_google_sheet").sheet1

wks.update_acell('B2', "it's working.")

# Fetch a cell range
cell_list = wks.range('A1:B7')
