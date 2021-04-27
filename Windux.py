import time
import datetime
from terminaltables import AsciiTable

def windux():
    while True:
        time.sleep(2)
        ans=True
        ans=input("Windux:")
        if ans=="-help":
            table_data = [
                ['COMMANDS', 'DEFENITION'],
                ['"-help"', 'Print commands list'],
                ['"-date"', 'Print complete date'],
                ['"-file; edit.txt"', 'Create and edit text files'],
                ['"-file; edit.bat"', 'Create ans edit bat files'],
                ['"-version"', 'Print version of the Terminal'],
                ['"-ck.updates"', 'Check updates']
            ]
            table = AsciiTable(table_data)
            print(table.table)

        elif ans=="-date":
            date = datetime.datetime.now()
            print(date)

        elif ans=="-file; edit.txt":
            file_txt = open('file.txt', 'a')
            file_txt_write = True
            file_txt_write = input("File write:")
            file_txt.write(file_txt_write, "\n")
            file_txt.close()

        elif ans=="-file; edit.bat":
            file_bat = open('file.bat', 'a')
            file_bat_write = True
            file_bat_write = input("File write:")
            file_bat_write(file_bat_write, "\n")
            file_bat.close()

        elif ans=="-version":
            print("Version: Windux 1.0.0")

        elif ans=="-ck.updates":
            print("You already have the most updated version of Windux 1.0.0")
            

        else:
            print("Command or syntax incorrect!")
windux()

