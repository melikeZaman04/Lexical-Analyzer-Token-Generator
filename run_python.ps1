try {
    python -c "import py_lexer.gui as g; g.main()"
} catch {
    Write-Error "Failed to run GUI. Make sure Python is installed and available on PATH."
}
