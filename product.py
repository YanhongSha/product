# 创建二维清单
# 分割split(',') ,分割的结果是List
# strip() 去掉 回车'/n', 空格' '


# 读取档案，并存储
products = []

with open('product.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '产品,价格' in line:
			continue                            # 跳过某行
		name,price = line.strip().split(',')    # 存储为清单  
		products.append([name,price])
print(products)


# 使用者输入信息

while True:
	name = input('please input the product name:')
	if name == 'q':
		break
	price = input('Please input the price of the product:')
	products.append([name, price])
print(products)

# 打印出所有购买记录
for p in products:
	print('The price of 'p[0], 'is' p[1], '.')


# 写入档案

with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('产品,价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] +'\n')


