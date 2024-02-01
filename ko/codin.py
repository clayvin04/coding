##########randi kfx da5l gamil ,name phone#########


def add_user(name, gmail, phone, dec):
        dec[name] = {"gmail":gmail, "phone": phone}


def delete_user(name, dec):
    if name in dec:
        dec.clear["name"]
    else:
        print("your data not found ")

def update_user(update, dec, name):
    change = input(f"update your old  {update} : ").lower()
    if name in dec:
        dec[name][update] = change
    else:
        print('The user does not exist')


def game():
    dec = {}
    service = input('what service do you want this time Sir. type "add" to add a new user, "clear" to delete your data, "update" to update your informations : ').lower()
    name = input("ur name ").lower()
    if service == 'add':
        gmail = input("ur gmail ")
        phone = int(input("ur phone "))
        add_user(name, gmail, phone, dec)
    elif service == 'clear':
        delete_user(name, dec)
        print("your name was deeted successfuly")
    else:
        print(dec)
        update = input("what do u want to change. type 'gmail' to change the gmail, and 'phone' to change ur name ").lower()
        update_user(update, name, dec)
    print("thank you Sir ")


game()






