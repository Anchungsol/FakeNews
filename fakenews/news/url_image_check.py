


#1. URL 변조 체크
#- URL 에서 www. ~ .com 까지 추출 
#- 배열에 10개 넣고 비교해서 아니면 count + 1
#https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=005&aid=0001264262


class Fakenews_takes:
	
	def __init__(self):
		self.result = 0

	def url_image_Modulation(self,url,image_name):	
		#점수
		count = 0
		
		#변조 체크 (T/F) 
		check=False

		# url 변조 체크 
		check_list = ['daum','chosun','joins','hani','kmib','hankookilbo','seoul','naver','asiatoday']
		check_list_v1 = {
		'daum' : 'news.v.daum.net', 
		'chosun' : 'news.chosun.com', 
		'joins':'news.joins.com', 
		'hani' : 'www.hani.co.kr', 
		'kmib' : 'news.kmib.co.kr',
		'hankookilbo' : 'www.hankookilbo.com', 
		'seoul' : 'www.seoul.co.kr', 
		'naver' :'news.naver.com', 
		'asiatoday' : 'www.asiatoday.co.kr'
		} 

		#사진이름 != 체크 url 체크  
		check_image_list = {
		'news.v.daum.net' : 't1.daumcdn.net',
		'news.chosun.com' : 'image.chosun.com/sitedata/image',
		'news.joins.com' : 'pds.joins.com/news/component/htmlphoto_mmdata',
		'www.hani.co.kr' : 'flexible.img.hani.co.kr/flexible/normal',
		'news.kmib.co.kr' : 'image.kmib.co.kr/online_image',
		'www.hankookilbo.com' : 'newsimg.hankookilbo.com',
		'www.seoul.co.kr' : 'img.seoul.co.kr/img/upload',
		'news.naver.com' : 'imgnews.pstatic.net/image',
		'www.asiatoday.co.kr' : 'img.asiatoday.co.kr/file'
		}

		# URL slice = www.naver.~/ 
		# 언론사중 젤 긴 글자 25
		check_url = url[0:25]

		for value in check_list:
			if (value in check_url):
				pressNames=value
				break;
			else:
				pass


		for value in check_list_v1.values():
			if (value in check_url):
				check_url = value
				check = False
				break

			else:
				check = True

		if (check == True):
			count = count + 1	
			check = False

		else :
			pass

		# imageName slice 후 비교 
		for value in check_image_list.values():
			if (value in image_name):
				image_name = value
				check = False
				break
			else:
				check = True

		if (check == True):
			count =count +1

		else:
			pass

		return count,pressNames,check_url

	def date_Check(self,date,image_name):
		
		# 판별체크 변수 
		check = False

		# 판별점수 변수a
		count = 0 

		#print(image_name)

		# 초기 입력 값 : 2019.  12.  01.  10:26
		date = date.replace(" ","").replace(".",":")
		if (len(date) > 16):
			date = date[0:16]
		
		#2019:12:01:10:26

		#201912011026
		date_list_1 = date.replace(":","")
		#print(date_list_1)
		#20191201
		date_list_2 = date_list_1[0:8]
		#print(date_list_2)
		#2019/1201	
		date_list_3 = date.replace(":","/")
		date_list_3 = date_list_3[0:4] + "/" + date_list_3[4:10].replace("/","")
		#print(date_list_3)
		#201912/01
		date_list_4 = date_list_3[0:7].replace("/","") + "/" + date_list_3[8:10] 
		#print(date_list_4)

		while True:
			if (date_list_1 in image_name):
				check = False
				break
			elif (date_list_2 in image_name):
				check = False
				break
			elif (date_list_3 in image_name):
				check = False
				break
			elif (date_list_4 in image_name):
				check = False
				break
			else:
				check = True
				break

		if (check == True):
			count =count+ 1
		
		else:
			count = 0		
		
		return count 		



#main
#urls = "https://news.naver.comg/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=005&aid=0001264262"
#image_name = "https://imgnews.pstatic.net/image/022/2019/12/01/20191201508921_20191201220501896.jpg?type=w647"
#date = "2019.  12.  01.  10:26"

#test = Fakenews_takes()
#print(test.url_image_Modulation(urls,image_name))
#print(test.date_Check(date,image_name))

# https://news.v.daum.net/v/20191201201015469
# http://news.chosun.com/site/data/html_dir/2019/12/01/2019120100520.html
# https://news.joins.com/article/23646188?cloc=joongang-home-toptype1basic
# http://www.hani.co.kr/arti/society/society_general/919182.html?_fr=mt2
# http://news.kmib.co.kr/article/view.asp?arcid=0013985964&code=61121111&sid1=soc
# https://www.hankookilbo.com/News/Read/201912011725064590?did=PA&dtype=3&dtypecode=3529
# https://www.seoul.co.kr/news/newsView.php?id=20191202004002
# https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=015&aid=0004250487
# http://www.asiatoday.co.kr/view.php?key=20191201010000416&ref=main_top


# -naver
# https://imgnews.pstatic.net/image/005/2019/12/01/201912012132_11120924110820_1_20191201213301559.jpg?type=w647
# https://imgnews.pstatic.net/image/022/2019/12/01/20191201508921_20191201220501896.jpg?type=w647
# https://imgnews.pstatic.net/image/022/2019/12/01/20191201507706_20191201220501908.jpg?type=w647
# https://imgnews.pstatic.net/image/022/2019/12/01/20191201508217_20191201212301987.jpg?type=w647

# -아시아투데이
# http://img.asiatoday.co.kr/file/2019y/12m/02d/2019120201000098500003981.jpg
# http://img.asiatoday.co.kr/file/2019y/12m/01d/2019120101000087900003711.jpg
# http://img.asiatoday.co.kr/file/2019y/12m/01d/2019120101000097200003941.jpg

# -서울신문 
# //img.seoul.co.kr/img/upload/2019/12/01/SSI_20191201185748_V.jpg
# //img.seoul.co.kr/img/upload/2019/11/28/SSI_20191128153134_V.jpg
# //img.seoul.co.kr/img/upload/2019/11/26/SSI_20191126042641_V.jpg

# -한국일보 
# https://newsimg.hankookilbo.com/2019/12/01/201912011859064382_1.jpg
# https://newsimg.hankookilbo.com/2019/11/29/201911292238754968_2.jpg
# https://newsimg.hankookilbo.com/2019/11/30/201911301165789998_1.jpg

# -국민일보
# http://image.kmib.co.kr/online_image/2019/1201/611111110013985960_1.jpg
# http://image.kmib.co.kr/online_image/2019/1201/611115110013985699_1.jpg
# http://image.kmib.co.kr/online_image/2019/1201/611111110013985827_1.jpg


# -한겨례
# http://flexible.img.hani.co.kr/flexible/normal/698/359/imgdb/original/2019/1130/20191130500005.jpg
# http://flexible.img.hani.co.kr/flexible/normal/800/320/imgdb/original/2019/1201/20191201501417.jpg
# http://flexible.img.hani.co.kr/flexible/normal/936/600/imgdb/original/2019/1201/20191201500590.jpg


# -중앙일보
# https://pds.joins.com/news/component/htmlphoto_mmdata/201912/01/a491afcc-0678-40b7-824f-b0247e358d79.jpg
# https://pds.joins.com/news/component/htmlphoto_mmdata/201912/01/8a80fbaf-1171-49b3-9b57-e01fe3d9028e.jpg
# https://pds.joins.com/news/component/htmlphoto_mmdata/201912/01/60d9d66a-88fd-4c11-b641-c6abb12277f7.jpg

# -조선일보 
# https://image.chosun.com/sitedata/image/201912/01/2019120100409_0.png
# https://image.chosun.com/sitedata/image/201912/01/2019120100361_0.png
# https://image.chosun.com/sitedata/image/201912/01/2019120100258_0.jpg

# -다음뉴스
# https://t1.daumcdn.net/news/201912/01/seouleconomy/20191201173802228axku.jpg
# https://t1.daumcdn.net/news/201912/01/segye/20191201204014186ozvr.jpg
# https://img3.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/201912/01/NEWS1/20191201220154131hqct.jpg
# https://img2.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/201912/01/khan/20191201224809998rvel.jpg
# https://t1.daumcdn.net/news/201912/01/yonhap/20191201170747991afyh.jpg
# https://t1.daumcdn.net/news/201912/01/yonhap/20191201213245156tdpf.jpg
# https://t1.daumcdn.net/news/201912/01/yonhap/20191201225245994lpkc.jpg
# https://img1.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/201912/01/NEWS1/20191201112258202nhkh.jpg


