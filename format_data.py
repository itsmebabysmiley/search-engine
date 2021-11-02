'''
This is just a script for remove characters that is not English alphabet and replace with ***.
@author: Baby
@last modify: Nov 2,2021
'''
new_file = open("magna_json_normalize.json", "x")
file = open("magna-sample.json", "r",encoding='utf-8')
for line in file:
    for character in line:
        try:
            character.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            print(f'NOT ENGLISH! = {character}')
            new_file.write('***')
        else:
            new_file.write(character)

file.close()
new_file.close()

# new_file = open("magna_json_normalize.json", "r")

# print(new_file.read())

# new_file.close()