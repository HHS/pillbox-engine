## Pillbox Documentation [link](http://hhs.github.io/pillbox-engine/)

Pillbox Documentation is powered by [mkdocs](http://www.mkdocs.org).

To run the documentation site locally make sure you have mkdocs installed:

    $: pip install mkdocs

And then run:

    $: mkdocs server

To build the a new documentation run:

    $: mkdocs build --clean

To copy the built documentation to gh-pages branch run:

    $: git subtree push --prefix docs/site origin gh-pages
