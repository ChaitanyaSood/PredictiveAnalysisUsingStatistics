import streamlit as st
import urllib.request
import re
import random
from pytube import YouTube
from pydub import AudioSegment
import sys
import os


def main():
    X = st.text_input("Enter Artist Name: ")
    N = st.number_input("Enter number of YouTube videos to use: ")
    Y = st.number_input("Enter duration for audio segments (in seconds): ")
    file_name = st.text_input("Enter file name for the final mashup: ")

    X = X.lower()
    X = X.replace(" ", "") + "musicvideos"
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + X)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    l = len(video_ids)
    url = []
    for i in range(int(N)):
        url.append("https://www.youtube.com/watch?v=" +
                   video_ids[random.randint(0, l - 1)])

    final_aud = AudioSegment.empty()
    for i in range(int(N)):
        audio = YouTube(url[i]).streams.filter(only_audio=True).first()
        audio.download(filename='Audio-' + str(i) + '.mp3')
        aud_file = os.path.join(os.getcwd(), 'Audio-' + str(i) + '.mp3')
        file1 = AudioSegment.from_file(aud_file)
        extracted_file = file1[:Y * 1000]
        final_aud += extracted_file
        final_aud.export(file_name, format="mp3")

    st.write("Customized Mashup successfully created!")


if __name__ == '__main__':
    st.title("Custom YouTube Mashup")
    main()
