from itertools import permutations

class Graph:


    def __init__(self, inicial_state:list, final_state:list, jars_len:list) -> None:
        
        self.initial_state = inicial_state
        self.final_state = final_state
        self.jars_len = jars_len
        self.actual_state = [inicial_state]
        self.closed_states = []
        self.last_states = [inicial_state]
        self.last_states_2 = [inicial_state]
        self.token = False


    def is_jar_empty(self, jar:int) -> bool:

        return jar == 0


    def is_jar_full(self, jar:int, index:int) -> bool:

        return jar == self.jars_len[index]

    
    # This function is going to drain out from the jar out to jar in,
    # Untill jar_out is 0
    def drain_jar_out(self, state:list, indexes:tuple) -> None:

        state_ = []
        state_ = [s for s in state]
        
        if (state_[indexes[0]] + state_[indexes[1]] <= self.jars_len[indexes[0]]) and (not(self.is_jar_empty(state_[indexes[1]]))):
        
            state_[indexes[0]] += state_[indexes[1]]
            state_[indexes[1]] = 0

            if state_ == self.final_state:   

                print("ROLOU")
                exit()

            if state_ not in self.closed_states:
                
                self.actual_state.append(state_)
        
        else:
            
            pass

    # This function is going to drain out from the jar out to jar in,
    # Untill jar_out is full
    def fill_all_jar(self, state:list, indexes:tuple) -> None:

        state_ = []
        state_ = [s for s in state]

        if self.jars_len[indexes[0]] - state_[indexes[0]] < state_[indexes[1]]:

            missing = self.jars_len[indexes[0]] - state_[indexes[0]]
            state_[indexes[0]] += missing
            state_[indexes[1]] -= missing

            if state_ == self.final_state:   

                print("ROLOU")
                exit()

            if state_ not in self.closed_states:
                
                self.actual_state.append(state_)

        else:

            pass


    def get_next_states(self) -> None:

        i = 1
        while self.token == False:

            for state in self.last_states:
                
                comb = permutations([0, 1, 2], 2)
                self.closed_states.append(state)

                for c in comb:

                    self.fill_all_jar(state, c)
                    self.drain_jar_out(state, c)

            self.last_states = self.actual_state
            self.actual_state = []
            i+=1
            print(i)



if __name__ == "__main__":

    initial_state = [10, 20, 11]
    final_state = [4, 20, 17]
    jars_len = [12, 25, 17]

    initial_state_2 = [9, 11, 11]
    final_state_2 = [0, 25, 6]
    jars_len_2 = [16, 28, 29]

    initial_state_3 = [10, 9, 13]
    final_state_3 = [17, 0, 15]
    jars_len_3 = [29, 10, 24]

    initial_state_n = [20, 0, 9]
    final_state_n = [0, 10, 19]
    jars_len_n = [29, 11, 20]

    Graph(initial_state_n, final_state_n, jars_len_n).get_next_states()