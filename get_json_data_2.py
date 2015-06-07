import json
import urllib

results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/adgmajn2?apikey=L63EvSC1x5vG8iSbm9Jon3784mkDp1Or"))

#parse_result  = json.loads(results)

for i in range(0, 10, 1):
    print results['results'] ['collection1'] [i] ['title']['text'] 

