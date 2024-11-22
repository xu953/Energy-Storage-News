import requests
import datetime as dt
from bs4 import BeautifulSoup


def from_batteryindustry(date) -> list:
    url = 'https://batteryindustry.tech'

    cur_date = date.strftime("%d %B %Y")
    print(cur_date)
    response = requests.get(url)
    news_url_set = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Battery Industry news
        breakingnews_div = soup.find('div', class_='td_block_inner td-mc1-wrap')
        othernews_div = soup.find('div', class_='td_block_inner tdb-block-inner td-fix-index')

        if breakingnews_div and othernews_div:
            # Find all the article sections within the main <div>
            all_sub_divs_breaking = breakingnews_div.find_all('div', recursive=False)
            all_sub_divs_other = othernews_div.find_all('div', recursive=False)

            for sub_div in all_sub_divs_breaking:
                try:
                    link = sub_div.find('h3').find('a').get('href')
                    date = sub_div.find('time').text

                    if date == cur_date:
                        news_url_set.append(str(link))
                except:
                    pass

            for sub_div in all_sub_divs_other:
                try:
                    link = sub_div.find('h3').find('a').get('href')
                    date = sub_div.find('time').text

                    if date == cur_date:
                        news_url_set.append(str(link))
                except:
                    pass

            print(f'Number of News today({cur_date}): ' + str(len(news_url_set)))

        else:
            print('Main article container not found on the page.')

    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    contents_BattIndustry = []
    for url in news_url_set:
        response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('div', class_='td-post-content tagdiv-type')
        if article:
            paragraph = article.find('p')
            contents_BattIndustry.append(paragraph.text)
        else:
            print('Article not found on the page.')
    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    return contents_BattIndustry


def from_energystorage(date) -> list:
    url = 'https://www.energy-storage.news/category/news/'

    cur_date = date.strftime("%B %d, %Y")

    response = requests.get(url)
    news_url_set = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Energy Storage News
        main_div = soup.find('div', class_='jet-listing-grid__items grid-col-desk-1 grid-col-tablet-1 grid-col-mobile-1 jet-listing-grid--513')

        if main_div:
            # Find all the article sections within the main <div>
            all_sub_divs = main_div.find_all('div', recursive=False)

            for sub_div in all_sub_divs:
                try:
                    link = sub_div.find('a').get('href') 
                    date = sub_div.find('div', class_='jet-listing-dynamic-field__content').text

                    if date == cur_date:
                        news_url_set.append(str(link))
                except:
                    pass

            print(f'Number of News today({cur_date}): ' + str(len(news_url_set)))

        else:
            print('Main article container not found on the page.')

    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    contents_EnergyStorageNews = []
    for url in news_url_set:
        response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('div', class_='wpwp-non-paywall')
        if article:
            paragraph = article.find('p')
            contents_EnergyStorageNews.append(paragraph.text)
        else:
            print('Article not found on the page.')
    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    return contents_EnergyStorageNews


def from_electrek(date) -> list:
    cur_date = date.strftime("%Y/%m/%d/")

    url = 'https://electrek.co/' + cur_date

    response = requests.get(url)
    news_url_set = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # electrek News
        main_div = soup.find('div', class_='river')

        if main_div:
            # Find all the article sections within the main <div>
            all_sub_divs = main_div.find_all('div', class_='container med left river__posts')
            for sub_div in all_sub_divs:
                articles = sub_div.find_all('article', class_='article standard')
                for article in articles:
                    link = article.find('a', class_='article__title-link').get('href')
                if 'podcast'  in str(link):
                    pass
                else:
                    news_url_set.append(str(link))

            print(f'Number of News today({cur_date}): ' + str(len(news_url_set)))

        else:
            print('Main article container not found on the page.')

    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    contents_electrek = []
    for url in news_url_set:
        response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('div', class_='container med post-content') 
        if article:
            paragraph = article.find('p')
            contents_electrek.append(paragraph.text)
        else:
            print('Article not found on the page.')
    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    return contents_electrek


if __name__ == "__main__":
    mydate = dt.datetime.now(dt.timezone.utc)+dt.timedelta(hours=-50)
    print(mydate)

    contents_BattIndustry = from_batteryindustry(mydate)
    contents_EnergyStorageNews = from_energystorage(mydate)
    contents_electrek = from_electrek(mydate)

    all_news = contents_EnergyStorageNews + contents_BattIndustry + contents_electrek
    print(f'Total News on {mydate} is: {len(all_news)}')

    for news in all_news:
        print(news)
        print('-------------------------------------------------')