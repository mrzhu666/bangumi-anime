import requests as r
from constant import BASE, COLLECTIONS_URL, HEADERS
from config import USER_INFO, CODE_CONFIG
from utils import getRespon, getDict, check_number, type_filter, item_select, generate_svg, img_filter
from tqdm import tqdm

url_no_params = BASE + COLLECTIONS_URL

user_name = USER_INFO["name"]
cols, rows = USER_INFO["cols"], USER_INFO["rows"]

subject_type = CODE_CONFIG["subject_type"]
limit = CODE_CONFIG["limit"]
anime_type_list = CODE_CONFIG["anime_type"]
single_height, single_width = CODE_CONFIG["height"], CODE_CONFIG["width"]
svg_delta_h, svg_delta_w = CODE_CONFIG["delta_h"], CODE_CONFIG["delta_w"]
output_path = CODE_CONFIG["output_path"]
offset = 0

embedding = CODE_CONFIG["embedding"]
data = []

# --------------- download info --------------------
while True:
    url = url_no_params.format(user_name, subject_type, offset, limit)
    response = getRespon(url, HEADERS)
    user_info = getDict(response)

    if "title" in user_info and 'Bad Request' == user_info["title"]:
        # 400 Bad Request, loop exits from here
        break

    data += user_info["data"]

    check_number(cols, rows, user_info["total"])  # only run once
    offset += limit

# --------------- filter unneeded --------------------
data_filtered = []
for item in data:
    if type_filter(item, anime_type_list) and img_filter(item):
        data_filtered.append(item)

# --------------- select items --------------------
data_selected = item_select(data_filtered, cols=cols, rows=rows)

# --------------- generate svg images --------------------
generate_svg(data_selected, output_path,
             embedding=embedding,
             cols=cols, rows=rows,
             height=single_height, width=single_width,
             delta_h=svg_delta_h, delta_w=svg_delta_w)
