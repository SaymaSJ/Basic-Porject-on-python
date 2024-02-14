# #GUI
# import tkinter as tk

# def update_label():
#     label.config(text="you calculator")

# # Create a new Tkinter window
# window = tk.Tk()

# # Set the window title
# window.title("Calculator")

# # Create a label widget
# label = tk.Label(window, text="Hello!")

# # Create a button widget
# button = tk.Button(window, text="Click Me for opening the calculator option", command=update_label)

# # Add the label and button to the window
# label.pack()
# button.pack()

# # Start the Tkinter event loop
# window.mainloop()

import tkinter as tk

def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            label_result.config(text="Cannot divide by zero")
        else:
            result = num1 / num2
            label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input")

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Simple Calculator")

# Create input fields for numbers
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1)

# Create buttons for operations
button_add = tk.Button(window, text="Add", command=add)
button_add.grid(row=2, column=0)

button_subtract = tk.Button(window, text="Subtract", command=subtract)
button_subtract.grid(row=2, column=1)

button_multiply = tk.Button(window, text="Multiply", command=multiply)
button_multiply.grid(row=3, column=0)

button_divide = tk.Button(window, text="Divide", command=divide)
button_divide.grid(row=3, column=1)

# Create a label to display the result
label_result = tk.Label(window, text="")
label_result.grid(row=4, columnspan=2)

# Start the Tkinter event loop
window.mainloop()


