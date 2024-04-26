<!-- English | [简体中文](./README_cn.md) -->

<div align="center">
<!-- 标题 -->

<h1 align="center">
  - Bangumi-Anime - 
</h1>

<!-- star数, fork数, pulls数, issues数, contributors数, 开源协议 -->
<a href="https://github.com/DrRyanHuang/bangumi-anime/stargazers"><img src="https://img.shields.io/github/stars/DrRyanHuang/bangumi-anime" alt="Stars Badge"/></a>
<a href="https://github.com/DrRyanHuang/bangumi-anime/network/members"><img src="https://img.shields.io/github/forks/DrRyanHuang/bangumi-anime" alt="Forks Badge"/></a>
<br/>
<a href="https://github.com/DrRyanHuang/bangumi-anime/pulls"><img src="https://img.shields.io/github/issues-pr/DrRyanHuang/bangumi-anime" alt="Pull Requests Badge"/></a>
<a href="https://github.com/DrRyanHuang/bangumi-anime/issues"><img src="https://img.shields.io/github/issues/DrRyanHuang/bangumi-anime" alt="Issues Badge"/></a>
<a href="https://github.com/DrRyanHuang/bangumi-anime/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/DrRyanHuang/bangumi-anime?color=2b9348"></a>
<a href="https://github.com/DrRyanHuang/bangumi-anime/blob/master/LICENSE"><img src="https://img.shields.io/github/license/DrRyanHuang/bangumi-anime?color=2b9348" alt="License Badge"/></a>





<!-- logo -->
<img alt="LOGO" src="logo/Frieren_sleep.png" width="30%"> </img>
<br/>
<i>Loved the project? Please consider forking the project to help it improve!</i>🌟

</div>


### Getting Started 🚀

To get started, simply fork this repository and modify the contents of the config.py file:


```python
USER_INFO = {
    "name": "ryanbgm",   # <------ Replace with your Bangumi username

    # Ensure that the total number of anime you've watched exceeds cols x rows
    "cols": 10,          # Number of columns
    "rows": 4,           # Number of rows
}
```

Once you've updated the configuration, sit back and let the GitHub Action work its magic! ✨ After the action completes, you'll find your personalized anime watchlist image in the status.svg file, with the titles arranged in chronological order.


### Customization 🎨

Feel free to dive into the main.py and utils.py files to customize your watchlist further. You can modify these files to filter anime titles based on specific criteria or genres, tailoring the list to your preferences. 🎯


### Under the Hood 🔍
This project leverages the official Bangumi API to fetch your watched anime data and utilizes the svgwrite library to generate the SVG image. The combination of these powerful tools allows for a seamless and efficient creation of your personalized anime watchlist. 🧩💡

### Feedback and Contributions 🙌
If you have any questions, suggestions, or would like to contribute to the project, please don't hesitate to open an issue on the GitHub repository. Your feedback is invaluable and greatly appreciated! 😊👍

