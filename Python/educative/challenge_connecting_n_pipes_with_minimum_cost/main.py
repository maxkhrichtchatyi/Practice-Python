def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """

    total_cost = 0
    selected_pipe = 0

    for pipe in sorted(pipes):
        if not selected_pipe:
            selected_pipe = pipe
        else:
            selected_pipe += pipe
            total_cost += selected_pipe
 
    return total_cost
