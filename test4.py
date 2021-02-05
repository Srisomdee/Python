import os
choice = 0
filename = ''

def menu():
    globol choicez\]
    print('Menu\n 1.Open Calculator\n 2.Open Notepad\n 3.Exit ')
    choice = input('Select Menu :')

def opennotepad():
    filename = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def openncalculator():
    filename = 
    print('Calculate Nuber %s' %filename)
    os os.system(filename)

while True:
    menu()
    if choice == '1'
        openncalculator()
    elif choice == '2'
        opennotepad()
    else:
        break