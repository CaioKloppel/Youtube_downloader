from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import os
import re

pasta = ""
Programa = ""

while not os.path.isdir(pasta):
    pasta = input(r"""Endereço da pasta a qual você gostaria que o vídeo ou áudio seja baixado.
Exemplo: C:\Users\Usernick\OneDrive\Youtube_downloads
Endereço: """)
    if os.path.isdir(pasta):
        print("Endereço válido.")
    else:
        print("Endereço inválido.")

while Programa.lower() != 'audio' and Programa.lower() != 'video':
    Programa = input("Download audio ou video: ")
    if Programa.lower() != 'audio' and Programa.lower() != 'video':
        print("Único formato aceito: 'Audio' ou 'Video'.")


if Programa.lower() == "video":
    isValid = False
    while not isValid:
        link = input("Video url: ")
        try:
            yt = YouTube(link)
            name = yt.title.replace(" ", "_")
            name = re.sub(r"[^a-zA-Z0-9_]", "", name)

            video = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
            audio = yt.streams.filter(only_audio=True)[0]

            print("Downloading video...")
            video_baixado = video.download(output_path=pasta, filename="Video.mp4")
            print("Downloading audio...")
            audio_baixado = audio.download(output_path=pasta, filename="Audio.mp3")

            output_path = os.path.join(pasta, f"{name}.mp4")


            video_clip = VideoFileClip(video_baixado)
            audio_clip = AudioFileClip(audio_baixado)
            final_audio = CompositeAudioClip([audio_clip])
            final_clip = video_clip.with_audio(final_audio)
            final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            os.remove(video_baixado)
            os.remove(audio_baixado)
            isValid = True

        except Exception as e:
            print(f"Ocorreu um erro: {e}")  
            print("Tente novamente.")
else:
    isValid = False
    while not isValid:
        link = input("Audio url: ")
        try:
            yt = YouTube(link)
            name = yt.title.replace(" ", "_")
            name = re.sub(r"[^a-zA-Z0-9_]", "", name)

            audio = yt.streams.filter(only_audio=True)[0]
            print("Download audio...")
            audio.download(output_path=pasta, filename=f"{name}.mp3")
            isValid = True
        except Exception:
            print("Invalid url.")
            print("Tente novamente.")
