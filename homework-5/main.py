import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    #print(pl.show_best_video())
    assert pl.title == "Редакция. АнтиТревел"
    assert pl.url == "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"

    duration = pl.total_duration
    assert str(duration) == "3:41:01"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 13261.0

    assert pl.show_best_video() == "https://www.youtube.com/watch?v=9Bv2zltQKQA"
