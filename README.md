# 🚀 RAG UI & API Automated Testing Portfolio

[![RAG UI Automated Tests](https://github.com/D-dataguy/RAG_test/actions/workflows/tests.yml/badge.svg)](https://github.com/D-dataguy/RAG_test/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4%2B-orange.svg)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.55%2B-green.svg)](https://playwright.dev/python/)

A professional, recruiter-ready test automation framework for testing **Retrieval-Augmented Generation (RAG)** UI and AI chatbot applications. Built using **Python**, **Playwright**, and **Pytest**, implementing industry-standard architecture patterns including **Page Object Model (POM)** and **Data-Driven Testing**.

---

## 🏗️ Framework Architecture

```text
RAG_test/
│
├── config/
│   └── settings.py          # Centralized configuration management
│
├── pages/
│   └── rag_page.py          # Page Object Model (POM) for RAG UI encapsulation
│
├── tests/
│   ├── test_rag.py          # Core UI & interaction test cases
│   ├── test_data_driven.py  # Parameterized data-driven test cases
│   └── test_api.py          # Backend RAG endpoint validation
│
├── test_data/
│   └── questions.json       # Externalized test queries and expected keywords
│
├── utils/
│   └── logger.py            # Structured execution logging utility
│
├── reports/                 # Test execution reports
├── screenshots/             # Auto-captured failure screenshots
├── logs/                    # Execution logs
│
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions CI/CD pipeline configuration
│
├── conftest.py              # Pytest fixtures and failure hooks
├── pytest.ini               # Pytest configurations
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Key Technical Competencies Demonstrated

| Skill / Pattern | Implementation Details |
| :--- | :--- |
| **Page Object Model (POM)** | Encapsulates selectors and actions in `pages/rag_page.py` for maintainability. |
| **Robust Locators** | Uses accessible role-based selectors (`get_by_role`, `get_by_text`) instead of brittle CSS classes. |
| **Data-Driven Testing** | Parameterized test suites loading externalized queries from `test_data/questions.json`. |
| **API Testing** | Validates backend endpoint status, headers, and payload responses using Playwright API requests. |
| **CI/CD Pipeline** | Automated GitHub Actions workflow (`tests.yml`) running tests on every push/PR with artifact retention. |
| **Failure Diagnostics** | Custom hooks in `conftest.py` capturing full-page screenshots and execution logs upon test failure. |

---

## 🚀 Getting Started & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/D-dataguy/RAG_test.git
cd RAG_test
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python -m playwright install --with-deps
```

---

## 🏃 Running the Test Suite

Run all UI, API, and Data-Driven tests in headless mode:
```bash
python -m pytest -v
```

Run specific test modules:
```bash
# Run UI tests
python -m pytest tests/test_rag.py -v

# Run Data-Driven tests
python -m pytest tests/test_data_driven.py -v

# Run API endpoint tests
python -m pytest tests/test_api.py -v
```

---

## 📊 CI/CD Automation (GitHub Actions)

This repository is integrated with **GitHub Actions**. Every push or pull request automatically triggers:
1. Environment setup (Python 3.11 + Playwright browsers).
2. Execution of the complete test suite (`pytest -v`).
3. Upload of test failure screenshots as downloadable artifacts if any test fails.

View workflow runs under the [Actions tab](https://github.com/D-dataguy/RAG_test/actions).
