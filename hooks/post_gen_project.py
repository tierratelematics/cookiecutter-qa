#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(*filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, *filepath))


def remove_folder(*folderpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, *folderpath))


if __name__ == '__main__':
    # used by third party as good known versions reference
    remove_file('requirements_functional.txt')

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs', 'authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        remove_file('{{ cookiecutter.project_slug }}', 'cli.py')

    if '{{ cookiecutter.testrail }}' == 'n':
        remove_file('testrail.cfg')

    if '{{ cookiecutter.pytest_play }}' == 'n':
        remove_folder('{{cookiecutter.project_slug}}', 'tests', 'play')
