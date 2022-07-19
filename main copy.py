import time
import traceback
from pybit import inverse_perpetual
from time import sleep
from datetime import datetime
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import pytz
import telebot
import os





scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("haynes-bybit-b58869a98ed4.json", scope)

googleClient = gspread.authorize(creds)

sheet = googleClient.open("Trades - Bybit").worksheet("Sheet2")





def test_app():
    allRows = []

    allRows.append(["Test", "Test", "Test", "Test", "Test", "Test", 0.4, "Test", 0.5, "Test", "Test", "Test", "Test", "Test", "", "", "=((P4-O4)/O4) * 100", "Test", "=(Q4-R4)/ABS(R4)"])

    sheet.insert_rows(allRows, row=4, value_input_option='USER_ENTERED')



def main():
    # poll_bybit()
    test_app()
    



if __name__ == "__main__":
    main()