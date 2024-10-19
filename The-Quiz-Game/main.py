from question_model import Question

from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    text = item["text"]
    answer = item["answer"]
    new_question = Question(text , answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
 quiz.next_question()

print(f"your total score is {quiz.score}/{quiz.question_number}")

