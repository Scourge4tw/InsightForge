# 🚀 InsightForge

<p align="center">
  <h3 align="center">Autonomous Multi-Agent Research Platform</h3>
  <p align="center">
    AI-powered research platform that discovers, extracts, synthesizes, and evaluates information from the web using autonomous agents.
  </p>
</p>

---

## 📖 Overview

InsightForge is a multi-agent AI research platform designed to automate the process of gathering and synthesizing information from the internet.

Instead of relying on a single language model, InsightForge uses specialized AI agents that collaborate to perform different stages of research:

- Discover reliable web sources
- Extract detailed webpage content
- Generate structured research reports
- Review and evaluate report quality

The application combines the reasoning capabilities of **Mistral AI** with **LangChain**, **Tavily Search**, and **BeautifulSoup** to create a streamlined, source-backed research workflow.

---

# ✨ Key Features

- 🌐 Intelligent web search using Tavily Search API
- 📄 Automatic webpage content extraction
- 🤖 Multi-agent architecture
- 📝 AI-powered research report generation
- ✅ Automated report quality evaluation
- 🎨 Interactive Streamlit dashboard
- ⚡ Powered by Mistral Small 2506
- 📚 Source-backed research
- 🔍 Real-time information retrieval
- 💾 Download generated reports

---

# 🧠 Multi-Agent Workflow

InsightForge follows a sequential autonomous workflow.

```text
                User
                  │
                  ▼
        Research Topic Input
                  │
                  ▼
     ┌──────────────────────────┐
     │  Discovery Agent         │
     │  Tavily Web Search       │
     └────────────┬─────────────┘
                  │
                  ▼
     ┌──────────────────────────┐
     │ Knowledge Extraction     │
     │ BeautifulSoup Scraper    │
     └────────────┬─────────────┘
                  │
                  ▼
     ┌──────────────────────────┐
     │ Report Generator         │
     │ Mistral AI               │
     └────────────┬─────────────┘
                  │
                  ▼
     ┌──────────────────────────┐
     │ Quality Reviewer         │
     │ Mistral AI               │
     └────────────┬─────────────┘
                  │
                  ▼
         Final Research Report
```

---

# 🛠 Tech Stack

## Programming Language

- Python

## Large Language Model

- Mistral Small 2506

## AI Framework

- LangChain

## Search Engine

- Tavily Search API

## Web Scraping

- BeautifulSoup
- Requests

## Frontend

- Streamlit

## Environment Management

- Python Dotenv

---

# 📂 Project Structure

```text
InsightForge/
│
├── app.py
├── agents.py
├── tools.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── assets/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/InsightForge.git
```

Move into the project directory

```bash
cd InsightForge
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

# ▶️ Running the Application

Launch the application

```bash
streamlit run app.py
```

The application will be available at

```
http://localhost:8501
```

---

# 📊 Workflow Explained

### 1. Discovery

The Discovery Agent searches the web using Tavily Search API to identify the most relevant and trustworthy sources for the requested topic.

---

### 2. Knowledge Extraction

The Knowledge Extraction Agent scrapes the selected webpage using BeautifulSoup and extracts meaningful textual information while removing unnecessary HTML elements.

---

### 3. Report Generation

The Writer module processes all collected information and generates a structured research report including:

- Introduction
- Key Findings
- Conclusion
- Sources

---

### 4. Quality Evaluation

The Review Agent evaluates the generated report by scoring it and providing:

- Strengths
- Weaknesses
- Improvement suggestions
- Overall verdict

---

# 📷 Application Preview

Add screenshots here.

Example:

```
Home Screen

Workflow

Generated Report

Critic Feedback
```

---

# 💡 Example Topics

- Artificial Intelligence
- Quantum Computing
- Renewable Energy
- Blockchain Technology
- Cybersecurity
- Climate Change
- Space Exploration
- Medical Innovations

---

# 🚀 Future Improvements

- PDF Export
- DOCX Export
- Citation Formatting (APA/IEEE)
- Multiple webpage extraction
- LangGraph orchestration
- Persistent chat history
- Conversation memory
- Research summarization
- PDF document ingestion
- RAG integration
- Multi-model support
- Dark/Light theme switch
- Docker deployment
- Authentication
- Report templates

---

# 📈 Possible Applications

InsightForge can be used for

- Academic research
- Technical documentation
- Market analysis
- Literature review
- Competitive analysis
- Technology exploration
- Business intelligence
- Research assistance

---

# ⚠️ Current Limitations

- Scrapes one webpage at a time
- No persistent memory
- No citation formatting
- No PDF processing
- Limited customization of reports
- Depends on publicly accessible webpages

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Mrinal Kumar**

Built with ❤️ using

- Mistral AI
- LangChain
- Tavily Search
- BeautifulSoup
- Streamlit

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
