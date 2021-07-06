# Text summarization

We explored two types of summarization: **abstractive** and **extractive** to derive pros and cons of the both approaches.

## Preparation:
We parsed articles of the **Russian Foreign Economic Bulletin** for the source material in non-ML extractive approaches.
We also used sentence tokinzer tool created by MIPT DeepPavlov Lab.

## Extractive approach:
We started our research with **non-ML approaches** and used Text/LexRank for summarizations.

We relied on the experiences described in the following papers:
- [LexRank: Graph-based Lexical Centrality as Salience in Text Summarization](https://arxiv.org/pdf/1109.2128.pdf)
- [TextRank: Bringing Order into Texts](https://aclanthology.org/W04-3252.pdf)

In terms of **ML-approach** for extractive summarization we used BERTSUM approach:
- [Fine-tune BERT for Extractive Summarization](https://arxiv.org/pdf/1903.10318.pdf)

## Abstractive approach:
Under the condition of the first iteration in RnD we used **PGN-architecture** on the base of AllenNLP framework.
We relied on the experience described in the following paper:
- [Point-less: More Abstractive Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1905.01975.pdf)

## Study perspectives:
Right now we are working on improvement of the study in both fields:
- Extractive approach: LM-tuning for specific domain, domain adaptation
- Abtractive approach: as ROUGE metric is discrete it cannot be optimised, we study RL+ML approach for objective function modelling
