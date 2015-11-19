import urllib2
import requests
import yaml
import pandas as pd
import numpy as np


def get_auth_token():
    '''
     get an auth token from json response
    '''
    global token_string
    global endpoint 
    endpoint = "https://truthposse2.survos.com/api1.0/"
    username = raw_input('Please enter your username')
    password = raw_input('Please enter your password')    # Edit your password here
    response = requests.post(endpoint+"security/login",
                             data={"username": username, "password": password})
    json_obj = response.json()
    token_string = json_obj["accessToken"].encode("ascii", "ignore")
    #return token_string

 # Developing
 def get_response_json_object(object, project, *arg):
    '''
      returns json object with info
    '''
    global headers
    headers = {"Authorization": "Bearer %s" % token_string}
    req = urllib2.Request(
        endpoint+"members", None, headers)
    response = urllib2.urlopen(req)
    json_string = response.read()
    members_list = yaml.safe_load(json_string)
    return members_list

### Developing
class member:
    #return index number
    #member  = members_list(member_list[i])
    
    def accept(self):
    '''
    Accept/Reject members by specific values
    '''
    url = endpoint+"members/applicants/accept"
    acc_id = member_df["id"][(member_df["zip"] == 11104)]
    data = {'id': acc_id}
    response = requests.patch(url, headers=headers,
                              data=data)  
    print response.json()
    
    def rejct(self):
    '''
    Accept/Reject members by specific values
    '''
    url = endpoint+"members/applicants/rejct"
    acc_id = member_df["id"][(member_df["zip"] == 11104)]
    data = {'id': acc_id}
    response = requests.patch(url, headers=headers,
                              data=data)  
    print response.json()


if __name__ == "__main__":
    get_auth_token()
