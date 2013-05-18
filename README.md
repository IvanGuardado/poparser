poparser
========

A python parser for [gettext](http://www.gnu.org/software/gettext/manual/gettext.html) catalog files

### How to use
Use the parse() method to get the table of symbols with the grouped data for each msgid

<pre>
import poparser
poparser.parse(filename)
</pre>

### Example
Here you can see what the function outputs for the below gettext file:
<pre>
#
#  <>, 2012.
#
msgid ""
msgstr ""
"Project-Id-Version: Project X\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2013-05-17 19:51+0200\n"
"PO-Revision-Date: 2013-05-10 13:58+0100\n"
"Last-Translator: \n"
"Language-Team: \n"
"Language: es_ES\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"X-Poedit-KeywordsList: _;gettext;gettext_noop;translate\n"
"X-Poedit-Basepath: /path/to/project\n"
"X-Poedit-SourceCharset: UTF-8\n"
"X-Poedit-SearchPath-0: application\n"

# An author comment
#. A comment in code
#: application/foo.php:21
#: application/bar.php:10
#, fuzzy
msgid "Hello wordl!"
msgstr "Hola mundo!"
</pre>

This will output:

<pre>
[[('TRANSLATOR_COMMENT', ''),
  ('TRANSLATOR_COMMENT', '<>, 2012.'),
  ('TRANSLATOR_COMMENT', ''),
  ('MSG_ID', ''),
  ('MSG_STR',
   'Project-Id-Version: Project X\\n"\nReport-Msgid-Bugs-To: \\n"\nPOT-Creation-Date: 2013-05-17 19:51+0200\\n"\nPO-Revision-Date: 2013-05-10 13:58+0100\\n"\nLast-Translator: \\n"\nLanguage-Team: \\n"\nLanguage: es_ES\\n"\nMIME-Version: 1.0\\n"\nContent-Type: text/plain; charset=UTF-8\\n"\nContent-Transfer-Encoding: 8bit\\n"\nX-Poedit-KeywordsList: _;gettext;gettext_noop;translate\\n"\nX-Poedit-Basepath: /path/to/project\\n"\nX-Poedit-SourceCharset: UTF-8\\n"\nX-Poedit-SearchPath-0: application\\n"\n')],
 [('TRANSLATOR_COMMENT', 'An author comment'),
  ('EXTRACTED_COMMENT', 'A comment in code'),
  ('REFERENCE', 'application/foo.php:21'),
  ('REFERENCE', 'application/bar.php:10'),
  ('FLAG', 'fuzzy'),
  ('MSG_ID', 'Hello wordl!'),
  ('MSG_STR', 'Hola mundo!')]]
</pre>

