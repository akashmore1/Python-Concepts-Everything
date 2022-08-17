from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for que in question_data:
    question_bank.append(
        Question(que['text'], que['answer'])
    )

ask_q = QuizBrain(question_bank)

while ask_q.still_has_questions():
    ask_q.next_question()


