from pathlib import Path

path = Path('learn.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()

for line in lines:
    print(f"- {line}")
    
# learn_string = ''
# for line in lines:
#     learn_string += line
    
# learn_string.replace('Python', 'Java')

print("\nAfter replacement:")
print(contents.replace('Python', 'Java'))