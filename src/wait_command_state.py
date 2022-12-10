from abstract_state import State
from locating_state import LocatingState

"""
This wait command state implements a TUI for sending commands to the machine. In real life this would be done using 
serial input like uart, can, or i2c

When the request command and the id of the item requested is given, the state machine will move on to the locating 
state and pass along the id value.
"""


def print_help():
    print("List of Accepted Commands:")
    print("----------------------------------------------")
    for c in ACCEPTED_COMMANDS:
        print("name: {name}".format(name=c['name']))
        print("parameter type: {type}".format(type=c['input']))
        print("----------------------------------------------")


ACCEPTED_COMMANDS = [
    {'name': ['request', 'req', 'r'],
     'input': 'int',
     'function': None},
    {'name': ['help', 'h'],
     'input' : None,
     'function': print_help},
    {'name': ['list', 'ls', 'l'],
     'input': None,
     'function': None}
]


def get_command(cmd):
    for c in ACCEPTED_COMMANDS:
        for n in c['name']:
            if cmd == n:
                return c
    return None


class WaitCommandState(State):
    def handle(self, data) -> None:
        while True:
            command = input("Enter Command (h for help) > ")
            command = command.strip().split(' ')
            cmd = get_command(command[0])
            if cmd is not None:
                if cmd['function'] is not None:
                    cmd['function']()
                elif 'r' in cmd['name']:
                    if len(command) == 2:
                        target = int(command[1])
                        self.context.transition_to(LocatingState(), target)
                        break
                    else:
                        print("use request command followed by the id of the item you are requesting\n eg. req <id>")
                elif 'l' in cmd['name']:
                    self.context.sim.print_items()



