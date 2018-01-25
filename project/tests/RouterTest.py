import unittest
from project import Router


class RouterTest(unittest.TestCase):

    def setUp(self):
        self.app = Router.app.test_client()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
