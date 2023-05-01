from src.channel import Channel

if __name__ == '__main__':
    # Создаем два экземпляра класса
    kuplinov = Channel('UCdKuE7a2QZeHPhDntXVZ91w')
    redactsiya = Channel('UC1eFXmJNkjITxPFWTy6RsWg')

    # Используем различные магические методы
    print(kuplinov)  # 'kuplinov (https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA)'
    print(kuplinov + redactsiya)  # 13970000
    print(kuplinov - redactsiya)  # 6630000
    print(redactsiya - kuplinov)  # -6630000
    print(kuplinov > redactsiya)  # True
    print(kuplinov >= redactsiya)  # True
    print(kuplinov < redactsiya)  # False
    print(kuplinov <= redactsiya)  # False
    print(kuplinov == redactsiya)  # False
    
