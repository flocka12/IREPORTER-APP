User =[{
    "id" : 1,
    "firstname" : 'string',
    'lastname': 'string',
    'othernames': 'string',
    'email' : 'string',
    'phonenumber': 'string',
    'username' : 'string',
    'registered' : 'Date',
    'isAdmin' : 'boolean'
}]
class UserName(object):
    def __init__(self):
        self.db = User
        self.id = len(User) - 1

    def save(self,username,email,phonenumber):
        data = {
                "id" : self.id,
                "firstname" : 'string',
                'lastname': 'string',
                'othernames': 'string',
                'email' : email,
                'phonenumber': phonenumber,
                'username' : username,
                'registered' : 'Date',
                'isAdmin' : 'boolean'
                    }

        User.append(data)

        return User
    
    def validator(User):
        for usr in User:
            if usr['username'] == username:
                return True
            else:
                return False, 'user not found'
