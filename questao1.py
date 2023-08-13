from bs4 import BeautifulSoup
import pandas as pd
import requests

html = requests.get('https://www.reddit.com/r/programming/').content

soup = BeautifulSoup(html, 'html.parser')

reddit_url = 'https://www.reddit.com'

posts = []
posts_number = 0

while posts_number < 4:
    if (posts_number == 1):
        posts_number += 1
        continue
    else:
        posts += soup.findAll(True, {'feedindex':[posts_number]})
        posts_number += 1
        continue

output = [
{'Título': posts[0]['post-title'], 'UpVotes': posts[0]['score'], 'Link': reddit_url + posts[0]['permalink']},
{'Título': posts[1]['post-title'], 'UpVotes': posts[1]['score'], 'Link': reddit_url + posts[1]['permalink']},
{'Título': posts[2]['post-title'], 'UpVotes': posts[2]['score'], 'Link': reddit_url + posts[2]['permalink']}
]

df = pd.DataFrame(output)
df.to_excel("Table.xlsx")
print(df)





