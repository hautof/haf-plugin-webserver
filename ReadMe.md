### haf plugin web server

    The plugin web server of haf

[![Build Status](https://travis-ci.org/hautof/haf-plugin-webserver.svg?branch=master)](https://travis-ci.org/hautof/haf-plugin-webserver)
[![PyPI](https://img.shields.io/pypi/v/hafapiserver.svg)](https://img.shields.io/pypi/v/hafapiserver.svg)

### How to get it?

> by pip tool

```shell
    tsbx-mw# pip install hafapiserver
```

> by src

```shell
    tsbx-mw# git clone https://github.com/hautof/haf-plugin-webserver ./
    tsbx-mw# python setup.py install
```

### usage

> using as haf params

```bash
    python -m haf run -ws=True
```

> using as haf config

```json
    {
        "run":
        {
            "web_server": {
            "host": "",
            "port": "",
            "run": true
        }
    }

```