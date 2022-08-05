# nuitka示例

## 准备工作

需要一个支持 C11 或 C++03 1的编译器，

可以使用 mingw64 或 Visual Studio 2022 或更高版本。

mingw64 在 https://sourceforge.net/projects/mingw-w64/ 下载
Visual Studio 2022 在  https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx 下载。

## 创建环境

    poetry install
    poetry shell

打包命令

    python -m nuitka hello.py