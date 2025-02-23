# ---------------------------- IMPORTS ------------------------------- # 
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=2, row=1)

# Buttons
# # Start Button
button_start = Button(text="Start", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
button_start.grid(column=1, row=3)
# # Reset Button
button_start = Button(text="Reset", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
button_start.grid(column=3, row=3)

# Checkmark
checkmark = Label(text="✔", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
checkmark.grid(column=2, row=4)




window.mainloop()