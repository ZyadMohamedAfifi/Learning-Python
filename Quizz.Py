class Question:
 def __init__(self, prompt, answer):
     self.prompt = prompt
     self.answer = answer

Question_prompt = [
     "what color is the sky \n(a) Blue \n(b) Red \n(c) purple\n\n",
     "What color are apples\n(a)Red \n(b) Green \n(c) brown \n(d) Both Red and Green\n\n",
     "What color are banans \n(a)Yellow \n(b)Cyan \n(c)Black\n\n",
]

questions = [
     Question(Question_prompt[0], "a"),
     Question(Question_prompt[1], "d"),
     Question(Question_prompt[2], "a"),
]

def Quiz(questions):
   Score = 0
   for question in questions:
    
    answer = input(question.prompt).strip().lower()
    if answer.lower() == question.answer:
      Score += 1
       
 
   print("hey you get " + str(Score)+ "/" + str(len(questions)) + "correct")
       
       
Quiz(questions)
