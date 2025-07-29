from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    q = Question(question["text"],question["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)


while quiz.still_has_answers():
    quiz.next_question()

print(f"You've completed the quiz.\n"
      f"Your Final score is: {quiz.score}/{quiz.num_questions} ")