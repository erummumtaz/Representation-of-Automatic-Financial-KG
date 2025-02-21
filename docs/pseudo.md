BEGIN
    Load financial dataset (CSV file)
    Convert dataset into text format
    Perform Named Entity Recognition (NER) for ontology extraction
    
    IF Text2KGBench's extraction script exists THEN
        Run 'gen_prompt.py' for automatic triple extraction
    ELSE
        Use fallback method (hidden_extraction.py) to extract triples
    ENDIF
    
    Construct Knowledge Graph:
        FOR each extracted triple (subject, relation, object)
            Add subject and object as nodes
            Add relation as an edge
        ENDFOR
    
    Display ontology counts
    Visualize Knowledge Graph
END
