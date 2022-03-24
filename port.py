#!/usr/bin/env python3
import requests as rq
import bs4
import sys


def error():
    print("Usage example: python3 portnum.py 80")


def main():
    port = sys.argv[1]

    if len(sys.argv) == 2:
        result = rq.get("https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers")
        soup = bs4.BeautifulSoup(result.text, "lxml")
        rows = soup.find_all('tr')

        for row in rows:
            cols=row.find_all('td')
            cols=[x.text.strip() for x in cols]

            if port in cols:
                print(f"Port {port}: {cols[5]}")
                sys.exit()
    else:
        error()


if __name__ == "__main__":
    main()