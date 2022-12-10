import abstract_state
from MachineSim import MachineSim


class PartStorageStateMachine:
    """
    The PartStorageStateMachine defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: abstract_state.State) -> None:
        self.sim = MachineSim(10)
        self.transition_to(state)

    def transition_to(self, state: abstract_state.State, data=None):
        """
        The script automatically moves from state to state from within the states handle function. The handle functions
        must not return a value and must always result in a state change. All logic is implemented in each state
        handler.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self
        self._state.handle(data)
