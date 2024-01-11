str = input()

converted_str=""
for char in str:
    if char.islower():
        converted_str += char.upper()
    elif char.isupper():
        converted_str += char.lower()
    else:
        break
        
print(converted_str)