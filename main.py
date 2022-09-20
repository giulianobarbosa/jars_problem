from Graph import Graph
from reader import get_cases
import time


if __name__ == "__main__":

    cases_list = []

    initial_state_impossible = [10, 10, 10]
    final_state_impossible = [0, 0, 0]
    jars_len_impossible = [10, 10, 10]

    cases = get_cases('casos_de_teste.txt')
    for case in cases:
        start_time = time.time()
        jars_len, initial_state, final_state, moviments = case
        initial_state = [int(i_s) for i_s in initial_state]
        final_state = [int(f_s) for f_s in final_state]
        jars_len = [int(j_l) for j_l in jars_len]
        Graph(initial_state, final_state, jars_len).get_next_states()
        print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    Graph(initial_state_impossible, final_state_impossible, jars_len_impossible).get_next_states()
    print("--- %s seconds ---" % (time.time() - start_time))