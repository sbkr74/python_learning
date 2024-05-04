'''
Here's a brief overview of what an AST object represents:

Module: The top-level container for the entire Python source code.
FunctionDef: Represents a function definition.
ClassDef: Represents a class definition.
Assign: Represents an assignment statement.
Name: Represents a variable or a function name.
Call: Represents a function or method call.
BinOp: Represents a binary operation like addition, subtraction, etc.
If: Represents an if statement.
For: Represents a for loop.
'''
import ast

code = """
def greet(name):
    print("Hello, " + name)
"""

tree = ast.parse(code)
print(tree)

# --------------------------------------------------------------
class FunctionVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print("Found function:", node.name)

tree = ast.parse(code)
visitor = FunctionVisitor()
visitor.visit(tree)
# -----------------------------------------------------------------
class AddLogging(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        print_stmt = ast.parse('print("Function called:", "{}")'.format(node.name)).body[0]
        node.body.insert(0, print_stmt)
        return node

tree = ast.parse(code)
transformer = AddLogging()
new_tree = transformer.visit(tree)
print(ast.dump(new_tree))
# --------------------------------------------------------------------
new_code = compile(new_tree, filename="", mode="exec")
exec(new_code)

