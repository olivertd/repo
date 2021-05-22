#ALLA IMPORTS
import PySimpleGUI as sg
import time
from pathlib import Path
import time
import sys


#FIXA BUGG TA BORT WHILE TRUE SATSER PÅ EVENT
transaktionslista = []

#Här är en funktion för en ruta, just denna är för terminationsrutan
def terminationwindow():

    layout = [[sg.Text('THIS IS THE TERMINATE ACCOUNT PAGE, WARNING!!', font='Helvetica 30')],
    [sg.Text('WARNING! IF YOU CLICK TERMINATE BUTTON THERE IS NO TURNING BACK!', font='Helvetica 30')],            
                 [sg.Button('TERMINATE ACCOUNT'), sg.Button('BACK to main menu')]]

    # Create the Window
    window = sg.Window('DJ BOLIVER BANK 2', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        window.close()
    if event == 'BACK to main menu': # Om användaren klickar på back
        window.close()
        mainmenuwindow()
    if event == 'TERMINATE ACCOUNT': # Om användaren klickar på terminate account
        window.close() #stänger rutan och resettar filerna som är länkade
        file_path1 = Path('balance.txt')
        file_path1.unlink()
        file_path2 = Path('transactions.txt')
        file_path2.unlink()



#funktion för transaktion window
def transactionwindows():
    transaktionslista.clear()
    minfil = open('transactions.txt')
    transactions_list = minfil.readlines()

#här är layouten
    layout =  [[sg.Text('Transactions')],
            [sg.Multiline(default_text=transactions_list, size=(62, 10))],
            [sg.Button('BACK to')],
            [sg.Text('DJ BOLIVER HASSAN FINANCIAL BANK APP', justification='center', size=(62, 1), font='Helvetica 10')]]
        
    window = sg.Window('dddDJ BOLIVER HASSAN FINANCIAL BANK APP', layout)

    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        window.close()
    if event == 'BACK to': #om användaren kilickar på back
        window.close()
        mainmenuwindow()


#Sätter TEMAT VAPORWAVE PURPLE!!!!!
sg.theme('DarkPurple6')  

#KOLLAR OM FILERNA FINNS (BALANCE.TXT) O TRANSACTIONS.TXT
if Path('balance.txt').is_file() and Path('transactions.txt').is_file():
    pass
else:
    with open('balance.txt', 'w+') as f:
       f.write("1000")
    with open('transactions.txt', 'w+') as f:
        pass

#kollar balansen
with open('balance.txt') as f:
    balanceerz = f.read()

#Funktion för att deposita mängden som är i deposit värdet
#def depositfunction():
    

#Gör en funktion för WELCOME WINDOWS som välkommnar användaren
def welcomewindow():
    layout = [  [sg.Text('WELCOME TO DJ BOLIVER HASSAN FINANCIAL BANK APP')],
                [sg.Text('YOU ARE STILL POOR')],
                [sg.Text('LEEETS GO!!!')],
                [sg.Button('GOOOO TO YOUR EMPTY BANK ACCOUNT!'),] ]

    # Create the Window
    window = sg.Window('DJ BOLIVER BANK', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'GOOOO TO YOUR EMPTY BANK ACCOUNT!': # if user closes window or clicks cancel
        window.close()
        mainmenuwindow()


#Gör en funktion för MAIN MENUWINDOWS som välkommnar användaren
def mainmenuwindow():
    with open('balance.txt') as f:
        balanceerz = f.read()
        #nedanför är layouten
    layout = [  [sg.Text("""Balance : """)],
        [sg.Text(balanceerz)],
        [sg.Text("""
    Enter number
1 : Deposit
2 : Withdraw
3 : View transactions
4 : Terminate account
5 : Exit
""")],
[sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5')]]

    # Create the Window
    window = sg.Window('DJ BOLIVER BANK', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '5': # if user closes window or clicks cancel
            break 
        if event == '1': #Här är om användaren klickar och sedan alla knapparna
            window.close() #alla under öppnar en ny ruta och stänger den aktiva rutan
            depositwindow()
        if event == '2':
            window.close()
            withdrawwindow()
        if event == '3':
            window.close()
            transactionwindows()
        if event == '4': #event 4 är close window
            window.close()
            terminationwindow()

#Gör en string och en variabel
depositnmrstr = []
b = 0

#Här gör jag en ny ruta som är för DEPOSITWINDOWss
def depositwindow():
    #härr är layouten
    layout = [  
                [sg.Text("Amount to DEPOSIT: ")],
                [sg.Text("________________________$", key='-TEXT-')],
                [sg.Submit(), sg.Button('Back')],
                [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4')],
                [sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8')], 
                [sg.Button('9'), sg.Button('0'), sg.Button('←')]]  

    # Create the Window
    window = sg.Window('DJ BOLIVER BANK', layout)

    #key sak för identifering
    text_elem = sg.Text('', key='-TEXT-')
    the_key = text_elem.Key

#while true sats för att lyssna och processa event
#while sats för att få numpadden att fungera korrekt, basically så den fungerar är att jag har en lista, och 2 variablar,
#listan har nummer i sig exempel följande "3" "4" "6" sen finns det en variabel som får listans värde i exakt nummer så
#denna hade haft 346 sen finns kan man med hjälp av numpadden lägga till nummer och ta bort nummer från listan
#när submit knappen är gjord kalkulares exakt vad som ska sättas in på kontot
    while True:
            event, values = window.read()
            number_of_elements = len(depositnmrstr)
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            if event == '1': #All dessa if event nedanför gör samma sak och det det med appenda till listan och ändra så att variablen är korrekt
                depositnmrstr.append("1")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '2':
                depositnmrstr.append("2")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '3':
                depositnmrstr.append("3")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '4':
                depositnmrstr.append("4")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '5':
                depositnmrstr.append("5")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '6':
                depositnmrstr.append("6")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '7':
                depositnmrstr.append("7")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '8':
                depositnmrstr.append("8")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '9':
                depositnmrstr.append("9")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            if event == '0':
                depositnmrstr.append("0")
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)

            if event == '←' and number_of_elements == 1:
                window['-TEXT-'].update("0")
                del depositnmrstr[-1]

            if event == '←' and number_of_elements > 1:
                del depositnmrstr[-1]
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)

            if event == 'Back':
                depositnmrstr.clear()
                window.close()
                mainmenuwindow()

            if event == 'Submit':
                if b == 0:
                    window.close()
                    sg.popup("DOINK ERRORR I REPEAT ERROR . ENTER NUMBER WIGGER DIGGER DOINK!!!")
                    depositwindow()
                else:
                    a = depositnmrstr
                    b = int(''.join(depositnmrstr))
                    print(f'{b} {type(b)}')
                    depositamounters = b
                    with open('balance.txt', 'r+') as f:
                        balancerzdepsoit = int(f.read())
                        print(balancerzdepsoit)
                        depositwriter = balancerzdepsoit + depositamounters
                        f.seek(0); f.truncate()
                        f.write(str(depositwriter))
                    with open('transactions.txt', 'a') as f:
                        f.write("Deposit of ${}\n".format(depositamounters))
                    depositnmrstr.clear()
                    window.close()
                    mainmenuwindow()
                    
#Gör en ny lista och en ny variabel för samma som innan fast för withdraw denna gångebn
withdrawnmrstr = []
d = 0

#Här är en funktion för en ruta, just denna är för withdraw rutan
def withdrawwindow():
    #här är layouten
    layout = [
                [sg.Text("Amount to WITHDRAW: ")],
                [sg.Text("________________________$", key='-TEXT-')],
                [sg.Submit(), sg.Button('Back')],
                [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4')],
                [sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8')], 
                [sg.Button('9'), sg.Button('0'), sg.Button('←')]]  

    # Create the Window
    window = sg.Window('DJ BOLIVER BANK', layout)

    #key sak
    text_elem = sg.Text('', key='-TEXT-')
    the_key = text_elem.Key

#while sats för att få numpadden att fungera korrekt, basically så den fungerar är att jag har en lista, och 2 variablar,
#listan har nummer i sig exempel följande "3" "4" "6" sen finns det en variabel som får listans värde i exakt nummer så
#denna hade haft 346 sen finns kan man med hjälp av numpadden lägga till nummer och ta bort nummer från listan
#när submit knappen är gjord kalkulares exakt vad som ska sättas in på kontot
    while True:
            event, values = window.read()
            number_of_elements = len(withdrawnmrstr)
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            if event == '1':
                withdrawnmrstr.append("1")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '2':
                withdrawnmrstr.append("2")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '3':
                withdrawnmrstr.append("3")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '4':
                withdrawnmrstr.append("4")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '5':
                withdrawnmrstr.append("5")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '6':
                withdrawnmrstr.append("6")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '7':
                withdrawnmrstr.append("7")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '8':
                withdrawnmrstr.append("8")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '9':
                withdrawnmrstr.append("9")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)
            if event == '0':
                withdrawnmrstr.append("0")
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)


            if event == '←' and number_of_elements == 1:
                window['-TEXT-'].update("0")
                del withdrawnmrstr[-1]

            if event == '←' and number_of_elements > 1:
                del withdrawnmrstr[-1]
                c = withdrawnmrstr
                d = int(''.join(withdrawnmrstr))
                print(f'{d} {type(d)}')
                window['-TEXT-'].update(d)

            if event == 'Back': #om användaren klickar på back så clearar den withdraw variebln
                withdrawnmrstr.clear()
                window.close()
                mainmenuwindow()

#om eventet är lika med submit så submittar den det variabeln är värd in txt FILEN och visar ett error om variabeln är inkorrekt
            if event == 'Submit':
                if event == d:
                    window.close()
                    sg.popup("DOINK ERROPR ENTER NUMBER WHORE")
                    withdrawwindow()
                else:
                    c = withdrawnmrstr
                    d = int(''.join(withdrawnmrstr))
                    print(f'{d} {type(d)}')
                    withdrawamounters = d
                    #Här skriver den in korrekta värden i TXT filen
                    with open('balance.txt', 'r+') as f:
                        balancerzwithdraw = int(f.read())
                        print(balancerzwithdraw)
                        withdrawwriter = balancerzwithdraw - withdrawamounters
                        f.seek(0); f.truncate()
                        f.write(str(withdrawwriter))
                    with open('transactions.txt', 'a') as f:
                        f.write("Withdrawal of ${}\n".format(withdrawamounters))
                    withdrawnmrstr.clear()
                    window.close()
                    mainmenuwindow()

#Kör funktionen för att öppna welcome window

welcomewindow()