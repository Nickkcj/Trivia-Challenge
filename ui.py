from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        
        #Create the white board
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)

        #Create the score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        #Put the false and true buttons
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, bd=0,
                                   highlightbackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, bd=0,
                                   highlightbackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0)
        
        





        self.window.mainloop()
