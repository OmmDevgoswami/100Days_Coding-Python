from Data import question_data
from Question_Model import question
from Quiz_Brain import quiz_brain


question_resource = []
for question_item in question_data:
    question_text = question_item["text"]
    question_answer = question_item["answer"]
    question_trivia = question_item["trivia"]
    new_question = question(question_text, question_answer, question_trivia)
    question_resource.append(new_question)
    
print (question_resource)