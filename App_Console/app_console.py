
import commands

class AppConsole():

    def __init__(self) -> None:
        commands.fill_commands()
        print(commands.get_commands())


if __name__== '__main__':
    AppConsole()
    

