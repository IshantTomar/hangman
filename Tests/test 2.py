import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.geometry("400x300")

# Create a CTkLabel with a border
guesslabel = ctk.CTkLabel(app, text="Guess: ", font=("Arial", 30), border_width=2, border_color="white")
guesslabel.grid(row=4, column=0, padx=20, pady=20)

# Run the application
app.mainloop()