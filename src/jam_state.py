from abstract_state import State
import finished_state

"""
The machine just pauses here and waits for confirmation that the machine is not jammed. 
On a real machine, the machine's controller would verify that its ejection mechanism is cleared of any objects using its
sensors before allowing you to continue.
"""


class JamState(State):
    def handle(self, data=None) -> None:
        input("Press enter once youve unjammed the machine and completely removed the part")
        self.context.transition_to(finished_state.FinishedState())
