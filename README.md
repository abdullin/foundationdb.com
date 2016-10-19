# foundationdb.com

`import.py` is a script that downloads foundationdb.com site from the internet archive and cleans it up by making all links relative. This makes is possible to browse documentation locally without an http server.

Not all links are available (e.g. courses are missing).

This repository also contains a copy of the site recovered with `import.py`.

## Usage

1. __To view docs online__: go to [html preview](https://htmlpreview.github.io/?https://raw.githubusercontent.com/abdullin/foundationdb.com/master/doc/key-value-store/documentation/index.html).

2. __To view docs locally__: clone the repository, then open `doc/key-value-store/documentation/index.html`.

3. __To regenerate the site__: run `import.py` as a shell script (uses Python)
