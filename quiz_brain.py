class QuizBrain:
    def __init__(self, list_of_questions):
        self.score = 0
        self.question_number = 0
        self.question_list = list_of_questions

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.problem} (True/False): ")
        self.check_score(answer, current_question.solution)

    def check_score(self, answer, correct_answer):
        if correct_answer.lower() == answer:
            self.score += 1
            print("You are correct !!")
        else:
            print("You got it wrong")
        print(f"Your score is {self.score}")
        print(f"The correct answer is {correct_answer}")