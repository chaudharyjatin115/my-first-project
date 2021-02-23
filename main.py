from questions import Question
question_prompts = [
    " Who is the PM of India\n (a) MODI\n (b) Rahul\n (c) Akhilesh\n\n",
    "who is pres of us\n (a) trump\n (b)harsh (c) biden\n\n",
    "who is pm of pak\n ()imran\n (b)irfan\n (c) ritik\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")




]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(" You got " + str(score) + "/" + str(len(questions)) + " correct ")
run_test(questions)