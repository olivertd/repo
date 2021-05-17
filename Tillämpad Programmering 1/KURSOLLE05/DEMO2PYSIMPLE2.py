import PySimpleGUI as sg

layout = [[sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4')],
[sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8')], 
[sg.Button('9'), sg.Button('0'), sg.Button('←')]    ]

event, values = sg.Window('List Comprehensions', layout).read(close=True)