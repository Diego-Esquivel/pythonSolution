/**
 * @file graph_tools.cpp
 * This is where you will implement several functions that operate on graphs.
 * Be sure to thoroughly read the comments above each function, as they give
 *  hints and instructions on how to solve the problems.
 */

#include "graph_tools.h"
using namespace std;
/**
 * Finds the minimum edge weight in the Graph graph.
 * THIS FUNCTION IS GRADED.
 *
 * @param graph - the graph to search
 * @return the minimum weighted edge
 *
 * @todo Label the minimum edge as "MIN". It will appear blue when
 *  graph.savePNG() is called in minweight_test.
 *
 * @note You must do a traversal.
 * @note You may use the STL stack and queue.
 * @note You may assume the graph is connected.
 *
 * @hint Initially label vertices and edges as unvisited.
 */
int GraphTools::findMinWeight(Graph& graph)
{
  //TODO: YOUR CODE HERE
    setUNVISITED(graph);
    vector<Edge> vEdge = graph.getEdges();
    int min = INT_MAX;
    int x = 0;
    for (size_t i = 0; i < vEdge.size(); i++) {
      if(vEdge[i].getWeight()<min){
        min = vEdge[i].getWeight();
        x = i;
      }
    }
    graph.setEdgeLabel(vEdge[x].source, vEdge[x].dest, "MIN");
    return min;

}

void GraphTools::setUNVISITED(Graph &graph)
{
    Vertex start = graph.getStartingVertex();
    queue<Vertex> q;
    graph.setVertexLabel(start,"UNVISITED");
    q.push(start);
    while(!q.empty())
    {
        Vertex v = q.front();
        vector <Vertex> adj = graph.getAdjacent(v);
        q.pop();
        for (unsigned long i = 0; i < adj.size(); i++)
        {
            Vertex w = adj[i];
            if (graph.getVertexLabel(w).compare("UNVISITED") != 0)
            {
                graph.setEdgeLabel(v,w, "UNVISITED");
                graph.setVertexLabel(w, "UNVISITED");
                q.push(w);
            } else if (graph.getEdgeLabel(v,w).compare("UNVISITED")!= 0)
                graph.setEdgeLabel(v,w,"UNVISITED");
        }
    }
}

/**
 * Returns the shortest distance (in edges) between the Vertices
 *  start and end.
 * THIS FUNCTION IS GRADED.
 *
 * @param graph - the graph to search
 * @param start - the vertex to start the search from
 * @param end - the vertex to find a path to
 * @return the minimum number of edges between start and end
 *
 * @todo Label each edge "MINPATH" if it is part of the minimum path
 *
 * @note Remember this is the shortest path in terms of edges,
 *  not edge weights.
 * @note Again, you may use the STL stack and queue.
 * @note You may also use the STL's unordered_map, but it is possible
 *  to solve this problem without it.
 *
 * @hint In order to draw (and correctly count) the edges between two
 *  vertices, you'll have to remember each vertex's parent somehow.
 */
int GraphTools::findShortestPath(Graph& graph, Vertex start, Vertex end)
{
  //TODO: YOUR CODE HERE
  vector<Vertex> vv = graph.getVertices();
  for(size_t i = 0; i < vv.size();i++){
    graph.setVertexLabel(vv[i],"UNVISITED");
  }

	queue<Vertex> qv;
	qv.push(start);
	unordered_map<Vertex,Vertex> parent;
	parent.emplace(start,start);
	int count = 1;

	while(qv.empty() == false)
	{
		Vertex vert = qv.front();
		qv.pop();
        graph.setVertexLabel(vert,"VISITED");

		vector<Vertex> near = graph.getAdjacent(vert);
		for(size_t i =0; i < near.size() ;i++)
		{
			if(graph.getVertexLabel(near[i]) == "UNVISITED")
            {
                graph.setVertexLabel(near[i],"VISITED");
                qv.push(near[i]);
                parent.emplace(near[i],vert);
            }
		}
	}

   Vertex e = end;
    if(parent[e] == start){
        graph.setEdgeLabel(e,parent[e],"MINPATH");
        return 1;
    }

    while(parent[e]!=start){
        graph.setEdgeLabel(e,parent[e],"MINPATH");
        e = parent[e];
        count++;

    }

    if(parent[e] == start){
        graph.setEdgeLabel(e,parent[e],"MINPATH");
    }

return count;
}

/**
 * Finds a minimal spanning tree on a graph.
 * THIS FUNCTION IS GRADED.
 *
 * @param graph - the graph to find the MST of
 *
 * @todo Label the edges of a minimal spanning tree as "MST"
 *  in the graph. They will appear blue when graph.savePNG() is called.
 *
 * @note Use your disjoint sets class from MP 7.1 to help you with
 *  Kruskal's algorithm. Copy the files into the dsets.h and dsets.cpp .
 * @note You may call std::sort instead of creating a priority queue.
 */
void GraphTools::findMST(Graph& graph)
{
    //TODO: YOUR CODE HERE
    vector<Edge> ve = graph.getEdges();
    vector<Vertex> vv = graph.getVertices();
    int eSize = ve.size();
    int vSize = vv.size();
    int count = 0;

    sort(ve.begin(),ve.end());

    DisjointSets dsj;
    dsj.addelements(vSize);

    while(count < vSize -1){
    for(int i = 0; i < eSize; i++){
        Edge current = ve[i];
        int ps = find(vv.begin(),vv.end(),current.source) - vv.begin();
        int pd =find(vv.begin(),vv.end(),current.dest) - vv.begin();

        if(dsj.find(ps) != dsj.find(pd))
        {
            dsj.setunion(ps,pd);
            graph.setEdgeLabel(current.source,current.dest,"MST");
            count++;
        }
    }
}
}
