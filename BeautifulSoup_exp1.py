from bs4 import BeautifulSoup 
html = '<!DOCTYPE html>\
<html lang="en">\
<head>\
	<meta charset="UTF-8">\
	<title>Document</title>\
</head>\
<body>\
	<a href="">asdasd</a>\
	<p id ="kkk">ppppppp</p>\
	<p class ="123">ppppppp</p>\
</body>\
</html>'

soup = BeautifulSoup (html)
print soup.select('#kkk')
print soup.select('.123')
print soup.select('a')