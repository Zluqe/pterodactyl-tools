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
            print(f"Suspended server found: {server['attributes']['name']}")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}")
except Exception as err:
    print(f"Error: {err}")