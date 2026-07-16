# 🚀 InsightForge

### Autonomous Multi-Agent Research Platform

InsightForge is an AI-powered research platform that leverages autonomous agents to discover, extract, synthesize, and evaluate information from the web. Built using **Mistral AI**, **LangChain**, **Tavily Search**, and **Streamlit**, it automates the research workflow and produces structured, source-backed reports.

---

## ✨ Features

- 🌐 Intelligent web search using Tavily Search API
- 📄 Deep webpage content extraction with BeautifulSoup
- 🤖 Autonomous multi-agent workflow
- 📝 AI-generated structured research reports
- ✅ Automated report quality evaluation
- 🎨 Interactive Streamlit interface
- ⚡ Powered by Mistral Small 2506

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
              Research Topic
                      │
                      ▼
        ┌─────────────────────────┐
        │   Discovery Agent       │
        │  (Tavily Web Search)    │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Knowledge Extraction    │
        │ (BeautifulSoup Scraper) │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Report Generation       │
        │   (Mistral AI)          │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Quality Review          │
        │   (Mistral AI)          │
        └────────────┬────────────┘
                     │
                     ▼
         Final Research Report
