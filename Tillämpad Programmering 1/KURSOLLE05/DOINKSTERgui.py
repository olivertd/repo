import PySimpleGUI as sg
import time
from pathlib import Path
import time
import sys

sg.theme('DarkPurple6')   # Sätter TEMAT VAPORWAVE PURPLE!!!!!

#Gör en funktion för MAIN MENUWINDOWS som välkommnar användaren
def mainmenuwindow():
    layout = [  [sg.Text("""Enter number
1 : View Balance
2 : Deposit
3 : Withdraw
4 : View transactions
5 : Terminate account
6 : Exit
""")],
                [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6')] ]


    # Create the Window
    window = sg.Window('Window Title', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'GOOOO TO YOUR EMPTY BANK ACCOUNT!': # if user closes window or clicks cancel
            break

#Gör en funktion för WELCOME WINDOWS som välkommnar användaren
def welcomewindow():
    layout = [  [sg.Text('WELCOME TO SELK FINANCIAL BANK APP')],
                [sg.Text('YOU ARE STILL POOR')],
                [sg.Text('LEEETS GO!!!')],
                [sg.Button('GOOOO TO YOUR EMPTY BANK ACCOUNT!'),] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'GOOOO TO YOUR EMPTY BANK ACCOUNT!': # if user closes window or clicks cancel
        window.close()
        mainmenuwindow()

            

#Kör funktionen för att öppna welcome window
welcomewindow()