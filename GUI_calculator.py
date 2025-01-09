import tkinter as tk

# Function to handle button click
def button_click(event):
    global expression
    text = event.widget.cget("text")  # Get the text of the clicked button
    if text == "=":
        try:
            result = eval(expression)  # Evaluate the expression
            input_var.set(result)     # Display the result
            expression = str(result)
        except Exception as e:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""              # Clear the expression
        input_var.set(expression)
    else:
        expression += text           # Append the button text to the expression
        input_var.set(expression)

# Initialize main application window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#2b2b2b")  # Background color

expression = ""  # To hold the current expression
input_var = tk.StringVar()

# Input field for displaying numbers and results
input_field = tk.Entry(
    root,
    textvar=input_var,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify=tk.RIGHT,
    bg="#333333",  # Dark background for input
    fg="white"     # White text
)
input_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame to hold the calculator buttons
button_frame = tk.Frame(root, bg="#2b2b2b")
button_frame.pack()

# Button layout with colors
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

button_colors = {
    "C": "#d9534f",  # Red for clear
    "=": "#5cb85c",  # Green for equal
    "+": "#5bc0de",  # Blue for operators
    "-": "#5bc0de",
    "*": "#5bc0de",
    "/": "#5bc0de",
}

# Create buttons and add them to the button frame
for row in buttons:
    frame_row = tk.Frame(button_frame, bg="#2b2b2b")
    frame_row.pack(expand=True, fill="both")
    for button_text in row:
        btn_color = button_colors.get(button_text, "#f0ad4e")  # Default orange for numbers
        btn = tk.Button(
            frame_row,
            text=button_text,
            font=("Arial", 20, "bold"),
            bg=btn_color,
            fg="white",
            bd=2,
            relief=tk.RAISED,
            height=2,
            width=5
        )
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", button_click)  # Bind button click event

# Run the application
root.mainloop()
