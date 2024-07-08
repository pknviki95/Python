"""
Escape characters:

- **An escape character is a character followed by a backslash (\).** 
- **It tells the Interpreter that this escape character (sequence) has a special meaning.**
"""

# \'	- Single quote		
# \”	- Double quote		
# \	- backslash		
# \n	- New line		
# \r	- Carriage Return		
# \t	- Horizontal tab		
# \b	- Backspace		
# \f	- form feed		
# \v	- vertical tab		
# \0	- Null character		
# \N{name}	- Unicode Character Database named Lookup		
# \uxxxxxxxx	- Unicode Character with 16-bit hex value XXXX		
# \Uxxxxxxxx	- Unicode Character with 32-bit hex value XXXXXXXX		
# \ooo	- Character with octal value OOO		
# \xhh	- Character with hex value HH


# \’	- Single quote:

# It helps to use single quotes inside string
print('Hello! \'Good Morning!!!\'')


# \"	- Double quote:

# It helps to use Double quotes inside string
print('Hello! \"Good Morning!!!\"')

# \	- backslash

# It helps to use backslash inside string - Mostly on path usage
print('C:\\Program Files\\norton\\appx')

# \n	- New line
		
# It helps to print the change in new line
print('Hello!\nWelcome to India')

# \r	- Carriage Return

# It helps to print the change in beginning of same line
print('Hello!\rWelcome to India')	

# \t	- Horizontal tab	

# It helps to move the change to horizontal tab (2 spaces) of same line
print('Hello!\tWelcome to India')

# \b	- Backspace		

# It helps to remove the change; perform backspace operation
print('Hello!\bWelcome to India')

# \v	- vertical tab	

# It helps to move the change to vertical tab.
print('Hello!\vWelcome to India')