---
output:
  pdf_document:
    citation_package: natbib
    keep_tex: true
    fig_caption: true
    latex_engine: pdflatex
    template: ~/Dropbox/miscelanea/svm-r-markdown-templates/svm-latex-ms.tex
title: "Python Decorators"
thanks: "Replication files are available on the author's Github account (http://github.com/svmiller). **Current version**: `r format(Sys.time(), '%B %d, %Y')`; **Corresponding author**: svmille@clemson.edu."
author:
  - name: Steven V. Miller
    affiliation: Clemson University
abstract: "This document provides an introduction to R Markdown, argues for its benefits, and presents a sample manuscript template intended for an academic audience. I include basic syntax to R Markdown and a minimal working example of how the analysis itself can be conducted within R with the `knitr` package."
keywords: "pandoc, r markdown, knitr"
date: "`r format(Sys.time(), '%B %d, %Y')`"
geometry: margin=1in
fontfamily: mathpazo
fontsize: 11pt
# spacing: double
bibliography: ~/Dropbox/master.bib
biblio-style: apsr
endnote: no
---
