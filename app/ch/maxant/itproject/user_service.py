from ch.maxant.itproject.data.user_repository import UserRepository


class UserService:
    """A service is a place to have logic. It also helps us structure our code so that it becomes easier to
        understand when there is a lot of it.
        This one is for working with user data.

    :type user_repository: UserRepository
    :param user_repository: the repository used for accessing the database - we say it "encapsulates" the database
                            (it wraps it up and hides details)
    """

    def __init__(self, user_repository):
        self.userRepository = user_repository

    def get_user(self, id):
        """Gets the user with the given id.

        :type id: int
        :param id: the id of the user to fetch
        :returns the user for the given id
        """
        return self.userRepository.get_user(id)
