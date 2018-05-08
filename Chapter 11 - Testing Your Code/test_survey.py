import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for class anonymous survey."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Russian', 'English', 'Chinese']

    def test_store_single_rensonse(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_responce(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_threee_responses(self):
        """Test that three repsonses are stored correctly."""
        for response in self.responses:
            self.my_survey.store_responce(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()