def read_file(filename):
	goods = []		
	with open (filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			goods.append([name, price])
	print(goods)	
	return goods



def input_file(goods):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		goods.append([name, price])
	print(goods)
	print(goods[0][1])
	return goods
def print_file(goods):
	
	for good in goods:
		print('商品名稱{}商品價格{}'.format(good[0], good[1]))

#product = []
#article = []
#article.append(name)
#article.append(price)
#product.append(article)

def write_file(filename, goods):
	with open(filename, 'w') as f:
		f.write('商品,價格\n')	
		for good in goods:
			f.write(good[0] + ',' + good[1] + '\n')
def main(filename):
	import os
	if os.path.isfile(filename):
		print('找到檔案!')
		goods = read_file(filename)		
	else:
		print('找不到檔案!')


	goods = input_file(goods)
	print_file(goods)
	write_file(filename, goods)

main('products.csv')