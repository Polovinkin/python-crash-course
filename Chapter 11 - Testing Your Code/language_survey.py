from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, then store responses to the question
my_survey.show_question()
print('Enter "q" any time to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_responce(response)

# Show the survey results.
print('\nThanks for participating!')
my_survey.show_results()