# automooc
慕课自动化工具，针对超星播放器自动处理视频中题目
## 依赖
### windows
- python3
- python包：pillow selenium pytesseract
- tesseract-ocr(非必须，可提高效率)
- firefox及[geckodriver](https://github.com/mozilla/geckodriver/releases)
- 目前已知可运行在firefox v59.0.3和geckodriver v0.20.0上


### ubuntu

- ```sh
  sudo apt-get update
  sudo apt-get install -y firefox tesseract-ocr python3-pip
  pip3 install pillow selenium pytesseract
  ```

- 正确版本的[geckodriver](https://github.com/mozilla/geckodriver/releases)

- 目前已知可运行在firefox v59.0.2和geckodriver v0.20.0上

## 运行

1. 更新**gen_linkdata.py**中的用户名和密码以及geckodriver的路径
2. 运行**gen_linkdata.py**并在打开的界面中输入验证码并点击登陆
3. 点击想要刷的课程进入其待完成任务点列表，并将其url复制到运行**gen_linkdata.py**的终端内，回车后自动生成各课程链接文件linkdata
4. 在**automooc.py**同一目录下新建文件夹，名为figure
5. 更新**automooc.py**中的用户名和密码以及geckodriver的路径
6. 运行**automooc.py**并在打开的界面中输入验证码，**不**点击登陆
7. 在终端中输入任意字符并回车，刷视频开始
