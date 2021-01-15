"""Simple program for computing the edge chromatic number of a graph
"""

def disp(item, n):
    if item:
        if type(item[0]) is list:
            print()

            if item[0][0] == 0:
                print("==Adjacency matrix==")
                
                for i in range(len(item)):
                    print(item[i], sep="")

            else:
                print("==Colours of each vertex==")
                
                for i in range(len(item)):
                    print("V", i + 1, " ", item[i], sep="")
                
        elif type(item[0]) is int:
            print()
            colour_index = 0
            print("==Colour of each edge==")
            latest = edge_list[0][0]
            
            for edge in edge_list:
                if edge[0] != latest:
                    print()
                    
                print("V", edge[0], "V", edge[1], "| ", item[colour_index], sep="")
                latest = edge[0]
                
                colour_index += 1

            print()
            

def get_adj_matrix():
    print("========================")
    n = int(input("Enter number of vertices: "))

    if n == 0:
        return None, n
    
    print("Enter adjacency matrix, rows separated by new line OR 1 for complete graph: ")

    matrix = [[] for i in range(n)]


    for i in range(n):
        string = input()

        if string == "1":
            for i in range(n):
                for j in range(n):
                    if i == j:
                        matrix[i] += [0]
                    else:
                        matrix[i] += [1]

            break

        elif string[0] == "0":
            row = []
            
            for char in string:
                if char == "0" or char == "1":
                    row = row + [int(char)]

            matrix[i] = list(row)            

            for i in range(n):
                for j in range(n):
                    matrix[i][j] = int(matrix[i][j])
            
    return matrix, n

def initialise(adj_matrix, n):
    colours_matrix = [[] for i in range(n)]
    edge_colours = []
    edge_list = []

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                if [j + 1, i + 1] not in edge_list:
                    edge_list = edge_list + [[i + 1, j + 1]]

    return (colours_matrix, edge_colours, edge_list)

def find_colours(colours_matrix, edge_list, edge_colours):
    for edge in edge_list:
        colour = 1

        while (colour in colours_matrix[edge[0] - 1]) or (colour in colours_matrix[edge[1] - 1]):
            colour += 1

        colours_matrix[edge[0] - 1].append(colour)
        colours_matrix[edge[1] - 1].append(colour)

        edge_colours.append(colour)

    return colours_matrix, edge_colours

def main():
    n = -1

    while n != 0:
        adj_matrix, n = get_adj_matrix()
        disp(adj_matrix, n)

        if n == 0:
            break

        global edge_list
        (colours_matrix, edge_colours, edge_list) = initialise(adj_matrix, n)

        colours_matrix, edge_colours = find_colours(colours_matrix, edge_list, edge_colours)

        disp(colours_matrix, n)
        disp(edge_colours, n)

        print("This graph has edge chromatic number of ", max(edge_colours), ".\n", sep="")

main()

