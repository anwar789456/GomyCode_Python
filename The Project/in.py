import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from PIL import Image, ImageTk
class Quiz:
    def __init__(self):
        self.score = 0
        self.current_question = 0
        self.total_questions = 0
        self.questions = []
    def load_questions_from_json(self, json_file):
        with open(json_file, 'r') as file:
            self.questions = json.load(file)
        self.total_questions = len(self.questions)
    def add_to_score(self):
        self.score += 1
    def set_total_questions(self, total_questions):
        self.total_questions = total_questions
    def get_current_question_id(self):
        return self.current_question
    def return_total_questions(self):
        return self.total_questions
    def jump_current_question(self):
        self.current_question += 1
    
    def get_score(self):
        return self.score

def check_answer():
    selected_answer = answer_var.get()
    correct_answer = quiz.questions[quiz.get_current_question_id()]["answer"]
    if selected_answer == correct_answer:
        quiz.add_to_score()
    quiz.jump_current_question()
    if quiz.get_current_question_id() == quiz.return_total_questions():
        show_results()
        show_quiz_finished_message(quiz.get_score())
    if quiz.get_current_question_id() < quiz.return_total_questions():
        update_question()

def show_quiz_finished_message(score):
    if score <=2:
        messagebox.showinfo("Quiz Finished", "You have completed the quiz, but your score is down bad\nmaybe you should switch your career.", icon="info")
    elif 3<=score<=6:
        messagebox.showinfo("Quiz Finished", "You have completed the quiz, your score might get you hired at a small startup.", icon="info")
    elif score>=7:
        messagebox.showinfo("Quiz Finished", "You have completed the quiz, your score shows you are ready for the technical interview.", icon="info")
    root.destroy()

def update_question():
    for widget in root.winfo_children():
        widget.destroy()
    create_widgets()

def show_results():
    score = quiz.get_score()
    messagebox.showinfo("Quiz Results", f"You scored {score} out of {quiz.return_total_questions()} questions!")

def start_quiz():
    difficulty = difficulty_var.get()
    if difficulty.lower() == "easy":
        quiz.load_questions_from_json("C:/Users/anoua/Documents/1st checkpoint/Project/json_file(easy).json")
    elif difficulty.lower() == "hard":
        quiz.load_questions_from_json("C:/Users/anoua/Documents/1st checkpoint/Project/json_file(hard).json")
    update_question()
    

def create_widgets():
    global question_label, answer_var

    question_label = ttk.Label(root, 
                               text=quiz.questions[quiz.get_current_question_id()]["question"],
                               background=background_color,
                               font=("TkHeadingFont" ,30,"bold"),
                               foreground="white")
    question_label.pack(pady=10)

    answer_var = tk.StringVar()
    for option in ["option1", "option2", "option3"]:
        if option in quiz.questions[quiz.get_current_question_id()]:
            ttk.Radiobutton(root,
                            text=quiz.questions[quiz.get_current_question_id()][option],
                            variable=answer_var, value=quiz.questions[quiz.get_current_question_id()][option],
                            ).pack()
    next_button = tk.Button(root, 
                             text="Next",
                             relief=tk.RAISED,
                             bg="#28393a",
                             fg="white",
                             cursor="hand2",
                             activebackground="#badee2",
                             activeforeground="black",
                             font=("TkHeadingFont",20),
                             command=check_answer)
    next_button.pack(pady=10)

# main window
root = tk.Tk()
root.title("Crack The Coding Interview")
x = root.winfo_screenwidth()//4
y = int(root.winfo_screenheight()*0.11)
root.geometry(f"1200x800+{str(x)}+{str(y)}")
root.resizable(height=False, width=False)
background_color = "#3d6466"
root.configure(bg=background_color)


# style for the radio buttons
style = ttk.Style()
style.configure("TRadiobutton",
                background=background_color,
                foreground="black",
                font=("Arial", 25),
                padding=10
                )

logo_img = ImageTk.PhotoImage(file="./images/logo_icon.png")
# width and height for the logo
logo_width = 250
logo_height = 250
# Load image
original_logo_img = Image.open("./images/logo_icon.png")
# Resize image
resized_logo_img = original_logo_img.resize((logo_width, logo_height))
logo_img = ImageTk.PhotoImage(resized_logo_img)
logo_widget = tk.Label(root, image=logo_img, bg="#3d6466")
logo_widget.pack()

tk.Label(root,
          text="Cracking The Coding Interview\n\nTry this mock interview to check if you \nare ready to pass the technical coding interview\n", 
          bg=background_color,
          fg="white",
          font=("TkHeadingFont" ,25),
          ).pack()
# Difficulty selection
difficulty_var = tk.StringVar()
difficulty_label = ttk.Label(root, text="Select Difficulty:",font=("TkHeadingFont" ,25,"bold"),foreground="black",background=background_color,)
difficulty_label.pack(pady=10)
easy_radio = ttk.Radiobutton(root, text="Easy", variable=difficulty_var, value="easy")
easy_radio.pack()
hard_radio = ttk.Radiobutton(root, text="Hard", variable=difficulty_var, value="hard")
hard_radio.pack()
difficulty_var.set("easy")  # Default selection
quiz = Quiz()
# Start button
start_button = tk.Button(
    root,
    text="Start",
    font=("TkHeadingFont",20),
    relief=tk.RAISED,
    width=10,
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=start_quiz)
start_button.pack(pady=20)

# Quit button
tk.Button(
    root,
    text="Quit",
    font=("TkHeadingFont",20),
    relief=tk.RAISED,
    width=10,
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda : quit()
    ).pack()
root.mainloop()