# AI-Powered Customer Support Chatbot Using Rasa and NLP with Python

## Project Objective
This beginner-friendly chatbot answers customer support questions such as product information, delivery time, refund policy, complaints, contact support, and order status.

## Tools Required
- Python
- VS Code
- Rasa
- Rasa SDK
- Command Prompt / Terminal

## Install Steps

### 1. Create virtual environment
```bash
python -m venv venv
```

### 2. Activate virtual environment
Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install packages
```bash
pip install -r requirements.txt
```

### 4. Train chatbot
```bash
rasa train
```

### 5. Test chatbot
```bash
rasa shell
```

### 6. Optional custom action server
Open another terminal:
```bash
rasa run actions
```

## Sample Questions
- hello
- tell me about your product
- what is your refund policy
- how many days for delivery
- I want to complain
- contact customer care
- where is my order

## Project Files
- `data/nlu.yml` teaches user questions/intents.
- `domain.yml` stores bot responses.
- `data/rules.yml` stores fixed reply rules.
- `data/stories.yml` stores conversation examples.
- `config.yml` stores NLP pipeline and policies.
- `actions/actions.py` stores optional Python custom actions.

