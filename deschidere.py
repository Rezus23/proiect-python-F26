import tkinter as tk
from forex_python.converter import CurrencyRates
from proiect import ConverterApp



def execute_converter():
    root = tk.Tk()
    app = ConverterApp(root)
    main_window.destroy()
    root.mainloop()
    
class Table:
    def __init__(self, root, back_command):
        self.root = root
        self.back_command = back_command
        self.create_table()

    def create_table(self):
        header_values = ["Factor", "Name", "Symbol", "Factor", "Name", "Symbol"]
        data_values = [
            ("10^1", "deca", "da", "10^(-1)", "deci", "d"),
            ("10^2", "hecto", "h", "10^(-2)", "centi", "c"),
            ("10^3", "kilo", "k", "10^(-3)", "milli", "m"),
            ("10^6", "mega", "M", "10^(-6)", "micro", "μ"),
            ("10^9", "giga", "G", "10^(-9)", "nano", "n"),
            ("10^12", "tera", "T", "10^(-12)", "pico", "p"),
            ("10^15", "peta", "P", "10^(-15)", "femto", "f"),
            ("10^18", "exa", "E", "10^(-18)", "atto", "a"),
            ("10^21", "zetta", "Z", "10^(-21)", "zepto", "z"),
            ("10^24", "yotta", "Y", "10^(-24)", "yocto", "y")
        ]
        total_rows = len(data_values)
        total_columns = len(data_values[0])

       
        background_color = '#f9ecde'  

        # Display header
        for j, header in enumerate(header_values):
            label = tk.Label(self.root, text=header, font=('Arial', 16, 'bold'), background=background_color, padx=10, pady=5, relief=tk.GROOVE)
            label.grid(row=0, column=j)

        # Display data with table lines
        for i, data_row in enumerate(data_values):
            for j, value in enumerate(data_row):
                label = tk.Label(self.root, text=value, font=('Arial', 12), background=background_color, padx=10, pady=5,)
                label.grid(row=i + 1, column=j)

        # Add a back button
        back_button = tk.Button(self.root, text="Back", command=self.back_command)
        back_button.grid(row=total_rows + 1, column=0, columnspan=total_columns, pady=10)

def multiples_and_submultiples():
    def back_to_main():
        root.destroy()  
        main_window.deiconify() 

    root = tk.Toplevel()
   
    root.title("Multiples and Submultiples Table")
    
    
    t = Table(root, back_command=back_to_main)
    root.mainloop()
    
   


main_window = tk.Tk()
main_window.geometry("400x400")
main_window.title("Converter Opener")
main_bg_image_path = "C:\\Users\\Catalin\\Desktop\\science-objects-icons-seamless-pattern_1308-134774.png"  
main_bg_image = tk.PhotoImage(file=main_bg_image_path)

main_bg_label = tk.Label(main_window, image=main_bg_image)

main_bg_label.place(relwidth=1, relheight=1)

label1 = tk.Label(main_window, text="Welcome!", font=('Times New Roman',25),bg='#D3D3D3')
label1.pack(pady=15)

button1 = tk.Button(main_window, text="Open converter app", command=execute_converter,bg='#95daf8',activebackground='blue',activeforeground='black')
button1.pack(pady=100)

button2 = tk.Button(main_window, text="Open table of units", command=multiples_and_submultiples)
button2.pack()


main_window.mainloop()

