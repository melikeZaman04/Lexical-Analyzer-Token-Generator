import tkinter as tk
from tkinter import ttk, messagebox
from .tokenizer import Tokenizer
from .token import TokenType
from .keywords import load_keywords


class LexerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lexical Analyzer - DFA (Python)')
        self.geometry('1000x600')

        self.left = tk.Text(self, wrap='none', font=('Consolas', 11))
        self.left.insert('1.0', self.sample())
        self.left.pack(side='left', fill='both', expand=True)

        frame = tk.Frame(self)
        frame.pack(side='right', fill='both', expand=False)

        cols = ('Lexeme','Token','Line','Column')
        self.tree = ttk.Treeview(frame, columns=cols, show='headings', height=25)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=120 if c=='Lexeme' else 80)
        self.tree.pack(fill='both', expand=True)

        btn = tk.Button(frame, text='Tokenize', command=self.on_tokenize)
        btn.pack(fill='x')

        self.keywords = load_keywords()
        self.tokenizer = Tokenizer(self.keywords)
        # status label to show number of loaded keywords (helps debugging when keywords file not found)
        self.status = tk.Label(frame, text=f'Keywords loaded: {len(self.keywords)}')
        self.status.pack(fill='x')

    def on_tokenize(self):
        src = self.left.get('1.0', 'end')
        try:
            tokens = self.tokenizer.tokenize(src)
            for i in self.tree.get_children():
                self.tree.delete(i)
            for t in tokens:
                self.tree.insert('', 'end', values=(t.lexeme, t.type.name, t.line, t.column))
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def sample(self):
        return ('#define PI 3.14\n'
                '// sample code\n'
                'public class Test {\n'
                '    /* block comment */\n'
                '    public static void main(String[] args) {\n'
                '        double r = 10;\n'
                '        double area = PI * r * r; // area\n'
                '        System.out.println("Area: " + area);\n'
                '    }\n'
                '}\n')


def main():
    app = LexerGUI()
    app.mainloop()


if __name__ == '__main__':
    main()
