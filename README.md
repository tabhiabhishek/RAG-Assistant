<p align="center">
  <img src="docs/images/banner.svg" alt="Local RAG Assistant" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-LCEL-1C3C3C?logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/Ollama-llama3.2-000000?logo=ollama&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/ChromaDB-vector%20store-FF6F61" alt="ChromaDB">
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
</p>

# 🖥️ Local RAG Document Assistant

A 100% local, private, and free Retrieval-Augmented Generation (RAG) application. Upload any PDF and ask questions about its contents without sending your data to external APIs.

<p align="center">
  <img src="docs/images/preview.svg" alt="Local RAG Assistant UI preview" width="100%">
  <br>
  <sub>Upload a PDF, ask in plain English, and get an answer from a local llama3.2 model with the exact source pages it used.</sub>
</p>

## ✨ Key Features
- **100% Local & Private:** No API keys, no data leaves your machine.
- **Modern LangChain Architecture:** Built using LangChain Expression Language (LCEL) for clean, modular, and production-ready code.
- **Dual Local AI Stack:** 
  - **Embeddings:** `nomic-embed-text` via Ollama for lightning-fast vectorization.
  - **Generation:** `llama3.2` via Ollama for intelligent, context-aware answers.
- **Source Tracking:** Displays the exact PDF chunks and page numbers used to generate the answer, ensuring transparency and reducing AI hallucinations.

## ⚙️ How It Works

<p align="center">
  <img src="docs/images/architecture.svg" alt="How Local RAG Assistant works" width="100%">
</p>

## 🛠️ Tech Stack
- **Python 3.11+**
- **LangChain** (Core, Community, Text Splitters)
- **Ollama** (Local LLM & Embedding inference)
- **ChromaDB** (Local Vector Database)
- **Streamlit** (Interactive Web UI)

## 🚀 Getting Started

### Prerequisites
1. Install [Ollama](https://ollama.com/download) on your machine.
2. Pull the required local models via your terminal: