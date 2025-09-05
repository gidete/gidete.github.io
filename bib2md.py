from pybtex.plugin import find_plugin
from pybtex.database import parse_file

APA = find_plugin('pybtex.style.formatting', 'apa7')()
MD = find_plugin('pybtex.backends', 'md')()

def bib_to_apa7_md(bibfile):
    bibliography = parse_file(bibfile, 'bibtex')
    formatted_bib = APA.format_bibliography(bibliography)
    return " ".join(entry.text.render(MD) for entry in formatted_bib)


md = bib_to_apa7_md("pubs.bib")
print(md)
