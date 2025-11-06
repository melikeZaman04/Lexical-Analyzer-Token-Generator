import re
from typing import List, Dict
from .token import Token, TokenType


class Tokenizer:
    def __init__(self, keywords=None):
        # keywords may be provided as a dict (lexeme->tokenType) or an iterable of lexemes
        self.keywords_map = {}
        if keywords:
            # dict-like
            try:
                for k, v in keywords.items():
                    if k:
                        self.keywords_map[k.lower()] = v.upper() if isinstance(v, str) else str(v).upper()
            except Exception:
                # treat as iterable
                for k in keywords:
                    if k:
                        self.keywords_map[k.lower()] = 'KEYWORD'

    def process_defines(self, source: str) -> str:
        defines: Dict[str, str] = {}
        out_lines = []
        for line in source.splitlines():
            stripped = line.strip()
            if stripped.startswith('#'):
                parts = stripped.split(None, 2)
                if len(parts) >= 3 and parts[0] == '#define':
                    defines[parts[1]] = parts[2]
                # drop preprocessor lines
            else:
                out_lines.append(line)
        processed = '\n'.join(out_lines)
        # replace whole word occurrences
        for k, v in defines.items():
            processed = re.sub(r'\\b' + re.escape(k) + r'\\b', v, processed)
        return processed

    def remove_comments(self, src: str) -> str:
        # remove block comments
        src = re.sub(r'/\\*.*?\\*/', '', src, flags=re.S)
        # remove line comments
        src = re.sub(r'//.*?(?=\\n|$)', '', src)
        return src

    def tokenize(self, source: str) -> List[Token]:
        if source is None:
            source = ''
        # apply defines
        processed = self.process_defines(source)
        # remove comments
        processed = self.remove_comments(processed)

        tokens: List[Token] = []
        i = 0
        line = 1
        col = 1
        length = len(processed)

        def add(tok_type, lex, l, c):
            tokens.append(Token(tok_type, lex, l, c))

        while i < length:
            c = processed[i]
            if c == '\n':
                i += 1
                line += 1
                col = 1
                continue
            if c.isspace():
                i += 1
                col += 1
                continue

            token_line = line
            token_col = col

            # identifier / keyword
            if c.isalpha() or c == '_':
                start = i
                while i < length and (processed[i].isalnum() or processed[i] == '_'):
                    i += 1
                lex = processed[start:i]
                # lookup in keywords_map (case-insensitive)
                mapped = self.keywords_map.get(lex.lower())
                if mapped:
                    # map string name to TokenType if possible
                    try:
                        tok_type = TokenType[mapped]
                    except Exception:
                        tok_type = TokenType.KEYWORD
                else:
                    tok_type = TokenType.IDENTIFIER
                add(tok_type, lex, token_line, token_col)
                col += i - start
                continue

            # number (simple)
            if c.isdigit():
                start = i
                while i < length and processed[i].isdigit():
                    i += 1
                if i < length and processed[i] == '.':
                    i += 1
                    while i < length and processed[i].isdigit():
                        i += 1
                lex = processed[start:i]
                add(TokenType.NUMBER, lex, token_line, token_col)
                col += i - start
                continue

            # string literal
            if c == '"':
                start = i
                i += 1; col += 1
                sb = ['"']
                while i < length:
                    cc = processed[i]
                    sb.append(cc)
                    i += 1; col += 1
                    if cc == '\\':
                        if i < length:
                            sb.append(processed[i]); i += 1; col += 1
                        continue
                    if cc == '"':
                        break
                    if cc == '\n':
                        line += 1; col = 1
                lex = ''.join(sb)
                add(TokenType.STRING, lex, token_line, token_col)
                continue

            # char literal
            if c == "'":
                sb = ["'"]
                i += 1; col += 1
                while i < length:
                    cc = processed[i]
                    sb.append(cc)
                    i += 1; col += 1
                    if cc == '\\':
                        if i < length:
                            sb.append(processed[i]); i += 1; col += 1
                        continue
                    if cc == "'":
                        break
                    if cc == '\n':
                        line += 1; col = 1
                lex = ''.join(sb)
                add(TokenType.CHAR, lex, token_line, token_col)
                continue

            # two-char operators
            two = processed[i:i+2]
            if two in {'==','!=','<=','>=','++','--','&&','||','+=','-=','*=','/=','%=' ,'<<','>>','->'}:
                add(TokenType.OPERATOR, two, token_line, token_col)
                i += 2; col += 2; continue

            # single char operators / separators
            singles = set('+ - * / % = < > ! & | ^ ~ ; , . ( ) { } [ ] :'.split())
            one = c
            if one in singles:
                tok_type = TokenType.SEPARATOR if one in {';','(',',',')','{','}','[',']',':','.'} else TokenType.OPERATOR
                add(tok_type, one, token_line, token_col)
                i += 1; col += 1; continue

            # unknown
            add(TokenType.UNKNOWN, c, token_line, token_col)
            i += 1; col += 1

        return tokens
