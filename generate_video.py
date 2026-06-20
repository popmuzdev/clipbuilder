import os
from moviepy.editor import ImageClip, AudioFileClip

def merge_audio_video():
    # Имена файлов, которые мы загрузим на следующем шаге
    audio_file = "track.mp3"
    image_file = "cover.jpg"
    output_file = "output.mp4"
    
    print("Проверяем наличие файлов...")
    if not os.path.exists(audio_file) or not os.path.exists(image_file):
        print(f"Ошибка! Убедитесь, что файлы {audio_file} и {image_file} загружены в репозиторий.")
        return

    print("Загружаем аудиофайл...")
    audio = AudioFileClip(audio_file)
    
    print("Создаем видеоряд из картинки...")
    # Создаем статичный кадр и растягиваем его ровно на длину трека
    video = ImageClip(image_file).set_duration(audio.duration)
    
    print("Соединяем аудио и видео...")
    video = video.set_audio(audio)
    
    print("Начинаем финальный рендер видео...")
    video.write_videofile(
        output_file, 
        fps=24, 
        codec="libx264", 
        audio_codec="aac",
        threads=4
    )
    
    audio.close()
    video.close()
    print("Рендеринг успешно завершен!")

if __name__ == "__main__":
    merge_audio_video()
