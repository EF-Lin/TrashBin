from timing import timer
from dataclasses import dataclass
import asyncio
import requests
import io
import os


@dataclass
class Downloader:
    URL: str
    NAME: list

    def __post_init__(self):
        self.session = requests.session()
        self.session.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, '
                                              'like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    def __str__(self):
        return f'Main download link: {self.URL}'

    def add_name_number(self):
        for i in range(len(self.NAME)):
            self.NAME[i] = f'{i+1}_{self.NAME[i]}'

    def download_files(self, file_type: str, main_path='./file'):
        async def dl_file(url, file_name):
            nonlocal loop
            response = await loop.run_in_executor(None, lambda: self.session.get(url))
            with open(os.path.normpath(f'{main_path}/{file_name}.{file_type}'), 'wb') as f:
                f.write(io.BytesIO(response.content).getvalue())

        loop = asyncio.new_event_loop()
        tasks = []
        for i in range(1, len(self.NAME) + 1):
            tasks.append(loop.create_task(dl_file(self.URL.format(str(i) if i >= 10 else f'0{i}'), self.NAME[i - 1])))
        loop.run_until_complete(asyncio.wait(tasks))


def reform_name():
    n = ''
    while True:
        s = str(input())
        if s == 'Stop':
            print(n)
            break
        elif s != '':
            n += f'\"{s}\",\n'
        else:
            pass


def output_name(name: list):
    an = []
    for i, j in zip(name, range(len(name))):
        an.append(f'{j + 1}_{i.split('  ')[0]}參考答案')
    print(str(an).replace(' ', '\n'))


if __name__ == '__main__':
    timer()
    hd_name = ['1_第一章講義  預備知識',
               '2_第二章講義  極限',
               '3_第三章講義  導函數',
               '4_第四章講義  導函數的應用',
               '5_第五章講義  積分',
               '6_第六章講義  積分應用 (一)',
               '7_第七章講義  積分技巧',
               '8_第八章講義  積分應用 (二)',
               '9_第九章講義  微分方程',
               '10_第十章講義  參數式與極座標',
               '11_第十一章講義  級數',
               '12_第十二章講義  向量',
               '13_第十三章講義  向量值函數',
               '14_第十四章講義  偏導數',
               '15_第十五章講義  重積分',
               '16_第十六章講義  向量微積分',
               '17_第十七章講義  微分方程']
    ans_name = ['1_第一章講義參考答案',
                '2_第二章講義參考答案',
                '3_第三章講義參考答案',
                '4_第四章講義參考答案',
                '5_第五章講義參考答案',
                '6_第六章講義參考答案',
                '7_第七章講義參考答案',
                '8_第八章講義參考答案',
                '9_第九章講義參考答案',
                '10_第十章講義參考答案',
                '11_第十一章講義參考答案',
                '12_第十二章講義參考答案',
                '13_第十三章講義參考答案',
                '14_第十四章講義參考答案',
                '15_第十五章講義參考答案',
                '16_第十六章講義參考答案',
                '17_第十七章講義參考答案']
    handouts = Downloader(URL='http://www.math.ntu.edu.tw/~hchu/Calculus/Calculus%5b104%5d-{}.pdf',
                          NAME=hd_name)
    handouts.download_files('pdf')
    answer = Downloader(URL='http://www.math.ntu.edu.tw/~hchu/Calculus/AnsEx%5b{}%5d.mht',
                        NAME=ans_name)
    answer.download_files('mht')
