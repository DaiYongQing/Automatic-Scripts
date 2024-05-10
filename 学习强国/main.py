from threading import Thread
import pyttsx3
from DrissionPage import ChromiumPage, ChromiumOptions


def read_article(tab):
    article_list = tab.eles('x://div[@class="text-wrap"]')
    for i in range(8):
        tab = article_list[i].click.for_new_tab()
        tab.wait(65)  # 等待65秒
        tab.close()


# 阅览文章
def listen_video(tab):
    video_list = tab.eles('x://div[@class="_1PcbELBKVoVrF5XKNSE_SF"]')
    for i in range(20):
        tab = video_list[i].click.for_new_tab()
        tab.wait(20)
        tab.close()


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
