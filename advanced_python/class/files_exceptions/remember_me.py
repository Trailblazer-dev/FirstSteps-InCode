from pathlib import Path
import json

path = Path('username.json')

if path.exists():
    contents = path.read_text()
    username  = json.loads(contents)
    print(f"Welcome back, {username}")


else:
    username = input("What is your name?")
    path = Path('username.json')
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll rember you when you come back, {username} !")

