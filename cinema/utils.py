import random
import string
from django.utils.text import slugify
import re
import requests
from bs4 import BeautifulSoup


DONT_USE = ['create', 'accounts']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
	"""
	Creates slug from title and makes it unique
	by adding random alphanumeric characters
	param: cinema title
	return: url slug for the cinema
	"""
	slug = slugify(instance.title)
	new_slug =  "{slug}_{randstr}".format(
	            slug=slug,
	            randstr=random_string_generator(size=5)
	        )
	return new_slug

def rt_crawler(title, year, headers):
	"""
	Request webpages from Rotten Tomatoes & scrapes movie data
	param: title, year
	return: tomato-meter score, synopsis
	"""
	meter, syn = '', ''
	try:
		rt_url=('https://www.rottentomatoes.com/m/' + title.replace(' ', '_').lower())
		resr = requests.get(rt_url,headers=headers)
		resr.raise_for_status()
		soupr = BeautifulSoup(resr.text,'html5lib')
		if (str(year) in soupr.find('span',{'class':'h3 year'}).text):
			if soupr.find('div',{'id':'movieSynopsis'}):
				syn=soupr.find('div',{'id':'movieSynopsis'}).text.encode('ascii','ignore')
			if soupr.find('span',{'class':'meter-value'}):
				meter=soupr.find('span',{'class':'meter-value'}).text
			print(11) # if new film and slug points to new film by default
			print(rt_url)
			return meter, syn
	except:
		pass

	try:
		rt_url=('https://www.rottentomatoes.com/m/' + title.replace(' ', '_').lower())
		resr = requests.get(rt_url,headers=headers)
		resr.raise_for_status()
		soupr = BeautifulSoup(resr.text,'html5lib')
		if ((str(year+1) or str(year-1)) in soupr.find('span',{'class':'h3 year'}).text):
			if soupr.find('div',{'id':'movieSynopsis'}):
				syn=soupr.find('div',{'id':'movieSynopsis'}).text.encode('ascii','ignore')
			if soupr.find('span',{'class':'meter-value'}):
				meter=soupr.find('span',{'class':'meter-value'}).text
			print(22) # if server database has wrong year
			print(rt_url)
			return meter, syn
	except:
		pass

	try:
		rt_url=('https://www.rottentomatoes.com/m/' + title.replace(' ', '_').lower()+'_'+str(year))
		resr = requests.get(rt_url,headers=headers)
		resr.raise_for_status()
		soupr = BeautifulSoup(resr.text,'html5lib')
		if (str(year) in soupr.find('span',{'class':'h3 year'}).text):
			if soupr.find('div',{'id':'movieSynopsis'}):
				syn=soupr.find('div',{'id':'movieSynopsis'}).text.encode('ascii','ignore')
			if soupr.find('span',{'class':'meter-value'}):
				meter=soupr.find('span',{'class':'meter-value'}).text
			print(33) # if slug has year
			print(rt_url)
			return meter, syn
	except:
		pass

	try:
		titleslug = title.replace(' ', '_').lower()
		titleslug ='-'.join(titleslug.split('_')[-2:])
		rt_url=('https://www.rottentomatoes.com/m/' + titleslug)
		resr = requests.get(rt_url,headers=headers)
		resr.raise_for_status()
		soupr = BeautifulSoup(resr.text,'html5lib')
		if (str(year) in soupr.find('span',{'class':'h3 year'}).text):
			if soupr.find('div',{'id':'movieSynopsis'}):
				syn=soupr.find('div',{'id':'movieSynopsis'}).text.encode('ascii','ignore')
			if soupr.find('span',{'class':'meter-value'}):
				meter=soupr.find('span',{'class':'meter-value'}).text
			print(44) # if slug has no 'the' and no year
			print(rt_url)
			return meter, syn
	except Exception:
		print("Shit is legendary")
		pass
	finally:
		return meter, syn


def mc_crawler(title, year, headers):
	"""
	Request webpages from Metacritic & scrapes movie data
	param: title, year
	return: metascore, director(s)
	"""
	dirm, meta = '', ''
	try:
		mc_url='https://www.metacritic.com/movie/'+title.replace(' ', '-').lower()
		resm = requests.get(mc_url,headers=headers)
		resm.raise_for_status()
		soupm = BeautifulSoup(resm.text,'html5lib')
		if (str(year) in soupm.find('span',{'class':'release_year'}).text):
			if soupm.find('div',{'class':'director'}):
				dirm=soupm.find('div',{'class':'director'}).text.split('\n')[2].strip()
			if soupm.find('div',{'class':'metascore_w'}):
				meta=soupm.find('div',{'class':'metascore_w'}).text
			print(111) # if new film and slug points to new film by default
			print(mc_url)
			return dirm, meta
	except:
		pass

	try: 
		mc_url='https://www.metacritic.com/movie/'+title.replace(' ', '-').lower()+'-'+str(year)
		resm = requests.get(mc_url,headers=headers)
		resm.raise_for_status()
		soupm = BeautifulSoup(resm.text,'html5lib')
		if (str(year) in soupm.find('span',{'class':'release_year'}).text):
			if soupm.find('div',{'class':'director'}):
				dirm=soupm.find('div',{'class':'director'}).text.split('\n')[2].strip()
			if soupm.find('div',{'class':'metascore_w'}):
				meta=soupm.find('div',{'class':'metascore_w'}).text
			print(222) # if a year is needed in slug
			print(mc_url)
			return dirm, meta
	except Exception:
		print("Shit is legendary")
		pass
	finally:
		return dirm, meta
		

def wp_crawler(title, year, headers):
	"""
	Request webpages from Wikipedia & scrapes movie data
	param: title, year
	return: cast
	"""
	cast =''
	wp_url='https://en.m.wikipedia.org/wiki/'+title
	resw = requests.get(wp_url,headers=headers)
	try:
		resw.raise_for_status()
	except:
		print("Shit is legendary")
		return "Ain't no Wikipedia page for that shit.", "https://en.m.wikipedia.org/"
	soupw = BeautifulSoup(resw.text,'html5lib')
	temp=soupw.find('table',{'class':'infobox vevent'})
	if bool(temp)==False:
		wp_url='https://en.m.wikipedia.org/wiki/'+title+'_(film)'
		resw = requests.get(wp_url,headers=headers)
		resw.raise_for_status()
		soupw = BeautifulSoup(resw.text,'html5lib')
		temp=soupw.find('table',{'class':'infobox vevent'})
		if bool(temp)==False:
			wp_url='https://en.m.wikipedia.org/wiki/'+title+'_('+str(year)+' film)'
			resw = requests.get(wp_url,headers=headers)
			resw.raise_for_status()
			soupw = BeautifulSoup(resw.text,'html5lib')
			temp=soupw.find('table',{'class':'infobox vevent'})
	cast=temp.text.split('Starring')[1].split('Music')[0].strip().replace('\n', ', ')
	print (cast)
	if cast:
		if ('Music', 'Cinematography' or 'Narrated' in cast):
			cast=temp.text.split('Starring')[1].split('Cinematography')[0].strip().replace('\n', ', ')
			print (cast)
			cast=cast.split('Music')[0]
			print (cast)
			cast=cast.split('Narrated')[0]
			print (cast)
	return cast, wp_url.replace(' ', '%20')
	print(wp_url)

def metadata_generator(title, year):
	"""
	Calls the 3 crawling/scraping functions
	"""
	cast, dirm, meta, meter, syn = '', '', '', '', ''
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
	
	meter, syn = rt_crawler(title, year, headers)
	dirm, meta = mc_crawler(title, year, headers)
	cast, wp_url = wp_crawler(title, year, headers)
	return cast, dirm, meta, meter, syn, wp_url
