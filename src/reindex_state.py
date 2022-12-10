from abstract_state import State
import locating_state
"""
Upon reindexing you will discover a weird item with id 1000 is in actually the machine. If you request id 1000, it will
fail to find it. Then the machine will reindex and relocate the item. Then proceed to eject the item.
"""


class ReindexState(State):
    def handle(self, data) -> None:
        self.context.sim.reindex()
        self.context.transition_to(locating_state.LocatingState(), data)
