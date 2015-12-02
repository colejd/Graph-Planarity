# Graph Planarity Algorithms

This is a program that generates graphs and runs various tests for planarity on them. Written with Python 2.7.

Implemented algorithms:

* Brute force method using [Wagner's Theorem](https://en.wikipedia.org/wiki/Wagner%27s_theorem)

Planned algorithms:

* Hopcroft and Tarjan's path addition algorithm


###Installation
You'll need the following Python modules installed on your machine:

* networkx
* pydot
* graphviz

To install these dependencies, run:


```
pip install --user networkx pydot graphviz
```


Note: You don't need the ```--user``` flag for typical installation, but you'll need it if you're 
running El Capitan; pip won't be able to get proper permissions to install due to SIP otherwise.


###Running the program
To run this program, execute
`python Main.py`
in the command line.

