/* Your code here! */
#include <vector>
#include "dsets.h"
using namespace std;
void DisjointSets::addelements(int num){
  for (int i = 0; i < num; i++) {
    v_.push_back(-1);
  }
}

int DisjointSets::find(int elem){
  int out = 0;
  if(v_[elem] < 0)
    out = elem;
  else{
    out = find(v_[elem]);
    v_[elem] = out;
  }
  return out;
}

void DisjointSets::setunion(int a, int b){
  a = find(a);
  b = find(b);
  int newSize = v_[a] + v_[b];
  if(v_[a] < v_[b]){
    v_[b] = a;
    v_[a] = newSize;
  }
  else{
    v_[a] = b;
    v_[b] = newSize;
  }
}

int DisjointSets::size(int elem){
  return -(v_[find(elem)]);
}
