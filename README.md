# conversion_tofix

## 1) Make a test

* Clone this repository to your home folder
* Test it running `python test_conversion.py`, does it fail?
* Checkout the code version just before the last commit, does it still fail? How do you go back to the last commit?

## 2) Bisect

* Identify the commit causing the bug with `git bisect`, see <https://git-scm.com/docs/git-bisect>

## 3) Fix in branch

* Create a new branch `fix_bug`
* Undo it with `git revert` <https://git-scm.com/docs/git-revert>

## 4) Create Pull Request

* Try to push it back to the original repository with `git push origin fix_bug`, does it work?

### Using the Github cli

* Look at `gh` docs at <https://cli.github.com/>
* Create fork, push the branch to fork and create a PR all from the command line

### Using the Github website

* Fork the repository under your Github account through the Github website
* Rename the `origin` remote to `upstream` <https://help.github.com/articles/renaming-a-remote/>
* Add your **fork** of the repository as a remote to the repository on Comet
* `git push` your `fix_bug` to your repository
* Go to <https://github.com/zonca/conversion_tofix>, create a Pull Request!

## 5) Synchronize upstream

* I will create a new commit in my repository
* Create 2 branches, test `rebase` in one and `merge` in the other
* After merge, inspect with `git log --graph --oneline`

## 6) Synchronize upstream with conflicts

* I will create a new commit in my repository with a conflict
* Do a rebase and handle conflicts

## 7) Erase commit

* Use `git rebase` to completely wipe the commit from history
* Try to push

## 8) Hard reset

* Wipe the last commit with `git reset --hard`

## 9) Github actions

* Setup a Github action to test the code on the `main` branch of your fork

## 10) Create gist with `gh`

* Publish `conversion.py` as a Gist using `gh`
