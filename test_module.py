import unittest

################## INI - Test for Practice 1 #############
#import pytest
#from arithmetic_arranger import arithmetic_arranger

# test_cases = [
#     pytest.param(
#         [['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']],
#         'Error: Numbers must only contain digits.',
#         'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."',
#         id='test_only_digits')
# ]

# @pytest.mark.parametrize('arguments,expected_output,fail_message', test_cases)
# def test_successful_no_result(arguments, expected_output, fail_message):
#     result = arithmetic_arranger(*arguments)
#     assert result == expected_output, fail_message

################## FIN - Test for Practice 1 #############

################## INI - Test for Practice 3 #############
# import budget
# from budget import create_spend_chart

# class UnitTests(unittest.TestCase):
#     maxDiff = None
#     def setUp(self):
#         self.food = budget.Category("Food")
#         self.entertainment = budget.Category("Entertainment")
#         self.business = budget.Category("Business")
    
#     def test_check_funds(self):
#         self.food.deposit(10, "deposit")
#         actual = self.food.check_funds(20)
#         expected = False
#         self.assertEqual(actual, expected, 'Expected `check_funds` method to be False')
#         actual = self.food.check_funds(10)
#         expected = True
#         self.assertEqual(actual, expected, 'Expected `check_funds` method to be True')

#     def test_to_string(self):
#         self.food.deposit(900, "deposit")
#         self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#         self.food.transfer(20, self.entertainment)
#         actual = str(self.food)
#         print(self.food)
#         expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
#         print(expected)
#         self.assertEqual(actual, expected, 'Expected different string representation of object.')
        
#     def test_create_spend_chart(self):
#         self.food.deposit(900, "deposit")
#         self.entertainment.deposit(900, "deposit")
#         self.business.deposit(900, "deposit")
#         self.food.withdraw(105.55)
#         self.entertainment.withdraw(33.40)
#         self.business.withdraw(10.99)
#         actual = create_spend_chart([self.business, self.food, self.entertainment])
#         print(actual)
#         expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
#         print(expected)
#         self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')

################## FIN - Test for Practice 3 #############

################## INI - Test for Practice 4 #############
# import shape_calculator
# class UnitTests(unittest.TestCase):
#     maxDiff = None
#     def setUp(self):
#         self.rect = shape_calculator.Rectangle(3, 6)
#         self.sq = shape_calculator.Square(5)
            
#     def test_set_attributes(self):
#         self.rect.set_width(7)
#         self.rect.set_height(8)
#         self.sq.set_side(2)
#         actual = str(self.rect)
#         expected = "Rectangle(width=7, height=8)"
#         self.assertEqual(actual, expected, 'Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"')
#         actual = str(self.sq)
#         expected = "Square(side=2)"
#         self.assertEqual(actual, expected, 'Expected string representation of square after setting new values to be "Square(side=2)"')
#         self.sq.set_width(4)
#         actual = str(self.sq)
#         expected = "Square(side=4)"
#         self.assertEqual(actual, expected, 'Expected string representation of square after setting width to be "Square(side=4)"')   

################## FIN - Test for Practice 4 #############

################## INI - Test for Practice 5 #############
import prob_calculator

class UnitTests(unittest.TestCase):
    maxDiff = None
    def test_hat_class_contents(self):
        hat = prob_calculator.Hat(red=3,blue=2)
        actual = hat.contents
        expected = ["red","red","red","blue","blue"]
        self.assertEqual(actual, expected, 'Expected creation of hat object to add correct contents.')
        
    def test_hat_draw(self):
        hat = prob_calculator.Hat(red=5,blue=2)
        actual = hat.draw(2)
        expected = ['blue', 'red']
        self.assertEqual(actual, expected, 'Expected hat draw to return two random items from hat contents.')
        actual = len(hat.contents)
        expected = 5
        self.assertEqual(actual, expected, 'Expected hat draw to reduce number of items in contents.')
        
    def test_prob_experiment(self):
        hat = prob_calculator.Hat(blue=3,red=2,green=6)
        probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
        actual = probability
        expected = 0.272
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
        hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
        probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')

################## FIN - Test for Practice 5 #############

########## - Using Unit TEST - ###########
if __name__ == "__main__":
    unittest.main()
