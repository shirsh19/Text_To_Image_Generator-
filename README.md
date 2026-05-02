---

## 📌 Key Features

*   **GCP Integration:** Uses Google Cloud keys to authenticate and authorize AI generation requests.
*   **Prompt Engineering:** Optimized for sending descriptive text to Gemini for high-fidelity visual output.
*   **VS Code Optimized:** Tailored for a lightweight, efficient development workflow in Visual Studio Code.

---

## ⚙️ How to Reproduce

*   **Step 1: Clone the Repository**
    ```bash
    git clone [https://github.com/shirsh19/Text_To_Image_Generator-](https://github.com/shirsh19/Text_To_Image_Generator-)
    ```
*   **Step 2: Environment Setup**
    *   Create a virtual environment and install `requirements.txt`.
*   **Step 3: GCP Authentication**
    *   Place your **GCP API Key** or **Service Account JSON** in the root directory (ensure it's listed in `.gitignore`).
*   **Step 4: Execute**
    ```bash
Based on your repository structure and the fact that you are using **GCP** with **VS Code**, this YAML error is likely occurring in a configuration file like `app.yaml`, `cloudbuild.yaml`, or a `.github/workflows` file.

The error `did not find expected alphabetic or numeric character while scanning an alias` usually happens because YAML interprets an asterisk (`*`) or an ampersand (`&`) as a special character (an alias or an anchor) rather than a string.

### 🛠️ Common Fixes for this Error

*   **Wrap values in quotes:** If you have a line like `password: *something` or `pattern: *.py`, YAML thinks `*` is the start of an alias. Change it to:
    ```yaml
    pattern: "*.py" 
    ```
*   **Check for invalid characters:** Ensure there are no hidden special characters or incorrect indentation at line 3.
*   **GCP Keys in YAML:** If you are pasting a GCP service account key or API key directly into a YAML file (which is not recommended), ensure the entire block is properly indented and quoted if it contains special characters.

---

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

*   **Cloud-First AI:** Connects Google’s Generative AI models to a local development environment in VS Code.
*   **Scalable Architecture:** Designed for prompt-to-image workflows using cloud-based inference.

---

## 🛠️ Tech Stack

*   **Development Environment:** `VS Code`
*   **Cloud Platform:** `Google Cloud Platform (GCP)`
*   **AI Model:** `Gemini API` (for text-to-image generation)
*   **Language:** `Python`

---

## 📂 Repository Structure
```text
cc_pbl/
├── main.py             # Core script for API calls and logic
├── gcp_config.py       # GCP authentication and key management
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
