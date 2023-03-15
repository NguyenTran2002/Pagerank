# import libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from os import system, name

# cosmetic clear screen function
def clear():
    """
    Source: https://www.geeksforgeeks.org/clear-screen-python/
    """
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()


# ---------------------------------
# User Input

# overview instruction
print("PageRank is an iterative algorithm that starts out by assigning a default value of 1.0 to all pages.\n\
The algorithm then recalculates the PR value according to the specified number of loops below.\n\
Generally, the more loops chosen, the more accurate the PR values will be, and the more expensive the algorithm becomes.\n\
The default number of loops is 40 of nothing is given into the input.\n")

# read in user's number of loops
num_loops = input("Specify Number of Loops: ")

# if the user did not specify a number of loops, set it to 40
if len(num_loops) == 0:
    num_loops = 40
else:
    num_loops = int(num_loops)

# read in user's input network
network_data_file = input("\nYour Network Data (copy paste the file name from the Data folder): ")

# add the file extension if the user forgot to do so (and if the input is not empty)
if network_data_file[-4:] != ".csv" and len(network_data_file) > 0:
    network_data_file = network_data_file + ".csv"


# ---------------------------------
# Read & Prepare Data

# read in the network as a pandas dataframe
if len(network_data_file) > 0:
    network_df = pd.read_csv("Data/" + network_data_file)
else:
    network_data_file = "Network 1.csv"
    network_df = pd.read_csv("Data/" + network_data_file)

# replace all nan values with empty strings
network_df = network_df.fillna('')

# convert all columns of the dataframe to string type expect for nan values
network_df = network_df.astype(str)

# convert the read in network dataframe into an adjacency list

# create an empty dictionary
adjacency_list = {}

# loop through the dataframe
for index, row in network_df.iterrows():
    # get the source and target nodes
    page = row['Page']
    links = row['Links To']

    # split links into a list by ";"
    links = links.split(';')
    
    # if the page is not in the dictionary, add it
    if page not in adjacency_list:
        adjacency_list[page] = links


# ---------------------------------
# Compute Pagerank (PR) Values

# create a new dictionary to store the pagerank values of all the pages
pagerank = {}

# prefill the dictionary with 1.0 for all the pages
for page in adjacency_list:
    pagerank[page] = 1.0

# set the damping factor
damping_factor = 0.85

# keep updating the pagerank values until the change factor is less than 0.01
for i in range(num_loops):

    # create a copy of the current pagerank dictionary (just to calculate the change factor later on)
    old_pagerank = pagerank.copy()

    # loop through each item in the pagerank dictionary
    for page in pagerank:

        raw_score = 0

        # check which pages link to the current page
        for parent in adjacency_list:

            if page in adjacency_list[parent]:
                raw_score += pagerank[parent] / len(adjacency_list[parent])


        # calculate the pagerank value for the page
        pagerank[page] = (1 - damping_factor) + damping_factor * raw_score

    # ---------------------------------
    # Output Results Step by Step

    print ("\n\n---------------------------------\n\n")

    # print the current loop number
    print("Loop " + str(i + 1) + " of " + str(num_loops) + "\n")

    # print the current pagerank values
    print("Current Pagerank Values:")
    print(pagerank)

    # calculate the average pagerank value
    average_pagerank = sum(pagerank.values()) / len(pagerank)

    # print the average pagerank value
    print("\nAverage Pagerank Value:\n" + str(average_pagerank))

# ---------------------------------
# Draw the Network

# initialize the networkx graph object
network_graph = nx.DiGraph()

# add vertices to the graph from the adjacency list
for page in adjacency_list:
    network_graph.add_node(page)

# add edges to the graph from the adjacency list
for page in adjacency_list:
    
    for link in adjacency_list[page]:
        if len(link) > 0:
            network_graph.add_edge(page, link)


# generate file name for the graph
graph_file_name = network_data_file.replace('.csv', '.png')
graph_file_name = "Graphs/" + graph_file_name

# visualize the network graph as a directed graph

# set the graph options
options = {
    'node_color': 'teal',
    'node_size': 300,
    'font_color': 'whitesmoke',
    'width': 2,
    'arrowstyle': '-|>',
    'arrowsize': 13,
}

# draw and export the graph
nx.draw_networkx(network_graph, with_labels=True, arrows=True, **options)
plt.savefig(graph_file_name, format="png")