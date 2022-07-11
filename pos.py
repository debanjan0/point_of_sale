import os

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    os.system("pip install tabulate")
    from tabulate import tabulate

try:
    import pymongo
except ModuleNotFoundError:
    os.system("pip install pymongo")
    import pymongo



'''
Create a account in mongodb and paste the connection in your_url_and_password
'''
myclient = pymongo.MongoClient(<your_url_and_password>)
mydb = myclient["POS"]

item = mydb["item"]
sale = mydb["sale"]
cust = mydb["customers"]

cust_list=[ "name", "phone", "mail"]
item_list=[ "item_name", "price", "stock"]
sale_list=[ "cust_details", "items", "mop"]

def count_id(coll):
	x = item.find()
	length=0
	for i in x:
		length+=1
	return length


def add_customer(l):
	'''
	Input format :-
	{"cust_id": (count_id(cust) + 1), "name":<name>, "phone":<number>, "mail":<mail> }
	'''
	x = cust.insert_one(l)
	return (x.acknowledged)


def add_item(l):
	'''
	Input format :-
	{"item_id": (count_id(item) + 1), "item_name":<name>, "price":<price>, "stock":<stock> }
	'''
	x = item.insert_one(l)
	return (x.acknowledged)


def add_sale(l):
	'''
	Input format :-
	{"tx_id": (count_id(sale) + 1), "cust_details":"cust_id", "items":{ "item1_name":"quantity", "item2_name":"quantity" }, "mop":"online"}
	'''
	x = sale.insert_one(l)
	return (x.acknowledged)


def item_data():
	data1 = []
	for x in item.find({},{"_id": 0}):
		data = []
		for i in x.values():
			data.append(i)
		data1.append(data)
	print (tabulate(data1, headers=["Item ID", "Name", "Price", "Stock"]))


def customer_data():
	data1 = []
	for x in cust.find({},{"_id": 0}):
		data = []
		for i in x.values():
			data.append(i)
		data1.append(data)
	print (tabulate(data1, headers=["Customer ID", "Name", "Number", "Email"]))


def sale_data():
	data1 = []
	for x in sale.find({},{"_id": 0}):
		data = []
		for i in x.values():
			data.append(i)
		data1.append(data)
	print (tabulate(data1, headers=["Sale ID", "Customer ID", "Items", "Mode fo payment"]))


def take_input_make_arr(given_list,s,id_name):
	temp={}
	temp[id_name]=(int(count_id(s))+1)
	for i in given_list:
		if i == "items":
			n = int(input("How many item do you want ? "))
			temp_item_list = []
			for j in range(n):
				x_item = input("enter the item :- ")
				x_quan = int(input("enter the quantity :- "))
				temp_item_list[x_item] = x_quan
			temp[i] = temp_item_list

		x = input("enter the " + i + " :- ")
		temp[i] = x
	return temp


# li = {"cust_id": (count_id(cust) + 1), "name": "Raj", "phone":8414563029, "mail":"raj@gmail.com" }

# li1 = {"item_id": (count_id(item) + 1), "item_name":"headphone", "price":200, "stock":50 }
# li2 = {"item_id": (count_id(item) + 1), "item_name":"mouse pad", "price":40, "stock":70 }

# li3 = {"tx_id": (count_id(sale) + 1), "cust_details":1, "items":{ "mouse":1, "mouse pad":1 }, "mop":"online"}




while True:
	print("\n 1.to add_item \n"+"2.to add_sale \n"+"3.to add_customer \n"+"4.to show items \n"+"5.to show sale \n"+"6.to show customers \n"+"7.to exit \n")
	n=int(input(":- "))

	if n == 1:
		tempo_list = take_input_make_arr(item_list,"item","item_id")
		print(add_item(tempo_list))
	elif n == 2:
		tempo_list = take_input_make_arr(sale_list,"sale","tx_id")
		print(add_sale(tempo_list))
	elif n == 3:
		tempo_list = take_input_make_arr(cust_list,"cust","cust_id")
		print(add_customer(tempo_list))
	elif n == 4:
		item_data()
	elif n == 5:
		sale_data()
	elif n == 6:
		customer_data()
	elif n == 7:
		break
	else:
		print("enter a valid no")




