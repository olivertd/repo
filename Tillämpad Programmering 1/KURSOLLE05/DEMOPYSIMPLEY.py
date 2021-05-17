import PySimpleGUI as sg      
import PySimpleGUI as sg
import time
from pathlib import Path
import time
import sys


#KOLLAR OM FILERNA FINNS (BALANCE.TXT) O TRANSACTIONS.TXT
if Path('balance.txt').is_file() and Path('transactions.txt').is_file():
    pass
else:
    with open('balance.txt', 'w+') as f:
       f.write("1000")
    with open('transactions.txt', 'w+') as f:
        pass

#kollar balansen


depositnmrstr = []
b = 0


def balancewindow():
    with open('balance.txt') as f:
        balanceerz = f.read()

    layout = [[sg.Text(balanceerz)],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('Window Title', layout)    

    event, values = window.read()    
    window.close()
    mainmenuwindow()


def mainmenuwindow():
    layout = [[sg.Text('My one-shot window.')],
                [sg.Text('My layout')],  
                [sg.Text("Amount to deposit: ")],
                [sg.Text("________________________$", key='-TEXT-')],
                [sg.Submit(), sg.Cancel(), sg.Button('Check Balance')],
                [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4')],
                [sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8')], 
                [sg.Button('9'), sg.Button('0'), sg.Button('←')]]  

    # Create the Window
    window = sg.Window('DJ BOLIVER BANK', layout)

    #key sak
    text_elem = sg.Text('', key='-TEXT-')

    the_key = text_elem.Key


    while True:
            event, values = window.read()
            number_of_elements = len(depositnmrstr)
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            if event == '1':
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
                window['-TEXT-'].update("0000000000")
                del depositnmrstr[-1]

            if event == '←' and number_of_elements > 1:
                del depositnmrstr[-1]
                a = depositnmrstr
                b = int(''.join(depositnmrstr))
                print(f'{b} {type(b)}')
                window['-TEXT-'].update(b)
            #if event == 'Submit':
                #try:
                    #a = depositnmrstr
                    #b = int(''.join(depositnmrstr))
                    #print(f'{b} {type(b)}')
                #except Exception:
                    #print("doink error")
            if event == 'Submit':
                while True:
                    try:
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
                        break
                    except:
                        window.close()
                        sg.popup("DOINK ERROPR ENTER NUMBER WHORE")
                        mainmenuwindow()
                        break
        
            if event == 'Check Balance':
                depositnmrstr.clear()
                window.close()
                balancewindow()



mainmenuwindow()