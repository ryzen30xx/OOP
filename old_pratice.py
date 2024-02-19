from os import system
from time import sleep
owners = []
prices = []
areas = []
error_show = ""

def add_house(owner, price, area):
	if not owner:
		error_show = "Owner name must be not blank !"
	elif not price:
		error_show = "Price must be not blank !"
	elif price is not isdigit():
		error_show = "price must be integer number"
	elif not area:
		return("Area must be not blank !")
	elif owner in owners:
		return("Owner has exist !")
	else:
		owners.append(owner) 
		prices.append(int(price))
		areas.append(int(area))


def edit_price(owner, new_price):
	if not owner: 
		return("Owner name is must be not empty !")
	elif owner not in owners:
		return(f"Owner {owner} not exist in System !")
	
	else:
		for i in range(len(owners)):
			if (owner == owners[i]):
				prices[i] = new_price
				return(f"Price of owner {owners[i]} has been updated !")

def sell(owner):
	if not owner:
		return("Owner name is must be not empty !")

	elif owner not in owners:
		return(f"Owner {owner} not exist in System")

	for i in range(len(owners)):

		if owners[i] == owner:
			owners.pop(i), prices.pop(i), areas.pop(i)
			return(f"Owner {owner} has been deleted !")


def Show_all():
	count = 0
	for i in range(len(owners)):
		count += 1
		print(f"{count}: Owner by {owners[i]} with price {prices[i]} with {areas[i]}m2")


if __name__ == "__main__":
	running = True
	while running:
		system('cls')
		print("House Management System\n\n")
		print(f"Debug mode: {Show_error}")
		print("1: Add House\n2: Edit Price\n3: Sell A House\n4: Show All House\n5: Exit")
		choose = int(input("Choose your function: "))
		if 0 >= choose >= 5:
			system("cls")
			print("your choosen is incorrect !")
		elif choose == 1:
			system('cls')
			add_house(str(input("Enter Owner name :")), str(input("Enter Price: ")), str(input("Enter Area: ")))
		elif choose == 2:
			edit_price(str(input("Enter owner name to edit price: ")), int(input("Enter new price: ")))
		elif choose == 3:
			Sell(str(input("Enter owner to sell: ")))
		elif choose == 4:
			Show_all()
		else:
			system('cls')
			print("Thank for business with own company !")
			running = False