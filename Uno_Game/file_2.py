import difflib
import tkinter

from tkinter import messagebox

def parseInput (event = None):
# Copy of flag library to be ussed in flagFilter
	flag_copy = flag_libr.copy()
	user_input = input_tab.get()
	
	if user_input:
		#Data Type validation for user input
		dtype_is_valid = True
		flag_dtype = flag_libr.get('data', None)	
		if flag_dtype is not None: 
			flag_copy.pop('data')
			if not isinstance(user_input, tuple(flag_dtype)): dtype_is_valid = False
		if dtype_is_valid: 
			close_match, name_flag = flagFilter(user_input, flag_copy)
			if name_flag == 'invalid': messagebox.showwarning('PROFANITY',f'Please ensure input does not contain {close_match[0].upper()}')
			# Prompt for close match only valid if user input not exactly equal to match
			elif close_match and close_match[0] != user_input: 
				answer = messagebox.askyesno('VALIDATION', f'Were you trying to type {close_match[0]}')
				if answer == 'yes': user_input = close_match[0]
			elif close_match: player_names[user_input] = []
		else: messagebox.showerror('INVALID DATA TYPE', f'Please ensure input if of data type {flag_dtype}')
	else: messagebox.showerror('VOID ENTRY ERROR', 'Void input invalid')
	
	input_tab.delete(0, 'end')
		
		
def flagFilter (user_input, flag_copy):
	# Copy of flag library to be used in flagFilter
	return_match = ''; return_name = ''
	instance = False
	for flag_name, flag_elements in flag_copy.items():
		flag_match = difflib.get_close_matches(user_input, flag_elements, cutoff = 0.4, n = 1)
		if flag_match and flag_name == 'invalid': 
			return flag_match, flag_name
		elif flag_match and not instance:
			instance = True
			return_match = flag_match
			return_name = flag_name
	
	return return_match, return_name
	
def cancel (event = None):
	widget_root.destroy()

def centerWidget (widget_root, root_width, root_height):
  screen_width = widget_root.winfo_screenwidth()
  screen_height = widget_root.winfo_screenheight()
  print(f'SCREEN WIDTH {screen_width} and HEIGHT {screen_height}')
  x = (screen_width // 2) - (widget_width // 2)
  y = (screen_height // 2) - (widget_height // 2)
  widget_root.geometry(f"{root_width}x{root_height} + {x} + {y}")


flag_libr = {

#"valid": ['david','susan','mathew'],
'invalid': ['fuck','shit','crap','bitch'],
'data':[str],
'break_flag': ['cancel'],
'exit_flag': ['exit'],

}

player_names = {}

# Widget root

#Parameters
widget_colour = 'grey'
widget_width = 350
widget_height = 250
global_font = ('Arial', 14)

widget_root = tkinter.Tk()
widget_root.title('USER INPUT')
widget_root.config(bg = widget_colour)
#centerWidget(widget_root, widget_width, widget_height)
widget_root.geometry(f'{widget_width}x{widget_height}')

def change_xy (x_change = 0, y_change = 0): 
	x_0 += x_change
	y_0 += y_change
	cord_libr = {'relx': x_0, 'rely': y_0, 'anchor': 'center'}
	return cord_libr

entry_label = tkinter.Label(widget_root, text = 'Enter Name below', font = global_font, bg = 'black', fg = 'white')
x_0 = 0.5; y_0 = 0.3
entry_label.place(relx = x_0, rely = y_0, anchor = 'center')

input_tab = tkinter.Entry(widget_root, width = widget_width//10)
y_0 += 0.2
input_tab.place(relx = x_0, rely = y_0, anchor = 'center')

submit_button = tkinter.Button(widget_root, command = parseInput, text = 'Submit', font = global_font,bg = 'darkred', fg = 'white')
x_0 += -0.2; y_0 += 0.2
submit_button.place(relx = x_0, rely = y_0, anchor = 'center')

cancel_button = tkinter.Button(widget_root, command = cancel, text = 'Cancel', font = global_font, bg = 'darkred', fg = 'white')
x_0 += 0.4
cancel_button.place(relx = x_0, rely = y_0, anchor = 'center')

widget_root.bind('<Return>', parseInput)
widget_root.bind('<Escape>', cancel)

widget_root.mainloop()
	

print(f'Players are {player_names}')
	
	













