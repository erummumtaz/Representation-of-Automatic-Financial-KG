# Materials & Methods
# Computing Infrastructure
### Google Colab Environment:

**Python Version**: 3.9+

**GPU Settings:** NVIDIA A100 GPU

**TPU Settings:** Not utilized

**Text2KGBench Version:** Latest commit from the main branch (https://github.com/cenguix/Text2KGBench)

**Operating System:** Linux (Google Colab backend)

**RAM:** Approximately 32 GB (depending on Colab runtime)

**Other Hardware Info:** Colab Pro+ runtime with high-RAM GPU environment.

### Local System:

**Operating System:** Windows 11

**CPU:** To be specified (e.g., Intel i5,i7, AMD Ryzen)

**RAM:** To be specified (e.g., 16 GB)

**GPU:** no GPU's Specifically with the local system.

**Python Version:** 3.9+

**Text2KGBench Version:** Latest commit from the main branch (https://github.com/cenguix/Text2KGBench)

**Other Hardware Info:** None provided

## 3rd Party Dataset:
  - No external third-party dataset with DOI/URL was used.
  - The dataset used in this study (data.csv) is curated and provided directly within this repository under the data/ folder.
  - This dataset includes financial terminologies and values for knowledge graph extraction and analysis.

## Selection Method:

We selected the Text2KGBench framework based on its ability to handle complex financial text, its support for prompt-based triple extraction, and its compatibility with modern NLP models. Compared to other methods, Text2KGBench provides a scalable solution with minimal manual intervention for financial knowledge graph generation.

## Library Versions
The following library versions were used in this project, reflecting the latest stable releases as of **February–March 2024**:
- **pandas**: 1.5.3
- **networkx**: 3.2.1
- **matplotlib**: 3.7.1
- **spacy**: 3.5.0
- **text2kgbench**: 0.1.0 (probably initial release)

These versions were selected to ensure consistency and reproducibility of results during the experimental phase.

## GPU and TPU Considerations:

### GPU Settings in Google Colab:

#### Google Colab GPU Configuration:

- The project utilized NVIDIA A100 GPU within the Google Colab Pro environment. No additional manual configurations or optimizations (such as mixed precision training, batch size tuning, or memory management) were required due to the lightweight nature of the triple extraction tasks performed by Text2KGBench.
  
- The default Colab GPU environment was sufficient to handle financial data processing efficiently, with no notable need for further GPU parameter adjustments.

### TPU Usage Explanation:

#### TPUs Not Utilized:
- TPUs (Tensor Processing Units) were not considered in this project because Text2KGBench and its associated libraries (such as spaCy and networkx) are not optimized for TPU acceleration.
  
- TPUs are primarily designed to accelerate large-scale deep learning model training, whereas Text2KGBench focuses on text processing and rule-based extraction, which benefit more from CPUs and GPUs for their flexibility with diverse libraries.

#### Potential Impact of TPU Usage:

If TPUs were employed, there might be limited performance gains due to incompatibility with some core Python libraries, and additional effort would be required to adapt the codebase, with uncertain benefits for the types of computations involved in this study.

