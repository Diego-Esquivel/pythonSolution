/* Your code here! */
#ifndef DSETS
#define DSETS

#include <vector>
using namespace std;
class DisjointSets{
private:
  vector<int> v_;

public:
  void addelements(int num);
  int find(int elem);
  void setunion(int a, int b);
  int size(int elem);
};
#endif
