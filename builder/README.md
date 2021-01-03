# Builder Design Pattern

Separate construction from representation of a class so that construction process can do different things. Director orchestrates creation of objects but actual representation (aka product) is handled by builder.

## Where is this pattern used?

* Saving of a document to different file formats requires different builders
* In compilers, parser is the director while builder takes care of AST creation.