from abstract_state import State
from finished_state import FinishedState
from jam_state import JamState

"""
After the part is located it must be ejected from the device, this has a 1/5 chance of jamming the machine.
If the machine jams, the machine will transition to the jammed state which stops all movement of the machine and waits 
until the user has specified that the machine is no longer jammed.
Otherwise the machine transitions to the finished state.
"""


class EjectState(State):
    def handle(self, data=None) -> None:
        estat = self.context.sim.eject()
        if estat:
            self.context.transition_to(FinishedState())
        else:
            self.context.transition_to(JamState())
