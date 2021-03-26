#KURSOLLE
#SELK BANKAPP
from pathlib import Path
import time
import sys

#VÄLKOMNMNAR ANVÄNDAREN IN I PROGRAMMET MED FINA PRINTS 
print("WELCOME TO SELK FINANCIAL BANK APP")
print("YOU ARE STILL POOR")
print("LEEETS GO!!!")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print("GOOOO!!!!!!")


#MENY
mainmenuoptioners = """Enter number
1 : View Balance
2 : Deposit
3 : Withdraw
4 : View transactions
5 : Terminate account
6 : Exit
"""


#KOLLAR OM FILERNA FINNS (BALANCE.TXT) O TRANSACTIONS.TXT
if Path('balance.txt').is_file() and Path('transactions.txt').is_file():
    pass
else:
    with open('balance.txt', 'w+') as f:
       f.write("1000")
    with open('transactions.txt', 'w+') as f:
        pass

exit = False

#GÖR EN WHILE LOOP
while exit != True:
    #INITIERAR MENYN
    while True:
        try:
            mainmenuinputer = int(input(mainmenuoptioners))
            assert mainmenuinputer >= 1 and mainmenuinputer <= 6, "FRONXY DOINKSTER TO BIG OR SMALL NUBMERO"
            break
        except AssertionError as msg:
            #PRINTAR UT ETT ERROR
            print(msg)
        except:
            print("FRONXY ERROR [DID NOT ENTER A FRONXY]")

    # STÄNGER NER PROGRAMMET 
    if mainmenuinputer == 6:
        print("THANK YOU FOR USING SELK BANK APP")
        print("CURRENTLY BREAKING OUT OF THE TUSK LOOP")
        for i in range(100+1):
            time.sleep(0.1)
            sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
            sys.stdout.flush()
        print("BROKEN OUT!!")
        exit = True
    #KOLLAR HUR MÅNGA PENGAR SOM FINNS I BALANCE.TEXT
    if mainmenuinputer == 1:
        with open('balance.txt') as f:
            balanceerz = f.read()
            print("Your balance is currently ${}".format(balanceerz))
    #DEPOSITERAR IN PENGAR I BLANCE.TEXT OCH SKRIVER IN TRANSAKTIONEN I TRANSACTIONS.TEXT
    if mainmenuinputer == 2:
        while True:
            try:
                depositamounters = int(input("Enter amount to depositors: "))
                break
            except:
                print("YOUR DEPOSIT IS NOT AN NUMBERO!!! TRY AGAIN SIRSKY!!")
        with open('balance.txt', 'r+') as f:
            balancerzdepsoit = int(f.read())
            print(balancerzdepsoit)
            depositwriter = balancerzdepsoit + depositamounters
            f.seek(0); f.truncate()
            f.write(str(depositwriter))
        with open('transactions.txt', 'a') as f:
            f.write("Deposit of ${}\n".format(depositamounters))
    #WITHDRAWAR UR PENGAR UR BALANCE.TEXT OCH SKRIVER IN TRANSAKTIONEN I TRASACTIONS.TEXT
    if mainmenuinputer == 3:
        while True:
            try:
                withdrawamounters = int(input("Enter amount to withdraw: "))
                break
            except:
                print("YOUR WITHDRAWAL AMOUNT CAN*T BE THOSE LETTERS TRY INTEGER")
        with open('balance.txt', 'r+') as f:
            balancerzwithdraw = int(f.read())
            print(balancerzwithdraw)
            withdrawwriter = balancerzwithdraw - withdrawamounters
            f.seek(0); f.truncate()
            f.write(str(withdrawwriter))
        with open('transactions.txt', 'a') as f:
            f.write("Withdrawal of ${}\n".format(withdrawamounters))
    # KOLLER TRANSAKTIONEN OCH PRINTAR DEM
    if mainmenuinputer == 4:
        with open('transactions.txt') as f:
            print("\n{}".format(f.read()))
    # TA BORT KONTOFILERNA OCH RADERA KONTOT
    if mainmenuinputer == 5:
        for i in range(100+1):
            time.sleep(0.5)
            sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
            sys.stdout.flush()
        print("TERMINATOR INCOMERS!!!!")
        file_path1 = Path('balance.txt')
        file_path1.unlink()
        file_path2 = Path('transactions.txt')
        file_path2.unlink()
        time.sleep(3)
        print("TERMINATOR SUCCESS!!!!!!!")
        exit = True