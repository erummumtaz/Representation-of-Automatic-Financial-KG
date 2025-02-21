# Representation-of-Automatic-Financial-KG
This project utilizes Text2KGBench for extracting structured knowledge from financial reports. Text2KGBench is an existing framework designed to process textual data and convert it into meaningful Knowledge Graphs. Our implementation applies this framework specifically to financial datasets to extract entities, relationships, and ontologies automatically.

## Key Objectives

Apply Text2KGBench to financial reports for structured triple extraction.

### Ontology Identification: 

Utilize Named Entity Recognition (NER) to classify financial terms (e.g., ORG, CARDINAL, MONEY, DATE).

### Triple Generation: 

Extract subject-relation-object triples from financial data.

### Knowledge Graph Construction: 

Convert extracted triples into a structured graph representation.

### Seamless Framework Integration: 

Ensure smooth execution within the Text2KGBench framework without modifying its core algorithms.

## How It Works

### Dataset Preparation: 

The financial dataset is preprocessed and formatted for Text2KGBench.

### Automatic Extraction: 

Text2KGBench’s gen_prompt.py is used for entity and relation extraction.

### Fallback Mechanism: 

If automatic extraction fails, a secondary extraction method (hidden_extraction.py) ensures that triples are generated.

### Ontology Mapping: 

Identified entities are categorized based on financial ontology.

### Knowledge Graph Visualization: 

Extracted triples are used to construct a Knowledge Graph, making financial relationships more interpretable.

This project showcases how Text2KGBench can be leveraged in financial applications to automate the transformation of unstructured financial reports into structured knowledge representations.

Text2KGBench is a framework designed to extract structured knowledge from unstructured textual data, particularly in financial reports. It automates the process of identifying key entities, relationships, and terminologies to construct a Knowledge Graph. By leveraging state-of-the-art Natural Language Processing (NLP) techniques, Text2KGBench transforms raw text into meaningful triples that represent relationships between different financial concepts.

The framework operates in multiple stages, including preprocessing, entity recognition, relation extraction, and graph construction. Using Named Entity Recognition (NER), it identifies important entities such as organizations, monetary values, and dates. The extracted triples (subject, relation, object) are then used to build a Knowledge Graph, which provides a structured representation of the financial domain.

Text2KGBench ensures high accuracy and reliability by utilizing advanced NLP models and rule-based techniques. The framework is flexible and can be adapted to various financial datasets, making it a powerful tool for automated knowledge extraction and decision support systems.

Text2KGBench is a framework designed for automatic extraction of triples and ontologies from textual data, particularly financial reports. The extracted triples are then used to construct a Knowledge Graph.

## 🛠 Installation

- First, install the dependencies:

        pip install -r requirements.txt

## 🚀 Usage

- Run the main script:

    python src/text2kgbench_colab.py
