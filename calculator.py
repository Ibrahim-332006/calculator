import tkinter as tk

this_Calc = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["", "0", ".", "="],
]

right_calc = ["÷", "×", "-", "+", "="]
top_calc = ["AC", "+/-", "%"]

row_count = len(this_Calc)  # 5
column_count = len(this_Calc[0])  # 4

color_Black = "#000000"
color_White = "#FFFFFF"
color_saian = "#2c2b2b"
color_yello = "#ffbb02"
color_Ssian = "#555353"
color_white = "white"

# window setup
window = tk.Tk()
window.title("calculator")
window.resizable(True, False)

frame = tk.Frame(window)
label = tk.Label(
    frame,
    text="0",
    font=("Arial", 45),
    background=color_Black,
    foreground=color_White,
    anchor="e",
    width=column_count,
)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")


for row in range(row_count):
    for column in range(column_count):
        value = this_Calc[row][column]
        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 30),
            width=column_count - 1,
            height=1,
            command=lambda value=value: button_clicked(value),
        )
        if value in top_calc:
            button.config(foreground=color_White, background=color_Ssian)
        elif value in right_calc:
            button.config(foreground=color_White, background=color_yello)
        else:
            button.config(foreground=color_White, background=color_saian)
        button.grid(row=row + 1, column=column)

frame.pack()

A = "0"
operator = None
B = None


def calc_all():
    global A, B, operator

    A = "0"
    operator = None
    B = None


def remove_zero(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_calc, top_calc, label, A, B, operator

    if value in right_calc:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

            if operator == "+":
                label["text"] = remove_zero(numA + numB)
            elif operator == "-":
                label["text"] = remove_zero(numA - numB)

            elif operator == "×":
                label["text"] = remove_zero(numA * numB)

            elif operator == "÷":
                label["text"] = remove_zero(numA / numB)

            calc_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    if value in right_calc:
        pass
    if value in top_calc:
        if value == "AC":
            calc_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero(result)
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value

            else:
                label["text"] += value


# cinter the widow
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (screen_width / 2))
window_y = int((screen_height / 2) - (screen_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()

