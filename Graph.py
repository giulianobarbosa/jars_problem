from itertools import permutations


class Graph:

    def __init__(self, inicial_state:list, final_state:list, jars_len:list) -> None:
        
        self.initial_state = inicial_state
        self.final_state = final_state
        self.jars_len = jars_len
        self.actual_state = [inicial_state]
        self.closed_states = []
        self.last_states = [inicial_state]
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
                
                if self.actual_state == []:
                    print("Impossivel")
                    exit()

            self.last_states = self.actual_state
            self.actual_state = []
            i+=1
            print(i)
