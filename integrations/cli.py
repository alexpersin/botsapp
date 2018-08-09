from prompt_toolkit import prompt

print("--- Botsapp Command Line Interface ---\n")
print("Botsapp: Enter your name")
user_name = prompt('>')


while True:
    user_input = prompt('>')
    print(user_input)
    