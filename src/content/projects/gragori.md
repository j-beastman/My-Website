---
title: GRAGORI
tag: GenAI · Knowledge graph · Neo4j
summary: My own take on RFP Monster, swapping the vector database for a knowledge graph built from product documentation.
order: 2
---

GRAGORI is my own iteration of the RFP Monster bot. The idea was to replace the vector database behind RFP Monster with a knowledge graph, built in Neo4j from the product's documentation, and answer questions by querying that graph.

A vector database treats documentation as loose chunks of text. Product docs aren't loose, though: features, settings, errors and fixes all point at each other. A graph keeps those connections. Researchers at LinkedIn ran into the same problem with customer support tickets:

> "The conventional retrieval methods in retrieval-augmented generation (RAG) for large language models (LLMs) treat a large corpus of past issue tracking tickets as plain text, ignoring the crucial intra-issue structure and inter-issue relations, which limits performance."
>
> — Xu et al., [*Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering*](https://arxiv.org/abs/2404.17723), SIGIR 2024

Their knowledge-graph approach beat the plain-text baseline by 77.6% in MRR (a retrieval metric) and cut the median time to resolve an issue by 28.6% once deployed.
