import re
f = open("filter.txt","w")
with open('crawled.txt', 'r') as file:
	data = file.read()
	lst =re.findall('\S+=\S+',data)
	for Item in lst:
		f.write(Item+'\n')
f.close()