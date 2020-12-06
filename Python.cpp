#include "Python.h"

const char * Python::py_string(string cmd, Graph item){
	string output = "";
	output += cmd;
	std::stringstream ss;
	ss << item;
	output += " " + ss.str();
	//cout << output;
	const char* out = output.c_str();
	
	return out;
}