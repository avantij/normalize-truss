import sys
from normalize import NormalizeCSV

data = sys.stdin
test = NormalizeCSV(data)
test.normalize()