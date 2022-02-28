> # 🇺🇦 UKRAINE NEEDS YOUR HELP NOW!
>
> I'm the creator of this project.
>
> **Ukraine, [is being invaded by the Russian Federation, right now](https://www.bbc.com/news/world-europe-60504334)**.
> Russia is hitting target all over the country by ballistic missiles.
>
> Ukrainian National Bank opened [an account to Raise Funds for Ukraine’s Armed Forces](https://bank.gov.ua/en/news/all/natsionalniy-bank-vidkriv-spetsrahunok-dlya-zboru-koshtiv-na-potrebi-armiyi):
>
> ```
> SWIFT Code NBU: NBUA UA UX
> JP MORGAN CHASE BANK, New York
> SWIFT Code: CHASUS33
> Account: 400807238
> 383 Madison Avenue, New York, NY 10179, USA
> IBAN: UA843000010000000047330992708
> ```
>
> Bitcoin / Eth [Original Ukraine Govt tweet](https://twitter.com/Ukraine/status/1497594592438497282)
>
> BTC - 357a3So9CbsNfBBgFYACGvxxS6tMaDoa1P
> ETH and USDT (ERC-20) - 0x165CD37b4C644C2921454429E7F9358d18A45e14
>
> You can also donate to [charity supporting Ukrainian army](https://savelife.in.ua/en/donate/).
>
> **THANK YOU!**

> NB: I wrote a vscode extension that does the same thing this script does, but a bit more polished.

https://github.com/TheFern2/vscode-gutenberg

https://marketplace.visualstudio.com/items?itemName=TheFern.vscode-gutenberg

# Exporting a markdown book to PDF with Pandoc

I have been wanting to write a book for some time now. I've accumulated lots of experience both in my career as automation and controls engineer, and on my own I have learned tons in software engineering, game dev, etc, the list is huge.

All this stuff rattling in my head needs to come out at some point, at my job and for my personal projects I tend to document very well and that has pushed me to get better at writing.

I have decided to write maybe a few books in markdown, well we'll see how the first one goes.

## Setup

The markdown editor that you use makes no difference, I use [Typora](https://www.typora.io/). If you are not sure vscode has pretty good support for markdown files, and most text editors do. @awwsmm did a great write up on markdown editors [state-of-markdown-editors-2019](https://dev.to/awwsmm/state-of-markdown-editors-2019-2k49)

In addition to that, I use [Pandoc](https://pandoc.org/), you'll need LaTeX to print PDFs, make sure to follow the [instructions](https://pandoc.org/installing.html).

## Debian (Ubuntu)

Extra info:
https://linuxconfig.org/how-to-install-latex-on-ubuntu-20-04-focal-fossa-linux

```
sudo apt install pandoc
```

If you prefer latest binary then head over to releases:
https://github.com/jgm/pandoc/releases/

To export to pdf you need pdflatex which is in the below package:

```
sudo apt install texlive-latex-base
```

Follow this gists for full installation + fonts:
https://gist.github.com/rain1024/98dd5e2c6c8c28f9ea9d

For Latex, I am using MiKTeX:
https://miktex.org/download

This is a lot of experimentation, I had to switch to xelatex engine. When the python script is ran, you'll get a popup for MiKTeX as is trying to install required packages, and there are a lot. I recomment unchecking the checkbox, or it wil be a tons of clicking to accept hundreds of small packages.

## Exporting to PDF

> NB: The script relies on the numbering of the folders, and markdown files. Ensure you add a sequential numbers to chapter folders, and md files within the chapters. If you don't have chapter folders, then ensure your md files have sequential numbers. Folders and md files can be named anything.

I structured my chapters in directories, like shown below:

```
├── book
│   ├── Chapter1
│   │   ├── Scene1.md
│   │   └── Scene2.md
│   └── Chapter2
│       └── Scene1.md
├── images
│   └── lostbook.jpg
└── title.txt
```

> New addition to the `export_book.py` script, now it supports md files without chapter directories:

```
├── book_2
│   ├── Scene1.md
│   ├── Scene2.md
│   └── Scene3.md
├── images
│   └── lostbook.jpg
└── title.txt
```

The title is like a header for pandoc:

```
---
title: Book Example
author: Fernando B.
rights: Nah
language: en-US
---
```
### Pandoc Resources
- [Getting Started](https://pandoc.org/getting-started.html)
- [Demos](https://pandoc.org/demos.html)

The below command will add table of contents, output to book.pdf, get title info from title.txt and grab three markdown files.
```
pandoc --toc -o book.pdf title.txt .\book\Chapter1\Scene1.md .\book\Chapter1\Scene2.md .\book\Chapter2\Scene1.md
```

## Going beyond the command line

As you can imagine as your book grows, things will get harder to compile. I couldn't find a library or an easy parameter that takes a list of md files in a directory so I wrote a python script [export_book.py](https://github.com/kodaman2/markdown-book/blob/master/export_book.py).

> NB: Before you try `export_book.py` there's a simple command you can use, if you have a single directory with markdown files, the caveat is that all files need to be in a single directory. Chances are if you're writing a book, you're using multiple directories structure:

```
pandoc --toc ./book/*.md -o book.pdf
```

The script supports a few arguments:
```
usage: export_book.py [-h] -p ROOT_PATH [-c] [-f FILE_EXTENSION]

optional arguments:
  -h, --help            show this help message and exit
  -p ROOT_PATH, --root-path ROOT_PATH
                        Root path for book files
  -c, --using-chapter-folders
                        Are you using folders for chapters?
  -f FILE_EXTENSION, --file-extension FILE_EXTENSION

Examples:

python3 export_book.py -p /path/to/book
python3 export_book.py -p /path/to/book -c
python3 export_book.py -p /path/to/book -f rst
```
> NB: Other file extensions other than md, markdown, have not been tested proceed with caution. If it works let me know.

## Other items to think about
I need to experiment with css for formatting the book a bit better and adding header and footer, and so on, but this is a good start for anyone trying to accomplish the same or even writing academic papers as pandoc can output to different formats.
