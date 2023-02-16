# necessary libraries
import unittest
import phone_call 

class TestScript(unittest.TestCase):
    def test_main(self):
        """ new lines of code can be added to test a new phone number with its price """
        self.assertEqual(phone_call.main("46737367456"), 0.9)  # testing the sample phone numbers with their corresponding price from the description of the problem
        self.assertEqual(phone_call.main("12025550131"), 0.9)
        self.assertEqual(phone_call.main("46455263698"), 0.17)
        self.assertEqual(phone_call.main("26845856984"), 5.1)
        self.assertEqual(phone_call.main("46732695847"), 1.0)
        self.assertEqual(phone_call.main("48752566985"), 1.2)
        self.assertEqual(phone_call.main("66255884858"), False)
         
if __name__ == "__main__":
    unittest.main()