import random
import time
from threading import Thread
import pyttsx3
from DrissionPage import ChromiumPage, ChromiumOptions


def read_article(tab):
    article_list = tab.eles('x://span[@class="text"][@style="color: rgb(0, 0, 0); white-space: nowrap;"]')
    random.shuffle(article_list)
    for i in range(12):
        if len(article_list[i].text) >= 10:
            tab = article_list[i].click.for_new_tab()
            tab.wait(65)  # 等待65秒
            tab.close()
        else:
            i -= 1


# 阅览文章
def listen_video(tab):
    # 随机选择一个主题
    header = tab.eles('x://div[@class="_30AOPZ5kxkMqnxVwziYb3o"]')
    random.choice(header).click()
    tab.wait(1)
    for i in range(9):
        tab.scroll.to_bottom()
        print(f'正在下滑第{i + 1}次')
        tab.wait(1)
    # 随机取20条视频
    video_list = tab.eles('x://div[@class="_1PcbELBKVoVrF5XKNSE_SF"]')
    random.shuffle(video_list)
    # 开始计时
    start_time = time.time()
    for video in video_list:
        tab = video.click.for_new_tab()
        tab.wait.eles_loaded('x://span[@class="replay-btn"]', timeout=600)
        tab.close()
        if time.time() - start_time > 540:
            print('时间要求已满足')
            break


def main():
    # 设置静音
    co = ChromiumOptions()
    co.mute(True)
    page = ChromiumPage(co)
    # 阅读主页
    page.get('https://www.xuexi.cn/')
    login_btn = page.ele('x://a[@class="icon login-icon"]')
    if login_btn:
        page = login_btn.click.for_new_tab()

    engine = pyttsx3.init()

    # 视听页面
    video_tab = page.ele('x://section[@id="JEDXfdDkvQ"]').click.for_new_tab()

    reading = Thread(target=read_article, args=(page,))
    listening = Thread(target=listen_video, args=(video_tab,))

    reading.start()
    engine.say('阅读任务已开始')
    engine.runAndWait()

    listening.start()
    engine.say('视听任务已开始')
    engine.runAndWait()

    reading.join()
    listening.join()

    engine.say('学习通自动化脚本执行完毕')
    engine.runAndWait()
    page.quit()


if __name__ == '__main__':
    main()
