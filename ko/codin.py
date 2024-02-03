#####achine_coffee
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


game_end = True


def espresso(quarters, dimes, nickles, pennies, MENU):
    
    total =  0.25*quarters + 0.1 * dimes + 0.05*nickles + 0.01 * pennies
    if total > MENU["espresso"]["cost"]:
        if water > MENU["espresso"]["ingredients"]["water"]:
            if coffee  > MENU["espresso"]["ingredients"]["coffee"]:
                return water - MENU["espresso"]["ingredients"]["water"]
                return coffee  - MENU["espresso"]["ingredients"]["coffee"]
                sum = total - MENU["cappuccino"]["cost"]
                print(f"Here is {sum} in change.")
                print(f"Here is your espresso ☕️. Enjoy!")
            
            else:
                print("Sorry there is not enough coffee")
                game_end = False
        
        
        
        
        else:
            print("Sorry there is not enough water")
            game_end = False
    
    else:
        print("I don't have enough money sir")
        game_end = False




def latte(quarters, dimes, nickles, pennies, MENU):
    total =  0.25*quarters + 0.1 * dimes + 0.05*nickles + 0.01 * pennies
    if total > MENU["latte"]["cost"]:
        if water > MENU["latte"]["ingredients"]["water"]:
            if coffee  > MENU["latte"]["ingredients"]["coffee"]:
                return water - MENU["latte"]["ingredients"]["water"]
                return coffee  - MENU["latte"]["ingredients"]["coffee"]
                sum = total - MENU["cappuccino"]["cost"]
                print(f"Here is {sum} in change.")
                print(f"Here is your latte ☕️. Enjoy!")
            
            else:
                print("Sorry there is not enough coffee")
                game_end = False
        
        
        
        
        else:
            print("Sorry there is not enough water")
            game_end = False

    
    else:
        print("I don't have enough money sir")
        game_end = False
            


def cappuccino(quarters, dimes, nickles, pennies, MENU):
    total =  0.25*quarters + 0.1 * dimes + 0.05*nickles + 0.01 * pennies
    if total > MENU["cappuccino"]["cost"]:
        if water >= MENU["cappuccino"]["ingredients"]["water"]:
            if coffee  >= MENU["cappuccino"]["ingredients"]["coffee"]:
                return water - MENU["cappuccino"]["ingredients"]["water"]
                return coffee  - MENU["cappuccino"]["ingredients"]["coffee"]
                sum = total - MENU["cappuccino"]["cost"]
                print(f"Here is {sum} in change.")
                print(f"Here is your cappuccino ☕️. Enjoy!")
            
            else:
                print("Sorry there is not enough coffee")
                
        
        
        
        
        else:
            print("Sorry there is not enough water")
            game_end = False
    
    else:
        print("I don't have enough money sir")
        return



def Machine_coffee():
    water = 300
    milk= 200
    coffee = 100
    desire = input("What would you like? ('espresso'/'latte'/'cappuccino'):").lower()
    if desire == 'espresso':
        quarters = int(input("how many quarters?:") )
        dimes = int(input("how many dimes?:")) 
        nickles = int(input("how many nickles?:"))
        pennies = int(input("how many pennies?:")) 
        espresso(quarters, dimes, nickles, pennies, MENU, water, coffee) 
    elif desire =='latte':
        quarters = int(input("how many quarters?:") )
        dimes = int(input("how many dimes?:")) 
        nickles = int(input("how many nickles?:"))
        pennies = int(input("how many pennies?:")) 
        latte(quarters, dimes, nickles, pennies, MENU, water, coffee)
    elif desire == 'cappuccino':
        quarters = int(input("how many quarters?:") )
        dimes = int(input("how many dimes?:")) 
        nickles = int(input("how many nickles?:"))
        pennies = int(input("how many pennies?:")) 
        cappuccino(quarters, dimes, nickles, pennies, MENU,water, coffee)
    elif desire == "d":
        print(f"{water}ml")
        print(f"{milk}ml")
        print(f"{coffee}g")

while game_end :

    Machine_coffee()
##################kfx n9as man water o milk o coffee ############################

