########################################################################################################################
# This is what is called a Class. Nothing to do with school though!
# The word class is another word for "type". We "classify" things into groups. Each group has a type.
# People who use our application are "users". They are of the type "user". We can classify them as "users".
# Their class is "User". Each person is *a* user. Let's say that a user is an object of type User.
# Each one is an instance. We create an instance of the User class by calling a special function called the constructor.
# In Python that function is always named "__init__".
class User:

    # this function is what we call a "constructor", and is used when we create an object of type "User"
    # we pass it an ID and a name - two "attributes" of a User
    def __init__(self, input_id, name):

        # "self" is a special keyword which refers to the current object. In other languages it is called "this".
        # the following line says "take the input parameter called "id" and remember it as the "attribute" named "id".
        self.id = input_id
        self.name = name
