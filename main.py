import tkinter as tk
import json


def show_frame(frame):
    frame.tkraise()


def get_quiz():
    try:
        quiz_info = open("dependencies//quizzes.json", "r")
        quiz_info = json.load(quiz_info)
        quiz_info = quiz_info["Quizzes"]
        quiz_list = []
        for i in range(len(quiz_info)):
            quiz_list.append(quiz_info[i]["title"])
        return quiz_list
    except FileNotFoundError:
        print("File not found")
        quiz_list = []
        return quiz_list
    except json.decoder.JSONDecodeError:
        print("File is not in JSON format")
        quiz_list = []
        return quiz_list


# Set up the main window
window = tk.Tk()
window.title("Quiz")
window.configure(background="white")
window.resizable(False, False)
window.rowconfigure([0, 1], weight=1)
window.columnconfigure(0, weight=1)
window.state("zoomed")

# Set up different frames
title_frame = tk.Frame(window, bg="white")
load_quiz_frame = tk.Frame(window, bg="white")
edit_quiz_frame = tk.Frame(window, bg="white")
quiz_frame = tk.Frame(window, bg="white")

for frame in (title_frame, load_quiz_frame, edit_quiz_frame, quiz_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# ---------- Code for Title Screen ----------
welcome = tk.Frame(title_frame, bg="white")
heading = tk.Label(
    master=welcome,
    text="Welcome!",
    font=("Helvetica", 32),
    bg="white"
)
description = tk.Label(
    master=welcome,
    text="Create your own or load a quiz using the corresponding "
    "buttons below!",
    font=("Helvetica", 24),
    bg="white"
    )
buttons = tk.Frame(title_frame, bg="white")
create_button = tk.Button(
    master=buttons,
    text="Create Quiz",
    width=12,
    padx=90,
    pady=80,
    bd=0, bg="lightblue",
    activebackground="#5391b0",
    font=("Helvetica", 40),
    command=lambda: show_frame(edit_quiz_frame)
)
load_button = tk.Button(
    master=buttons,
    text="Load Quiz",
    width=12,
    padx=90,
    pady=80,
    bd=0,
    bg="lightblue",
    activebackground="#5391b0",
    font=("Helvetica", 40),
    command=lambda: show_frame(load_quiz_frame)
    )
# Pack everything
welcome.grid(row=0, column=0, sticky="ew", padx=18, pady=100)
heading.pack()
description.pack()
create_button.grid(row=0, column=0, sticky="ew", padx=106, pady=50)
load_button.grid(row=0, column=1, sticky="ew", padx=106, pady=50)
buttons.grid(row=1, column=0, sticky="ew")

# ---------- Code for Load Quiz Screen ----------
quiz_titles = get_quiz()
# Checks if there are quizzes to load
if len(quiz_titles) == 0:
    error_label = tk.Label(
        master=load_quiz_frame,
        text="Unable to load quizzes.\nNo quizzes found.",
        font=("Helvetica", 32),
        bg="white"
        )
    back_button = tk.Button(
        master=load_quiz_frame,
        text="Back to title screen",
        width=18,
        bd=0, bg="lightblue",
        activebackground="#5391b0",
        font=("Helvetica", 40),
        command=lambda: show_frame(title_frame)
    )
    # Pack everything
    error_label.grid(row=0, column=0, sticky="ew", padx=490, pady=100)
    back_button.grid(row=1, column=0, sticky="ew", padx=490, pady=100)
else:
    # Heading text
    heading = tk.Label(
        master=load_quiz_frame,
        text="Choose a quiz!",
        font=("Helvetica", 32),
        width=100,
        bg="white"
        )
    # Quiz Selector
    load_quiz_frame.columnconfigure([0, 3], weight=5)
    load_quiz_frame.columnconfigure(1, weight=100)
    load_quiz_frame.columnconfigure(2, weight=1)
    canvas_container = tk.Canvas(load_quiz_frame, height=480)
    options = tk.Frame(canvas_container)
    scrollbar = tk.Scrollbar(
        load_quiz_frame,
        orient="vertical",
        command=canvas_container.yview
        )
    canvas_container.create_window(
        (0, 0),
        window=options,
        anchor="nw"
        )
    # Getting quiz titles and creating buttons for list
    for item in quiz_titles:
        quiz_no = quiz_titles.index(item)
        button = tk.Button(
            master=options,
            text=item,
            width=58,
            wraplength=900,
            font=("Helvetica", 20),
            bg="lightblue",
            activebackground="#5391b0"
            # command=lambda: show_frame(quiz_frame)
            )
        button.pack(fill="x")
    options.update()
    canvas_container.configure(
        yscrollcommand=scrollbar.set,
        scrollregion="0 0 0 %s" % options.winfo_height()
        )
    # Back button
    back_button = tk.Button(
        master=load_quiz_frame,
        text="Back",
        width=18,
        bd=0, bg="lightblue",
        activebackground="#5391b0",
        font=("Helvetica", 18),
        command=lambda: show_frame(title_frame)
    )
    # Pack everything
    spacer1 = tk.Label(load_quiz_frame, bg="white")
    spacer2 = tk.Label(load_quiz_frame, bg="white")
    spacer1.grid(row=0, column=0, sticky="ew", padx=180)
    spacer2.grid(row=0, column=3, sticky="ew", padx=180)
    heading.grid(row=0, column=1, columnspan=2, sticky="ew", pady=60)
    canvas_container.grid(row=1, column=1, sticky="ew")
    scrollbar.grid(row=1, column=2, sticky="ns")
    back_button.grid(
        row=2, column=1, columnspan=2,
        sticky="ew", padx=200, pady=50
        )
    load_quiz_frame.grid(row=0, column=0)

# Run mainloop
if __name__ == "__main__":
    show_frame(title_frame)
    window.mainloop()
