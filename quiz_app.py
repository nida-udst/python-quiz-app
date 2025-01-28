import tkinter as tk

questions = [
    {
        "topic": "loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Correct answer is '0 1 2'
    },
    {
        "topic": "lists",
        "question": "What will be the result of this Python code?",
        "code": "lst = [1, 2, 3]\nlst.append(4)\nprint(lst)",
        "options": ["[4, 1, 2, 3]", "[1, 2, 4]", "[1, 2, 3, 4]", "[1, 3, 4]"],
        "answer": 2  # Correct answer is '[1, 2, 3, 4]'
    },
    {
        "topic": "dictionaries",
        "question": "What will be the output of this Python code?",
        "code": "d = {'a': 1, 'b': 2}\nd['c'] = 3\nprint(d)",
        "options": ["{'a': 1, 'b': 2}", "{'a': 1, 'b': 2, 'c': 3}", "{'c': 3, 'a': 1, 'b': 2}", "{'a': 1, 'b': 3, 'c': 2}"],
        "answer": 1  # Correct answer is "{'a': 1, 'b': 2, 'c': 3}"
    },
    {
        "topic": "string manipulation",
        "question": "What will be the output of this Python code?",
        "code": "s = 'hello'\nprint(s.upper())",
        "options": ["'hello'", "'HELLO'", "'hElLo'", "'Hello'"],
        "answer": 1  # Correct answer is "'HELLO'"
    },
    {
        "topic": "conditionals",
        "question": "What will be the output of this Python code?",
        "code": "x = 10\nif x > 5:\n    print('greater')\nelse:\n    print('lesser')",
        "options": ["'lesser'", "'equal'", "Nothing", "'greater'"],
        "answer": 3  # Correct answer is "'greater'"
    },
    {
        "topic": "functions",
        "question": "What will be the output of this Python code?",
        "code": "def func(a, b):\n    return a + b\nprint(func(2, 3))",
        "options": ["None", "6", "5", "23"],
        "answer": 2  # Correct answer is "5"
    }
]


window = tk.Tk()
window.title("Python Quiz")
window.geometry("400x450")
 
#Stores topic input
def store_input():
    topic = entry.get().strip().lower()
    for i in range(len(questions)):
        if questions[i]["topic"] == topic:
            display_question(i)
    
#Displays Topic Question and Options
def display_question(index):
    t = questions[index]["topic"]
    q = questions[index]["question"]
    c = questions[index]["code"]
    o = questions[index]["options"]
    global correct_answer
    correct_answer = questions[index]["answer"]
    topic.config(text=f"Topic: {t}")
    question.config(text=f"Question: {q}")
    code.config(text=c)

    selected.set(None)
    answer.config(text="")
    for widget in options_frame.winfo_children():
        widget.destroy()
    
    for i in range(len(o)):
        option = tk.Radiobutton(options_frame, text=o[i], value =i, variable=selected)
        option.grid()

#Checks answer
def check_answer():
    selected_answer = selected.get()
    if selected_answer == correct_answer:
        answer.config(text="Correct! Well donne!")
    else:
        answer.config(text="Not Quite! Try Again!")
    

#Choose Topic
topic_input = tk.Label(window, text="Enter Python Topic (Loops, Lists, Dictionaries, Functions, Conditionals)")
entry = tk.Entry(window, width=60)
button = tk.Button(window, text = "Submit Topic", width=50, command=store_input)

topic_input.grid(row=0, column=0,sticky="w",pady=5,padx=5)
entry.grid(row=1,column=0,pady=5,padx=5)
button.grid(row=2,column=0,pady=5,padx=5)


#Display Question
topic = tk.Label(text="Topic: ")
question = tk.Label(text="Question: ")
code = tk.Label(text="")
topic.grid(row=3,column=0)
question.grid(row=4, column=0)
code.grid(row=5, column=0)

options_frame = tk.Frame(window)
options_frame.grid()
selected = tk.IntVar()
selected.set(None)

#Submit Button and Answer
submit = tk.Button(window, text = "Submit Answer", width=20, command = check_answer)
submit.grid()
answer = tk.Label(text="")
answer.grid()

window.mainloop()
