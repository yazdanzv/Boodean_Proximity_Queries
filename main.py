from preprocessing import PreProcess
from building_inverted_index import Inverted_Index_Builder
from query import Query

a = PreProcess()  # Get an instance from PreProcess class to do the pre-processing on the documents
b = Inverted_Index_Builder(
    a.tokens_with_elimination)  # Get an instance from Inverted_Index_Builder to build inverted index data structure WITH elimination
b.build_optimized()  # Get the Inverted index optimized version that can held frequency and the index where the term accused
b.build()  # Get the simple inverted index that just held the number of the documents that contains the term we are looking for, and we do not use
c = Inverted_Index_Builder(
    a.tokens_without_elimination)  # Get an instance from Inverted_Index_Builder to build inverted index data structure WITHOUT elimination
c.build_optimized()  # Get the Inverted index optimized version that can held frequency and the index where the term accused
c.build()  # Get the simple inverted index that just held the number of the documents that contains the term we are looking for, and we do not use
print('Results :')
print("******************************************************")
print("Inverted Index with elimination")
print(b.inverted_index_optimized)
print(b.inverted_index)
print("Inverted Index without elimination")
print(c.inverted_index_optimized)
print(c.inverted_index)
print("******************************************************")
#  You can see all the queries that this IR system can handle and it can actually handle two ways of NOT query
q1 = Query('heart AND city', b.inverted_index_optimized, c.inverted_index_optimized, len(a.docs))
q2 = Query('heart OR city', b.inverted_index_optimized, c.inverted_index_optimized, len(a.docs))
q3 = Query('heart NOT city', b.inverted_index_optimized, c.inverted_index_optimized, len(a.docs))  # NOT query type one
q4 = Query('NOT city', b.inverted_index_optimized, c.inverted_index_optimized, len(a.docs))  # NOT query type two
q5 = Query('hear NEAR/3 city', b.inverted_index_optimized, c.inverted_index_optimized, len(a.docs))

