userlist = [
    {
        'number': 12345,
        'pin': 1234,
        'balance': 1000,
        'name': 'Karthik'
    },
    {
        'number': 12346,
        'pin': 1235,
        'balance': 1000,
        'name': 'MXCEE'
    },
]
print(len(userlist))
ccnumber = input('Enter cc number')
pin = input('Enter pin number')
userlist = sorted(userlist, key=lambda i: i['name'])

for i in userlist:
    if ccnumber == str(i['number']):
        name = i['name']
        print(f'Welcome,{name}')

#if (userlist[ccnumber]) and (userlist[pin]):
#    print(userlist)
