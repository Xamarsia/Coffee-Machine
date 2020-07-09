water = 400
milk = 540
coffee = 120
disposable_cups = 9
money = 550


def coffee_machine_has():
    print("The coffee machine has:  \n" +
        str(water) + " of water \n" +
        str(milk) + " of milk \n" +
        str(coffee) + " of coffee beans \n" +
        str(disposable_cups) + " of disposable cups \n" +
        str(money) + " of money\n")
    return


coffee_machine_has()
option = input("Write action (buy, fill, take):")


def buy():
    order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if order == '1':
        global water
        water = water - 250
        global milk
        milk = milk - 0
        global coffee
        coffee = coffee - 16
        global disposable_cups
        disposable_cups = disposable_cups - 1
        global money
        money = money + 4
        coffee_machine_has()

    elif order == '2':
        # global water
        water = water - 350
        # global milk
        milk = milk - 75
        # global coffee
        coffee = coffee - 20
        # global disposable_cups
        disposable_cups = disposable_cups - 1
        # global money
        money = money + 7
        coffee_machine_has()

    elif order == '3':
        # global water
        water = water - 200
        # global milk
        milk = milk - 100
        # global coffee
        coffee = coffee - 12
        # global disposable_cups
        disposable_cups = disposable_cups - 1
        # global money
        money = money + 6
        coffee_machine_has()
    return


def fill():
    water = int(input("Write how many ml of water do you want to add:"))
    milk = int(input("Write how many ml of milk do you want to add:"))
    coffee = int(input("Write how many grams of coffee beans do you want to add:"))
    disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    print("The coffee machine has: \n" +
        str(water + 400) + " of water \n" +
        str(milk + 540) + " of milk \n" +
        str(coffee + 120) + " of coffee beans \n" +
        str(disposable_cups + 9) + " of disposable cups \n"
                                     "550 of money \n")
    return


def take():
    global money
    print("I gave you $" + str(money))
    money = 0
    coffee_machine_has()
    return


if option == 'buy':
    buy()
elif option == 'fill':
    fill()
elif option == 'take':
    take()
