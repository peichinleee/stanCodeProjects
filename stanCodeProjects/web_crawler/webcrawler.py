"""
File: webcrawler.py
Name: Pei
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        items = soup.find_all('tbody')
        male = 0
        female = 0
        for item in items:
            # pick up the text, split and make into a list
            body = item.text.split()
            for i in range(len(body)):
                if i < 1000:  # exclude content that is not ranking
                    num = body[i]
                    # pick up the numbers and add to male/female
                    ans = ''
                    for ch in num:
                        if ch.isdigit():
                            ans += ch
                    if i % 5 == 2:  # male numbers
                        male += int(ans)
                    elif i % 5 == 4:  # female numbers
                        female += int(ans)
        print('Male Number: ' + str(male))
        print('Female Number: ' + str(female))


if __name__ == '__main__':
    main()
