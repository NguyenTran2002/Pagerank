# PageRank

This repository provides 3 programs using the PageRank algorithm.

# Install Pre-requisites
Run the command `pip3 install -r requirements.txt` or `pip install -r requirements.txt` depends on your Python version.

# How to Run

After installing all requirements, the user can simply any of the .py program by the command `python3 example_program.py` or `python example_program.py` depending on the user's Python version.

Other steps, such as providing the data to the program, will be instructed specifically to the user by the program themselves in the terminal.

# pagerank.py

This is the standard PageRank program that Google originally used. The program requires a user's input of a network of pages and an integer specifying how many loops of calculating PageRank should the program be run for.

This program will read in from the folder `Data` a .csv file that will then be intepreted as an adjacency list to create a graph.

The resulting PR values will be output to the terminal. In addition, a graphical representation of the input network will also be generated and stored in the folder `Graph`.

# pagerank_step_by_step_ver.py

This program is a simple extension of `pagerank.py`. On top of everything that `pagerank.py` already does, it also output the PR values of each iteration of the program to the terminal.

The user should use this program instead of `pagerank.py` if they wish to examine the calculation step by step.

# pagerank_alt_ver.py

This program is a rather unconventional way to run PageRank. The program only requires a user's input of a network stored in the `Data` folder.

This alternate version of PageRank will examine how much does the PR values change from one iteration to the next. Through the Google paper, we know that the more we run PageRank, the closer we will get to the actual PR values. Therefore, the program will terminate automatically and output to the terminal when it perceives the maximum change in PR values is less than 0.01%.

This alternate version can be quite costly to run on the actual Internet, but it proves useful for case study, when an user might want to find the best PR values as possible.

# random_network_generator.py

The user will specify a number of verticies they want to have in a network, then this program will generate a random network accordingly and store it in the `Data` folder.

The format of the output data is tailored to be usable by all 3 PageRank programs above without the need of manual adjustment.
