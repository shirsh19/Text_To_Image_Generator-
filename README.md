# 🖼️ Text to Image Generator (Backend)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![GCP](https://img.shields.io/badge/GCP-%234285F4.svg?style=flat&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![VS Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Gemini](https://img.shields.io/badge/Gemini-Pro-8E75B2.svg)](https://ai.google.dev/)

> **A backend system developed in VS Code that leverages Google Cloud Platform (GCP) and the Gemini API to transform text prompts into AI-generated imagery.**

## 📑 Table of Contents
- [🎯 Project Purpose](#-project-purpose)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Repository Structure](#-repository-structure)
- [📌 Key Features](#-key-features)
- [⚙️ How to Reproduce](#️-how-to-reproduce)

---

## 🎯 Project Purpose

This repository focuses on an automated image generation pipeline. By utilizing **GCP** infrastructure, the system performs complex generative tasks without requiring heavy local resources.

- **Cloud-First AI:** Connects Google’s Generative AI models to a local development environment in VS Code.
- **Scalable Architecture:** Designed for prompt-to-image workflows using cloud-based inference.

---

## 🛠️ Tech Stack

- **Development Environment:** `VS Code`
- **Cloud Platform:** `Google Cloud Platform (GCP)`
- **AI Model:** `Gemini API` (for text-to-image generation)
- **Language:** `Python`

---

## 📂 Repository Structure
```text
cc_pbl/
├── main.py             # Core script for API calls and logic
├── gcp_config.py       # GCP authentication and key management
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
