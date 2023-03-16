import requests

API = 'YOUR_ADMIN_API_KEY'
PANEL = 'panel.zluqe.com'

headers = {
    'Authorization': f'Bearer {API}'
}

try:
    response = requests.get(f'https://{PANEL}/api/application/servers', headers=headers)
    response.raise_for_status()
    data = response.json()

    for server in data['data']:
        if server['attributes']['suspended']:
            continue
        
        print(f"Scanning {server['attributes']['name']}...")
        
        headers2 = {
            'Authorization': f'Bearer {API}'
        }
        
        response2 = requests.get(f'https://{PANEL}/api/client/servers/{server["attributes"]["uuid"]}/resources', headers=headers2)
        response2.raise_for_status()
        data2 = response2.json()
        
        if data2['attributes']['resources']['disk_bytes'] != 0:
            continue
        
        confirmation = input(f"Are you sure you want to delete {server['attributes']['name']}? (y/n) ")
        
        if confirmation.lower() == 'y':
            response3 = requests.delete(f'https://{PANEL}/api/application/servers/{server["attributes"]["id"]}', headers=headers)
            response3.raise_for_status()
            print(f"Deleted: {server['attributes']['name']}")
        else:
            print(f"Not deleting {server['attributes']['name']}")

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}")
except Exception as err:
    print(f"Error: {err}")
