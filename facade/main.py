class Scanner:
    """Takes in a stream of characters and produces stream of tokens."""
    def __init__(self, stream):
        self._input_stream = stream

    def scan(self):
        """Tokenize the input."""
        return self._input_stream.split()


class Parser:
    """Uses ProgramNodeBulder to construct parse tree using Scanner tokens."""
    def __init__(self):
        pass

    def parse(self, scanner, program_node_builder):
        pass


class ProgramNodeBuilder:
    """Parser calls back on ProgramNodeBuilder to build the parse tree."""
    def __init__(self):
        self._node = None

    def new_variable(self, variable_name):
        pass

    def new_assignment(self, variable, expression):
        pass

    def get_root_node(self):
        pass


class ProgramNode:
    """Composite pattern for program node heirachy. Composite Pattern."""
    def __init__(self):
        self._children = []

    def add(self, program_node):
        self._children.append(program_node)

    def remove(self, program_node):
        self._children.remove(program_node)

    def traverse(self, code_generator):
        code_generator.visit(program_node=self)
        for program_node in self._children:
            program_node.traverse(code_generator)


class CodeGenerator:
    """Traverse operation takes a CodeGenerator. A Visitor."""
    def __init__(self, byte_code_stream):
        self._output = byte_code_stream

    def visit(self, program_node):
        """Generate the bytecode."""
        print(f'Generate the byte code for {program_node}')


class Compiler:
    """Facade for all the complexity of compilation."""
    def __init__(self):
        pass

    def compile(self, input_stream, byte_code_stream):
        scanner = Scanner(input_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()
        parser.parse(scanner, builder)
        generator = CodeGenerator(byte_code_stream)
        parse_tree = builder.get_root_node()
        parse_tree.traverse(generator)
