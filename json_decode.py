import requests

data_link = requests.get('https://www.jsonkeeper.com/b/3GOF')
my_list = data_link.json()



