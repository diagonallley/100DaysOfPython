with open('./Input/Names/invited_names.txt',mode='r') as data:
    names=data.read()

list_of_names=names.split('\n')


with open("./Input/Letters/starting_letter.txt") as data:
    messages=data.readlines()

for m in messages:
    if m=='\n':
        messages.remove('\n')
print(messages)
message=''.join(messages)

# with open("./Output/ReadyToSend") 

for name in list_of_names:
    message.strip()
    message=message.replace('[name]',name)
    print(message)
    with open(f'./Output/ReadyToSend/letter_for_{name}', mode='w') as data:
        data.write(message)
    message=message.replace(name,'[name]')