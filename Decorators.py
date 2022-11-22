# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def check(*args):
        if(args[0]['valid']):
            return fn(*args)
        else:
            return invalid()
    return check

@authenticated
def message_friends(user):
    print('message has been sent')

def invalid():
    print('Invalid User')

message_friends(user1)