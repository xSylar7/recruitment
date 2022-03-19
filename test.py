import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import recruitment


class ContainersTestCase(unittest.TestCase):
    def setUp(self):
        self.response = io.StringIO()
        self.skills = [
            "Python",
            "C++",
            "JavaScript",
            "Meeting",
            "Leeting",
            "Eating",
        ]
        self.desired_skill = self.skills[2]
        self.cv = {
            "name": "Harry",
            "age": 30,
            "experience": 10,
            "skills": [self.desired_skill],
        }

    def test_get_skills(self):
        skills = recruitment.get_skills()
        self.assertTrue(len(skills) >= 3, "Must have at least 3 random skills")

    def test_show_skills(self):
        with redirect_stdout(self.response):
            recruitment.show_skills(self.skills)
            stdout = self.response.getvalue()
            self.assertTrue(
                all(skill in stdout for skill in self.skills),
                "Skill(s) are missing from output",
            )

    def test_get_user_skills(self):
        user_input = [1, 2]
        expected = [self.skills[idx - 1] for idx in user_input]
        with redirect_stdout(self.response):
            with patch("builtins.input", side_effect=user_input):
                user_skills = recruitment.get_user_skills(self.skills)
                self.assertTrue(sorted(user_skills) == sorted(expected))

    def test_get_user_cv(self):
        expected = {
            "name": "Harry Potter",
            "age": 12,
            "experience": 4,
        }
        with redirect_stdout(self.response):
            with patch("builtins.input", side_effect=expected.values()):
                with patch(
                    "recruitment.get_user_skills", return_value=[]
                ) as mocked:
                    user_cv = recruitment.get_user_cv(self.skills)
                    mocked.assert_called_once()
                    expected["skills"] = []
                    self.assertTrue(
                        user_cv == expected,
                        f"Expected: '{expected}', got: '{user_cv}'",
                    )

    def test_accepted(self):
        self.assertTrue(
            recruitment.check_acceptance(self.cv, self.desired_skill)
        )

    def test_wrong_age(self):
        cv = dict(self.cv, age=100)
        self.assertFalse(recruitment.check_acceptance(cv, self.desired_skill))

    def test_wrong_experience(self):
        cv = dict(self.cv, experience=0)
        self.assertFalse(recruitment.check_acceptance(cv, self.desired_skill))

    def test_wrong_skill(self):
        self.assertFalse(recruitment.check_acceptance(self.cv, ""))

    @patch("recruitment.check_acceptance", return_value=True)
    @patch("builtins.input", return_value="")
    def test_main_accepted(self, get_input, check_acceptance):
        with redirect_stdout(self.response):
            with patch(
                "recruitment.get_skills", return_value=self.skills
            ) as get_skills:
                with patch(
                    "recruitment.get_user_cv", return_value=self.cv
                ) as get_user_cv:
                    recruitment.main()
                    self.assert_function_calls(
                        get_skills, get_user_cv, check_acceptance, get_input
                    )
                    self.assertTrue("accepted" in self.response.getvalue())

    @patch("recruitment.check_acceptance", return_value=False)
    @patch("builtins.input", return_value="")
    def test_main_rejected(self, get_input, check_acceptance):
        with redirect_stdout(self.response):
            with patch(
                "recruitment.get_skills", return_value=self.skills
            ) as get_skills:
                with patch(
                    "recruitment.get_user_cv", return_value=self.cv
                ) as get_user_cv:
                    recruitment.main()
                    self.assert_function_calls(
                        get_skills, get_user_cv, check_acceptance, get_input
                    )
                    self.assertTrue("rejected" in self.response.getvalue())

    def assert_function_calls(
        self, get_skills, get_user_cv, check_acceptance, get_input
    ):
        get_skills.assert_called_once()
        get_user_cv.assert_called_once_with(self.skills)
        check_acceptance.assert_called_once_with(self.cv, self.desired_skill)
        get_input.assert_not_called()


if __name__ == "__main__":
    unittest.main()
