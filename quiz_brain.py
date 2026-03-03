# here we will put the quizzing functionalities

class QuizBrain():

    def __init__(self, question_list):
        self.question = question_list
        self.question_number = 0
        self.score = 0 # deze attributes kan je in de hele file gebruiken
    
    def next_question(self):
        current_question = self.question[self.question_number]
        self.question_number += 1
        user_answer= input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_question(user_answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number != len(self.question):
            return True
        else:
            return False
    
    def check_question(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Right!")
            self.score += 1
        else:
            print("Wrong!")

    

            