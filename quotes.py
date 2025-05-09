#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
from quote_fetcher import QuoteFetcher

# Initialize the QuoteFetcher class
fetcher = QuoteFetcher()

def main():
    # Setup argument parsing
    parser = argparse.ArgumentParser(description="Fetch inspirational quotes from ZenQuotes")
    
    parser.add_argument('--random', action='store_true', help="Get a random quote")
    parser.add_argument('--today', action='store_true', help="Get today's quote")
    parser.add_argument('--author', type=str, help="Search quotes by a specific author")
    parser.add_argument('--list-authors', action='store_true', help="List popular authors")

    args = parser.parse_args()

    if args.random:
        fetcher.get_random()
        print(fetcher.quote)
        print(fetcher.author)
    elif args.today:
        fetcher.get_today()
        print(fetcher.quote)
        print(fetcher.author)
    elif args.author:
        fetcher.search_author(args.author)
        print(fetcher.quote)
        print(fetcher.author)
    elif args.list_authors:
        print("Popular authors to choose from:")
        print("Albert Einstein, Maya Angelou, Oscar Wilde, Confucius, Mark Twain, Rumi, Steve Jobs, Buddha, Socrates, Nelson Mandela")
    else:
        print("Please choose one of the options (--random, --today, --author AUTHOR, --list-authors)")

if __name__ == "__main__":
    main()

