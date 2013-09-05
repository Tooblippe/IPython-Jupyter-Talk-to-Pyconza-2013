IPython Notebooks and the Python Scienctific Stack
---

[IPython](http://ipython.org/) in action creating reproducible and publishable interactive work.

What is this?
------

This repo contains the full [talk](http://za.pycon.org/talks/10/) I indend to deliver (have delivered) at [PyConZA2013](http://za.pycon.org/). It contains all the files needed to build a final publishable PDF document and even adds a customer front page.

[The Complete Talk GitHub Website can be accessed here][6]

Background
-------------
IPython had become a popular choice for doing interactive scientific work. It extends the standard Python interpreter and adds many usefull new futures. There is realy no need to use the standard Python interpreter anymore.
In addition to this IPython offers a web based Notebook that makes interactive work much easier,and have been used to write repeatable scientific papers and more recently a book has been written using this platform, the online Notebook Viewer and GitHub. The development of this material and toolchain to compile the notebook to a publishable PDF, has inspired me to maybe even try and turn this into a complete (free) book. Lets see what happens.

Combining the most common scientific packages with IPython makes it a formidable tool and serious competition to R. ( _R is still awesome!_ )

As a matter of fact you can run R in the notebook session, embed YouTube Videos, Images and lots more but let me not get ahead of myself....

The science stack consists of (but not limited to):

package  |  description
---  |  ---
[pandas][1]  |  `dataframe` implementation (based on numpy)
[scipy][2]  |  efficient numerical routines
[sympy][3]  |  `symbolic mathematics`
[matplotlib][4]  |  python standard `plotting` package
[sci-kit learn][5] | machine learning and `well documented!`

Talk contents
--------
The talk will aim to introduce these tools and give some practical examples. Once completed it will be shown how easy it is to publish your work to various formats. Some of the topics covered in the talk are lister below:

item   | description
---- |  -------
ipython | quick intro to ipython and the notebook
setup  | set up your environment / get the talk files
notebook basics | navigate the notebook
notebook magics | special notebook commands that can be very usefull
getting input   | as from IPython 1.00 getting input from sdtin is possible
local files | how to link to local files in the notebook directory
plotting	| how to create beautifull inline plots
symbolic math | quick demo of sympy model
pandas  | quick intro to pandas dataframe
typsetting | include markdown, Latex via MathJax
loading code | how to load a remote .py code file
gist         | paste some of your work to gist for sharing
js		| some javascript examples
customising | loading a customer css and custom matplotlib config file
git cell    | add code to a special cell that would commit to git
output formats | how to publish your work to html, pdf or jeveal.js presentation


Get the talk files here
------
format  | description
------- | ------------
[IPython notebook](https://github.com/Tooblippe/zapycon2013_ipython_science/blob/master/src/pycon13_ipython.ipynb)  |  .ipynb file to run in browser
[IPython html notebook](http://htmlpreview.github.io/?https://github.com/Tooblippe/zapycon2013_ipython_science/blob/master/src/output/pycon13_ipython.html) | converted to HTML and served online
[IPython pdf notebook](https://github.com/Tooblippe/zapycon2013_ipython_science/blob/master/src/output/pycon13_ipython_pdf.pdf?raw=true)  | converted to PDF for download (to be added, needs pandoc)
[IPython pdf book](https://github.com/Tooblippe/zapycon2013_ipython_science/blob/master/src/output/pycon13_ipython_complete.pdf?raw=true)  | converted to pdf and frontpage stitched to it)
[Ipython reveal.js presentation](http://htmlpreview.github.io/?https://github.com/Tooblippe/zapycon2013_ipython_science/blob/master/src/output/pycon13_ipython.slides.html#/) | converted to a reveal.js presenation and served online
[Online IPython NBveiwer](http://nbviewer.ipython.org/urls/raw.github.com/Tooblippe/zapycon2013_ipython_science/master/src/pycon13_ipython.ipynb)  | view on the ipython notebook viewer


Dependancies
-------------
I was given the challenge to develop all of this on a Windows machine as some of my sponsers want to demostrate that this stuff can not only be done on GNU/Linux/OSX. So all the toolchains are Windows based. If you know Linux, then you are the type of person that would easily port this. That being said the Windows GitHub client is refressing.

package  |  description
-------- | ------------
IPython  | To use NBConvert you need V1.00. If you only want to use the interactive notebook then v0.13 will be ok.
pandoc 	 | The document converter used by IPythonr
MikeTex  | If you want to do a TEX to PDF transform. I had so many issues with the TEX to PDF conversion by NBConvert, so settled for wkhtmltopdf(below) to convert HTML to PDF rather. (Convert notebook to HTML with NBconvert and then from HTML to PDF with wkhtmltopdf
wkhtmltopdf  | Convert HTML to PDF
pdftk   |  Can be used to combine PDF's. In this case add a frontpage to the generated IPython notebook PDF.
ImageMagick | for compressing the PDF
GhostScript | needed by ImageMagick
anaconda  | install anaconda from Continuum Analystics. Almost all the Python packages are included and it has a virtual environment manager via it's console application `conda'

 
How to run the Interactive Notebook
--------
Navigate to the `src` directory and run from the command line:

 ```python
      ipython notebook
```

If everything works your browser should open and you can select the `notebook` and start experimenting!
 
PDF, HTML, SlideShow Build Script
------------
There is a build script in the `src` directory. It is an IPython file. You can basicaly build shell scripts this way. To use the power of IPython commands save the file with the `.ipy' extension and call it with IPython. Even the magics work. To build the document use `ipython builddocs.ipy` You will have to change the paths to the software however.


Some interesting links
-----------------------
* [A book written with IPython Notebook][7]
* [Notebook Viewer][8]
* [Anaconda - Installing almost everything you need][9]


About the presenter
----------
* I am an Electrical Engineer and is currently working for a [consulting firm][10] where I manage the Business Analytics and Quantitative Decision Support Services division.
* I use python in my day to day work as a practical alternative to the limitations of EXCEL in using large data sets.
* [LinkedIn][11]
* I am also a co-founder at [House4Hack][12]



  [1]: http://pandas.pydata.org/
  [2]: http://www.scipy.org/
  [3]: http://sympy.org/en/index.html
  [4]: http://matplotlib.org/
  [5]: http://scikit-learn.org/
  [6]: http://tooblippe.github.io/zapycon2013_ipython_science
  [7]: http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/
  [8]: http://nbviewer.ipython.org/
  [9]: http://www.continuum.io/downloads
  [10]: http://www.eon.co.za/index.php/our-services-main/our-services/business-analytics
  [11]: http://www.linkedin.com/in/tobienortje
  [12]: http://www.house4hack.co.za/