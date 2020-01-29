import io
from contextlib import redirect_stdout
from unittest.mock import patch
import unittest
import recruitment


class ContainersTestCase(unittest.TestCase):

	def setUp(self):
		self.response = io.StringIO()
		self.skill = 6
		self.age_max = "40"
		self.age_max = "25"
		self.experience = "3"

	def test_list_printed(self):
		skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
		user_input = ["kale", 33, 4, 1, 3]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				recruitment.main()
				for skill in skills:
					self.assertTrue( skill in self.response.getvalue())
		

	def test_skill_not_chosen(self):
		user_input = ["kale", 33, 4, 1, 3]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				recruitment.main()
				self.assertFalse( "accepted" in self.response.getvalue())

	def test_wrong_age(self):
		user_input = ["kale", 3, 4, 1, 4]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				recruitment.main()
				self.assertFalse( "accepted" in self.response.getvalue())

	def test_wrong_experience(self):
		user_input = ["kale", 1, 0, 1, 4]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				recruitment.main()
				self.assertFalse( "accepted" in self.response.getvalue())


	def test_accepted(self):
		user_input = ["kale", 30, 6, 1, 6]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				recruitment.main()
				self.assertTrue( "accepted" in self.response.getvalue())


if __name__ == '__main__':
	unittest.main()




