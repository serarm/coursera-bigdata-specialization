
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        if not word[0].isdigit():
            c=0
            if word[0].isupper() and len(word)>1 and word[1:]==word[1:].lower():
                c=1
            print >> sys.stderr, "reporter:counter:Wiki stats,Total words,%d" % 1
            print "%s\t%d" % (word.lower(), str(c)+":1")