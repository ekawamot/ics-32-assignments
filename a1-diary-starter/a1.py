# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Emiko Kawamoto
# ekawamot@uci.edu
# EKAWAMOT


import command_parser

def main():
    current_notebook = None
    while True:
        command = input('Please input a command.\n')
        command_to_use = command_parser.detect_command(command)

        if command_to_use == 'C':
            current_notebook = command_parser.c_command(command)
        elif command_to_use == 'D':
            command_parser.d_command(command)
        elif command_to_use == 'O':
            current_notebook = command_parser.o_command(command)
        elif command_to_use == 'E':
            command_parser.e_command(command)
        elif command_to_use == 'P':
            command_parser.p_command(command)
        elif command_to_use == 'Q':
            break

if __name__=="__main__":
    main()

