# Camouflage
Research Project for Anonymizing Computation

The idea is to introduce fake nodes into existing computation nodes for deluding any ML algorithm from detecting
the currently executing process by a user.

* Fake Node Addition Scenario

Automatically adds fake nodes to given algorithm, algorithm needs to be prepared as graphs with each node performing a simple computation or loop.

* Mixed Algorithm

Automatically combines 2-4 different algorithms into a single algorithm that executes in a linear manner or executes multiple nodes simultaneously using threads.

* Hybrid Version

Automatically combines 2-4 algorithms and adds fake nodes to create an excessive security measure that hides resource usage more efficiently. 

# Run Method
* Install all requirements from the requirements file.

* The files used to run the custom graphs are either encrypted already or large randomly generated graphs in csv files. The createFile.py inside the functions directory will allow the creation of the large files that are converted to arrays for input. Another filer encrypt.py encrypts the generated files for input. Make sure to generate the files before anything else.

* The scenarioRunner.py file contains the use of custom made graph for this research. They call their normal, remodeled/fake/anonymized execution, mixes them based on method calls to dataExtract folder. 

* The main.py file has several method calls for running either real_world_graphs, custom_graphs or allow anyone to create a random graph and test if they can be identified through their combined input_length, out_length and runtime. They can also test if the identification is reduced during anonymization. 

* To run any graphs in the main.py file. Identify what results you wish to generate call methods for them through proper arguments. 

* If any issue occurs check the paths for data reading and writing.

* Install the requirements in the machine_learning_graphs folder for working with real_world graphs.

* Find and download the necessary datasets to generate the required results. The dataset used are indicated in the readme.md file of machine_learning_graphs folder. 

* Similar to custom graphs find what results you want to generate and call the methods with appropriate arguments in the main.py file.
 
