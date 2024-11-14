import tkinter as tk
from ttkbootstrap import Style, Button, Toplevel


# Initialize main window and style
root = tk.Tk()
style = Style('cosmo')

# Function to create and show a custom dialog
def show_custom_dialog():
    # Create a top-level dialog window
    dialog = Toplevel(root)
    dialog.title("Custom Retry Cancel Dialog")
    dialog.geometry("300x150")
    dialog.transient(root)  # Set as a transient window to the root
    dialog.grab_set()  # Make the dialog modal

    # Add a label message
    label = tk.Label(dialog, text="Would you like to retry the operation?", font=("Helvetica", 12))
    label.pack(pady=20)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)

    # Variable to store the result
    result = tk.StringVar(value="")

    # Retry button with custom style
    retry_button = Button(
        button_frame, 
        text="Retry", 
        bootstyle="danger-outline",  # Red retry button
        command=lambda: [result.set("Retry"), dialog.destroy()]
    )
    retry_button.pack(side="left", padx=10)

    # Cancel button with custom style
    cancel_button = Button(
        button_frame, 
        text="Cancel", 
        bootstyle="secondary-outline",  # Gray cancel button
        command=lambda: [result.set("Cancel"), dialog.destroy()]
    )
    cancel_button.pack(side="right", padx=10)

    # Wait for the dialog to close and return the result
    root.wait_window(dialog)
    return result.get()

# Show the custom dialog and get the result
user_choice = show_custom_dialog()

# Check which button was clicked
if user_choice == "Retry":
    print("User chose to retry.")
elif user_choice == "Cancel":
    print("User chose to cancel.")

# Run the application
root.mainloop()