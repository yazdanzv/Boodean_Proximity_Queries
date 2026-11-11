# Boodean_Proximity_Queries

## Code guide

`main.py` runs examples of Boolean, proximity, spelling, and wildcard queries. `preprocessing.py` tokenizes and normalizes the document collection; `building_inverted_index.py` constructs the posting lists; `query.py` evaluates queries; and `miss_spelling.py` and `wild_card.py` handle term expansion. `document_collection_builder.py` generates the sample documents used by the examples. Install the packages in `requirements.txt`, prepare the `Documents/` collection expected by the scripts, and run `python main.py` from the repository root. The scripts contain Windows-style relative paths, so path adjustments may be needed on macOS or Linux.
