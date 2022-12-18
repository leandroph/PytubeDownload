from pytube import YouTube

youtube = YouTube(input("URL: "))

# destino para salvar o arquivo
destination = 'D:\Downloads'

# download do arquivo de melhor qualidade
youtube.streams.get_highest_resolution().download(output_path=destination)

print(f'{youtube.title} foi baixado com sucesso.')