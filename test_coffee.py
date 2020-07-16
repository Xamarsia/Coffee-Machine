water = 400
milk = 540
coffee = 120
disposable_cups = 9
money = 550
status = True
variable = " "
order = 0


class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    disposable_cups = 9
    money = 550
    variable = " "
    order = 0


    def __init__(self, water, milk, coffee, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.disposable_cups = disposable_cups
        self.money = money



    def remaining(self):   # yes
        print("The coffee machine has:  \n" +
            str(water) + " of water \n" +
            str(milk) + " of milk \n" +
            str(coffee) + " of coffee beans \n" +
            str(disposable_cups) + " of disposable cups \n" +
            str(money) + " of money\n")
        return


    def buy(self, order):   # yes
        self.order = order
        if self.order == '1':
            if self.water < 250:
                self.variable = "water"
            if self.coffee < 16:
                self.variable = "coffee"
            if self.disposable_cups < 1:
                self.variable = "cups"

            if self.water < 250 or self.coffee < 16 or self.disposable_cups < 1:
                print("Sorry, not enough {}!".format(self.variable))
            else:
                print("I have enough resources, making you a coffee!")
                global water
            water = self.water - 250
            global milk
            milk = self.milk - 0
            global coffee
            coffee = self.coffee - 16
            global disposable_cups
            disposable_cups = self.disposable_cups - 1
            global money
            money = self.money + 4

        elif self.order == '2':
            if self.water < 350:
                self.variable = "water"
            elif self.milk < 75:
                self.variable = "milk"
            elif self.coffee < 16:
                self.variable = "coffee"
            elif self.disposable_cups < 1:
                self.variable = "cups"

            if self.water < 350 or self.milk < 75 or self.coffee < 20 or self.disposable_cups < 1:
                print("Sorry, not enough {}!".format(self.variable))
            else:
                print("I have enough resources, making you a coffee!")
                water = self.water - 350
                milk = self.milk - 75
                coffee = self.coffee - 20
                disposable_cups = self.disposable_cups - 1
                money = self.money + 7

        elif self.order == '3':
            if self.water < 200:
                self.variable = "water"
            elif self.milk < 100:
                self.variable = "milk"
            elif self.coffee < 12:
                self.variable = "coffee"
            elif self.disposable_cups < 1:
                self.variable = "cups"

            if self.water < 200 or self.milk < 100 or self.coffee < 12 or self.disposable_cups < 1:
                print("Sorry, not enough {}!".format(self.variable))
            else:
                print("I have enough resources, making you a coffee!")
                water = self.water - 200
                milk = self.milk - 100
                coffee = self.coffee - 12
                disposable_cups = self.disposable_cups - 1
                money = self.money + 6
        return


    def fill(self, wat, mil, cof, cups):  # yes
        self.wat = wat
        self.mil = mil
        self.cof = cof
        self.cups =cups
        global water
        water = self.wat + self.water
        global milk
        milk = self.mil + self.milk
        global coffee
        coffee = self.cof + self.coffee
        global disposable_cups
        disposable_cups = self.cups + self.disposable_cups
        return


    def take(self):   # yes
        global money
        print("I gave you $" + str(self.money))
        money = 0
        return


while status:
    option = input("Write action (buy, fill, take, remaining, exit):")
    coffee_machine = CoffeeMachine(water, milk, coffee, disposable_cups, money)
    if option == 'buy':
        globals()['order'] = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        coffee_machine.buy(order)
        # coffee_machine.machine_has()
    elif option == 'fill':
        wat = int(input("Write how many ml of water do you want to add:"))
        mil = int(input("Write how many ml of milk do you want to add:"))
        cof = int(input("Write how many grams of coffee beans do you want to add:"))
        cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        coffee_machine.fill(wat, mil, cof, cups)
    elif option == 'remaining':
        coffee_machine.remaining()
    elif option == "exit":
        status = False
    elif option == 'take':
        coffee_machine.take()