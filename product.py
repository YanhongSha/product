
products = []

while True:
	name = input('please input the product name:')
	if name == 'q':
		break
	price = input('Please input the price of the product:')
	products.append([name, price])
print(products)

