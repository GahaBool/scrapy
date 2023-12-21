import books_parse
import os

def option1():
    print("One option")

def option2():
    isempty = os.stat('book.json').st_size
    print(isempty)

def clear_file():
    os.system(r'nul>book.json')

def option4():
    print("Two option")

def option5():
    print("Two option")

menu = {'1' : option1, '2' : option2, '3' : clear_file, '4' : "End"}


while True:

    options = menu.keys()
    for entry in options:
        print(entry)

    selection = input("Выберите опции: ")

    if selection == '1' or selection == '2' or selection == '3':
        menu[selection]()
    elif selection == '4':
        print("Пока")
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз")
