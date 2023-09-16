import requests
import time
import random
# from requests_toolbelt.multipart.encoder import MultipartEncoder

from threading import Thread




class RPSTester:
    def __init__(self, 
        requests_per_second: int, 
        epochs: int, 
        only_post: bool = False, 
        only_get: bool = False,
        random: bool = False
    ):
        self.requests_per_second = requests_per_second
        self.epochs = epochs
        self.urls = ['http://localhost:8001/HbHHvIBihfluQieCbW.png']
        self.get_times = []
        self.get_times_server = []
        self.post_times = []
        self.post_times_server = []
        self.only_post = only_post
        self.only_get = only_get
        self.random = random
        if not(only_get or only_post or random):
            raise Exception("Пожалуйста выберите один пункт")

    def run_test(self):
        for epoch in range(self.epochs):

            thread_pool = []
            for i in range(rps.requests_per_second):
                if not self.only_post and self.only_get:
                    m = 1
                if self.only_post and not self.only_get:
                    m = 2
                if self.random:
                    m = random.randint(1,2)
                if m == 1:
                    thread_pool.append(Thread(target=self.send_get, args=[]))
                elif m == 2:
                    thread_pool.append(Thread(target=self.send_post, args=[]))

            for thread in thread_pool:
                thread.start()
            print(f"Эпоха {epoch} запущена")
            time.sleep(1)

    def send_get(self):
        try:
            url = random.choice(self.urls)
            start = time.time()
            res = requests.get(url)
            self.get_times_server.append(float(res.headers['x-process-time']))
            self.get_times.append(time.time()-start)
        except:
            pass

    def send_post(self):
        try:
            start = time.time()
            res = requests.post(url="http://localhost:8001/", files={
                'file': (
                    'test.png', 
                    open('C:/vscode/AnoCat/file_server/tests/3mb.png', 'rb'), 
                    'image/png'
                ),
            })
            self.post_times_server.append(float(res.headers['x-process-time']))
            self.post_times.append(time.time()-start)
            self.urls.append(res.json()['link'])
        except:
            pass

    def results(self):
        ndigits = 3
        print("---------- RPS RESULTS ----------")
        print(f"Было эпох: {self.epochs}")
        print(f"Запросов в секунду: {self.requests_per_second}")
        print(f"Было запланировано запросов: {self.requests_per_second*self.epochs}")
        print(f"Успешно отправлены: {len(self.get_times)+len(self.post_times)}")

        if not self.only_post or self.random:
            print()
            print("----- Сохранение файлов -----")
            print(f"Было отправлено: {len(self.get_times)}")
            print(
f"Среднее время ожидания клиента: \
{round(sum(self.get_times)/len(self.get_times),ndigits)} \
s")
            print(
f"Из них виноват сервер в среднем за: \
{round(sum(self.get_times_server)/len(self.get_times_server), ndigits)} \
s")

        if not self.only_get or self.random:
            print()
            print("----- Загрузка файлов -----")
            print(f"Было отправлено: {len(self.post_times)}")
            print(
f"Среднее время ожидания клиента: \
{round(sum(self.post_times)/len(self.post_times),ndigits)} \
s")
            print(
f"Из них виноват сервер в среднем за: \
{round(sum(self.post_times_server)/len(self.post_times_server), ndigits)}\
s")







rps = RPSTester(50, 1, only_get=0, only_post=0, random=1)

rps.run_test()

rps.results()