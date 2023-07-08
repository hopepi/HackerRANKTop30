import requests

##top 30daki formların idsi
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'


r = requests.get(url)
submission_ids = r.json()
submission_dicts = []


##veriyi çekme ve tanımlama
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id} \t status: {r.status_code}")
    response_dict = r.json()
    submission_dict = {'title': response_dict['title'],'author': response_dict['by'],'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",'article_score': response_dict['score']
    }
    submission_dicts.append(submission_dict)


##print tarafı
for submission_dict in submission_dicts:

    print(f"\nTitle: {submission_dict['title']}")

    print(f"Author: {submission_dict['author']}")

    print(f"Discussion link: {submission_dict['hn_link']}")

    print(f"Article Score: {submission_dict['article_score']}")