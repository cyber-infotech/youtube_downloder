import pytube
url = input("url adresini giriniz lutfen:")
path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)
