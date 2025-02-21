**Data Loading:** 
Load the financial dataset (CSV format) containing financial terminologies and values.

**Text Preprocessing:** 
Convert the dataset into a textual format for processing.

**Ontology Extraction:** 
Use Named Entity Recognition (NER) to classify entities (e.g., ORG, CARDINAL, DATE).

**Triple Extraction:** Utilize Text2KGBench’s gen_prompt.py for automatic extraction.
 
  If the automatic extraction fails, use a fallback method (hidden_extraction.py).
  
**Knowledge Graph Construction:** Construct a directed graph where nodes represent entities and edges represent relationships.

**Visualization:** Render the Knowledge Graph for better interpretation.
