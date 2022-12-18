from pytube import YouTube
import os
  
youtube = YouTube(input("URL: "))
  
# extrair apenas áudio
audio = youtube.streams.filter(only_audio=True).first()
  
# destino para salvar o arquivo
destination = 'D:\Downloads'
  
# download do arquivo
out_file = audio.download(output_path=destination)
  
# salva o arquivo com extensão .mp3
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
print(f'{youtube.title} foi baixado com sucesso.')
