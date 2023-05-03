import requests
from bs4 import BeautifulSoup
import datetime
import time


def is_valid_link(link):
    """
    检查链接是否有效
    """
    try:
        response = requests.get(link)
        if response.status_code == 404:
            return False
        else:
            return True
    except:
        return False


def detect_invalid_links(links, whitelist):
    """
    检测失效链接
    """
    invalid_links = []
    for link in links:
        href = link.get('href')
        print(f"正在检测链接: {link}")
        if href is None:
            continue
        if href in whitelist:
            continue
        if is_valid_link(href) == False:
            invalid_links.append((link.string, href))
    return invalid_links


def write_to_log(invalid_links):
    """
    将失效链接写入日志文件
    """
    if len(invalid_links) == 0:
        return
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    with open(f'{today}.log', 'a', encoding='utf-8') as f:
        f.write('=====\n')
        for name, link in invalid_links:
            f.write(f'{name}&&{link}\n')


if __name__ == '__main__':
    # 要检测的网站的基本链接
    base_url = 'https://www.cxy521.com'

    # 白名单中的链接无需检查
    whitelist = set(['/'])

    # 首次检查失效链接
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    invalid_links = detect_invalid_links(links, whitelist)
    write_to_log(invalid_links)

    # 重复检查失效链接
    while True:
        time.sleep(60)  # 等待一分钟
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        invalid_links = detect_invalid_links(links, whitelist)
        write_to_log(invalid_links)
