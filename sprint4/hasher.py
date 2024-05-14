class MarsURLEncoder:

    def __init__(self):
        self.storage = {}

    def encode(self, long_url:str):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        encoded_url = '/'.join(('https://ma.rs', str(hash(long_url.lstrip('https://')))))
        while encoded_url in self.storage.values():
            encoded_url = '/'.join(('https:/', str(hash(long_url.lstrip('https://')))))
        self.storage[encoded_url]=long_url
        return encoded_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.storage[short_url]
    
    
link = MarsURLEncoder()
print(link.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))