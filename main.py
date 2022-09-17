from Graph import Graph


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

    initial_state_impossible = [10, 10, 10]
    final_state_impossible = [0, 0, 0]
    jars_len_impossible = [10, 10, 10]

    # Graph(initial_state_n, final_state_n, jars_len_n).get_next_states()
    Graph(initial_state_impossible, final_state_impossible, jars_len_impossible).get_next_states()