# A Multipurpose Python Application(Newstok Ml & NewsScraping)

This readme file provides instructions for setting up, running, and testing a Python application with various functionalities.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setting Up](#setting-up)
  - [Virtual Environment Setup](#virtual-environment-setup)
    - [Creating a Virtual Environment](#creating-a-virtual-environment)
    - [Activating the Virtual Environment](#activating-the-virtual-environment)
    - [Deactivating the Virtual Environment](#deactivating-the-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
  - [Setting Up Environment Variables](#setting-up-environment-variables)
- [Running the Application](#running-the-application)
- [API Testing](#api-testing)
  - [Text-to-Image Generation](#text-to-image-generation)
  - [Fake News Classification](#fake-news-classification)
  - [News Summarization](#news-summarization)
  - [News Scraping](#news-scraping)

---

## Features

This application provides a variety of functionalities designed to handle different tasks, including machine learning, text processing, and web scraping. Below are the key features:

- **Text-to-Image Generation:** Converts a text prompt into a generated image using advanced machine learning models.
- **News Summarization:** Summarizes lengthy news articles into concise summaries, making it easier to digest large amounts of information.
- **News Scraping:** Fetches and processes news articles from various sources, both in Bengali and English, based on specified categories.

## Prerequisites

* **Python 3.12.4 or higher:** Ensure you have Python 3.12.4 or a later version installed. You can verify this by running `python --version` in your terminal.

## Setting Up

1. **Activate a virtual environment:** It's recommended to activate a virtual environment to isolate project dependencies.

## Virtual Environment Setup

Using a virtual environment helps to manage dependencies and keep your project isolated from system-wide packages. Below are the instructions for setting up, activating, and deactivating a virtual environment.

### Creating a Virtual Environment

1. **Navigate to Your Project Directory:**
   Open your terminal and navigate to the root directory of your project.

2. **Create the Virtual Environment:**

   - On **Windows**:
     ```bash
     python -m venv env
     ```
   - On **macOS/Linux**:
     ```bash
     python3 -m venv env
     ```

   This will create a directory named `env` in your project directory containing the virtual environment.

### Activating the Virtual Environment

- **Windows**:
  ```bash
  .\env\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source env/bin/activate
  ```

Once activated, your terminal will show the name of the virtual environment (e.g., `(env)`) before the prompt, indicating that you’re now working inside the virtual environment.

### Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return your terminal to its normal state, and your system-wide Python interpreter will be used again.

## Installing Dependencies

After activating your virtual environment, run the following command in your terminal to install the required packages:

```bash
pip install --user Flask selenium webdriver_manager google google-generativeai Pillow transformers tensorflow
```

or

```bash
pip install -r requirements.txt
```

This will install all the dependencies listed in the `requirements.txt` file into your virtual environment.

## Setting Up Environment Variables

To securely manage API keys and other sensitive information, you'll need to set up environment variables using a `.env` file. 

1. **Create a `.env` file:**
   - Rename the provided `.env.example` file to `.env`.

2. **Add your API keys:**
   - Open the `.env` file and fill in the following variables with your corresponding API keys:
     ```bash
     AUTH_API_KEY=your_auth_api_key
     HUGGINGFACE_API_KEY=your_huggingface_api_key
     GEMINI_API_KEY=your_gemini_api_key
     ```

These keys are necessary for the application to interact with external APIs.

## Running the Application

1. Navigate to your project directory in the terminal.
2. Run the application using:

```bash
python app.py
```

This will start the Flask application.

## API Testing

The application offers several functionalities accessible through API endpoints:

### 1. Text-to-Image Generation

* **Endpoint:** `http://127.0.0.1:5000/ml/generate-image`
* **Request Method:** POST
* **Body (JSON):**

```json
{
  "prompt": "a man walking in the fire animated"
}
```

This endpoint generates an image based on a provided text prompt.


### 2.News Summarization

* **Endpoint:** `http://127.0.0.1:5000/ml/process-data`
* **Request Method:** POST
* **Body (JSON):**

```json
{
    "input_text": "He downplayed. He denied. He dismissed.President Biden’s first television interview since his poor debate performance last week was billed as a prime-time opportunity to reassure the American people that he still has what it takes to run for, win and hold the nation’s highest office..."
}
```

This endpoint summarizes a provided news article.

### 3. News Scraping

The application offers endpoints for scraping news articles:

* **Bangla News:**
    * **Endpoint:** `http://127.0.0.1:5000/scraping/scrape_bangla_news?topic=science-technology`
    * **Query Parameter:** `News category(topic)` (bangladesh,world,sports,science-technology,lifestyle,exception)
  
* **English News:**
    * **Endpoint:** `http://127.0.0.1:5000/scraping/scrape_english_news?topic=business-economy`
    * **Query Parameter:** `News category(topic)` (business-economy,city,front-page,back-page,entertainment,national,sports)

These endpoints retrieve news articles on a specific topic in the chosen language.
