import argparse
import pyttsx3
from quote_fetcher import QuoteFetcher
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="ZenQuotes CLI - Get inspired quotes from the terminal!")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--random", action="store_true", help="Fetch a random quote")
    group.add_argument("--today", action="store_true", help="Fetch today's quote")
    group.add_argument("--author", type=str, help="Fetch quote by a specific author")
    parser.add_argument("--speak", action="store_true", help="Read the quote aloud")
    parser.add_argument("--list-authors", action="store_true", help="List popular authors")
    args = parser.parse_args()

    fetcher = QuoteFetcher()

    if args.list_authors:
        fetcher.list_authors()
        return

    if args.random:
        fetcher.get_random()
    elif args.today:
        fetcher.get_today()
    elif args.author:
        fetcher.get_by_author(args.author)

    fetcher.display_quote()

    if args.speak:
        engine = pyttsx3.init()
        engine.say(fetcher._quote)
        engine.say(f"by {fetcher._author}")
        engine.runAndWait()

if __name__ == "__main__":
    main()
