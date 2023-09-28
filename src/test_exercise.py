import unittest as test
import exercise

class TestExercise(test.TestCase):

    def test_y_is_true(self):
        self.assertTrue(exercise.str_to_bool('y')) #* Check argument passed is true.

    def test_yes_is_true(self):
        self.assertTrue(exercise.str_to_bool('Yes'))

    def test_int_check(self):
        with self.assertRaises(AttributeError):
            self.assertTrue(exercise.str_to_bool(3))

if __name__=="__main__":
    test.main()