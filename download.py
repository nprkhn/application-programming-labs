def Download(word: str, count: int, destination: str) -> None:
    """
    Скачиваем изображения.

    :word - слово, по которому ищем и скачиваем изображения
    :count - количество скачиваемых изображений
    :destination - путь, по которому скачиваются изображения
    """
    from icrawler.builtin import BingImageCrawler

    bing_crawler = BingImageCrawler(storage={'root_dir': destination})
    bing_crawler.crawl(keyword=word, max_num=count)
