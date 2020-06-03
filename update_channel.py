import requests

# List of CHannel ID (asianetnews,manorama,news24,mathrubhumi,kairali,mediaone,NDTV News,CNN Live,Parumala,Reporter,news18,jeevan,janam)
CHANNEL_ID = ["UCf8w5m0YsRa8MHQ5bwSGmbw","UCP0uG-mcMImgKnJz-VjJZmQ","UCup3etEdjyF1L3sRbU-rKLw","UCwXrBBZnIh2ER4lal6WbAHw","UCkCWitaToNG1_lR-Si1oMrg","UC-f7r46JhYv78q5pGrO6ivA","UCZFMm1mMw0F81Z37aaEzTUA","UCef1-8eOpJgud7szVPlZQAQ","UC8ebJ_anG4byfhC_2hT7eKw","UCFx1nseXKTc1Culiu3neeSQ","UC-mMi78WJST4N5o8_i1FoXw","UCjX2Z1XGWEbKEGgKMACbhkw","UCNVkxRPqsBNejO6B9thG9Xw"]

# Fetching the API Key
file = open("api-key.txt", "r")
YOUR_API_KEY = file.readline()
file.close()

#Defined empty Links array
Links=[];

# For each Channel Id, updating the channel Links 
for channel in CHANNEL_ID:
	URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&eventType=live&type=video&key={}".format(channel,YOUR_API_KEY);
	req = requests.get(url = URL);
	data = req.json()
	try:
		link = data['items'][0]['snippet']['thumbnails']['default']['url'].split("/")[4];
		print(link)
	except:
		print("Link Not Found")
		link="404"
	finally:
		Links.append(link)

#Links File opened to write
file2 = open(r"links.txt","w+")
for link in Links:
	file2.write(link+"\n")
file2.close()