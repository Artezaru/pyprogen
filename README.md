# pyprogen

## Description

Generating Python project from Command Line Interface.

```
pyprogen
```

![pyprogen CLI]{pyprogen/ressources/pyprogen_CLI.png}

## Author

- Name: Artezaru
- Email: artezaru.github@proton.me
- GitHub: https://github.com/Artezaru/pyprogen.git

## Installation

Install with pip

```
pip install git+https://github.com/Artezaru/pyprogen.git
```

Clone with git

```
git clone https://github.com/Artezaru/pyprogen.git
```

## Documentation

Generate the documentation with sphinx
1. Install the sphinx package and the pydata-sphinx-theme

```
pip install sphinx
pip install pydata-sphinx-theme
```

2. Generate the documentation

```
make html
```

3. Open the documentation in a web browser

```
open docs/build/html/index.html
```


echo You can also use LateX to generate a PDF \(LateX must be install\)
1. Install the sphinx package and the pydata-sphinx-theme

```
pip install sphinx
pip install pydata-sphinx-theme
```

2. Generate the documentation

```
make html
```

3. Open the documentation in a web browser

```
open docs/build/latex/pyprogen.pdf
```

## License

See LICENSE
