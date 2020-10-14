#!/usr/bin/python 
 
import requests 
from requests.auth import HTTPBasicAuth 
import json
 
def http_put(url,jstr): 
    url= url 
    headers = {'Content-Type':'application/json'} 
    resp = requests.get(url,jstr,headers=headers,auth=HTTPBasicAuth('admin', 'admin')) 
    return resp

def get_flow_table_conut(res):
    return len(res["flow-node-inventory:flow"])
     
if __name__ == "__main__": 
    url = 'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1' 
    with open('hardtimeout.json') as f: 
        jstr = f.read() 
    resp = http_put(url,jstr) 
    print(resp.content)
    print(get_flow_table_conut(json.loads(resp.content)))
