import urllib.request
opener = urllib.request.build_opener()
response =  opener.open ("https://vk.com/")
print (response.read())
print("=======================================")
#кхурс битка
import requests
response = requests.get('https://coinmarketcap.com/')
response_text = response.text.split("<span>")
for parse_elem_1 in response_parse:
        if parse_elem_1.startswith('$'):
            #print(parse_elem_1)
            for parse_elem_2 in parse_elem_1.split('</span>'):
                    if parse_elem_2.startswith('$') and parse_elem_2[1].isdigit():
                            print(parse_elem_2)