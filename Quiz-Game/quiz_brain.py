class QuizBrain:
    def __init__(self, questions):
        self.num_questions = 0
        self.score = 0
        self.num_answers = questions

    def still_has_answers(self):
        if self.num_questions < len(self.num_answers):
            return True
        else:
            return False


    def next_question(self):
        current_question = self.num_answers[self.num_questions]
        self.num_questions += 1
        user_answer = input(f"Q. {self.num_questions} : {current_question.text} (True/False)?: ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, current_answer ):
        if user_answer.lower() == current_answer.lower():
            self.score+= 1
            print("You got it right!")
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer was: {current_answer}")
        print(f"Your current score is: {self.score}/{self.num_questions}")
        print("\n")
