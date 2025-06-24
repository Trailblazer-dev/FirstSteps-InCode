from pathlib import Path

path = Path('pi_digits.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"The file {path} does not exist.")
else:
    # print(contents)
    lines = contents.splitlines()

    for line in lines:
        print(line)
        