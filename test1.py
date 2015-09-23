from plasTeX.Renderers.MediaWiki import MediaWikiRenderer as Renderer
from plasTeX.TeX import TeX
# Instantiate a TeX processor and parse the input text
tex = TeX()
tex.ownerDocument.config['files']['split-level'] = -100
tex.ownerDocument.config['files']['filename'] = 'text.xml'
tex.input(r'''
\documentclass{book}
\begin{document}

\textbf{tutto bene}

ciao

\emph{ciao}

\textit{ciao corsivo}

\begin{equation}
x = 2t
\end{equation}
\end{document}''')

document = tex.parse()
renderer = Renderer()
renderer.render(document)

 
