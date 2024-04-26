import os
import sys
import json
import base64

import svgwrite
import requests as r

from constant import HEADERS


def getRespon(url, headers):
    response = r.get(url, headers=headers)
    if 200 == response.status_code:
        return response
    if 400 == response.status_code:
        return response
    else:
        print("状态码为：" + str(response.status_code), "请求失败")
        sys.exit(0)


def getDict(response, encoding=None):
    if encoding is None:
        response.encoding = response.apparent_encoding
    else:
        response.encoding = encoding

    try:
        return json.loads(response.text)
    except Exception as e:
        print("json解析失败")
        sys.exit(0)


# A Decorator that wraps a function to only run once.
def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return func(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@run_once
def check_number(cols, rows, total):
    # return cols * rows >= total
    if cols * rows <= total:
        pass
    else:
        print("多看点儿番吧")
        sys.exit(0)


def type_filter(info, anime_type_list):

    if -1 == anime_type_list:
        return True

    if info['type'] in anime_type_list:
        return True
    else:
        return False


def img_filter(info):

    return all(v for k, v in info['subject']['images'].items())


# customize your filter function and import it into main.py
def custom_filter(info):
    return True


def item_select(data, cols, rows):
    return data[: cols * rows]


def download_img_by_url(url, headers=None, embed=False):
    response = r.get(url, headers=HEADERS)

    if not embed:
        path = os.path.basename(url)
        with open(path, 'wb') as fh:
            fh.write(response.content)
    else:
        # 将图片内容嵌入的 svg 中则不需要下载到本地
        base64_data = base64.b64encode(response.content).decode('utf-8')
        return f'data:image/png;base64,{base64_data}'


def __calc_location(cols=8, rows=4,
                    height=175, width=128,
                    delta_h=10, delta_w=10):

    x, y = 0, 0
    location_list = []
    stride_x, stride_y = width + delta_w, height + delta_h
    for r in range(rows):
        for c in range(cols):
            x_new = stride_x*c + x
            y_new = stride_y*r + y
            location_list.append((x_new, y_new))

    return location_list


def generate_svg(data_selected,
                 output_path,
                 embedding=True,
                 cols=8, rows=4,
                 height=175, width=128,
                 delta_h=10, delta_w=10):
    """
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ^----^----^----^----^----^----^
    ^----^----^----^----^----^----^
    ^----^----^----^----^----^----^
    ^----^----^----^----^----^----^
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ^----^----^----^----^----^----^
    ^----^----^----^----^----^----^
    ^----^----^----^----^----^----^
    ^----^----^----^----^----^----^
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    这么操作的话, 外边的那个边儿不需要了
    """
    location_list = __calc_location(cols=cols, rows=rows,
                                    height=height, width=width,
                                    delta_h=delta_h, delta_w=delta_w)

    img_height = height * rows + delta_h * (rows-1)
    img_width = width * cols + delta_w * (cols-1)
    dwg = svgwrite.Drawing(output_path, size=(
        '%dpx' % img_width, '%dpx' % img_height)
    )

    for idx in range(cols * rows):

        x, y = location_list[idx]
        item = data_selected[idx]

        img_url = item['subject']['images']['small']

        if embedding:

            embedded_image_data = download_img_by_url(
                img_url, HEADERS, embed=embedding)
            image = dwg.image(embedded_image_data, insert=(
                x, y), size=(width, height))
        else:
            img_path = img_url
            image = dwg.image(img_path, insert=(x, y), size=(width, height))

        dwg.add(image)

    # 保存 SVG 文件
    dwg.save()
