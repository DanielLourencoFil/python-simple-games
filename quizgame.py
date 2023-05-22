user_name = input('Please, write your name\n')

print(f"Hi {user_name}, welcome to my computer game")

print("Let's try your math habilities...")
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    # def __str__(self):
    #     return f'{self.question} : {self.answer}'


question_1 = Question("2 + 2 = ", "4")
question_2 = Question("3 + 3 = ", "6")
question_3 = Question("4 + 4 = ", "8")
question_4 = Question("5 + 5 = ", "10")

questions = [question_1, question_2, question_3, question_4]

quiz_answers = []
for question in questions:
    result = input(question.question)
    if result == question.answer:
        quiz_answers.append(1)
    else:
        quiz_answers.append(0)

result = quiz_answers.count(1)
if result >= len(quiz_answers)/2:
    print(
        f'WeLl done, you have scored {result}/{len(quiz_answers)}. You passed the test!')
else:
    print(
        f'Sorry, you have scored only {result}/{len(quiz_answers)}. You falied the test!')


