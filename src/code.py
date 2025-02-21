import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import subprocess
import os
import sys
import importlib.util
import spacy
from collections import Counter

# Clone Text2KGBench Repository
repo_path = '/content/Text2KGBench'
if not os.path.exists(repo_path):
    subprocess.run(['git', 'clone', 'https://github.com/cenguix/Text2KGBench.git', repo_path])
os.chdir(repo_path)
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
subprocess.run(['pip', 'install', 'spacy'])
subprocess.run(['python', '-m', 'spacy', 'download', 'en_core_web_sm'])

# Add repository to Python path
sys.path.append(repo_path)

# Attempt to use gen_prompt.py for extracting triples
prompt_script = os.path.join(repo_path, 'src/baselines/gen_prompt.py')
config_path = os.path.join(repo_path, 'src/baselines/prompt_gen_config.json')
triples = []

# Ensure config file exists
if not os.path.exists(config_path):
    config_content = '{"dataset": "financial", "extraction_mode": "rule_based", "num_samples": 100}'
    with open(config_path, 'w') as config_file:
        config_file.write(config_content)

if os.path.exists(prompt_script):
    subprocess.run(['python', prompt_script, '--prompt_gen_config_path', config_path], capture_output=True, text=True)
else:
    print("Error: gen_prompt.py not found. Manual extraction required.")

# Load Dataset
uploaded_file_path = '/content/mcb-terminologies-values-2020_full.csv'  # Update to handle any uploaded file dynamically
df = pd.read_csv(uploaded_file_path)

# Convert dataset to text
text_data = " ".join(df.astype(str).values.flatten())

# Perform Named Entity Recognition (NER) for Ontology Counts
nlp = spacy.load("en_core_web_sm")
doc = nlp(text_data)
entity_counts = Counter([ent.label_ for ent in doc.ents])

print("\nOntology Counts")
for entity, count in entity_counts.items():
    print(f"{entity}: {count}")

# Dynamically load the hidden extraction module
hidden_extraction_path = os.path.join(repo_path, "hidden_extraction.py")
if os.path.exists(hidden_extraction_path):
    spec = importlib.util.spec_from_file_location("hidden_extraction", hidden_extraction_path)
    hidden_extraction = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_extraction)

    # Extract triples automatically
    if not triples:
        triples = hidden_extraction.extract_triples(df)
else:
    print("Error: Hidden extraction module not found.")
    triples = []

# Print Extracted Triples
print("\nExtracted Triples")
for triple in triples:
    print(triple)

# Construct the Knowledge Graph
G = nx.DiGraph()
for subj, rel, obj in triples:
    G.add_edge(subj, obj, label=rel)  # Relation is now extracted automatically

# Visualize the Knowledge Graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
edges = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges)
plt.title("Knowledge Graph from Text2KGBench")
plt.show()
