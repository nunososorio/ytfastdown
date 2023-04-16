import streamlit as st
import youtube_dl

def main():
	path = st.text_input('Enter URL of any youtube video')
	option = st.selectbox(
     'Select type of download',
     ('audio', 'highest_resolution', 'lowest_resolution'))
	
	matches = ['audio', 'highest_resolution', 'lowest_resolution']
	if st.button("download"): 
		with youtube_dl.YoutubeDL() as ydl:
			info_dict = ydl.extract_info(path, download=False)
			video_title = info_dict.get('title', None)
			st.write("Title of Video: " + str(video_title))
			st.write("Number of Views: " + str(info_dict.get('view_count', None)))
			if option=='audio':
				ydl_opts = {
					'format': 'bestaudio/best',
					'postprocessors': [{
						'key': 'FFmpegExtractAudio',
						'preferredcodec': 'mp3',
						'preferredquality': '192',
					}],
				}
				ydl.download([path])
			elif option=='highest_resolution':
				ydl_opts = {
					'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
				}
				ydl.download([path])
			elif option=='lowest_resolution':
				ydl_opts = {
					'format': 'worstvideo+worstaudio',
				}
				ydl.download([path])
	if st.button("view"): 
		st.video(path) 

if __name__ == '__main__':
	main()
