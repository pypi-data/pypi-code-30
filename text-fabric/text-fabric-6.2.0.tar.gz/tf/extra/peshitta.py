import os
import re
import types

from tf.fabric import Fabric
from tf.apphelpers import (
    search,
    table, plainTuple,
    show, prettyPre, pretty, prettyTuple, prettySetup,
    getData,
    getBoundary, getFeatures,
    htmlEsc, mdEsc,
    dm, dh, header, outLink,
    URL_NB, API_URL
)
from tf.server.common import getConfig
from tf.notebook import location

CSS = '''
<style type="text/css">
.verse {
    display: flex;
    flex-flow: row wrap;
    direction: rtl;
}
.vl {
    display: flex;
    flex-flow: column nowrap;
    justify-content: flex-end;
    align-items: flex-end;
    direction: ltr;
    width: 100%;
}
.outeritem {
    display: flex;
    flex-flow: row wrap;
    direction: rtl;
}
.word {
    padding: 0.1em;
    margin: 0.1em;
    border-radius: 0.1em;
    border: 1px solid #cccccc;
    display: flex;
    flex-flow: column nowrap;
    direction: rtl;
    background-color: #ffffff;
}
.occs {
    font-size: x-small;
}
.sy,.sy a:visited,.sy a:link {
    font-family: "Estrangelo Edessa", sans-serif;
    font-size: large;
    color: #000044;
    direction: rtl;
    text-decoration: none;
}
.syb,.syb a:visited,.syb a:link {
    font-family: "Estrangelo Edessa", sans-serif;
    font-size: large;
    direction: rtl;
    text-decoration: none;
}
.nd {
    font-family: monospace;
    font-size: x-small;
    color: #999999;
}
.features {
    font-family: monospace;
    font-size: medium;
    font-weight: bold;
    color: #0a6611;
    display: flex;
    flex-flow: column nowrap;
    padding: 0.1em;
    margin: 0.1em;
    direction: ltr;
}
.features .f {
    font-family: sans-serif;
    font-size: x-small;
    font-weight: normal;
    color: #5555bb;
}
.word .features div,.word .features span {
    padding: 0;
    margin: -0.1rem 0;
}

.hl {
    background-color: #ffee66;
}
</style>
'''

CSS_FONT = '''
    <link rel="stylesheet" href="/data/static/fonts.css"/>
'''
CSS_FONT_API = '''
    <link
      rel="stylesheet"
      href="https://github.com/Dans-labs/text-fabric/raw/master/tf/extra/peshitta-app/static/fontsweb.css"
    />
'''

CLASS_NAMES = dict(
    verse='verse',
    word='word',
)

SECTION = {'book', 'chapter', 'verse'}
VERSE = {'verse'}

NONE_VALUES = {None, 'NA', 'none', 'unknown'}

STANDARD_FEATURES = '''
    word word_etcbc
    trailer trailer_etcbc
    book book@en
    chapter verse
'''

EXCLUDED_FEATURES = set()

PASSAGE_RE = re.compile('^([A-Za-z0-9_ -]+)\s+([0-9]+)\s*:\s*([0-9]+)$')


class Peshitta(object):
  def __init__(
      self,
      api=None,
      name=None,
      version='0.1',
      locations=None,
      modules=None,
      asApi=False,
      lgc=False,
      hoist=False,
  ):
    config = getConfig('peshitta')
    cfg = config.configure(lgc=lgc, version=version)
    self.asApi = asApi
    self.version = version
    self.docUrl = cfg['docUrl']
    self.condenseType = cfg['condenseType']
    self.peshitta = cfg['peshitta']
    self.exampleSection = (
        f'<code>Genesis 1:1</code> (use'
        f' <a href="https://github.com/{cfg["org"]}/{cfg["repo"]}'
        f'/blob/master/tf/{version}/book%40en.tf" target="_blank">'
        f'English book names</a>)'
    )
    self.exampleSectionText = 'Genesis 1:1'

    self.standardFeatures = set(STANDARD_FEATURES.strip().split())

    if asApi or not api:
      getData(
          cfg['repo'],
          cfg['release'],
          cfg['firstRelease'],
          cfg['url'],
          f'{cfg["org"]}/{cfg["repo"]}/tf',
          version,
          lgc,
      )
      locations = cfg['locations']
      modules = cfg['modules']
      TF = Fabric(locations=locations, modules=modules, silent=True)
      api = TF.load('', silent=True)
      self.api = api
      if api is False:
        return
      allFeatures = TF.explore(silent=True, show=True)
      loadableFeatures = allFeatures['nodes'] + allFeatures['edges']
      useFeatures = [f for f in loadableFeatures if f not in EXCLUDED_FEATURES]
      result = TF.load(useFeatures, add=True, silent=True)
      if result is False:
        self.api = False
        return
    else:
      api.TF.load(self.standardFeatures, add=True, silent=True)
    self.prettyFeaturesLoaded = self.standardFeatures
    self.prettyFeatures = ()
    self.api = api
    self.cwd = os.getcwd()

    if not asApi:
      (inNb, repoLoc) = location(self.cwd, name)
      if inNb:
        (nbDir, nbName, nbExt) = inNb
      if repoLoc:
        (thisOrg, thisRepo, thisPath, nbUrl, ghUrl) = repoLoc
    repo = cfg['repo']
    tutUrl = f'{URL_NB}/{cfg["org"]}/{repo}/blob/master/tutorial/search.ipynb'
    extraUrl = f'https://dans-labs.github.io/text-fabric/Api/Peshitta/'
    dataLink = outLink(
        repo.capitalize(),
        f'{self.docUrl}/about.md',
        'provenance of this corpus',
    )
    featureLink = outLink(
        'Feature docs', self.featureUrl(self.version),
        f'{repo.capitalize()} feature documentation'
    )
    peshittaLink = outLink('Peshitta API', extraUrl, 'Peshitta API documentation')
    tfLink = outLink(
        f'Text-Fabric API {api.TF.version}', API_URL(''),
        'text-fabric-api'
    )
    tfsLink = outLink(
        'Search Reference',
        API_URL('search-templates'),
        'Search Templates Introduction and Reference'
    )
    tutLink = outLink(
        'Search tutorial', tutUrl,
        'Search tutorial in Jupyter Notebook'
    )
    if asApi:
      self.dataLink = dataLink
      self.featureLink = featureLink
      self.tfsLink = tfsLink
      self.tutLink = tutLink
    else:
      if inNb:
        lf = ['book@ll'] + [f for f in api.Fall() if '@' not in f] + api.Eall()
        dm('**Documentation:**' f' {dataLink} {featureLink} {peshittaLink} {tfLink} {tfsLink}')
        dh(
            '<details open><summary><b>Loaded features</b>:</summary>\n'
            +
            ' '.join(
                outLink(feature, self.featureUrl(self.version), title='info')
                for feature in lf
            )
            +
            '</details>'
        )
        if repoLoc:
          dm(
              f'''
This notebook online:
{outLink('NBViewer', f'{nbUrl}/{nbName}{nbExt}')}
{outLink('GitHub', f'{ghUrl}/{nbName}{nbExt}')}
'''
          )

    self.classNames = CLASS_NAMES
    self.noneValues = NONE_VALUES

    if not asApi:
      if inNb:
        self.loadCSS()
      if hoist:
        docs = api.makeAvailableIn(hoist)
        if inNb:
          dh(
              '<details open><summary><b>API members</b>:</summary>\n'
              +
              '<br/>\n'.join(
                  ', '.join(
                      outLink(entry, API_URL(ref), title='doc')
                      for entry in entries
                  )
                  for (ref, entries) in docs
              )
              +
              '</details>'
          )
    self.table = types.MethodType(table, self)
    self.plainTuple = types.MethodType(plainTuple, self)
    self.show = types.MethodType(show, self)
    self.prettyTuple = types.MethodType(prettyTuple, self)
    self.pretty = types.MethodType(pretty, self)
    self.prettySetup = types.MethodType(prettySetup, self)
    self.search = types.MethodType(search, self)
    self.header = types.MethodType(header, self)

  def featureUrl(self, version):
    return f'{self.docUrl}/transcription-{version}.md'

  def loadCSS(self):
    asApi = self.asApi
    if asApi:
      return CSS_FONT + CSS
    dh(CSS_FONT_API + CSS)

  def pshLink(self, n, text=None, className=None, asString=False, noUrl=False):
    api = self.api
    L = api.L
    T = api.T
    F = api.F
    version = self.version
    nType = F.otype.v(n)

    (bookE, chapter, verse) = T.sectionFromNode(n)
    bookNode = n if nType == 'book' else L.u(n, otype='book')[0]
    book = F.book.v(bookNode)
    passageText = (
        bookE if nType == 'book' else '{} {}'.format(bookE, chapter)
        if nType == 'chapter' else '{} {}:{}'.format(bookE, chapter, verse)
    )
    href = '#' if noUrl else self.peshitta.format(
        version=version,
        book=book,
    )
    if text is None:
      text = passageText
      title = 'show this passage in the Peshitta source'
    else:
      title = passageText
    if noUrl:
      title = None
    target = '' if noUrl else None
    result = outLink(text, href, title=title, className=className, target=target)
    if asString:
      return result
    dh(result)

  def webLink(self, n):
    return self.pshLink(n, className='rwh', asString=True, noUrl=True)

  def nodeFromDefaultSection(self, sectionStr):
    api = self.api
    T = api.T
    match = PASSAGE_RE.match(sectionStr)
    if not match:
      return (f'Wrong shape: "{sectionStr}". Must be "book chapter:verse"', None)
    (book, chapter, verse) = match.groups()
    verseNode = T.nodeFromSection((book, int(chapter), int(verse)))
    if verseNode is None:
      return (f'Not a valid verse: "{sectionStr}"', None)
    return ('', verseNode)

  def plain(
      self,
      n,
      linked=True,
      withNodes=False,
      asString=False,
  ):
    asApi = self.asApi
    api = self.api
    L = api.L
    T = api.T
    F = api.F

    nType = F.otype.v(n)
    result = ''
    if asApi:
      nodeRep = f' <a href="#" class="nd">{n}</a> ' if withNodes else ''
    else:
      nodeRep = f' *{n}* ' if withNodes else ''

    syriac = True
    if nType == 'word':
      rep = mdEsc(htmlEsc(T.text([n])))
    elif nType in SECTION:
      fmt = ('{}' if nType == 'book' else '{} {}' if nType == 'chapter' else '{} {}:{}')
      rep = fmt.format(*T.sectionFromNode(n))
      syriac = False
      rep = mdEsc(htmlEsc(rep))
      if nType in VERSE:
        if linked:
          rep = self.pshLink(n, text=rep, asString=True)
        rep += ' <span class="syb">' + T.text(L.d(n, otype="word")) + '</span>'
    else:
      rep = mdEsc(htmlEsc(T.text(L.d(n, otype='word'))))

    if linked and nType not in VERSE:
      rep = self.pshLink(n, text=rep, asString=True)

    if syriac:
      rep = f'<span class="syb">{rep}</span>'
    result = f'{rep}{nodeRep}'

    if asString or asApi:
      return result
    dm((result))

  def _pretty(
      self,
      n,
      outer,
      html,
      firstSlot,
      lastSlot,
      condenseType=None,
      withNodes=True,
      suppress=set(),
      highlights={},
  ):
    goOn = prettyPre(
        self,
        n,
        firstSlot,
        lastSlot,
        withNodes,
        highlights,
    )
    if not goOn:
      return
    (
        slotType, nType,
        className, boundaryClass, hlClass, hlStyle,
        nodePart,
        myStart, myEnd,
    ) = goOn

    api = self.api
    F = api.F
    L = api.L
    T = api.T
    otypeRank = api.otypeRank

    bigType = False
    if condenseType is not None and otypeRank[nType] > otypeRank[condenseType]:
      bigType = True

    if nType == 'book':
      html.append(self.pshLink(n, asString=True))
      return
    if nType == 'chapter':
      html.append(self.pshLink(n, asString=True))
      return

    if bigType:
      children = ()
    elif nType == 'verse':
      (thisFirstSlot, thisLastSlot) = getBoundary(api, n)
      children = L.d(n, otype='word')
    elif nType == slotType:
      children = ()

    doOuter = outer and nType == 'slotType'
    if doOuter:
      html.append('<div class="outeritem">')

    html.append(f'<div class="{className} {boundaryClass}{hlClass}"{hlStyle}>')

    if nType == 'verse':
      passage = self.pshLink(n, asString=True)
      html.append(
          f'''
    <div class="vl">
        <div class="vrs">{passage}</div>
        {nodePart}
    </div>
'''
      )
    else:
      if nodePart:
        html.append(nodePart)

      heading = ''
      featurePart = ''
      occs = ''
      if nType == slotType:
        text = T.text([n])
        heading = f'<div class="sy">{text}</div>'
        featurePart = getFeatures(
            self,
            n,
            suppress,
            ('word_etcbc',),
        )
      html.append(heading)
      html.append(featurePart)
      html.append(occs)

    for ch in children:
      self._pretty(
          ch,
          False,
          html,
          firstSlot,
          lastSlot,
          condenseType=condenseType,
          withNodes=withNodes,
          suppress=suppress,
          highlights=highlights,
      )
    html.append('''
</div>
''')
    if doOuter:
      html.append('</div>')
