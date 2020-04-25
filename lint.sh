#!/bin/bash
pylama -l mccabe,pep257,pydocstyle,pep8,pycodestyle,pyflakes,pylint,isort -i D213 .
