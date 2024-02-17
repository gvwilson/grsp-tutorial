"""Generate bibliography."""

import ark
from pathlib import Path
from pybtex.database import parse_file
from pybtex.plugin import find_plugin
import shortcodes
import util


@shortcodes.register("b")
def bibliography_ref(pargs, kwargs, node):
    """Handle [%b key1 key2 %] biblography reference shortcodes."""
    util.require(
        (len(pargs) > 0) and (not kwargs),
        f"Bad 'b' shortcode in {node} with {pargs} and {kwargs}",
    )
    base = "@root/bib"
    links = [f'<a class="bib-ref" href="{base}/#{k}">{k}</a>' for k in pargs]
    links = ", ".join(links)
    return f'<span class="bib-ref">[{links}]</span>'


@shortcodes.register("bibliography")
def bibliography(pargs, kwargs, node):
    """Convert bibliography to HTML."""
    def _format(key, body):
        return f'<dt id="{key}" class="bib-def">{key}</dt>\n<dd>{body}</dd>'

    util.require(
        (not pargs) and (not kwargs),
        f"Bad 'bibliography' shortcode in {node} with {pargs} and {kwargs}",
    )

    stylename = ark.site.config.get("bibstyle", None)
    util.require(stylename is not None, "No bibliography style specified (use 'bibstyle')")

    bib = _style_bibliography(stylename)
    html = find_plugin("pybtex.backends", "html")()
    entries = [_format(entry.key, entry.text.render(html)) for entry in bib]
    return '<dl class="bib-list">\n\n' + "\n\n".join(entries) + "\n\n</dl>"


def _style_bibliography(style):
    """Load the bibliography file."""
    filename = Path(ark.site.home(), "info", "bibliography.bib")
    bib = parse_file(filename)
    style = find_plugin("pybtex.style.formatting", style)()
    return style.format_bibliography(bib)
