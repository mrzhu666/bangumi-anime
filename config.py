USER_INFO = {
    "name": "ryanbgm",   # 用户名

    # 请确保你看过的所有番数量大于 cols x rows 这个值
    "cols": 10,          # 行数
    "rows": 4,           # 列数
}

'''
https://bangumi.github.io/api/

subject_type =>

1 为 书籍
2 为 动画
3 为 音乐
4 为 游戏
6 为 三次元
'''

CODE_CONFIG = {
    "limit": 25,
    "subject_type": 2,  # int only, TODO: support List
    "anime_type": -1,  # int | List, if -1, show all
    "height": 180,
    "width": 128,
    "delta_h": 10,
    "delta_w": 10,
    "embedding": True,
    "output_path": "status.svg",
}
