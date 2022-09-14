# Simple ECA
## A simple tool to generate graphics of elementary cellular automata

<br>

### Requirements
``` 
numpy
matplotlib
```

### Main Usage
1. run simpleECA.py
2. Enter the Wolfram code for the rule set to follow
3. Enter the number of generations to show (if n is the number of generations, the plot will be 2n + 1 wide)


### Module usage
If imported as a module, generateECA(rule, generation) will return a 2D array of an ECA where rule is a 0-255 int Wolfram code and generation is an int of the amount of generations to run. In the array, int 1 is "alive" and int 0 is "dead"