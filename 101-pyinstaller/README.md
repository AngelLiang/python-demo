# pyinstaller 打包示例

## 快速开始

    # -F 选项，打包成一个exe文件，默认是 -D，意思是打成一个文件夹。
    pyinstaller -F main.py

去掉命令行黑框

    # -w 选项可以打桌面程序，去掉命令行黑框
    pyinstaller -F -w main.py

修改程序默认图标

    # -i 可以设置图标路径，将图标放在根目录：
    pyinstaller -F -w -i gen.ico TestDataGen.py
