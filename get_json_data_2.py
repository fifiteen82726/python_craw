import json
import urllib

results = json.load(urllib.urlopen("http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json"))

#parse_result  = json.loads(results)

#print len(results)

for i in range(0, len(results), 1):
	print results[i]['SiteId'] +  " "+ results[i]['Rainfall1hr'] + " "+results[i]['PublishTime']  

	
    #['results'] ['collection1'] [i] ['title']

