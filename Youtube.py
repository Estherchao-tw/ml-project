from pytube import YouTube

url = 'https://www.youtube.com/watch?v=Xokmm1h29w8&list=RDX1hNIRNQQE4&index=11&ab_channel=讚美之泉StreamOfPraiseMusicMinistries'

yt = YouTube(url)

# 抓取標題試試看
yt.title
stream = yt.streams
video = yt.streams.filter(only_audio=True).first()
down = video.download()