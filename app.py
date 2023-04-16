import streamlit as st
from pytube import YouTube

def main():
	path = st.text_input('Enter URL of any youtube video')
	option = st.selectbox(
     'Select type of download',
     ('audio', 'highest_resolution', 'lowest_resolution'))
	
	matches = ['audio', 'highest_resolution', 'lowest_resolution']
	if st.button("download"): 
		video_object =  YouTube(path)
		st.write("Title of Video: " + str(video_object.title))
		st.write("Number of Views: " + str(video_object.views))
		if option=='audio':
			video_object.streams.get_audio_only().download()
			st.write("Download Link: " + str(video_object.streams.get_audio_only().url))
		elif option=='highest_resolution':
			video_object.streams.get_highest_resolution().download()
			st.write("Download Link: " + str(video_object.streams.get_highest_resolution().url))
		elif option=='lowest_resolution':
			video_object.streams.get_lowest_resolution().download()
			st.write("Download Link: " + str(video_object.streams.get_lowest_resolution().url))
	if st.button("view"): 
		st.video(path) 

if __name__ == '__main__':
	main()
