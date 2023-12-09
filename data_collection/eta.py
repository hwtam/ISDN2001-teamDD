import requests
import subprocess
import datetime
import sys
import os

os.chdir(os.path.dirname(__file__))
subprocess.run("cls", shell=True)

def get(route_id, route_seq, stop_seq) :
  url = f"https://data.etagmb.gov.hk/eta/route-stop/{route_id}/{route_seq}/{stop_seq}"
  response = requests.get(url)
  if response.status_code == 200:
      data = response.json()
      return data
  else:
      print("Failed")
      return None
  
for i in range(1, 8):
    eta = get(2004825, 2, i)['data']['eta']
    print(str(i) + " : " + eta[0]['timestamp'][11:-10] + " , " + eta[1]['timestamp'][11:-10] + " , " + eta[2]['timestamp'][11:-10])