# Command Design Pattern

Encapsulate requests and functions as an object so that we can parametrize them. You can pass these objects around. Client doesn't have to care about passing the parameters to an operation because they are encapsulated during the command creation. Our command can have unexecute or undo method!

## Where is this patten used?

* Python `__call__` aka callable is exactly this pattern!
* Used for transforms and models in PyTorch. Compare PyTorch's Module to functional interface.
* Transaction for database operations.
