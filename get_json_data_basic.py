import json
import urllib

results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/6xcbj2hu?apikey=L63EvSC1x5vG8iSbm9Jon3784mkDp1Or"))


json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(results) 
print parsed_json