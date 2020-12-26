# Composite Design Pattern

Compose objects into tree structure to represent part-whole hierarchy. Essentially useful wherever you see 'container'. Both container and leaf class inherit same base class. Client ignores the difference between containers and leafs.

This pattern basically handles things gracefully using recursion.


## Where is this used?

* PyTorch's Module which holds more modules
* More obviously, PyTorch's Compose transform