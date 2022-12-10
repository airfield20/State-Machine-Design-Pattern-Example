from abstract_state import State
import wait_command_state

"""
The finished state is useful because it allows you to execute commands once all operations have stopped. 

On a real machine, I would transmit an OK or finished signal here to indicate to the user that the device is ready to be
interacted with.
"""


class FinishedState(State):
    def handle(self, data=None) -> None:
        print("Retrieval Process finished")
        print("Transmit OK Signal")
        self.context.transition_to(wait_command_state.WaitCommandState())
