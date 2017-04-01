# Rabidus-Scriptor.py

"Rabidus-Scriptor" is a little experiment to create a Google Blogger, text-based client, using git, Python the [Elementree Library](https://pypi.python.org/pypi/elementtree/) and the [Google Data Python Library](https://github.com/google/gdata-python-client) to handle their API. 

# Premises

The following are a sequence of steps followed to prepare our system to be able to properly run-and-create TwoEatMe. This may serve you in case you want to play with the code.

Usage of it relies on your own responsibility: it's not Rocket Science, but in case something goes wrong, you are fully responsible for the use of it (the intended usage of whatever I put in here is for my own personal use).

Please [report bugs here](https://github.com/nomagev/twoeat/issues) if you find one.

The code and the things contained within the repository (excluding content accessible through links) are offered under a [GPL 2.0 License](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html): Sharing is caring.

# Dependencies

To run this code, you may need to have installed in your computer or have available to the following set of components:

  1. **Python:** you need to have Python installed. I am working with Python 2.X, so I am not sure on whether the code may work with Python 3.X.
  2. **Python pip:** you need to have Python pip installed. This normally may be available on your Python Installation. Otherwise, please check [the Python Pip Page](https://pypi.python.org/pypi/pip/).
  3. **Elementtree:** you may need to have the Elementtree Python Library Installed (in later Python 2.X versions, it should come already installed). If that was not the case, assuming Steps 1 and Step 2 are already covered ([Python](https://www.python.org) and [Pip](https://pypi.python.org/pypi/pip/)), go into your terminal and shell and run `pip install elementtree`.
  4. **Google API Python Client:** you need the Google API Python Client Library Installed (if that was not the case, assuming Steps 1 and Step 2 are already covered ([Python](https://www.python.org) and [Pip](https://pypi.python.org/pypi/pip/)), go into your terminal and shell and run `pip install google-api-python-client`.
  5. **Google Account:** You may need a [Google Account](https://www.google.com/accounts).
  6. **Google Blogger API Credentials:** you may need the [Google Blogger API Credential](https://developers.google.com/blogger/docs/3.0/using) to gain the required credentials you need to interact with it (checking whether this is really needed or not).

# Program

The program is hosted under the [master folder](https://github.com/nomagev/Rabidus-Scriptor/) on this repository (check 'Rabidus-Scriptor.py').

You can run it on your terminal (do not forget to check the "Dependencies" on the section above) or your Command Prompt by copying your file on your local drive and, on the same folder, run 'python Rabidus-Scriptor.py'.

# Current Status (as of April 1st 2017)

Not defined Yet.

# Road map

__[master branch](https://github.com/nomagev/Rabidus-Scriptor)__

- [ ] Dependency checks (Google Library, chcp, Google API Key)

__[next-release branch](https://github.com/nomagev/Rabidus-Scriptor/tree/next-release)__

- [ ] Display Menu with options:
  - [ ] Publish a Post.
  - [ ] Check Existing Post.
  - [ ] Quit the Program and re-establish prompt preconditions (i.e. chcp)
- [ ] Review and Improve Code Quality

__Future: [See Issues Page](https://github.com/nomagev/Rabidus-Scriptor/issues)__

- [ ] Enter **YOUR** idea or request in [the issues area](https://github.com/nomagev/Rabidus-Scriptor/issues).

