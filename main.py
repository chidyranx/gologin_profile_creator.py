import time

from gologin import GoLogin
import requests
import os
from datetime import datetime
token = "{{ your gologin token/api }}"
API_URL = 'https://api.gologin.com'
PROFILES_URL = 'https://gprofiles-new.gologin.com/'
response = requests.get(  "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25",  headers={ "Authorization": "{{ your webshare token/api }}" })


gl = GoLogin({
	"token": token,
	})
num_iterations = 100
path = "C:\\Users\\HP\\Desktop\\GologinProfiles"

# Check if the path exists
if not os.path.exists(path):
    # Create the directory
    # 'path' can also be replaced with the variable you have defined
    os.makedirs(path)

for i in range(num_iterations):
    # Specify the path where you want to create the folder
    num_items = len(os.listdir(path))
    position_to_access = num_items + 1

  
    profile_id = gl.create({
        "name": num_items + 1,
        "os": 'mac',
        "navigator": {
            "language": 'en-US',
            "userAgent": 'random',  # Your userAgent (if you don't want to change, leave it at 'random')
            "resolution": '1024x768',  # Your resolution (if you want a random resolution - set it to 'random')
            "platform": 'win',
        },
        'proxyEnabled': False,  # Specify 'false' if not using proxy
        'proxy': {
        'mode': 'gologin', # Specify 'none' if not using proxy
        'autoProxyRegion': 'us'
        # "host": '',
        # "port": '',
        # "username": '',
        # "password": '',
    },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
        },
    });
    profile = gl.getProfile(profile_id);
    file_number = f'{num_items + 1} - {profile_id}.txt'
    print(file_number)
    text_file_path = os.path.join(path, file_number)
    with open(text_file_path, 'w') as f:
        f.write(str(num_items))
