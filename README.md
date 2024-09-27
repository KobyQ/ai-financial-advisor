# ai-financial-advisor
Personalized chatbot that helps customers make better financial decisions, such as investment options, retirement planning, and saving strategies

## Table of Contents

- [Requirements](#requirements)

- [Installation](#installation)

- [Running the Server](#running-the-server)

- [Running the CLI](#running-the-cli)

## Requirements
Ensure the following software is installed on your system:
1.  **Python (>= 3.x)**: You can download Python from [python.org](https://www.python.org/).

2.  **pip**: Python's package manager (should come installed with Python).

3.  **Virtualenv** (optional but recommended): To create an isolated environment for your project.

## Installation
1.  **Clone the repository:**
```bash
git clone https://github.com/KobyQ/ai-financial-advisor.git
```

2.  **Create virtual env**
```bash
python3 -m venv ai-financial-advisor-env
source ai-financial-advisor-env/bin/activate # On Windows, use venv\Scripts\activate
```

4.  **Intall requirements**
```bash
pip3 install -r requirements.txt
```

## Running the CLI
```bash
cd chat
python financial-advisor.py
```
This will allow you to ask questions and get answers in the terminal

## Troubleshooting

On Macs, you should probably install unixODBC first if you don't already have an ODBC driver manager installed