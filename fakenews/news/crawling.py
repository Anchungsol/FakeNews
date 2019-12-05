
from bs4 import BeautifulSoup
import urllib.request
import re

class Crawling_data:
	def __init__(self):
		self.result = 0
	def get_text(self,URL):
		if 'news.na' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="_article_body_contents") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'enter' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="end_body_wrp"):
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'chosun' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="par") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'daum' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="news_view") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'joins' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup.encoding = 'utf-8'
			text =''
			for item in soup.find_all(class_="article_body fs1 mg"):
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'hani' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="text") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'kmib' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="tx") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'hankookilbo' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="article-story") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'seoul' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="user-snb-wrapper") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		elif 'asiatoday' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			text = ''
			for item in soup.find_all(class_="news_bm") :
				text = text + str(item.find_all(text = True))
				for n in text:
					text = re.sub('&nbsp;| |\t|\r|\n', ' ',text)
					text = re.sub('<script.*?>.*?</script>','', text)
					text = text.replace(r"\xa0", "")
					text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',"",text)
					text = re.sub('[a-zA-Z]','',text)
					text = text.replace("  ", "")
					text = text.strip()
		return text
	def get_title(self,URL):
		if 'news.na' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('h3', id = 'articleTitle').text
			title = title.strip()
		elif 'enter' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('h2', class_= 'end_tit').text
			title = title.strip()
		elif 'chosun' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('h1', id = 'news_title_text_id').text
			title = title.strip()
		elif 'daum' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('h3', class_= 'tit_view').text
			title = title.strip()
		elif 'joins' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('h1', id = 'article_title').text
			title = title.strip()
		elif 'hani' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('h4').text
			title = title.strip()
		elif 'kmib' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('h3').text
			title = title.strip()
		elif 'hankookilbo' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('title').text
			title = title.strip()
		elif 'seoul' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('title').text
			title = title.strip()
		elif 'asiatoday' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			title = soup.find('title').text
			title = title.strip()
		return title
	def get_date(self,URL) :
		if 'news.na' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find("span", {"class":"t11"}).text
			date = re.sub('[r-힗]','',date)
		elif 'enter' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find("span", {"class":"author"}).text
			date = re.sub('[r-힗]','',date)
		elif 'chosun' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find(class_="news_date").text
			date = re.sub('[r-힗]','',date)
			date = date.strip()
		elif 'daum' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find("span", {"class":"info_aside"}).text
			date = re.sub('[r-힗]','',date)
		elif 'joins' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find(class_="byline").text
			date = re.sub('[r-힗]','',date)
			date = date.replace("[]", "")
		elif 'hani' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find("p", {"class":"date-time"}).text
			date = re.sub('[r-힗]','',date)
		elif 'kmib' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find("span", {"class":"t11"}).text
			date = re.sub('[r-힗]','',date)
			date = date.strip()
		elif 'hankookilbo' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find(class_="info").text
			date = re.sub('[ㄱ-힗]','',date)
			date = date.strip()
		elif 'seoul' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find(class_="info-text").text
			date = re.sub('[ㄱ-힗]','',date)
			date = re.sub('[a-zA-Z]','',date)
			date = date.replace("@", "")
			date = date.strip()
			date = date.replace("   ", " ")
		elif 'asiatoday' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			date = soup.find("span", {"class":"wr_day"}).text
			date = re.sub('[ㄱ-힗]','',date)
			date = re.sub('[a-zA-Z]','',date)
			date = date.replace("@", "")
			date = date.strip()
			date = date.replace("   ", " ")
		return date
	def get_image(self,URL):
		if 'news.na' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="_article_body_contents")
			img = soup.find("img")["src"]
		elif 'enter' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="end_body_wrp")
			img = soup.find("img")["src"]
		elif 'chosun' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="news_imgbox def")
			img = soup.find("img")["src"]
		elif 'daum' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="news_view")
			img = soup.find("img")["src"]
		elif 'joins' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="article_body fs1 mg")
			img = soup.find("img")["src"]
		elif 'hani' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="text")
			img = soup.find("img")["src"]
		elif 'kmib' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="tx")
			img = soup.find("img")["src"]
		elif 'hankookilbo' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="article-story")
			img = soup.find("img")["src"]
		elif 'seoul' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="user-snb-wrapper")
			img = soup.find("img")["src"]
		elif 'asiatoday' in URL:
			source_code_from_URL = urllib.request.urlopen(URL)
			soup = BeautifulSoup(source_code_from_URL, 'html.parser')
			soup = soup.find("div", class_="news_bm")
			img = soup.find("img")["src"]
		return img
	
