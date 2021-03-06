/**
 * @file premade_graphs.h
 *
 */

#ifndef _PREMADE_GRAPHS_
#define _PREMADE_GRAPHS_
#include "graph.h"
/**
 * This namespace contains code that builds three example graphs
 *  with the Graph library. The examples have real weights between
 *  cities in miles. Unfortunately, graphviz draws the nodes with a
 *  best-fit algorithm, so relative locations of cities are wrong.
 */
namespace PremadeGraphs
{

    /**
     * Creates a map of some US cities.
     * @param isWeighted - whether to show distance between
     *  cities in miles.
     * @return the graph of a few cities in the United States
     */
    Graph createUSMap(bool isWeighted);

    /**
     * Creates a map of some European cities.
     * @param isWeighted - whether to show distance between
     *  cities in miles.
     * @return the graph of a few cities in Europe
     */
    Graph createEuropeMap(bool isWeighted);

    /**
     * Creates a map of some Japanese cities.
     * @param isWeighted - whether to show distance between
     *  cities in miles.
     * @return the graph of a few cities in Japan
     */
    Graph createJapanMap(bool isWeighted);
}

#endif
