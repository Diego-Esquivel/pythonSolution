#include <iostream>
#include <cstdlib>
#include "graph.h"
#include "premade_graphs.cpp"
#include "Python.h"

using std::string;
using std::cout;
using std::endl;

/**
 * Draws the three example graphs with weights.
 * All graphs saved as PNGs are in lab12/images/.
 */
void createPremadeGraphs(Graph& us, Graph& europe, Graph& japan)
{
    us = PremadeGraphs::createUSMap(true);
    europe = PremadeGraphs::createEuropeMap(true);
    japan = PremadeGraphs::createJapanMap(true);

    // print to terminal
    cout << "\nDisplaying a graph of Europe...\n\n";
    europe.print();
}

/**
 * Create the US map without weights.
 */
void createUnweightedUS()
{
    Graph us_uw = PremadeGraphs::createUSMap(false);
}

/**
 * Create and print a random weighted graph with
 *  9 vertices and random seed 777.
 */
void createRandomGraph()
{
    cout << "\nDisplaying a random graph...\n\n";
    Graph graph(true, 9, 777);
    graph.print();
}

/**
 * Build a graph by manually inserting vertices.
 */
void buildGraph()
{
    cout << "Displaying a manually created graph...\n\n";
    Graph graph(true);
    graph.insertVertex("A");
    graph.insertVertex("B");
    graph.insertVertex("C");
    graph.insertEdge("A", "B");
    graph.insertEdge("A", "C");
    graph.setEdgeWeight("A", "B", 7);
    graph.setEdgeWeight("A", "C", 11);
    graph.setEdgeLabel("A", "C", "AN EDGE");
    graph.print();
}

/**
 * Run all the different examples.
 */

int main() {
	Graph us(true);
	Graph europe(true);
	Graph japan(true);
	createPremadeGraphs(us,europe,japan);
    createUnweightedUS();
    createRandomGraph();
    buildGraph();
    char filename[] = "sortingfake.py";
    FILE* fp;
	const char* trm_string = Python::py_string("C:\\Users\\mpidi\\Desktop\\ProjectResi\\VisualStuRes\\APythonSoln\\main\\the_file", us);
    cout << trm_string;
    std::system(trm_string);
    /*Py_Initialize();
    
    fp = _Py_fopen(filename, "r");
    PyRun_SimpleFile(fp, filename);

    Py_Finalize();*/
    return 0;
}