# 创建二维清单
# 分割split(',') ,分割的结果是List
# strip() 去掉 回车'/n', 空格' '


# 读取档案，并存储
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:    # 读取档案，并存储
		for line in f:
			if '产品,价格' in line:
				continue                            # 跳过某行
				name,price = line.strip().split(',')    # 存储为清单  
				products.append([name,price])
	return products

# 使用者输入信息
def user_input(products):
	while True:
		name = input('please input the product name:')
		if name == 'q':
			break
		price = input('Please input the price of the product:')
		products.append([name, price])
	print(products)
	return products

# 打印出所有购买记录
def print_product(products):
	for p in products:
		print('The price of ', p[0] , ', is', p[1], '.')

# 写入档案
def write_file(filename,products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('产品,价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] +'\n')        # 字符串运算


import os   #载入操作系统，operation system

def main():
	filename = 'product.csv'
	if os.path.isfile(filename):    #检查是否存在某文件
		print('Yes, it is Here')
		products = read_file('product.csv')
	else:
		print('NONONO...')

	products = user_input(products)
	print_product(products)
	write_file('product.csv', products)
	
main()