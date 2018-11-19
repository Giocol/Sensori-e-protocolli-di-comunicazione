# POuL reveal.js template

This is a base template that will allow you to make state-of-art presentations
using advanced technologies such as Markdown, reveal.js (thus the
industry-standard language JavaScript), still complying with the mandatory
design guidelines.

## How do I use this thing?

### Where do I write my stuff?

[Download][download] this repo and put your content inside the 'content.md'
file placed in the root of this directory. What were you expecting?

### How do I write my stuff?

Using a text editor and typing Markdown syntax on your keyboard.

[Here][markdown-guide] you can find a comprehensive guide to the syntax.

Remember to use three dashes (`---`) to create a new slide horizontally and
four dashes (`----`) to create a new one vertically.

### How do I see my stuff?

Make sure you have Python 3 installed. Nothing more is required.

Make the deploy.py script executable with

    chmod +x deploy.py

Then just run

    ./deploy.py --show

A new tab will open in your default browser showing the presentation.

You can spacify your browser using the `BROWSER` environment variable.

    BROWSER=surf ./deploy.py --show

You can see what kind of trickery this script is able to do running it with the
`-h` or `--help` flag.

#### Why?

This is required since modern browsers won't allow you to include a local file
(the Markdown document) from JavaScript.

The Python script will run a small HTTP server and fix this issue.

## How do I make a PDF out of the slides?

Append `?print-pdf` at the end of the URL.

For instance if you're running the `deploy.py` script locally the URL will be
something like `http://127.0.0.1:8080/?print-pdf`.

Then just use the print function of your browser to make a PDF of the page.


[download]: https://gitlab.poul.org/corsi/revealjs-poul/repository/archive.zip?ref=master
[markdown-guide]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
