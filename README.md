# conversion_tofix

* Clone this repository to Comet
* Test it running `python test_conversion.py`, does it fail?
* Identify the commit causing the bug with `git bisect`, see <https://git-scm.com/docs/git-bisect>
* Create a new branch `fix_bug`
* Undo it with `git revert` <https://git-scm.com/docs/git-revert>
* Try to push it back to the original repository with `git push origin fix_bug`, does it work?
* Fork the repository under your Github account through the Github website
* Rename the `origin` remote to `upstream` <https://help.github.com/articles/renaming-a-remote/>
* Add your **fork** of the repository as a remote to the repository on Comet
* `git push` your `fix_bug` to your repository
* Go to <https://github.com/zonca/conversion_tofix>, create a Pull Request!

