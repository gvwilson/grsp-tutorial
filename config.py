# Tutorial data.
title = "Growing a Research Software Project"
subtitle = ""
repo = "https://github.com/gvwilson/grsp-tutorial"
release = "https://github.com/gvwilson/grsp-tutorial/raw/main/grsp-tutorial.zip"
plausible = "gvwilson.github.io/grsp-tutorial"
author = {
    "name": "Greg Wilson",
    "email": "gvwilson@third-bit.com",
}

# Theme information.
theme = "tut"
src_dir = "pages"
out_dir = "docs"
rouge_style = "github.css"
lang = "en"
extension = "/"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}


if __name__ == "__main__":
    import sys
    USAGE = "usage: config.py [lang]"
    status = 0
    if len(sys.argv) == 1:
        print(USAGE, file=sys.stderr)
    elif len(sys.argv) != 2:
        print(USAGE, file=sys.stderr)
        status = 1
    elif sys.argv[1] == "lang":
        print(lang)
    else:
        print(USAGE, file=sys.stderr)
        status = 1
    sys.exit(status)
