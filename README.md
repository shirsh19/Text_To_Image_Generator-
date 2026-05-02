---

## 📌 Key Features

* **Cloud-Native Generation:** Offloads the heavy lifting of image creation to GCP, ensuring fast results regardless of your local hardware.
* **API Key Management:** Securely handles GCP/Gemini credentials to authenticate requests.
* **VS Code Optimized:** Includes configuration files for a seamless "Plug and Play" experience in Visual Studio Code.
* **High-Fidelity Output:** Leverages the latest Gemini models for high-quality, prompt-accurate visuals.

---

## ⚙️ How to Reproduce

Follow these steps to set up the environment and run the generator:

* **Step 1: Clone the Repository**
    ```bash
    git clone [https://github.com/shirsh19/Text_To_Image_Generator-](https://github.com/shirsh19/Text_To_Image_Generator-)
    cd Text_To_Image_Generator-
    ```

* **Step 2: Set Up Virtual Environment**
    ```bash
    python -m venv venv
    # Activate on Windows:
    .\venv\Scripts\activate
    # Activate on Mac/Linux:
    source venv/bin/activate
    ```

* **Step 3: Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

* **Step 4: Configure GCP Key**
  1. Obtain your key from the **Google Cloud Console** or **Google AI Studio**.
  2. Create a `.env` file in the root directory.
  3. Add your key:
     ```ini
     GCP_API_KEY=your_key_here
     ```

* **Step 5: Run the Script**
    ```bash
    python main.py
    ```

---
*If you find this project usefulMy mistake—I'll strip out the Flutter and AWS references entirely and pivot the focus to a pure **GCP-integrated backend** managed in **VS Code**. 

Since you're using a key from Google Cloud but aren't certain which one, it is highly likely the **Gemini API Key** (managed via Google AI Studio/Vertex AI) or a **Service Account Key** for cloud storage or vision tasks. I've updated the setup to reflect that ambiguity.

---

# 🖼️ Text to Image Generator (Backend)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![GCP](https://img.shields.io/badge/GCP-%234285F4.svg?style=flat&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![VS Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Gemini](https://img.shields.io/badge/Gemini-Pro-8E75B2.svg)](https://ai.google.dev/)

> **A robust backend system developed in VS Code that leverages Google Cloud Platform (GCP) and Gemini models to transform text descriptions into AI-generated imagery.**

## 📑 Table of Contents
- [🎯 Project Purpose](#-project-purpose)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Repository Structure](#-repository-structure)
- [📌 Key Features](#-key-features)
- [⚙️ How to Reproduce](#️-how-to-reproduce)

---

## 🎯 Project Purpose

This repository contains the logic for an automated image generation pipeline. By utilizing Google Cloud's infrastructure, the system can handle complex generative tasks that would typically require heavy local GPU resources.

* **Effortless Integration:** Seamlessly connects Google’s Generative AI with a local development environment.
* **Scalable AI:** Built to handle prompt-to-image workflows using cloud-based inference.

---

## 🛠️ Tech Stack

This project is built using a streamlined Python environment optimized for cloud service interaction.

* **Development Environment:** `VS Code`
* **Cloud Platform:** `Google Cloud Platform (GCP)`
* **AI Model:** `Gemini API` (for text processing and image generation)
* **Language:** `Python`

---

## 📂 Repository Structure
```text
cc_pbl/
├── main.py             # Core script for API calls and logic
├── gcp_config.py       # Configuration for GCP authentication
├── requirements.txt    # Necessary Python libraries
├── .env.example        # Template for your GCP/Gemini keys
└── README.md           # Project documentation
