import tkinter as tk

def check_input():
    user_input = entry.get()
    print(f"User entered: {user_input}")
    # Schedule the check_input function to run again after 1000 milliseconds (1 second)
    root.after(1000, check_input)

root = tk.Tk()
root.title("Constant Input Check")

entry = tk.Entry(root)
entry.pack(pady=10)

check_input()  # Start the input check loop

root.mainloop()