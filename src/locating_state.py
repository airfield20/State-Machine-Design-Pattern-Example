from abstract_state import State
from eject_state import EjectState
from reindex_state import ReindexState

"""
LocatingState is a Concrete State implementation. As you can see, the logic here is very simple and is indicative of
the flow diagram in the readme.

if the simulated machine fails to locate the item, it will reindex its contents. This cycle will repeat until the part 
is found.

On a real machine, if the item is not found even after reindexing, I would transition the state to operation finished
with "Not found" as data.
"""


class LocatingState(State):
    def handle(self, data: int) -> None:
        lstat = self.context.sim.locate(data)
        if lstat:
            self.context.transition_to(EjectState())
        else:
            self.context.transition_to(ReindexState(), data)

