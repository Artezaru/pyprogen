# pyprogen

## Description

CLI PYthon PROject GENerator.

Once install on your python environment, running the following ``pyprogen`` command will create a project with thegiven structure:

```
pyprogen
├── pyprogen
│   ├── __init__.py
│   ├── __main__.py
│   ├── __version__.py
│   ├── ressources
│   │   ├── __init__.py
├── tests
│   └── __init__.py
├── examples
│   └── example.py
├── laboratory
│   └── laboratory.py
├── venv
├── docs
│   ├── source
│   │   ├── conf.py
│   │   ├── index.rst
│   │   ├── installation.rst
│   │   ├── usage.rst
│   │   └── api.rst
│   └── build
│       ├── html
│       └── latex
├── .github
│   └── workflows
│       └── sphinx.yml
├── README.md
├── LICENSE
├── Makefile
├── requirements.txt
├── pyproject.toml
├── .bumpver.toml
├── .gitlab-ci.yml
└── .gitignore
```

This structure include:

- Virtual Environment
- pyproject.toml tools
- Sphinx documentation
- Deploy documentation
- Git Repository
- And tools as bumpver / pyinstaller / pytest / etc ...

## Authors

- Artezaru <artezaru.websites@proton.me>

- **Git Plateform**: https://github.com/Artezaru/pyprogen.git
- **Online Documentation**: https://Artezaru.github.io/pyprogen

## Installation

Install with pip

```
pip install git+https://github.com/Artezaru/pyprogen.git
```

Clone with git

```
git clone https://github.com/Artezaru/pyprogen.git
```

## License

See LICENSE
