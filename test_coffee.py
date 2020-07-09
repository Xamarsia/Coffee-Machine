water = 400
milk = 540
coffee = 120
disposable_cups = 9
money = 550
status = True
variable = " "



def coffee_machine_has():
    print("The coffee machine has:  \n" +
        str(water) + " of water \n" +
        str(milk) + " of milk \n" +
        str(coffee) + " of coffee beans \n" +
        str(disposable_cups) + " of disposable cups \n" +
        str(money) + " of money\n")
    return


def buy():
    order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if order == '1':
        global water
        global milk
        global coffee
        global disposable_cups
        global money
        global variable
        if water < 250:
            variable = "water"
        if coffee < 16:
            variable = "coffee"
        if disposable_cups < 1:
            variable = "cups"

        if water < 250 or coffee < 16 or disposable_cups < 1:
            print("Sorry, not enough {}!".format(variable))
        else:
            print("I have enough resources, making you a coffee!")
        water = water - 250
        milk = milk - 0
        coffee = coffee - 16
        disposable_cups = disposable_cups - 1
        money = money + 4

    elif order == '2':
        if water < 350:
            variable = "water"
        elif milk < 75:
            variable = "milk"
        elif coffee < 16:
            variable = "coffee"
        elif disposable_cups < 1:
            variable = "cups"

        if water < 350 or milk < 75 or coffee < 20 or disposable_cups < 1:
            print("Sorry, not enough {}!".format(variable))
        else:
            print("I have enough resources, making you a coffee!")
            water = water - 350
            milk = milk - 75
            coffee = coffee - 20
            disposable_cups = disposable_cups - 1
            money = money + 7

    elif order == '3':
        if water < 200:
            variable = "water"
        elif milk < 100:
            variable = "milk"
        elif coffee < 12:
            variable = "coffee"
        elif disposable_cups < 1:
            variable = "cups"

        if water < 200 or milk < 100 or coffee < 12 or disposable_cups < 1:
            print("Sorry, not enough {}!".format(variable))
        else:
            print("I have enough resources, making you a coffee!")
            water = water - 200
            milk = milk - 100
            coffee = coffee - 12
            disposable_cups = disposable_cups - 1
            money = money + 6
    return


def fill():
    wat = int(input("Write how many ml of water do you want to add:"))
    mil = int(input("Write how many ml of milk do you want to add:"))
    cof = int(input("Write how many grams of coffee beans do you want to add:"))
    cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    global water
    water = wat + water
    global milk
    milk = mil + milk
    global coffee
    coffee = cof + coffee
    global disposable_cups
    disposable_cups = cups + disposable_cups
    return


def remaining():
    coffee_machine_has()


def exit():
    global status
    status = False


def take():
    global money
    print("I gave you $" + str(money))
    money = 0
    return


while status:
    option = input("Write action (buy, fill, take, remaining, exit):")
    if option == 'buy':
        buy()
    elif option == 'fill':
        fill()
    elif option == 'take':
        take()
    elif option == 'remaining':
        remaining()
    elif option == 'exit':
        exit()