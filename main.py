"""
"""

from itertools import permutations

class Graph:

    def __init__(self, inicial_state:list, final_state:list, jars_len:list) -> None:
        
        self.initial_state = inicial_state
        self.final_state = final_state
        self.jars_len = jars_len
        self.actual_state = inicial_state


    def is_jar_empty(self, jar:int) -> bool:

        return jar == 0


    def is_jar_full(self, jar:int, index:int) -> bool:

        return jar == self.jars_len[index]

    
    # This function is going to drain out from the jar out to jar in,
    # Untill jar_out is 0
    def drain_jar_out(self, index_jar_in:int, index_jar_out:int):
        
        if (self.actual_state[index_jar_in] + self.actual_state[index_jar_out] <= self.jars_len[index_jar_in]) and (not(self.is_jar_empty(self.actual_state[index_jar_out]))):
        
            self.actual_state[index_jar_in] += self.actual_state[index_jar_out]
            self.actual_state[index_jar_out] = 0
        
        else:

            pass


    # This function is going to drain out from the jar out to jar in,
    # Untill jar_out is full
    def fill_all_jar(self, index_jar_in:int, index_jar_out:int):

        if self.jars_len[index_jar_in] - self.actual_state[index_jar_in] < self.actual_state[index_jar_out]:

            missing = self.jars_len[index_jar_in] - self.actual_state[index_jar_in]
            self.actual_state[index_jar_in] += missing
            self.actual_state[index_jar_out] -= missing

        else:

            pass


    def get_next_states(self):

        comb = permutations([0, 1, 2], 2)

        for c in comb:
        
            self.fill_all_jar(self.actual_state[c[0]], self.actual_state[c[1]])
            self.drain_jar_out(self.actual_state[c[0]], self.actual_state[c[1]])




initial_state = [10, 20, 11]
final_state = [4, 20, 17]
jars_heuristic = [12, 25, 17]