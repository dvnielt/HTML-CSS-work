"""A programming language survey written in Python with Tkinter"""

import tkinter as tk

# Create the root window
root = tk.Tk()

# set the title
root.title('CS Problem Solving and Solution Survey')

# set the root window size
root.geometry('640x480+300+300')
root.resizable(False, False)


# Widgets

# Use a Label to show the title
# 'font' sets a font
title = tk.Label(
  root,
  text='Please take survey',
  font=('Arial 16 bold'),
  bg='black',
  fg='white'
)


# Use string vars for strings
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var, justify='left')

# Use boolean var for True/False
like_var = tk.BooleanVar()
language_inp = tk.Checkbutton(
  root, variable=like_var, text='Check this box if you like Python',anchor='w',
  justify='left'
)

# Use int var for whole numbers
# Value can set a default
num_var = tk.IntVar(value=3)
num_label = tk.Label(text='How many hours do you work on Python homework a week?')
# note that even with an intvar, the key is still 'textvariable'
num_inp = tk.Spinbox(
  root,
  textvariable=num_var,
  from_=0,
  to=1000,
  increment=1
)


# Use OptionMenu with variables instead of Listbox
language_var = tk.StringVar(value='Any')
language_label = tk.Label(
  root,
  text='What is the best programming language?'
)
language_choices = (
  'Any', 'C', 'C++', 'Java', 'Javascript', 'Python'
)
language__inp = tk.OptionMenu(
  root, language_var, *language_choices
)

python_label = tk.Label(root, text='Do you expect an A in COP2080?')
# Use a Frame to keep widgets together
alpha_frame = tk.Frame(root)

# use any kind of var with Radiobuttons,
# as long as each button's 'value' property is the
# correct type
python_var = tk.BooleanVar()
# The radio buttons are connected by using the same variable
# The value of the var will be set to the button's 'value' property value
alpha_yes_inp = tk.Radiobutton(
  alpha_frame,
  text='Yes',
  value=True,
  variable=python_var
)
python_no_inp = tk.Radiobutton(
  alpha_frame,
  text='If not, try forming study groups',
  value=False,
  variable=python_var
)
# -----------------------------------------------------------------
options = ("Adv Topics", "Software Engineering", "Cyber Security",
           "Game Development", "AI", "Big Data", "Autonomous Systems")
options_var = tk.StringVar(value = "any")
options_label = tk.Label(
  root,
  text="What is your concentration?"
)
options_var.set('Select an Option')

options__inp = tk.OptionMenu(root, options_var,*options)
# -----------------------------------------------------------------


# The Text widget doesn't support variables
python_haiku_label = tk.Label(root, text='Write a haiku about Python')
python_haiku_inp = tk.Text(root, height=3)

# Buttons are used to trigger actions

submit_btn = tk.Button(root, text='Submit Survey')

# Labels can use a StringVar for their contents
output_var = tk.StringVar(value='')
output_line = tk.Label(
  root,
  textvariable=output_var,
  anchor='w',
  justify='left'
)



# Geometry Management #

# Using Grid instead of pack
# Put our widgets on the root window
#title.grid()
# columnspan allows the widget to span multiple columns
title.grid(columnspan=2)

# add name label and input
# Column defaults to 0
name_label.grid(row=1, column=1)
name_label.place(x=5, y=25,  ) # cn Change the placement

# The grid automatically expands
# when we add a widget to the next row or column
name_inp.grid(row=1, column=1)


# 'sticky' attaches the widget to the named sides,
# so it will expand with the grid
language_inp.grid(row=2, columnspan=2, sticky='we')
# tk constants can be used instead of strings
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))

#padx and pady can still be used to add horizontal or vertical padding
language_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
language__inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

#  use pack on the alpha frame.
# pack and grid can be mixed in a layout as long as we don't
# use them in the same frame
alpha_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
python_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
python_label.grid(row=6, columnspan=2, sticky=tk.W)
alpha_frame.grid(row=7, columnspan=2, stick=tk.W)

options_label.grid(row=8, sticky=tk.W)
options__inp.grid(row=8, columnspan=1, sticky=tk.E, padx=6)


# Sticky on all sides will allow the widget to fill vertical and horizontal
python_haiku_label.grid(row=9, sticky=tk.W)
python_haiku_inp.grid(row=10, columnspan=2, sticky='NSEW')

# Add the button and output
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

# columnconfigure can be used to set options on the columns of the grid
# 'weight' means that column will be preferred for expansion
root.columnconfigure(1, weight=1)

# rowconfigure works for rows
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)


# Add some behavior


def on_submit():
  """To be run when the user submits the form"""

  # Vars all use 'get()' to retreive their variables
  name = name_var.get()
  # Because of IntVar, .get() will try to convert
  # the contents of num_var to int.
  try:
    number = num_var.get()
  except tk.TclError:
    number = 10000

  # OptionMenu makes things simple
  language_ = language_var.get()

  # Checkbutton and Radiobutton values
  python_liker = like_var.get()
  python_user = python_var.get()


  # Text widgets require a range
  haiku = python_haiku_inp.get('1.0', tk.END)

  # Update the text in our output
  message = f'Thanks for taking the survey, {name}.\n'

  # -----------------------------------------------------------------

  options_ = options_var.get()
  message += f'{options_} is a great concentration \n'

  # -----------------------------------------------------------------


  if not python_liker:
    message += "You should give Python another chance!\n"

  else:
    message += f'Enjoy studying {number} hours on Python vs {language_} \n'

  if python_user:
    message += 'Enjoy programming Python!'
  else:
    message += 'May you successfully avoid programming in Python'

  if haiku.strip():
    message += f'\n\nYour Haiku:\n{haiku}'

  # Set the value of a variable using .set()
  # instead of  output_var = 'my string'
  output_var.set(message)

# configure the button to trigger submission
submit_btn.configure(command=on_submit)

# Execute App
root.mainloop()