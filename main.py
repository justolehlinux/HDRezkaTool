from HDRezkaAPI import *


search_text = input('Поиск: ')
search_result = Search(search_text)

print(search_result)

title_id = int(input('Введите номер: '))

movie_data = search_result.get_data(title_id)
movie_info = MovieInfo(movie_data)

download_data = movie_info.get_data()

if 0:
    dorl = input('PLS?')
    quality = input("Введите качество: ")
else:
    dorl = "pls"
    quality = "1080p]"

downloader = Download(download_data, dorl, quality)

print(movie_info)

if download_data['type'] == 'movie':
    downloader.download_movie()
    print('Скачивание успешно завершено!')
else:
    download_type = int(input('2 - Скачать сезон сериала\n3 - Скачать эпизоды сериала\n4 - Скачать сезонs сериала\n5 - Скачать сериал\n'
                            'Выберите тип скачивания: '))

    if download_type == 2:
        season = int(input('Введите номер сезона: '))   
        downloader.download_season(season)
        print('Скачивание успешно завершено!')
    elif download_type == 3:
        correct_episode = False
        season = int(input('Введите номер сезона: '))
        episodes_count = download_data['seasons_episodes_count'][season]
        print(f'В данном сезоне количество эпизодов: {episodes_count}')
        start = int(input('Введите стартовый эпизод: '))
        end = int(input('Введите конечный эпизод: '))
        while not correct_episode:
            try:
                downloader.download_episodes(season, start, end)
                correct_episode = True
            except EpisodeNumberIsOutOfRange:
                print('Неверный диапазон!')
                episode = int(input('Снова введите диапазон эпизодов: '))
        print('Скачивание успешно завершено!')
    elif download_type == 4:
        correct_season = False
        start = int(input('Enter the starting season number: '))
        end = int(input('Enter the ending season number: '))
        while not correct_season:
            try:
                downloader.download_seasons(start, end)
                correct_season = True
            except SeasonNumberIsOutOfRange:
                print('Invalid season range!')
                start = int(input('Enter the starting season number again: '))
                end = int(input('Enter the ending season number again: '))
        print('Download successful!')
    if download_type == 5:
        downloader.download_all_serial()
        print('Скачивание успешно завершено!')
    if dorl == "pls":
         downloader.convert_to_pls()


    else:
        print('Неверный тип скачивания!')
