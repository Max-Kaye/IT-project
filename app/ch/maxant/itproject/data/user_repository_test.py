import unittest

from ch.maxant.itproject.data.user_repository import UserRepository


class TestStringMethods(unittest.TestCase):

    def test_get_user(self):
        u = UserRepository.get_user(1)
        self.assertEqual(u.id, 1)
        self.assertEqual(u.name, 'Ant')

    ####################################################################################################################
    # below here are some examples:

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
