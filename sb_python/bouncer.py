# age =19

# if age >=21:
#     print('you can drink')
# elif age >=18:
#     print('you can come in but no drinking')
# else:
#     print('sorry go home kid')


age =19
isBirthday=False

if age >=21:
    print('you can drink')
    if isBirthday:
        print('happy birthday, here is a free martini')
elif age >=18:
    print('you can come in but no drinking')
    if isBirthday:         
        print('happy birthday, here is a free shirley temple')
    
else:
    print('sorry go home kid')