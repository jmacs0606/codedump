from lexer import Lexer

while True:
    try:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        print(list(tokens))````