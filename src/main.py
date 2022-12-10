from __future__ import annotations
from PartStorageStateMachine import PartStorageStateMachine
from wait_command_state import WaitCommandState

if __name__ == "__main__":
    # The client code.

    sm = PartStorageStateMachine(WaitCommandState())
    sm.event('start')
