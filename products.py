
goods = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	goods.append([name, price])
print(goods)
print(goods[0][1])
for good in goods:
	print('商品名稱{}商品價格{}'.format(good[0], good[1]))

#product = []
#article = []
#article.append(name)
#article.append(price)
#product.append(article)

with open('products.csv','w') as f:
	f.write('商品,價格\n')	
	for good in goods:
		f.write(good[0] + ',' + good[1] + '\n')