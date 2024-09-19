import tkinter as tk

class CoquiUI: 
    window_width = 0
    window_height = 0

    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height

    def init(self):
        # Create the main window
        ui = tk.Tk()
        ui.title("CoquiUI By Rshme")

        # Center the window
        self.center_window(ui)

        # Disable window resizing (width=False, height=False)
        ui.resizable(False, False)

        self.drawLanguageOptions(ui)

        # Create a label
        label = tk.Label(ui, text="This window is centered!")
        label.pack(pady=50)

        ui.mainloop()

    def center_window(self, ui):
        # Get the screen dimensions
        screen_width = ui.winfo_screenwidth()
        screen_height = ui.winfo_screenheight()

        # Calculate the position for the window to be centered
        x = (screen_width // 2) - (self.window_width // 2)
        y = (screen_height // 2) - (self.window_height // 2)

        # Set the dimensions and position of the window
        ui.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def drawLanguageOptions(self, ui):
        # Define the options for the dropdown
        self.languages = ["en", "sp", "fr", "gr", "ch"]
        # Variable to store the selected language
        self.selected_language = tk.StringVar()
        self.selected_language.set(self.languages[0])  # Set default language to "English"

        # Create the OptionMenu (dropdown) widget
        dropdown = tk.OptionMenu(ui, self.selected_language, *self.languages)
        dropdown.pack(pady=10)

        # Create a label to display the selected language
        self.output_label = tk.Label(ui, text="You selected: English")
        self.output_label.pack(pady=20)

        # Trace the selected_language variable and update the label directly
        self.selected_language.trace_add("write", lambda *args: self.output_label.config(
            text=f"You selected: {self.selected_language.get()}"
        ))

