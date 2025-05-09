# ZenQuotes CLI – Inspirational Quotes from the Terminal

A simple Python program that fetches inspirational quotes from the [ZenQuotes API](https://zenquotes.io/). You can:

- 🌀 Get a random quote  
- 🌞 Get today’s quote  
- 🧠 Search quotes by author *(requires API key)*  
- 🧾 View a list of popular authors

---

### 🚀 Features

- Lightweight CLI tool using `requests` and `colorama`
- Compatible with both **terminal** and **Jupyter/Colab notebooks**
- Optionally supports **ZenQuotes API key** for advanced features

---

### 📁 File Structure
```
zenquotes-cli/
├── quotes.py
├── quote_fetcher.py
├── requirements.txt
└── README.md
```


### 🛠️ Installation

1. Clone the repo:

```bash
git clone https://github.com/AAliAhmadi/zenquotes-cli.git
cd zenquotes-cli
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

### ⚙️ Usage
You can use one of the following options:
```bash
python quotes.py --random             # Get a random quote
python quotes.py --today              # Get today's quote
python quotes.py --author "Confucius" # Get quote by an author
python quotes.py --list-authors       # Show popular authors
python quotes.py --random --speak     # Random quote and speak aloud
```

### 💡 Tip:
To see a list of popular authors, run:
```bash
python quotes.py --list-authors
```





