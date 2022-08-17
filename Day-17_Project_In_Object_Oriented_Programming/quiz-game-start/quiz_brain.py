
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.count = 0

    def next_question(self):
        user_answer = input(f'Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)')
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.count += 1
            print("Yeah that's correct!")
        else:
            print("Wrong answer.")
        print(f'The correct answer was {correct_answer}')
        print(f'Your score is {self.count}')
