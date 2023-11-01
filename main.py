from preprocessing import PreProcess
from building_inverted_index import Inverted_Index_Builder

a = PreProcess()
b = Inverted_Index_Builder(a.tokens_with_elimination)
b.build_optimized()
b.build()
c = Inverted_Index_Builder(a.tokens_without_elimination)
c.build_optimized()
c.build()
print("Inverted Index with elimination")
print(b.inverted_index_optimized)
print(b.inverted_index)
print("Inverted Index without elimination")
print(c.inverted_index_optimized)
print(c.inverted_index)
