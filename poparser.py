keywords = ['#', '#:', '#.', '#,', '#|', 'msgid', 'msgstr']

types = {
  '#': 'TRANSLATOR_COMMENT',
  '#:': 'REFERENCE',
  '#.': 'EXTRACTED_COMMENT',
  '#,': 'FLAG',
  '#|': 'PREV_UNTRANSLATED_STRING',
  'msgid': 'MSG_ID',
  'msgstr': 'MSG_STR'
}
f = None
filePos = None
def open_file(filename):
  global f, filePos
  f =  open(filename, 'r')
  filePos = f.tell()  

def extract_multiline(words):
  next_line()
  s = " ".join(words[1:]).strip('"')
  while has_line():
    line = peek_line()
    if(line and line[0] == '"'):
      s += line.strip('"')
      next_line()
    else: break
  return (types[words[0]], s)

def extract_line(words):
  next_line()
  return (types[words[0]], " ".join(words[1:]).strip('"'))

def next_line():
  return f.readline()

def peek_line():
  filePos = f.tell()
  l = next_line()
  f.seek(filePos)
  return l;

def has_line():
  return peek_line() != ""

def parse(filename):
  open_file(filename)
  symbols = []
  data = []
  while has_line():
    line = peek_line()
    words = line.split()
    if len(words):
      key = words[0]
      if key in keywords:
        if(key in ['msgid', 'msgstr']):
          symbols.append(extract_multiline(words))
          if key == 'msgstr':
            data.append(symbols)
            symbols = []
        else:
          symbols.append(extract_line(words))
      else:
        print 'Unknown keyword ' + key
        next_line()
    else: next_line()
  return data

