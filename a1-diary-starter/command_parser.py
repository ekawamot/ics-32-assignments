# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Emiko Kawamoto
# ekawamot@uci.edu
# EKAWAMOT


# C "/home/john/ics 32/my notebooks" -n my_diary

import notebook
from pathlib import Path

def detect_command(user_input):
    if user_input[0].upper() in ['C', 'D', 'O', 'E', 'P', 'Q']:
        return user_input[0].upper()
    else:
        print('Sorry, that command was not recognized.')

def c_command(user_input):
    command_parts = user_input.split()
    notebook_directory = Path(command_parts[1]+'.json')
    username = str(input(''))
    password = str(input(''))
    bio = str(input(''))
    users_notebook = notebook.Notebook(username, password, bio)
    users_notebook.save(command_parts[1]+'.json')
    print(command_parts[1] + '.json' + 'CREATED')
    return users_notebook

def d_command(user_input):
    note_path = user_input.split()
    to_delete = Path(note_path[1])
    try:
        to_delete.unlink()
    except FileNotFoundError:
        print('ERROR')
    else:
        print(to_delete, "DELETED")

def o_command(user_input):
    note_path = user_input.split()
    note_to_load = Path(note_path[1])
    if note_to_load.exists():
        user_notebook = notebook.Notebook()
        user_notebook.load(note_path[1])
        username = input('')
        password = input('')
        if username == user_notebook.username and password == user_notebook.password:
            return user_notebook
        else:
            print('ERROR')
    else:
        print('')


def e_command(user_input, user_notebook):
    if user_notebook is None:
        print('ERROR')
    else:
        edit_commands = user_input.split()
        for (index, value) in enumerate(edit_commands[1::2]):
            if value == '-usr':
                user_notebook.username = edit_commands[index + 1]
            elif value == '-pwd':
                user_notebook.username = edit_commands[index + 1]
            elif value == '-bio':
                user_notebook.bio = edit_commands[index + 1]
            elif value == '-add':
                new_diary = notebook.Diary(edit_commands[index + 1])
                user_notebook.add_diary(new_diary)
            elif value == '-del':
                try: 
                    to_delete = int(edit_commands[index + 1])
                except ValueError:
                    print('ERROR')
                    break
                else:
                    user_notebook.del_diary(to_delete)
    
            

def print_diaries(user_notebook):
    diaries = user_notebook.get_diaries()
    for index, value in enumerate(diaries):
        print(f'{index}: {value}')


def p_command(user_input, user_notebook):
    if user_notebook is None:
        print('ERROR')
    else:
        edit_commands = user_input.split()
        for (index, value) in enumerate(edit_commands[1]):
            if value == '-usr':
                print(user_notebook.username)
            elif value == '-pwd':
                print(user_notebook.password)
            elif value == '-bio':
                print(user_notebook.bio)
            elif value == '-diaries':
                print_diaries(user_notebook)
            elif value == '-diary':
                diaries = user_notebook.get_diaries()
                try:
                    print(diaries[int(index)])
                except ValueError:
                    print('ERROR')
                    break

        





