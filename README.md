##  `app.py` - A Multipurpose Python Application

This readme file provides instructions for setting up, running, and testing a Python application with various functionalities.

### Prerequisites

* **Python 3.12 or higher:** Ensure you have Python 3.12 or a later version installed. You can verify this by running `python --version` in your terminal.

### Setting Up

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

--- 

3. **Install dependencies:** After activating your virtual environment, run the following command in your terminal to install the required packages:

```bash
pip install --user Flask selenium webdriver_manager google google-generative Pillow transformers tensorflow
```
or 

```bash
pip install -r requirements.txt
```

This will install all the dependencies listed in the `requirements.txt` file into your virtual environment.

### Running the Application

1. Navigate to your project directory in the terminal.
2. Run the application using:

```bash
python app.py
```

This will start the Flask application.

### API Testing

The application offers several functionalities accessible through API endpoints:

**1. Text-to-Image Generation:**

* **Endpoint:** `http://127.0.0.1:5000/ml/generate-image`
* **Request Method:** POST
* **Body (JSON):**

```json
{
  "prompt": "a man walking in the fire animated"
}
```

This endpoint generates an image based on a provided text prompt.

**2. Fake News Classification:**

* **Endpoint:** `http://127.0.0.1:5000/ml/classify`
* **Request Method:** POST
* **Body (JSON):**

```json
{
  "text": "In 2016, a story circulated that Pope Francis made an unprecedented and shocking endorsement of Donald Trump for president"
}
```

This endpoint classifies a text snippet as real or fake news.

**3. News Summarization:**

* **Endpoint:** `http://127.0.0.1:5000/ml/process-data`
* **Request Method:** POST
* **Body (JSON):**

```json
{
    "input_text": "He downplayed. He denied. He dismissed.President Biden’s first television interview since his poor debate performance last week was billed as a prime-time opportunity to reassure the American people that he still has what it takes to run for, win and hold the nation’s highest office.But Mr. Biden, with more than a hint of hoarseness in his voice, spent much of the 22 minutes resisting a range of questions that George Stephanopoulos of ABC News had posed — about his competence, about taking a cognitive test, about his standing in the polls.The president on Friday did not struggle to complete his thoughts the way he did at the debate. But at the same time he was not the smooth-talking senator of his youth, or even the same elder statesman whom the party entrusted four years ago to defeat former President Donald J. Trump.Instead, it was a high-stakes interview with an 81-year-old president whose own party is increasingly doubting him yet who sounded little like a man with any doubts about himself."
}
```

This endpoint summarizes a provided news article.

**4. News Scraping**

The application offers endpoints for scraping news articles:

* **Bangla News:**
    * **Endpoint:** `http://127.0.0.1:5000/scraping/scrape_bangla_news?topic=science-technology`
    * **Query Parameter:** `News category(topic)` (bangladesh,world,sports,science-technology,lifestyle,exception)
  
* **English News:**
    * **Endpoint:** `http://127.0.0.1:5000/scraping/scrape_english_news?topic=business-economy`
    * **Query Parameter:** `News category(topic)` (business-economy,city,front-page,back-page,entertainment,national,sports)

These endpoints retrieve news articles on a specific topic in the chosen language.
