/**
 * @file premade_graphs.h
 *
 * This file builds three example graphs with the Graph library.
 * The examples have real weights between cities in miles.
 * Unfortunately, graphviz draws the nodes with a best-fit algorithm,
 *  so relative locations of cities are wrong.
 * These graphs are also used in *_test.cpp.
 *
 * @author Diego G Esquivel
 * @date Fall 2020
 */

#ifndef _PYTHON_
#define _PYTHON_
#include "graph.h"
/**
 * This namespace contains code that builds three example graphs
 *  with the Graph library. The examples have real weights between
 *  cities in miles. Unfortunately, graphviz draws the nodes with a
 *  best-fit algorithm, so relative locations of cities are wrong.
 */
namespace Python
{

    /**
     * Creates a map of some US cities.
     * @param isWeighted - whether to show distance between
     *  cities in miles.
     * @return the graph of a few cities in the United States
     */
    const char* py_string(string cmd, Graph item);
}

#endif
