# """"
#
# Functions
#
# """
def myFullName(firstName="Unknown", lastName="Forger"):
    return firstName + " " + lastName

print(myFullName("Tanjiro", "Kamado"))
print(myFullName(firstName="Loid"))
print(myFullName())
print(myFullName(lastName="Smith"))
print(myFullName("Anna", "Forger"))
print(myFullName("Yor", "Forger"))
print(myFullName("Bond", "Forger"))

def redPotion(hp):
    return hp + 50
def bluePotion(mp):
    return mp + 30

current_hp = 70
print("Current HP:", current_hp)
current_hp = redPotion(current_hp)
print("After using Red potion", current_hp)