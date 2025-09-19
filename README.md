# AI-SmartChat

**AI-SmartChat** is an AI research assistant that uses **Google Gemini LLM** with **LangChain tools** to give structured, source-backed insights for efficient and reliable research.

---

## Features

* Gives **structured answers** with references
* **Context-aware** research responses
* Integrates tools like **DuckDuckGo** and **Wikipedia**
* Easy to use via command-line or script

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/codeK2004/AI-SmartChat.git
cd AI-SmartChat
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your API keys in a `.env` file:

```text
GOOGLE_API_KEY=your_google_api_key
GOOGLE_PROJECT_ID=your_project_id
```

---
## Usage

```bash
python main.py
```
* Enter your query
* AI-SmartChat returns structured insights with sources

---
