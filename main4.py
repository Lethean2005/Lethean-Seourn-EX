user_input= int(input('Enter your number'))
user_message=''
if user_input< 0:
    user_message = 'Negative Number'
else:
    user_message = "Positive number"
print(user_message)