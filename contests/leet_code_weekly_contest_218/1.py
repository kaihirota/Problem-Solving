from typing import *

class Solution:
    def interpret(self, command: str) -> str:
        # command = command.replace('G', 'G')
        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')
        return command

assert Solution().interpret("G()(al)") == 'Goal'