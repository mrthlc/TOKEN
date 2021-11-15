import requests

import json

from getpass import getpass

from requests.auth import HTTPBasicAuth

USER = input('Enter your username for DNA Center')
PASS = getpass('Enter your password for DNA Center')

BASEURL = 'https://sandboxdnac.cisco.com'
authAPI = '/dna/system/api/v1/auth/token'

payload={}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

dnaAuth = BASEURL + authAPI

response = requests.post(dnaAuth, auth=HTTPBasicAuth(USER, PASS), headers=headers, data=payload)

tokenJSON = response.json()

TOKEN = tokenJSON['Token']

print('Your  token was generated succesfully. Your token is:\n ' + TOKEN)
