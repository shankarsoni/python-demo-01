first = 'John'
second = 'Smith'
message = first+' ['+second+'] is a coder.'
print(message)

message = f'{first} [{second}] is a coder.'
print(message)
print(f'Message length: {len(message)}')
print(f'{message.lower()}')
print(f'Find result:: {message.find("is")}')

print(f'Is {message} contains "code" {"Coder" in message}')


