# ---------------------------- IMPORTS ------------------------------- # 
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARS ------------------------------- #
REP = 0
TIMER_LOOP=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global REP
    global TIMER_LOOP

    REP = 0
    window.after_cancel(TIMER_LOOP)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REP
    REP += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    current_sec = 0


    if REP % 2 == 0 and REP != 8: # If its short break time
        timer_label.config(text="Break", fg=PINK)
        current_sec = short_break_sec
    elif REP % 8 == 0: # if its long break time
        timer_label.config(text="Break", fg=RED)
        current_sec = long_break_sec
    else:
        timer_label.config(text="Work", fg=GREEN)
        current_sec = work_sec

    count_down(current_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global TIMER_LOOP

    count_min = math.floor(count/60)
    count_sec = count % 60

    # Formatting Seconds
    if(count_sec < 10):
        count_sec = f"0{count_sec}"

    # Formatting Minutes
    if(count_min < 10):
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER_LOOP=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Add a checkmark for each work done
        if REP % 2 == 0:
            current_text = checkmark.cget("text")
            checkmark.config(text=f"{current_text}✔")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

# Buttons
# # Start Button
button_start = Button(text="Start", font=(FONT_NAME, 15, "bold"), bg=YELLOW, highlightthickness=0, command=start_timer)
button_start.grid(column=1, row=3)
# # Reset Button
button_start = Button(text="Reset", font=(FONT_NAME, 15, "bold"), bg=YELLOW, highlightthickness=0, command=reset_timer)
button_start.grid(column=3, row=3)

# Checkmark
checkmark = Label(text="", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
checkmark.grid(column=2, row=4)


window.mainloop()