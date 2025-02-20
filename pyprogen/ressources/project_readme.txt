# {package_name}

## Description

## Author

- Name: {author_name}
- Email: {author_email}
- GitHub: {author_github}

## Installation

Install with pip

```
pip install git+{author_github}
```

Clone with git

```
git clone {author_github}
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
open docs/build/latex/{package_name}.pdf
```

## License

See LICENSE
