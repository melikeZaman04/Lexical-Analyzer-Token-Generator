from .tokenizer import Tokenizer
from .token import TokenType
from .keywords import load_keywords


def main():
    keywords = load_keywords()
    tokenizer = Tokenizer(keywords)
    sample = ('#define PI 3.14\n// test\npublic class Test {\n public static void main(String[] args) {\n double r = 10; double area = PI * r * r; }\n}\n')
    tokens = tokenizer.tokenize(sample)
    for t in tokens:
        print(str(t))

if __name__ == '__main__':
    main()
