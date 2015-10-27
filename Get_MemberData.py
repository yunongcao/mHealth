import urllib2
import requests
import json
import pandas as pd
import numpy as np


def get_auth_token():
    '''
     get an auth token from json response
    '''
    username = 'yunongcao'     # Edit your username here
    password = 'Cao_199181'    # Edit your password here
    # Sending request to api1.0/login by Python requests library
    r = requests.post("https://truthposse2.survos.com/api1.0/security/login",
                      data={"username": username, "password": password})
    json_obj = r.json()
    # Decode the json file and pass the token string to token_string
    token_string = json_obj["accessToken"].encode("ascii", "ignore")
    return token_string


def get_response_json_object(url):
    '''
      returns json object with info
    '''
    # call fuctions to pass the token string
    auth_token = get_auth_token()
    # Send request with token
    req = urllib2.Request(
        url, None, {"Authorization": "Bearer %s" % auth_token})
    response = urllib2.urlopen(req)
    html = response.read()
    # Store response json object to member_json
    member_json = json.loads(html)
    return member_json


def make_dataframe(member_data):
    '''
      Convert json information into pandas.DataFrame 
      to simplify the analysis process in the future
    '''
    # Check the size of members
    member_items = member_data["items"]
    num_item = len(member_data["items"])
    # Initialize the columns of the dataframe using numpy arrays
    member_id = np.zeros(num_item)
    task_count = np.zeros(num_item)
    assignment_count = np.zeros(num_item)
    permission_type_code = np.zeros(num_item)
    enrollment_status_code = np.zeros(num_item)
    # In case of decoding errors, convert some of the columns into Panda.Series
    permission_type_code = pd.Series(permission_type_code)
    enrollment_status_code = pd.Series(enrollment_status_code)
    # Fill data in each column
    for i in range(0, num_item):
        member_id[i] = member_items[i]["id"]
        task_count[i] = member_items[i]["task_count"]
        assignment_count[i] = member_items[i]["assignment_count"]
        permission_type_code[i] = member_items[i]["permission_type_code"]
        enrollment_status_code[i] = member_items[i]["enrollment_status_code"]
    # Concat different columns and make a dataframe
    members = pd.DataFrame({"id": member_id, "TaskCount": task_count, "AssignCount": assignment_count, "Permission": permission_type_code, "Enrollment": enrollment_status_code})
    return members


if __name__ == "__main__":
    URL = "https://truthposse2.survos.com/api1.0/members" # the URL where one wants to get data from
    member_data = get_response_json_object(URL)
    member_df = make_dataframe(member_data)
    print member_df # check result
