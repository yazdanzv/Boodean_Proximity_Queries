from preprocessing import PreProcess
from building_inverted_index import Inverted_Index_Builder
a = PreProcess()
b = Inverted_Index_Builder(a.tokens)
b.build()
print(b.inverted_index)
