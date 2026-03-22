import tkinter as tk
from tkinter import messagebox;

def addition():
        try:
            result = int(input1.get()) + int(input2.get())
            Result_output.config(bg="Black", fg="Green", text=result, font=("calibri",30,"bold"))
            verlauf(result)
        except Exception as error:
            Result_output.config(bg="Black" ,fg="Red",text="Error: Only Numbers Allowed")

def subtraction():
    try:
        result = int(input1.get()) - int(input2.get())
        Result_output.config(bg="Black", fg="Green", text=result, font=("calibri",30,"bold"))
        verlauf(result)
    except Exception as error:
         Result_output.config(bg="Black" ,fg="Red",text="Error: Only Numbers Allowed")

def multiplication():
    try:
        result = int(input1.get()) * int(input2.get())
        Result_output.config(bg="Black", fg="Green", text=result, font=("calibri", 30,"bold"))
        verlauf(result)
    except Exception as error:
         Result_output.config(bg="Black" ,fg="Red",text="Error: Only Numbers Allowed")

def division():
    try:
        result = int(input1.get()) / int(input2.get())
        Result_output.config(bg="Black", fg="Green", text=result, font=("calibri",30,"bold"))
        verlauf(result)
    except Exception as error:
         Result_output.config(bg="Black" ,fg="Red",text="Error: Only Numbers Allowed")

def potenzieren():
    try:
        if  int(input2.get()) > 50:
            raise ValueError
        
        p=int(input2.get())
        product = 1
        for i in range(p):
            product = product * int(input1.get())
        Result_output.config(bg="Black", fg="Green", text=product,font=("calibri",30,"bold"))
        result = product #variable für den verlauf
        verlauf(result)
    except Exception as error:
            Result_output.config(bg="Black" ,fg="Red",text="Error: Only Numbers lower than 50 Allowed")

def modulo():
    try:
          result = int(input1.get()) % int(input2.get())
          Result_output.config(text=result, bg="Black", fg="Green", font=("calibri",30,"bold"))
          verlauf(result)
    except Exception as error:
          Result_output.config(bg="Black" ,fg="Red",text="Error: Only Numbers Allowed")

def ggT():
    try:
        a = int(input1.get())
        b = int(input2.get())

        while True:
            r = a % b
            if r == 0:
                  Result_output.config(bg="Black", fg="Green", text=b,font=("calibri",30,"bold"))
                  loop = False
                  result = b # variable für den Verlauf
                  verlauf(result)
                  break
            a = b
            b = r

    except Exception as error:
         Result_output.config(bg="Black" ,fg="Red",text="Error: Only Numbers Allowed")

def insert_prev_result():
    letzte_zahl = Result_output.cget("text")
    input1.delete(0, tk.END)
    input1.insert(0, letzte_zahl)

def lightmode():
    window.config(bg="White")
    haupt_Frame.config(bg="White")
    button_Frame.config(bg="White")
    eingabe_Frame.config(bg="White")
    ausgabe_Frame.config(bg="White")
    input1.config(bg="#D3D3D3", fg="Black")
    input2.config(bg="#D3D3D3", fg="Black")
    Result_output.config(bg="#D3D3D3", fg="Green")

    lightmode_Knopf.grid_remove()
    darkmode_Knopf.grid(column=4,row=4)

def darkmode():
    window.config(bg="#2b2b2b")
    haupt_Frame.config(bg="#2b2b2b")
    button_Frame.config(bg="#2b2b2b")
    eingabe_Frame.config(bg="#2b2b2b")
    ausgabe_Frame.config(bg="#2b2b2b")
    input1.config(bg="#D3D3D3", fg="Black")
    input2.config(bg="#D3D3D3", fg="Black")
    Result_output.config(bg="#2b2b2b", fg="White")
    
    darkmode_Knopf.grid_remove()
    lightmode_Knopf.grid(column=4, row=4)

def version():
    messagebox.showinfo(f"Version Info", f"Version: 1.0.0 \n Author: Ganztagszocker")

def verlauf(result):
    try:
        alter_verlauf = prev_result.cget("text")
        neuer_verlauf = f"{alter_verlauf} \n {result}"
        prev_result.config(text=neuer_verlauf)
        return result
    except Exception as error:
        print(f"Error")



window = tk.Tk()
window.title("Calculator")
window.geometry("1000x700")
window.config(bg="#2b2b2b")

haupt_Frame = tk.Frame(window, bg="#2b2b2b")
haupt_Frame.place(relx=0.5, rely=0.2, anchor="center")
right_Frame = tk.Frame(window, bg="#2b2b2b")

button_Frame = tk.Frame(haupt_Frame, bg="#2b2b2b")
eingabe_Frame = tk.Frame(haupt_Frame, bg="#2b2b2b")
ausgabe_Frame = tk.Frame(haupt_Frame, bg="#2b2b2b")
settings_Frame = tk.Frame(window)
settings_Frame.place(relx=0.02, rely=0.98, anchor="sw")
right_Frame = tk.Frame(window)
right_Frame.place(relx=0.9, rely=0.3, anchor="e")

button_Frame.grid(column=0, row=0)
eingabe_Frame.grid(column=0,row=1)
ausgabe_Frame.grid(column=0,row=2)

addition_Knopf = tk.Button(button_Frame, text="Addition (+)", command=addition)
subtraction_Knopf = tk.Button(button_Frame, text="Subtraction (-)", command=subtraction)
multiplication_Knopf = tk.Button(button_Frame, text="Multioplication (*)", command=multiplication)
division_Knopf = tk.Button(button_Frame, text="Division (/)", command=division)
potenzieren_Knopf = tk.Button(button_Frame, text="Potenzieren", command=potenzieren)
modulo_Knopf = tk.Button(button_Frame, text="Modulo", command=modulo)
ggt_Knopf = tk.Button(button_Frame, text="ggT", command=ggT)
insert_prev_result_Knopf = tk.Button(button_Frame, text="insert result", command=insert_prev_result)

lightmode_Knopf = tk.Button(settings_Frame, text="Light Mode",command=lightmode )
darkmode_Knopf = tk.Button(settings_Frame, text="Dark Mode",command=darkmode )
version_button = tk.Button(settings_Frame,text="Version", command=version)

addition_Knopf.grid(column=0, row=0)
subtraction_Knopf.grid(column=1, row=0)
multiplication_Knopf.grid(column=2, row=0)
division_Knopf.grid(column=3, row=0)
potenzieren_Knopf.grid(column=0, row=1)
modulo_Knopf.grid(column=1, row=1)
ggt_Knopf.grid(column=0,row=2)
insert_prev_result_Knopf.grid(column=3,row=2)

lightmode_Knopf.grid(column=4,row=4)
darkmode_Knopf.grid(column=4,row=4)
darkmode_Knopf.grid_remove()
version_button.grid(column=5,row=4)

Result_output = tk.Label(ausgabe_Frame)
input1 = tk.Entry(eingabe_Frame)
input2 = tk.Entry(eingabe_Frame)
prev_result = tk.Label(right_Frame,bg="#2b2b2b", fg="White")

input1.grid(row=1, column=0, padx=20, pady=10)
input2.grid(row=2, column=0,  padx=20, pady=10)
Result_output.grid(row=3, column=0, padx=20, pady=10)
prev_result.grid(row=0,column=0)

window.mainloop()
