import json
import requests

def load_config(path="config.json") -> dict:
    with open(path, "r", encoding="utf-8") as config_file:
        return json.load(config_file)
    

def send_msg(msg:str) -> None:
    config = load_config()
    if not config['webhook']['url'] == "YOUR URL HERE":
        json_msg = {"text": msg}

        response = requests.post(config['webhook']['url'], json=json_msg)

        if response.status_code == 200:
            print("Successfully sent message")
        else:
            print(f"Failed to send message: {response.status_code}")
    else:
        print("u forgot to type ur google chat webhook url")
    
