import re

TOKEN_REGEX = re.compile(
    r'(?P<NOT>[¬!~])|'
    r'(?P<AND>[∧&])|'
    r'(?P<OR>[∨|])|'
    r'(?P<IFF>↔|<->)|'
    r'(?P<IMPLIES>→|->)|'
    r'(?P<LPAREN>\()|'
    r'(?P<RPAREN>\))|'
    r'(?P<VAR>[A-Za-z][A-Za-z0-9_]*)|'
    r'(?P<WS>\s+)|'
    r'(?P<ERR>.)'
)

class ParseError(Exception):
    def __init__(self, message, offset, token, text):
        super().__init__(f"{message} at offset {offset}: '{token}'")
        self.message = message
        self.offset = offset
        self.token = token
        self.text = text

class Parser:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        for m in TOKEN_REGEX.finditer(text):
            typ = m.lastgroup
            val = m.group(typ)
            off = m.start()
            if typ == 'WS': continue
            if typ == 'ERR':
                raise ParseError("Unknown character", off, val, text)
            self.tokens.append((typ, val, off))
        if not self.tokens:
            raise ParseError("Empty input", 0, "", text)
        self.pos = 0
        self.vars = set()

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos][0]
        return None

    def match(self, expected_type):
        if self.peek() == expected_type:
            self.pos += 1
            return True
        return False

    def parse_primary(self):
        if self.pos >= len(self.tokens):
            raise ParseError("Unexpected end of input", len(self.text), "", self.text)
        
        typ, val, off = self.tokens[self.pos]
        if typ == 'VAR':
            self.pos += 1
            self.vars.add(val)
            return val
        elif typ == 'LPAREN':
            self.pos += 1
            ast = self.parse_iff()
            if self.pos >= len(self.tokens) or self.tokens[self.pos][0] != 'RPAREN':
                raise ParseError("Unmatched parenthesis", off, val, self.text)
            self.pos += 1
            return ast
        else:
            raise ParseError("Expected variable or '('", off, val, self.text)

    def parse_not(self):
        if self.match('NOT'):
            arg = self.parse_not()
            return {"op": "not", "args": [arg]} # Wait, the logic adapter expects 'arg' for not!
        return self.parse_primary()

    def parse_and(self):
        left = self.parse_not()
        while self.match('AND'):
            right = self.parse_not()
            left = {"op": "and", "args": [left, right]}
        return left

    def parse_or(self):
        left = self.parse_and()
        while self.match('OR'):
            right = self.parse_and()
            left = {"op": "or", "args": [left, right]}
        return left

    def parse_implies(self):
        left = self.parse_or()
        if self.match('IMPLIES'):
            right = self.parse_implies() # Right associative
            return {"op": "implies", "args": [left, right]}
        return left

    def parse_iff(self):
        left = self.parse_implies()
        if self.match('IFF'):
            right = self.parse_implies()
            if self.peek() == 'IFF':
                t = self.tokens[self.pos]
                raise ParseError("Chained biconditionals are unparseable without parentheses", t[2], t[1], self.text)
            return {"op": "iff", "args": [left, right]}
        return left

def parse(text):
    if not text.strip():
        raise ParseError("Empty input", 0, "", text)
    p = Parser(text)
    ast = p.parse_iff()
    if p.pos < len(p.tokens):
        t = p.tokens[p.pos]
        raise ParseError("Trailing or adjacent tokens", t[2], t[1], text)
    
    # Fix the `not` op mapping which uses `arg` instead of `args` in logic.py
    def fix_not(node):
        if isinstance(node, str):
            return node
        if node["op"] == "not":
            return {"op": "not", "arg": fix_not(node["args"][0])}
        return {"op": node["op"], "args": [fix_not(a) for a in node["args"]]}
        
    return fix_not(ast), p.vars

