from tkinter import *

# This is to create a basic window
win = Tk()
# this is for the size of the window
win.geometry("460x410")
# this is to allow resizing the window
win.resizable(0, 0)
win.title("Calculator")


def btn_click(item):
    '''btn_click' function :
            This Function continuously updates the
            input field whenever you enter a number
    '''
    global expression  # global expression variable hold the user input
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    '''bt_clear' function :This is used to clear
        the input field
    '''
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    '''bt_equal':This method calculates the expression
        present in input field'''
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except Exception as e:
        input_text.set("Error")


def on_key_press(event):
    '''this function maps the key presses corresponding
        button actions'''
    #print(f"Key pressed: {event.char}")
    key_mapping = {
        '0': lambda: btn_click(0),
        '1': lambda: btn_click(1),
        '2': lambda: btn_click(2),
        '3': lambda: btn_click(3),
        '4': lambda: btn_click(4),
        '5': lambda: btn_click(5),
        '6': lambda: btn_click(6),
        '7': lambda: btn_click(7),
        '8': lambda: btn_click(8),
        '9': lambda: btn_click(9),
        '+': lambda: btn_click('+'),
        '-': lambda: btn_click('-'),
        '*': lambda: btn_click('*'),
        '/': lambda: btn_click('/'),
        '.': lambda: btn_click('.'),
        '': lambda: bt_equal()
    }
    # extract the data in the dict
    key = event.char
    if key in key_mapping:
        key_mapping[key]()


expression = ""
# 'StringVar()' :It is used to get the instance of the input field
input_text = StringVar()
# creating a frame for the input field
input_frame = Frame(win, width=400,
                    height=50,
                    bd=0,
                    highlightbackground="black",
                    highlightcolor="black",
                    highlightthickness=2
                    )

input_frame.pack(side=TOP)

# create an input field inside the 'Frame'

input_field = Entry(input_frame,
                    font=('arial', 18, 'bold'),
                    textvariable=input_text,
                    width=50, bg="#eee", bd=0,
                    justify=RIGHT
                    )
input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # internal padding to increase the height of the input field

# creating another 'Frame' for the button below the 'input_frame'

btns_frame = Frame(win, width=400, height=600, bg="black",bd=3)
btns_frame.pack()

# first row
clear_screen = Button(btns_frame,
               text="C",
               fg="white",
               width=37,
               height=2,
               bd=3,
               bg="#6BCAE2",
               cursor="hand2",
               command=lambda: bt_clear()
               )
clear_screen.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
division = Button(btns_frame,
                text="/",
                fg="white",
                width=10,
                height=3,
                bd=2,
                bg="#0A0806",
                cursor="hand2",
                command=lambda: btn_click("/")
                )
division.grid(row=0, column=3, padx=1, pady=1)
# second row
seven = Button(btns_frame,
               text="7",
               fg="white",
               width=10,
               height=3,
               bd=2,
               bg="#0A0806",
               cursor="hand2",
               command=lambda: btn_click(7)
               )
seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame,
               text="8",
               fg="white",
               width=10,
               height=3,
               bd=2,
               bg="#0A0806",
               cursor="hand2",
               command=lambda: btn_click(8)
               )
eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame,
              text="9",
              fg="white",
              width=10,
              height=3,
              bd=2,
              bg="#0A0806",
              cursor="hand2",
              command=lambda: btn_click(9)
              )
nine.grid(row=1, column=2, padx=1, pady=1)

multiplication = Button(btns_frame,
                  text="*",
                  fg="white",
                  width=10,
                  height=3,
                  bd=2,
                  bg="#0A0806",
                  cursor="hand2",
                  command=lambda: btn_click("*")
                  )
multiplication.grid(row=1, column=3, padx=1, pady=1)

# third row
four = Button(btns_frame,
              text="4",
              fg="white",
              width=10,
              height=3,
              bd=2,
              bg="#0A0806",
              cursor="hand2",
              command=lambda: btn_click(4)
              )
four.grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame,
              text="5",
              fg="white",
              width=10,
              height=3,
              bd=2,
              bg="#0A0806",
              cursor="hand2",
              command=lambda: btn_click(5)
              )
five.grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame,
             text="6",
             fg="white",
             width=10,
             height=3,
             bd=2,
             bg="#0A0806",
             cursor="hand2",
             command=lambda: btn_click(6)
             )
six.grid(row=2, column=2, padx=1, pady=1)

substraction = Button(btns_frame,
               text="-",
               fg="white",
               width=10,
               height=3,
               bd=2,
               bg="#0A0806",
               cursor="hand2",
               command=lambda: btn_click("-")
               )
substraction.grid(row=2, column=3, padx=1, pady=1)

# fourth row
one = Button(btns_frame,
             text="1",
             fg="white",
             width=10,
             height=3,
             bd=2,
             bg="#0A0806",
             cursor="hand2",
             command=lambda: btn_click(1)
             )
one.grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame,
             text="2",
             fg="white",
             width=10,
             height=3,
             bd=2,
             bg="#0A0806",
             cursor="hand2",
             command=lambda: btn_click(2)
             )
two.grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame,
               text="3",
               fg="white",
               width=10,
               height=3,
               bd=2,
               bg="#0A0806",
               cursor="hand2",
               command=lambda: btn_click(3)
               )
three.grid(row=3, column=2, padx=1, pady=1)

Addition = Button(btns_frame,
              text="+",
              fg="white",
              width=10,
              height=3,
              bd=2,
              bg="#0A0806",
              cursor="hand2",
              command=lambda: btn_click("+")
              )
Addition.grid(row=3, column=3, padx=1, pady=1)

# fourth row
zero = Button(btns_frame,
              text="0",
              fg="white",
              width=24,
              height=3,
              bd=2,
              bg="#0A0806",
              cursor="hand2",
              command=lambda: btn_click(0)
              )
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame,
               text=".",
               fg="white",
               width=10,
               height=3,
               bd=2,
               bg="#0A0806",
               cursor="hand2",
               command=lambda: btn_click(".")
               )
point.grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame,
                text="=",
                fg="white",
                width=10,
                height=3,
                bd=3,
                bg="#0A0806",
                cursor="hand2",
                command=lambda: bt_equal()
                )
equals.grid(row=4, column=3, padx=1, pady=1)

win.bind('<Key>', on_key_press)
win.bind('<Return>', on_key_press)
win.mainloop()
