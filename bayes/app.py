import re
from collections import Counter

class TextFileParser:
  def get_line(self, filepath):
    with open(filepath, 'r') as f:
      for line in f:
        yield line.rstrip()

  def normalize(line):
    return line.lower().

  def stripNonAlphaNum(text):
    return re.compile(r'\W+', re.UNICODE).split(text)

  def entropy(string):
    p, lns = Counter(string), float(len(string))
    return -sum( count/lns * math.log(count/lns, 2) for count in p.values() )







