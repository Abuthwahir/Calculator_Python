#======================#
#  Tkinter Calculator  #
#----------------------#
#  Abuthwahir's Calculator #
#======================#

# Import packages
from tkinter import *
import math

# Functions
# Function to add characters to the display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete the last character from the display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

# Function to calculate sine of an angle
def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1 / math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

# Function to find the square root of a number
def square_root():
    global calc_operator
    if int(calc_operator) >= 0:
        temp = str(eval(calc_operator + '**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Function to find the third root of a number
def third_root():
    global calc_operator
    if int(calc_operator) >= 0:
        temp = str(eval(calc_operator + '**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Function to change the sign of a number
def sign_change():
    global calc_operator
    if calc_operator[0] == '-':
        temp = calc_operator[1:]
    else:
        temp = '-' + calc_operator
    calc_operator = temp
    text_input.set(temp)

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    temp = str(eval(calc_operator + '/100'))
    calc_operator = temp
    text_input.set(temp)

# Function to evaluate an expression
def button_equal():
    global calc_operator
    try:
        temp_op = str(eval(calc_operator))
        text_input.set(temp_op)
        calc_operator = temp_op
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Variables
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'

tk_calc = Tk()
tk_calc.configure(bg="#2D3A4E", bd=10)  # Background color
tk_calc.title("Abuthwahir's Calculator")  # Title

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth=5, bg='#DDD', justify='right').grid(columnspan=5, padx=10, pady=15)  # Entry background color

button_params = {'bd': 5, 'fg': '#FFF', 'bg': '#444444', 'font': ('sans-serif', 20, 'bold')}  # Button colors
button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#DDD', 'font': ('sans-serif', 20, 'bold')}  # Button colors

# Buttons
#--1st row--
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda: button_click('abs(')).grid(row=1, column=0, sticky="nsew")
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda: button_click('%')).grid(row=1, column=1, sticky="nsew")
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda: button_click('//')).grid(row=1, column=2, sticky="nsew")
factorial_button = Button(tk_calc, button_params, text='x!',
                           command=fact_func).grid(row=1, column=3, sticky="nsew")
eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda: button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")

#--2nd row--
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=2, column=0, sticky="nsew")
cosine = Button(tk_calc, button_params, text='cos',
                command=trig_cos).grid(row=2, column=1, sticky="nsew")
tangent = Button(tk_calc, button_params, text='tan',
                 command=trig_tan).grid(row=2, column=2, sticky="nsew")
cotangent = Button(tk_calc, button_params, text='cot',
                   command=trig_cot).grid(row=2, column=3, sticky="nsew")
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda: button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

#--3rd row--
second_power = Button(tk_calc, button_params, text='x²',
                      command=lambda: button_click('**2')).grid(row=3, column=0, sticky="nsew")
third_power = Button(tk_calc, button_params, text='x³',
                     command=lambda: button_click('**3')).grid(row=3, column=1, sticky="nsew")
nth_power = Button(tk_calc, button_params, text='x^n',
                   command=lambda: button_click('**')).grid(row=3, column=2, sticky="nsew")
inv_power = Button(tk_calc, button_params, text='x⁻¹',
                   command=lambda: button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
tens_powers = Button(tk_calc, button_params, text='10^x', font=('sans-serif', 15, 'bold'),
                     command=lambda: button_click('10**')).grid(row=3, column=4, sticky="nsew")

#--4th row--
square_root = Button(tk_calc, button_params, text='√',
                     command=square_root).grid(row=4, column=0, sticky="nsew")
third_root = Button(tk_calc, button_params, text='∛',
                    command=third_root).grid(row=4, column=1, sticky="nsew")
nth_root = Button(tk_calc, button_params, text='√',
                  command=lambda: button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
log_base10 = Button(tk_calc, button_params, text='log₁₀', font=('sans-serif', 16, 'bold'),
                    command=lambda: button_click('log(')).grid(row=4, column=3, sticky="nsew")
log_basee = Button(tk_calc, button_params, text='ln',
                   command=lambda: button_click('ln(')).grid(row=4, column=4, sticky="nsew")

#--5th row--
left_par = Button(tk_calc, button_params, text='(',
                  command=lambda: button_click('(')).grid(row=5, column=0, sticky="nsew")
right_par = Button(tk_calc, button_params, text=')',
                   command=lambda: button_click(')')).grid(row=5, column=1, sticky="nsew")
signs = Button(tk_calc, button_params, text='±',
               command=sign_change).grid(row=5, column=2, sticky="nsew")
percentage = Button(tk_calc, button_params, text='%',
                    command=percent).grid(row=5, column=3, sticky="nsew")
ex = Button(tk_calc, button_params, text='e^x',
            command=lambda: button_click('e(')).grid(row=5, column=4, sticky="nsew")

#--6th row (number buttons)--
button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda: button_click(7)).grid(row=6, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda: button_click(8)).grid(row=6, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda: button_click(9)).grid(row=6, column=2, sticky="nsew")
button_div = Button(tk_calc, button_params, text='/',
                    command=lambda: button_click('/')).grid(row=6, column=3, sticky="nsew")

#--7th row--
button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda: button_click(4)).grid(row=7, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda: button_click(5)).grid(row=7, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda: button_click(6)).grid(row=7, column=2, sticky="nsew")
button_mul = Button(tk_calc, button_params, text='*',
                    command=lambda: button_click('*')).grid(row=7, column=3, sticky="nsew")

#--8th row--
button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda: button_click(1)).grid(row=8, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda: button_click(2)).grid(row=8, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda: button_click(3)).grid(row=8, column=2, sticky="nsew")
button_sub = Button(tk_calc, button_params, text='-',
                    command=lambda: button_click('-')).grid(row=8, column=3, sticky="nsew")

#--9th row--
button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda: button_click(0)).grid(row=9, column=0, sticky="nsew")
button_dot = Button(tk_calc, button_params, text='.',
                    command=lambda: button_click('.')).grid(row=9, column=1, sticky="nsew")
button_clear = Button(tk_calc, button_params, text='C',
                      command=button_clear_all, bg='red').grid(row=9, column=2, sticky="nsew")  # Change color to red
button_del = Button(tk_calc, button_params, text='DEL',
                    command=button_delete, bg='red').grid(row=9, column=3, sticky="nsew")  # Change color to red
button_add = Button(tk_calc, button_params, text='+',
                    command=lambda: button_click('+')).grid(row=9, column=4, sticky="nsew")

#--10th row--
button_eq = Button(tk_calc, button_params, text='=',
                   command=button_equal).grid(row=10, column=0, columnspan=5, sticky="nsew")

# Configure rows and columns to expand
for i in range(11):
    tk_calc.grid_rowconfigure(i, weight=1)
for j in range(5):
    tk_calc.grid_columnconfigure(j, weight=1)

tk_calc.mainloop()
