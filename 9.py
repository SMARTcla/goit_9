import sys
catalog = {}
def check_name_and_phone(word):
    while not word[2].isdigit():
        print("Write number phone correctly")
        print("Phone : ")
        word[2] = input()
    while not word[1].isalpha():
        print("Write name correctly")
        print("Name : ")
        word[1] = input()
    return word


def find_name(word):
    global catalog
    if word[1] in catalog:
        number = catalog.get(word[1])
        return number


def input_error(function_to_decorate):
    def funct(word):
        global catalog
        if word.lower() == "hello":
            function_to_decorate(word)
            return
        elif word.lower() == "show all":
            function_to_decorate(word)
            return
        elif word.lower() == "good bye" or word.lower() == "exit" or word.lower() == "close":
            function_to_decorate("exit")
            return
        word = word.split()
        word[0] = word[0].lower()
        if len(word) == 3 and word[0] == "add":
            if word[1] in catalog:
                print("This name is already in the list")
                print("Do you want to change info of contact or add new phone with another name of contact(change/new): ")
                tmp = input()
                while True:
                    if tmp == "new" or tmp == "change":
                        break;
                    print("Uncorrect. Try again:")
                    tmp = input()
                if tmp == "change":
                    word = check_name_and_phone(word)
                    function_to_decorate(word)
                    return
                if tmp == "new":
                    print("Print new name")
                    word[1] = input()
                    while word[1] in catalog:
                        print("Already in the list")
                        word[1] = input()
                    word = check_name_and_phone(word)
                    function_to_decorate(word)
                    return
            word = check_name_and_phone(word)
            function_to_decorate(word)
        elif len(word) == 3 and word[0] == "change":
            while word[1] not in catalog:
                print("This name is not in the list")
                print("Do you want to change this name or add new item to the list(change/new)")
                tmp = input()
                while True:
                    if tmp == "new" or tmp == "change":
                        break;
                    print("Uncorrect. Try again:")
                    tmp = input()
                if tmp == "new":
                    word = check_name_and_phone(word)
                    function_to_decorate(word)
                    return
                if tmp == "change":
                    print("Print new name(or exit)")
                    word[1] = input()
                    while word[1] not in catalog:
                        if word[1] == "exit":
                            return 
                        print("Not in the list")
                        word[1] = input()
                    word = check_name_and_phone(word)
                    function_to_decorate(word)
                    return
            word = check_name_and_phone(word)
            function_to_decorate(word)
        elif len(word) == 2 and word[0] == "phone":
            while word[1] not in catalog:
                print("This name is not in the list")
                print("Do you want to change this name or exit(change/exit)")
                tmp = input()
                while True:
                    if tmp == "exit" or tmp == "change":
                        break;
                    print("Uncorrect. Try again:")
                    tmp = input()
                if tmp == "exit":
                    return
                if tmp == "change":
                    print("Print new name(or exit)")
                    word[1] = input()
                    while word[1] not in catalog:
                        if word[1] == "exit":
                            return 
                        print("Not in the list")
                        word[1] = input()
                    function_to_decorate(word)
                    return
            function_to_decorate(word)
            return
        else:
            print("Command not recognized, please try again!")
            print("Commands : ")
            print("1 - hello")
            print("2 - add")
            print("3 - show all")
            print("4 - change ")
            print("5 - phone")
            print("6 - exit/good bye/close")
            print("Thanks for using my bot")
    return funct


@input_error
def bot_func(word):
    if word[0] == "add" or word[0] == "change":
        catalog[word[1]] = word[2]
        return
    if word[0] == "phone":
        number = find_name(word)
        print(number)
        return
    if word.lower() == "hello":
        print("How can I help you?")
        return
    if word.lower() == "show all":
        print(catalog)
        return
    if word.lower() == "exit":
        print("Good bye!")
        sys.exit()
    

word = input()
while word != ".":
    word = bot_func(word)
    word = input()
