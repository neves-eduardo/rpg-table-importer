import unittest
import dice_string_interpreter

class DiceStringInterpreter(unittest.TestCase):
    def test_should_do_sum(self): 
        self.assertEqual(dice_string_interpreter.interpret_dice_string("[1d1]+10"), 11)

    def test_should_do_sum_and_multiplication(self): 
        self.assertEqual(dice_string_interpreter.interpret_dice_string("[1d1]+10*10"), 101)
        
    def test_should_do_sum_and_multiplication_in_order(self): 
        self.assertEqual(dice_string_interpreter.interpret_dice_string("([1d1]+10)*10"), 110)
        
    def test_should_roll_dice(self): 
        self.assertTrue(10 > dice_string_interpreter.interpret_dice_string("[1d10]") > 1)
    
if __name__ == '__main__':
    unittest.main()