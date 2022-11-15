import requests,urllib
from requests.exceptions import HTTPError
import os.path
import json
import socket
#                          https://realpython.com/python-requests/



data = {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[23.026946783065796,40.50377395344608],[23.026249408721924,40.500673913263924],[23.029704093933105,40.50023336961206],[23.02955389022827,40.49967044851342],[23.032450675964355,40.499776506472855],[23.032890558242798,40.50164473072856],[23.030025959014893,40.50197105277172],[23.03021907806396,40.503308956552026],[23.026946783065796,40.50377395344608]]]}}]}
with open('data.geojson') as json_file:
    json_data = json.load(json_file)
#auth = ('EMAIL_ADDRESS', 'PASSWORD')
headers = {'Content-Type': 'application/json',}
# URL_BASE = 'http://localhost:63342/RESTfullAPI/rest-api/map.html/'
# print('Retrieving authentication token...')
# url = URL_BASE + 'get-auth-token'
# print(url)
# r = requests.get(url, auth=auth)
# print(r.status_code)
# print(r.headers)
# auth_request = r.json()
# token_auth = (auth_request['token'], 'unused')
for url in ['http://localhost:63342/RESTfullAPI/rest-api/map.html?_ijt=a4bd7o8nkfbsgp1ukdhcc0l0m8']:
    try:
        responsepost = requests.post(url, json = data ,headers = headers)
        responseget = requests.get(url)
        #response2 = requests.post(url, data = payload)

        # If the response was successful, no Exception will be raised
        responseget.raise_for_status()
        responsepost.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

#json_response = responsepost.json()
#print(json_response['data'])
# json_response= responseget.json
# responsepost.request.url
#print(responsepost.request.body)
# print(responseget.text)


#print(responseget.text)
#print(responsepost)


# json_response = responsepost.json()
#
# print(json_response)
# print(json_response['headers']['Content-Type'])


# url='https://httpbin.org/post'

#server is the website - client is python script

#make a GET request to get or retrieve data from a specified resource


# response = requests.get(url)

# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')

#GET method
# for url in ['https://api.github.com']: # mporw na balw osa URL thelw
#     try:
#         responseget = requests.get(url)
#         #response2 = requests.post(url, data = payload)
#
#         # If the response was successful, no Exception will be raised
#         responseget.raise_for_status()
#
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')


#GET method with AUTH
#IT can be used to identify only the authorized users

# r=requests.get('https://httpbin.org/basic-auth/emmanuel/testing', auth=('emmanuel', 'testing') )
#
#
# if r.status_code == 200:
#     print('AUTHORIZED USER - WELCOME TO OUR SERVICE')
# elif r.status_code == 401:
#     print('NOT AUTHORIZED USER')




# payload = { 'username': 'Emmanuel', 'password':'Testing'}

#POST method
# for url in ['https://httpbin.org/post']: # mporw na balw osa URL thelw
#     try:
#         #responseget = requests.get(url)
#         responsepost = requests.post(url, json = payload)
#
#         # If the response was successful, no Exception will be raised
#         responsepost.raise_for_status()
#
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')
#
# #responseget.encoding='utf-8'  #  Optional: requests infers this internally
#
# json_response = responsepost.json()
# print(responseget.text)
# # print(json_response)
# print(json_response['headers']['Content-Type'])

