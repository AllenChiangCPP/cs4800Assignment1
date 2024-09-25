import tkinter as tk
import math
from geminiAI import generate_answer

#Create main application window for the calculator
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("600x600")  

#store expression to send to Gemini
expression = ""

#function to update displayed function
def update_expression(val):
    global expression
    expression += str(val)
    text_input.set(expression)
    print(expression)

#function for solving the expression, uses generate answer function to solve expression and display answer and explanation with AI
def evaluate():
    global expression
    try:
        result = generate_answer(expression)
        text_box.delete(1.0, tk.END)  
        text_box.insert(tk.END, result)  
    except Exception as e:
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, "Error")

#function for clearing expression and results box
def clear():
    global expression
    expression = ""
    text_input.set("")
    text_box.delete(1.0, tk.END)

#function for deleting the most recent character
def backspace():
    global expression
    #Check if the expression ends with a specific function (sin, cos, tan, log, exp)
    if expression.endswith("sin"):
        expression = expression[:-3]  
    elif expression.endswith("cos"):
        expression = expression[:-3]  
    elif expression.endswith("tan"):
        expression = expression[:-3]  
    elif expression.endswith("log"):
        expression = expression[:-3]  
    elif expression.endswith("exp"):
        expression = expression[:-3]  
    else:
        #Remove the last character if not function
        expression = expression[:-1]
    
    text_input.set(expression) 
    print(expression)  


#Create a StringVar to hold the display text
text_input = tk.StringVar()

#Create a display text box for expressions
text_display = tk.Entry(root, font=('Arial', 12), textvariable=text_input, bd=20, insertwidth=4, width=40, justify='right')
text_display.grid(row=0, column=0, columnspan=4)

#Define button layout and functionality
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('Back', 5, 3)
]

#Create basic calculator buttons (1-9, =, etc)
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                  command=evaluate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                  command=clear).grid(row=row, column=col)
    elif text == 'Back':
        tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                  command=backspace).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                  command=lambda t=text: update_expression(t)).grid(row=row, column=col)

#Create special function buttons (sin, cos, tan, etc)
advanced_buttons = [
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
    ('exp', 7, 0), ('^', 7, 1)
]
#use for loop and list to construct button layout
for (text, row, col) in advanced_buttons:
    tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
              command=lambda t=text: update_expression(t)).grid(row=row, column=col)

#Create a large text box on the side for displaying the answer and explanation
text_box = tk.Text(root, height=40, width=95, font=('Arial', 12))  # Increased size
text_box.grid(row=0, column=5, rowspan=8, padx=5, pady=10)  # Moved to column 5 with padding

#Run the application
root.mainloop()
