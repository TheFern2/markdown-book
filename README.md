# Exporting a markdown book to PDF with Pandoc

I have been wanting to write a book for some time now. I've accumulated lots of experience both in my career as automation and controls engineer, and on my own I have learned tons in software engineering, game dev, etc, the list is huge.

All this stuff rattling in my head needs to come out at some point, at my job and for my personal projects I tend to document very well and that has pushed me to get better at writing.

I have decided to write maybe a few books in markdown, well we'll see how the first one goes.

## Setup

The markdown editor that you use makes no difference, I use [Typora](https://www.typora.io/). If you are not sure vscode has pretty good support for markdown files, and most text editors do. @awwsmm did a great write up on markdown editors [state-of-markdown-editors-2019](https://dev.to/awwsmm/state-of-markdown-editors-2019-2k49)

In addition to that, I use [Pandoc](https://pandoc.org/), you'll need LaTeX to print PDFs, make sure to follow the [instructions](https://pandoc.org/installing.html).

## Exporting to PDF

I structured my chapters in directories, like shown below:

```
├───title.txt
├───Chapter1
├───Chapter2
└───images
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
pandoc --toc -o book.pdf title.txt .\Chapter1\Scene1.md .\Chapter1\Scene2.md .\Chapter2\Scene1.md
```

## Going beyond the command line

As you can imagine as your book grows, things will get harder to compile. I couldn't find a library or an easy parameter that takes a list of md files in a directory so I wrote a python script [export_book.py](https://github.com/kodaman2/markdown-book/blob/master/export_book.py). For now the script needs to be in the book root directory, but in the future I will probably expand on it.

[Full Repo](https://github.com/kodaman2/markdown-book)

## Other items to think about
I need to experiment with css for formatting the book a bit better and adding header and footer, and so on, but this is a good start for anyone trying to accomplish the same or even writing academic papers as pandoc can output to different formats.