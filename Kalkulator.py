import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Ini Itu Kalkulator")
        master.config(bg='#BFEAF5')

        # Create the display widget
        self.display = tk.Entry(master, bg='#EAFDFC', width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Create the buttons
        button_colors = {
            "1": "#91D8E4", "2": "#91D8E4", "3": "#91D8E4", "/": "#82AAE3", "C": "#82AAE3",
            "4": "#91D8E4", "5": "#91D8E4", "6": "#91D8E4", "*": "#82AAE3", "Del": "#82AAE3",
            "7": "#91D8E4", "8": "#91D8E4", "9": "#91D8E4", "-": "#82AAE3", "Exit": "#82AAE3",
            "0": "#91D8E4", ".": "#82AAE3", "=": "#82AAE3", "+": "#82AAE3", 
        }
        buttons = [
            "1", "2", "3", "/", "C",
            "4", "5", "6", "*", "Del",
            "7", "8", "9", "-", "Exit",
            "0", ".", "=", "+", 
        ]

        # Add the buttons to the grid
        row = 1
        col = 0
        for button in buttons:
            if button == "":
                continue
            command = lambda x=button: self.button_click(x)
            tk.Button(master, text=button, width=5, bg=button_colors[button], command=command).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Configure the grid to resize with the window
        for i in range(5):
            master.grid_columnconfigure(i, weight=1)
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)

    def button_click(self, button):
        if button == "C":
            self.display.delete(0, tk.END)
        elif button == "CE":
            self.display.delete(0, tk.END)
        elif button == "Exit":
            self.master.destroy()
        elif button == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "Del":
            self.display.delete(len(self.display.get())-1, tk.END)
        else:
            self.display.insert(tk.END, button)

# Create the main window and start the event loop
root = tk.Tk()
root.title("Calculator")
root.geometry("250x300")
calculator = Calculator(root)
root.mainloop()