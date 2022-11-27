import json

commands_json = r'json/commands.json'
gpio_json = r'json/gpio.json'
commands = []

def get_commands():
    return commands

def fill_commands():
    with open(commands_json, 'r') as json_file:
        json_commands = json.loads(json_file.read())
        for command in json_commands:
            if command['type'] == 'generic':
                commands.append(Command(**command))
            elif command['type'] == 'gpio':
                commands.append(GPIO_command(**command))

class Command():
    '''
    Command class that is build up from the json data.
    '''
    def __init__(self, command, help, options, type) -> None:
        self.command = command
        self.help = help
        self.options = options
        self.type = type

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self) -> str:
        return (f'Command: {self.command} \n'
                f'      help: {self.help} \n'
                f'      options: {self.options} \n'
                f'      type: {self.type} \n'
                f'      binary_pack: {self.make_binary_packet()} \n')

    def make_binary_packet(self):
        return bytes(self.command, 'ascii')


class GPIO_command(Command):
    pin = None

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def set_pin(self, pin):
        self.pin = pin


class EMS_command(Command):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

class LIN_command(Command):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

