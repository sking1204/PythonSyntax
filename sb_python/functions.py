# def greet (person):
#     return f"Hello there, {person}"

# def greet (person):
#     print(f"Hello there, {person}")

# def divide(a,b):
#     return a/b

# def divide(a,b):
#     if type(a) is int and type(b) is int:
#         return a/b
#     return 'a and b must be integers'

# def three_things(a,b,c):
#     print('Hi')


# def send_email(to_email,from_email,subject,body):
#     email =f"""
#         to: {to_email}
#         from: {from_email}
#         subject: {subject}     
#         ___________________

#         body: {body} 
#         """
#     print(email)


# send_email(subject="MEOW",to_email="Annie@cat.com",
#            from_email='Naz@hello.com,',
#            body="Hi Annie, you are my cat. I love you!")

# def power(num,power=2):
#     return num **power

def add_limited_numbers(a,b):
    """Add two numbers, making sure sum caps at 100."""

    sum = a+b

    #If this required explanation, comment like this

    if sum > 100:
        sum=100

    return sum
