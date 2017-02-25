import moviecredits.connections as connections
import numpy as np

def main():
    actors, colleagues, connections_matrix = connections.matrix()
    print(connections_matrix)

    # next... to output the previous output examples to complement the matrix.

    # the index position represents the index in the array.
    # colleagues[0], actors[0] is:
    print(connections_matrix[(0,0)])
    print()

    # index positions value > 0
    colleagues_index, actor_index = np.where(connections_matrix > 0)

    for index in range(len(actor_index)):
        print("colleague {} | actor {}".format(colleagues[colleagues_index[index]], actors[actor_index[index]]))
        print("weight %d "% connections_matrix[(colleagues_index[index], actor_index[index])])

























if __name__ == '__main__':
    main()