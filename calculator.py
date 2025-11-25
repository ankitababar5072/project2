from tkinter import *
import math

# Global variables
expr = ""
history_list = []  # Stores calculation history


def press(key):
    """Handle button press"""
    global expr
    expr += str(key)
    display.set(expr)


def equal():
    """Evaluate the expression"""
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        history_list.append(expr + " = " + result)
        update_history()
        expr = ""
    except:
        display.set("Error")
        expr = ""


def clear_entry():
    """Clear only current entry (C)"""
    global expr
    expr = expr[:-1]
    display.set(expr)


def all_clear():
    """Clear all (AC)"""
    global expr
    expr = ""
    display.set("")
    history_list.clear()
    update_history()


def square():
    """Square operation"""
    global expr
    try:
        result = str(eval(f"({expr})**2"))
        display.set(result)
        history_list.append(expr + "² = " + result)
        update_history()
        expr = ""
    except:
        display.set("Error")
        expr = ""


def sqrt():
    """Square root"""
    global expr
    try:
        result = str(math.sqrt(eval(expr)))
        display.set(result)
        history_list.append("√(" + expr + ") = " + result)
        update_history()
        expr = ""
    except:
        display.set("Error")
        expr = ""


def log():
    """Logarithm (base 10)"""
    global expr
    try:
        result = str(math.log10(eval(expr)))
        display.set(result)
        history_list.append("log(" + expr + ") = " + result)
        update_history()
        expr = ""
    except:
        display.set("Error")
        expr = ""


def exp():
    """Exponent (e^x)"""
    global expr
    try:
        result = str(math.exp(eval(expr)))
        display.set(result)
        history_list.append("exp(" + expr + ") = " + result)
        update_history()
        expr = ""
    except:
        display.set("Error")
        expr = ""


def pi():
    """Insert pi constant"""
    global expr
    expr += str(math.pi)
    display.set(expr)


def percent():
    """Percentage"""
    global expr
    try:
        result = str(eval(expr + "/100"))
        display.set(result)
        history_list.append(expr + "% = " + result)
        update_history()
        expr = ""
    except:
        display.set("Error")
        expr = ""


def power():
    """Power x^y"""
    global expr
    expr += "**"
    display.set(expr)


def update_history():
    """Show recent history"""
    history_box.delete(1.0, END)
    for item in history_list[-5:]:
        history_box.insert(END, item + "\n")


# ----------- UI DESIGN -------------
if __name__ == "__main__":
    root = Tk()
    root.title("Advanced Calculator")
    root.configure(bg="grey")
    root.geometry("460x600")

    display = StringVar()
    entry = Entry(root, textvariable=display, font=("Arial", 18), bd=8, insertwidth=2, width=22, borderwidth=4, relief="ridge")
    entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

    # Row 1 - Basic Numbers and Operators
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3)
    ]

    for (text, row, col) in buttons:
        Button(root, text=text, fg='black', bg='White', font=('Arial', 14, 'bold'),
               command=lambda t=text: press(t), height=2, width=8, relief="raised").grid(row=row, column=col, padx=3, pady=3)

    # Row 5 - Scientific + Clear
    Button(root, text='x²', bg='White', font=('Arial', 14, 'bold'), command=square, height=2, width=8).grid(row=5, column=0)
    Button(root, text='√', bg='White', font=('Arial', 14, 'bold'), command=sqrt, height=2, width=8).grid(row=5, column=1)
    Button(root, text='xʸ', bg='White', font=('Arial', 14, 'bold'), command=power, height=2, width=8).grid(row=5, column=2)
    Button(root, text='log', bg='White', font=('Arial', 14, 'bold'), command=log, height=2, width=8).grid(row=5, column=3)

    # Row 6 - Unique scientific functions
    Button(root, text='π', bg='White', font=('Arial', 14, 'bold'), command=pi, height=2, width=8).grid(row=6, column=0)
    Button(root, text='exp', bg='White', font=('Arial', 14, 'bold'), command=exp, height=2, width=8).grid(row=6, column=1)
    Button(root, text='%', bg='White', font=('Arial', 14, 'bold'), command=percent, height=2, width=8).grid(row=6, column=2)
    Button(root, text='+', bg='White', font=('Arial', 14, 'bold'), command=lambda: press('+'), height=2, width=8).grid(row=6, column=3)

    # Row 7 - Equal and Clear buttons
    Button(root, text='AC', bg='White', fg='Black', font=('Arial', 14, 'bold'), command=all_clear, height=2, width=8).grid(row=7, column=0)
    Button(root, text='C', bg='White', fg='Black', font=('Arial', 14, 'bold'), command=clear_entry, height=2, width=8).grid(row=7, column=1)
    Button(root, text='=', bg='White', fg='Black', font=('Arial', 14, 'bold'), command=equal, height=2, width=18).grid(row=7, column=2, columnspan=2)

    # History Label + Box
    Label(root, text="History (last 5):", bg="white", font=('Arial', 12, 'bold')).grid(row=8, column=0, columnspan=4)
    history_box = Text(root, height=5, width=52, bg="white", font=("Arial", 10))
    history_box.grid(row=9, column=0, columnspan=4, padx=5, pady=5)

    root.mainloop()
