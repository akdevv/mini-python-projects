from data import q_data
from quiz_brain import QuizBrain
from question_model import Question

q_bank = []

for q in q_data: 
    new_q = Question(q["text"], q["answer"])
    q_bank.append(new_q)

quiz = QuizBrain(q_bank)

while quiz.still_has_q():
    quiz.next_q()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.q_number}")