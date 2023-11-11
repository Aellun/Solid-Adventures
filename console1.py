#!/usr/bin/python3
import cmd
import os
import platform


class ConsoleHello(cmd.Cmd):
    prompt = f'{os.getcwd()} >>'
    intro = "simple comamand line"

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undo_header'

    ruler = '_'

    def do_prompt(self, line):
        '''change the interactive promt'''
        self.prompt = line + ":"

    def do_quit(self, arg):
        '''Exits the program or stop the running process'''
        return True
    #aliasing the quit command line command
    do_exit = do_quit
    do_eof = do_quit

    def do_list(self, arg):
        '''list the content of the current directory'''
        files = os.listdir(".")
        for file in files:
            print(file)
    #aliasing the list directory command
    do_ls = do_list
    do_dir = do_list

    def do_clear(self, arg):
        '''clear the console screen'''
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    # aliasing the clear; clears the console screen despite the platform
    do_clear = do_clear
    do_cls = do_clear

    def do_cd(self, arg):
        '''change the curent directory'''
        try:
            os.chdir(arg)
            print(f'current directory: {os.getcwd()}')
        except FileNotFoundError:
            print(f'Directory not found:{arg}')
        except Exception as e:
            print(f'Error: {e}')

    def do_pwd(self, arg):
        '''prints the current working directory'''
        print(f'curent directory: {os.getcwd()}')

    def do_mkdir(self, arg):
        '''creates a new directory'''
        try:
            os.mkdir(arg)
            print(f'directory "{arg}" created successfully.')
        except FileExistsError:
            print(f'Directory "{arg}" already exists')
        except Exception as e:
            print(f'Error: {e}')

    def do_touch(self, arg):
        try:
            with open(arg, 'w'):
                pass
            print(f'File "{arg}" created successfully')
        except FileExistsError:
            print(f'File "{arg}" already exist')
        except Exception as e:
            print(f'Error: {e}')

#alising the touch command
    def do_nul(self, arg):
        '''alias for touch'''
        self.do_touch(arg)




ConsoleHello()
if __name__ == '__main__':
    ConsoleHello().cmdloop()
