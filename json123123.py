import requests

response = requests.get('http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json')
                       
data = response.json()

print data