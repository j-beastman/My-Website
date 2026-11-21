---
title: RFP Monster
tag: DataRobot hackathon · 2nd place
summary: A RAG bot that drafts answers to the hundreds of questions in a client RFP, then scores how much to trust each one.
order: 1
cover: ./rfp-monster.gif
coverAlt: RFP Monster demo
---

I worked with [Marshall Krassenstein](https://www.marshallpk.com/) to build out this bot for DataRobot's company-wide hackathon. The goal: help the sales team answer RFPs, which are questionnaires that can run past 200 questions, faster and better.

- **Retrieval-augmented generation:** about 600 pages of platform documentation, security policies and previously answered RFPs are chunked into a vector database (LangChain + FAISS). For each question, the closest chunks go to the LLM as context.
- **Audit model:** we hand-labeled generated answers as correct, hallucinated, or missing from the knowledge base, then trained a classifier to give every new answer a confidence score.
- **Re-querying:** when confidence is low, the app asks the LLM again in different ways.
- **Feedback loop:** new question–answer pairs can be added to the vector database, and feedback retrains the audit model.

It took 2nd place, was presented at the company's [Fall launch](https://www.youtube.com/watch?v=Wf0iF5akLOA), and was later featured in [Wired](https://www.wired.com/story/generative-ai-chatgpt-is-coming-for-sales-jobs/).

Please read the full post here: [marshallpk.com/project/rfp-monster](https://www.marshallpk.com/project/rfp-monster/)

## RAG at NERA

I've since implemented RAG in my current work at NERA. Researchers, consultants and managing directors can query our project folders to find relevant analyst commentary across hundreds of embedded analyst reports, build citations, pull figures from SEC filings, and more!
