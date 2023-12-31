from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data["results"]:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quizbrain.score}/{len(question_bank)}")