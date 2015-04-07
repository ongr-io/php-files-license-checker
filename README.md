# Licence checker

Simple licence checker tool.
There are two scripts:
  - github_licence_checker.py
  - licence_replacer.py

### github_licence_checker.py
This scripts checks licenses in github repositories. Required libraries for this script are: [PyGithub]

`pip install PyGithub`

To run this script you need to edit the file `github_licence_checker.py`:
  - enter `github` login and password.
  - update `organization` if you need.
  - update `do_not_check` to skip others repositories.
  - run the script.

### licence_replacer.py
This script replaces all licences in provided directory.
Usage:
  - update `dir_name`.
  - run the script.
  
[PyGithub]:http://jacquev6.net/PyGithub/v1/