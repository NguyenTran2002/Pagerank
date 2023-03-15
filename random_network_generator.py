# import libraries
import pandas as pd
import random
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

# read in user's input network
num_vertices = int(input("Specify Number of Web Pages: "))

# list storing data to export
list_vertices = []
list_links = []

# loop through the vertices
for i in range(num_vertices):

    list_vertices.append(i)

    # random a number between 0 and the number of vertices
    num_links = random.randint(0, num_vertices)

    # create a list of links
    links = []

    # loop through the number of links
    for j in range(num_links):
            
        # random a number between 0 and the number of vertices
        link = random.randint(0, num_vertices - 1)

        # if the number is NOT already added
        if link not in links:
            links.append(link)

    # convert the list of links to a string separated by ";"
    links = ";".join(str(x) for x in links)

    # add the links to the list
    list_links.append(links)

# ---------------------------------
# Save Data

# create a dataframe
df = pd.DataFrame(list(zip(list_vertices, list_links)), columns =['Page', 'Links To'])

# read in user's desired name
name = input("File Name to Save (in Data Folder): ")

# add the file extension if the user forgot to do so (and if the input is not empty)
if len(name) == 0:
    name = "Random Network.csv"

elif name[-4:] != ".csv":
    name = name + ".csv"

else:
    pass

path = "Data/" + name

# export the dataframe to a csv file in the Data folder
df.to_csv(path, index=False)