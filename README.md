# ZenQuotes CLI – Inspirational Quotes from the Terminal

A simple Python program that fetches inspirational quotes from the [ZenQuotes API](https://zenquotes.io/). You can:

- 🌀 Get a random quote  
- 🌞 Get today’s quote  
- 🧠 Search quotes by author *(requires API key)*  
- 🧾 View a list of popular authors

---

### 🚀 Features

- Lightweight CLI tool using `requests`, `pyttsx3` and `colorama`
- Compatible with both **terminal** and **Jupyter/Colab notebooks**
- Optionally supports **ZenQuotes API key** for advanced features

---

### 📁 File Structure
`
zenquotes-cli/
├── quotes.py
├── quote_fetcher.py
├── requirements.txt
└── README.md
`


### 🛠️ Installation

1. Clone the repo:

```bash
git clone https://github.com/AAliAhmadi/zenquotes-cli.git
cd zenquotes-cli
```

2. Install dependencies

- 🧪 Requirements
```Python 3.7+```, ```requests```, ```colorama```, ```python-dotenv```, ```pyttsx3```

- Use command below to install them all.
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

### 📄 License
MIT

### 🙏 Thanks
- [ZenQuotes API](https://zenquotes.io)
- [Colorama](https://github.com/tartley/colorama)

### ⚠️ Note on Jupyter Notebooks and Colorama

If you are running this project in a **Jupyter Notebook** environment, please note that **Colorama** might not display the colors as expected. Jupyter Notebooks do not support ANSI escape sequences (which are used by Colorama to generate colored text in the terminal). 

For proper color output, it is recommended to run this program in a regular terminal or command prompt. Alternatively, you can modify the code to use HTML or other libraries such as `termcolor` for color output in Jupyter Notebooks.


