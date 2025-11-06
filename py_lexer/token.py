from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    CHAR = 'CHAR'
    OPERATOR = 'OPERATOR'
    SEPARATOR = 'SEPARATOR'
    BOOLEAN_LITERAL = 'BOOLEAN_LITERAL'
    NULL_LITERAL = 'NULL_LITERAL'
    UNKNOWN = 'UNKNOWN'


@dataclass
class Token:
    type: TokenType
    lexeme: str
    line: int
    column: int

    def __str__(self):
        return f"{self.lexeme} ({self.type.name}) at {self.line}:{self.column}"
