# Modern Blue Resume Template

一个适合中文技术岗求职的一页纸 XeLaTeX 简历模板。

模板风格偏现代、克制，适合用于：

- AI / LLM / Agent 工程师
- 深度学习算法实习生
- 机器学习 / 数据科学方向
- 计算机相关技术岗位
- 中文技术简历与实习简历

## 预览特点

- 一页纸紧凑排版
- 蓝色侧边 Section 标题
- 三行两列个人信息栏
- 右侧照片栏位
- 技能 Tag Pill 样式
- 支持 GitHub 项目链接
- 支持 ATS-friendly PDF 书签结构
- 适配 Overleaf XeLaTeX 编译

## 文件结构

```text
modern-blue-resume-template/
├── main.tex        # 简历主文件
├── photo.jpg       # 个人照片，可选
├── README.md       # 项目说明
├── .gitignore
└── LICENSE
````

## 使用方式

### 方式一：Overleaf 编译

1. 新建 Overleaf 项目
2. 上传 `main.tex`
3. 如果需要照片，上传一张照片并命名为 `photo.jpg`
4. 在 Overleaf 左上角菜单中将编译器设置为 **XeLaTeX**
5. 点击编译

### 方式二：本地编译

确保本地安装了 TeX Live 或 MacTeX，然后执行：

```bash
xelatex main.tex
```

如果需要多次刷新 PDF 书签，可以执行两次：

```bash
xelatex main.tex
xelatex main.tex
```

## 如何修改个人信息

在 `main.tex` 的 Header 区域修改姓名、岗位方向、邮箱、电话、GitHub、现居城市等信息：

```latex
{\fontsize{28pt}{30pt}\selectfont\bfseries\color{accent} 你的姓名}\\[6pt]
{\Large\bfseries AI Agent / LLM 应用工程师}\\[5pt]
```

个人信息栏采用三行两列结构：

```latex
邮箱：xxx@example.com      电话：(+86) xxx-xxxx-xxxx
GitHub：github.com/xxx    现居：澳门 / 深圳
意向城市：广州 / 深圳     可实习：立即到岗，每周 5 天
```

## 如何添加照片

将照片命名为：

```text
photo.jpg
```

然后放在和 `main.tex` 同一目录下。

如果没有上传照片，模板会自动显示一个照片占位框，不会影响编译。

## 如何修改颜色

模板主色在 `main.tex` 中定义：

```latex
\definecolor{accent}{HTML}{2563EB}
\definecolor{body}{HTML}{1F2937}
\definecolor{muted}{HTML}{6B7280}
```

其中：

* `accent`：主蓝色，用于标题、分隔线、技能标签
* `body`：正文颜色
* `muted`：辅助灰色文字

如果想换主题色，只需要修改 `accent` 即可。

例如改成深绿色：

```latex
\definecolor{accent}{HTML}{059669}
```

## 如何添加项目链接

项目命令格式如下：

```latex
\cvproject
{项目名称}
{项目时间}
{技术栈}
{GitHub 链接}
```

示例：

```latex
\cvproject
{Academic RAG with Hybrid Retrieval：中英文学术混合检索}
{2025.12 -- 2026.03}
{Python · ChromaDB · BGE-M3 · BM25 · Gradio}
{https://github.com/your-username/your-repo}
```

如果暂时没有项目链接，最后一个参数留空即可：

```latex
{}
```

## 如何修改技能标签

技能标签使用 `\skilltag{}` 命令：

```latex
\skillrow{LLM / Agent}{
  \skilltag{Claude API}
  \skilltag{DeepSeek / OpenAI API}
  \skilltag{MCP}
  \skilltag{ReAct}
}
```

可以根据岗位方向自行增删。

## ATS-friendly 说明

模板加入了 PDF metadata 和英文 PDF bookmark：

```latex
\pdfbookmark[1]{Education}{sec:education}
\pdfbookmark[1]{Projects}{sec:projects}
\pdfbookmark[1]{Skills}{sec:skills}
```

这样不会影响人眼看到的中文简历版式，同时能让部分 PDF 解析工具更容易识别简历结构。

注意：为了视觉效果，模板使用了图标、颜色和技能标签。若投递系统对 ATS 解析极其严格，可以另存一份纯文本 ATS 版本。

## 推荐编译环境

* Overleaf
* TeX Live 2023+
* MacTeX 2023+
* XeLaTeX

推荐使用 XeLaTeX，不建议使用 pdfLaTeX。

## 注意事项

1. GitHub 仓库名建议使用英文，例如：

```text
modern-blue-resume-template
```

2. 不建议在仓库名里使用中文。
3. 上传到 GitHub 前，建议删除自己的真实电话、邮箱或改成占位符。
4. 如果模板超出一页，可以优先调整：

   * `\fontsize{9.95pt}{11.35pt}`
   * `\usepackage[left=...,right=...,top=...,bottom=...]{geometry}`
   * `itemsep`
   * 项目 bullet 数量

## License

本模板使用 MIT License。你可以自由使用、修改和分发。

