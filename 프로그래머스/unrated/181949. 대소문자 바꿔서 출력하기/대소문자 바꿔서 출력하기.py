msgs = input()

answer = ''
for msg in msgs:
    if msg.isupper():
        answer += msg.lower()
    elif msg.islower():
        answer += msg.upper()
        
print(answer)