"""
 * This file is part of the ONGR package.
 *
 * (c) NFQ Technologies UAB <info@nfq.com>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
"""

import os

licence = 'licence.txt'
dir_name = '/Users/mantjonu/Sites/CategoryManagerBundle'

extensions = ['php']
skip_dirs = ['cache', 'vendor', '.git', '.vagrant', 'app']


def read_file(file):
    with open(file, 'r') as f:
        return f.readlines()

licence_data = read_file(licence)


def check_licence(file):
    with open(file, 'r') as f:
        data = f.read()
        return licence in data


def replace_licence(file):
    end_symbol = ' */\n'
    licence_text = ['<?php'] + ['\n\n'] + licence_data
    data = read_file(file)
    end_symbol_index = data.index(end_symbol)
    new_data = licence_text + data[end_symbol_index + 1:]
    os.remove(file)
    with open(file, 'w') as f:
        for s in new_data:
            f.write(s)


def check_dir(path):
    for root, dirs, files in os.walk(path):
        for i in skip_dirs:
            if i in dirs:
                dirs.remove(i)
        for ext in extensions:
            for file in files:
                if file.endswith(ext):
                    print file
                    replace_licence(os.path.join(root, file))


check_dir(dir_name)
