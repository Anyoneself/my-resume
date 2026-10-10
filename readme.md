# 刘元智的 LaTeX 简历

使用 TeX Live / XeLaTeX 编译的中文简历。当前版本为两页，保留原简历文字、照片、校徽和背景，在实习经历标题右侧加入对应公司图标。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| `刘元智_简历.tex` | 简历源码，修改内容和版式的主要入口 |
| `刘元智_简历.pdf` | 当前编译结果，可直接预览 |
| `刘元智 (18).pdf` | 原始简历，作为内容核对基准 |
| `编译简历.sh` | 自动调用 XeLaTeX 两次并更新根目录 PDF |
| `核对简历.py` | 比较原始 PDF 和编译结果的文字 |
| `assets/` | 照片、校徽、背景及公司图标 |
| `tmp/pdfs/` | 编译日志、辅助文件和预览图片，不提交到 Git |
| `assets/texmf/` | 本机补充的中文宏包及字体，不提交到 Git |

## 如何修改

使用支持 UTF-8 的编辑器打开 `刘元智_简历.tex`，直接修改对应文字。请勿只修改 PDF：PDF 是由源码生成的，下一次编译会覆盖根目录的同名结果。

### 文字和经历

- 姓名、电话、邮箱等信息在 `\begin{document}` 后的页首区域。
- 教育、项目、研究等条目的标题和日期使用 `\entry{标题}{日期}`。
- 各节标题使用 `\sectionline{标题}`。
- 实习标题使用 `\internship{公司名称}{图标路径}{日期}`。
- 列表中的每条内容以 `\item` 开头；重点文字用 `\textbf{文字}`。
- 研究链接使用 `\href{网址}{显示文字}`。

例如，修改公司名称、图标和日期：

```tex
\internship{Shopee（北京）}{assets/shopee.png}{2025年09月 - 至今}
```

添加一个功能点时，将它放入对应的 `itemize` 环境：

```tex
\begin{itemize}
  \item \textbf{功能点：}这里填写具体工作内容和结果；
\end{itemize}
```

LaTeX 中的特殊字符需要转义：百分号写成 `\%`，下划线写成 `\_`，与号写成 `\&`，井号写成 `\#`，美元符号写成 `\$`。普通中文、英文和数字可以直接输入。

### 图片和公司图标

| 图片 | 内容 |
| --- | --- |
| `assets/X84.png` | 个人照片 |
| `assets/X85.png` | 中国石油大学校徽及校名 |
| `assets/X4.png` | 页首背景 |
| `assets/shopee.png` | Shopee 图标 |
| `assets/bytedance.png` | 字节跳动图标 |
| `assets/aisphere.png` | 爱诗科技图标 |

替换图片时，可以保持原文件名，也可以修改源码中的 `\includegraphics` 或 `\internship` 图片路径。优先使用透明背景 PNG 或矢量 PDF。图片文件必须随源码一起保留。

公司图标尺寸在文件顶部的 `\internship` 定义中统一设置：

```tex
\includegraphics[width=15pt,height=15pt,keepaspectratio]{#2}
```

调整 `15pt` 可以改变图标大小；`keepaspectratio` 用于保持原始比例。`\raisebox{-3pt}` 调整垂直位置，`\hspace{9pt}` 调整图标与日期之间的距离。

### 版式

常用设置位于源码顶部：

| 设置 | 作用 |
| --- | --- |
| `geometry` 的 `left/right/top/bottom` | 页边距，目前均为 `8mm` |
| `\fontsize{9.5}{12.1}\selectfont` | 正文字号和基础行距，单位为 pt |
| `\setlength{\parskip}{2pt}` | 段落间距 |
| `\setlist[itemize]{...}` | 列表缩进和条目间距 |
| `resumeBlue`、`resumePale` | 标题、分隔线和标签颜色 |
| `\newpage` | 项目经历中预设的分页位置 |

新增文字后可能变为三页。请先检查冗余内容和段落间距，再酌情调整字号或分页位置；编译后确认标题、日期、图标和正文没有重叠。

## 如何编译

### 1. 准备环境

需要安装 TeX Live（macOS 上可使用 MacTeX 或 BasicTeX），并确保包含 XeLaTeX。

完整版 TeX Live 通常已包含所需宏包。精简安装需要补齐：

```sh
tlmgr install ctex xecjk zhnumber fandol enumitem pgf eso-pic geometry fontspec hyperref xcolor
```

宏包安装是否需要管理员权限取决于 TeX Live 的安装方式。不要使用 `pdflatex` 编译此源码。

英文主字体为 `Times New Roman`，需在操作系统中安装该字体。若没有，可将源码中的：

```tex
\setmainfont{Times New Roman}
```

替换为 TeX Live 自带的：

```tex
\setmainfont{TeX Gyre Termes}
```

中文字体使用 Fandol，由 `fandol` 宏包提供。

### 2. 推荐：使用脚本

在仓库根目录执行：

```sh
sh 编译简历.sh
```

脚本会：

1. 切换到脚本所在目录。
2. 将 `assets/texmf/` 设为本地宏包目录；标准 TeX Live 的系统宏包仍会被搜索。
3. 调用 XeLaTeX 两次，更新链接和 PDF 信息。
4. 将日志、辅助文件及中间 PDF 写入 `tmp/pdfs/`。
5. 仅在两次编译均成功后，更新根目录的 `刘元智_简历.pdf`。

若 PATH 中找不到 `xelatex`，脚本会尝试 macOS 的 `/Library/TeX/texbin/xelatex`。Linux 或 Windows 环境应将 XeLaTeX 加入 PATH；Windows 可以使用 Git Bash 运行脚本，或使用下面的手动命令。

### 3. 手动编译

在已安装所需系统宏包的环境中，于仓库根目录执行：

```sh
xelatex -interaction=nonstopmode -halt-on-error 刘元智_简历.tex
xelatex -interaction=nonstopmode -halt-on-error 刘元智_简历.tex
```

这些命令将 PDF 和辅助文件输出到根目录。如果依赖本机的 `assets/texmf/`，请使用编译脚本，它会自动设置宏包搜索目录。

### 4. 检查结果

打开 `刘元智_简历.pdf`，检查页数、中文显示、图片、日期对齐和分页。

编译失败时，先查看 `tmp/pdfs/刘元智_简历.log` 中的第一个错误：

- `File ... not found`：检查宏包是否安装、图片路径是否正确。
- `The font ... cannot be found`：安装指定字体或替换为可用字体。
- `Missing character`：当前字体缺少相应字符。
- `Overfull \hbox`：某行超宽，检查长链接、文字长度或布局宽度。

不要移动或删除 `assets/` 后单独编译 `.tex` 文件。

## 可选：核对原文

安装 Python 依赖后执行：

```sh
python3 -m pip install pdfplumber
python3 核对简历.py
```

脚本比较原始 PDF 和当前 PDF 的全部文字，忽略排版空格、列表符号和原始 PDF 中的部分 Unicode 异体编码。文字相同时返回退出码 0，否则列出差异并返回退出码 1；页数会打印出来，但不作为通过条件。

此检查用于验证重排没有改变原文。主动修改简历内容后，与旧 PDF 出现差异是正常的，不必为了通过检查恢复旧内容。该脚本不能代替版式检查。

## 更新 GitHub

修改并编译检查后，提交需要同步的文件：

```sh
git status
git add readme.md 刘元智_简历.tex 刘元智_简历.pdf assets 编译简历.sh 核对简历.py .gitignore
git commit -m "Update resume"
git push origin main
```

本机补充宏包、编译辅助文件及临时预览由 `.gitignore` 排除。仓库包含个人联系方式、照片和简历内容，变更仓库可见性或分享前请确认这些信息适合公开。
