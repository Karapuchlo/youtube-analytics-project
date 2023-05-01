from src.channel import Channel

if __name__ == '__main__':
    kuplinov = Channel('UCdKuE7a2QZeHPhDntXVZ91w')

    # получаем значения атрибутов
    print(kuplinov.title)  # Куплинов
    print(kuplinov.video_count)  # 163 (может уже больше)
    print(kuplinov.url)  # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

    # менять не можем
    kuplinov.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'kuplinov.json' с данными по каналу
    kuplinov.to_json('kuplinov.json')
