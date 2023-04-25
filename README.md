# PHSX 815: Week 11
## Central Limit Theorem

This repository includes a script that demonstrates the K-means clustering algorithm, showing a method of separating clusters of data. 

---

### Homework 12:

### Running the Code
The construction plots are made by the `kmeans.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import sys
  import numpy as np
  from sklearn.cluster import KMeans
  import matplotlib.pyplot as plt
```

To run this script from the terminal in linux, run:

> $ python3 kmeans.py

This runs the file with the default parameters which is seed number 555 for the Random algorithm. This can be changed from the terminal.

For example, it may looks something like this in linux:

> $ python3 kmeans.py -seed 486

which would run the algorithm with an initial seed value of 486 instead of the default 555.

### The Output

The script first outputs the raw data in a plot, and then a second plot with the K-means algorithm clusters separated by color. Then, the centroids of the clusters are outputted in the terminal as a print command. 

![plot1](https://user-images.githubusercontent.com/76142511/234176163-3b87f261-5a77-4714-9253-95a7526dbf66.png)

![plot2](https://user-images.githubusercontent.com/76142511/234176176-9f038b98-eefb-4340-a588-0bcae5032126.png)

SOURCES: Code was adpated from [this RealPython page.](https://realpython.com/k-means-clustering-python/)



