import requests

token = 'e14b32bb-2616-47c4-bc6b-178bac4881b5'
endpoint = 'https://api.botsonic.ai/v1/botsonic/generate'

headers = {
    # 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'User-Agent': 'python-requests/2.28.1',
    'accept': 'application/json',
    'token': token,
}

json_data = {
    'question': 'How to develop these skills?',
    'chat_history': [],
}

response = requests.post(endpoint, headers=headers, json=json_data)