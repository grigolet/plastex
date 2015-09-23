import string
from plasTeX.Renderers import Renderer

class MediaWikiRenderer (Renderer):

    outputType = unicode
    fileExtension = '.xml'
    lineWidth = 76

    def __init__(self, *args, **kwargs):
        Renderer.__init__(self, *args, **kwargs)
        
        # Load dictionary with methods
        for key in dir(self):
            if key.startswith('do_'):
                self[key[3:]] = getattr(self, key)

        self['default-layout'] = self['document-layout'] = self.default 
        self.footnotes = []
        self.blocks = []


    def default(self, node):
        s=[]
        s.append('<%s>' % node.nodeName)
        s.append(unicode(node))
        s.append('</%s>' % node.nodeName)
        return u''.join(s)
        


    def do_equation (self, node):
        s=[]
        s.append('<dmath>')
        #child nodes
        s.append(unicode(node))
        #endtah
        s.append('</dmath>')
        return u''.join(s)


    def do_textDefault(self, node):
        return node
        

    def do_document(self,node):
        content = unicode(node)
        return u'%s' % content

    def do_par(self, node):
        s = []
        s.append(u'\n')
        s.append(unicode(node))
        s.append(u'\n')
        return u''.join(s)
        
    def do_textbf(self,node):
        s=[]
        s.append(u"\'\'")
        s.append(unicode(node))
        s.append(u"\'\'")
        return u''.join(s)
        
    def do_textit(self,node):
        s=[]
        s.append(u"\'\'\'")
        s.append(unicode(node))
        s.append(u"\'\'\'")
        return u''.join(s)    

    do_emph = do_textbf
      
      