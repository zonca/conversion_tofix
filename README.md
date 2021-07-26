# Hands-on exercise for Advanced Git/Github training

## Notes

* Feel free to leave anytime
* It is hands-on, try to do exercise, then we will do together
* All the step-by-step solution will be available, no need to take notes
* If you get lost, try to reset the repository and start again
* Otherwise, feel free to just follow along, you can do on your own later

## 0) Preparation

* `module load gh` on Expanse
* `gh auth login`, protocol SSH, generate key with no password, authenticate via browser
* Clone this repository to your home folder with `gh`
* `git config --global user.name "FirstName LastName"`
* `git config --global user.email "your_github@email.com"`


## 0b) How to reset the status of the repository

If you ever get lost and have an incosistent status of the repository as you work through the example, you can wipe all local changes both to `main` and to `fix_bug` and go back to the initial state of `main` and restart from there:

    git checkout main
    git reset --hard origin/original_main

After you created the `fix_bug` branch:

    git checkout fix_bug
    git reset --hard origin/original_main

## 1) Make a test

* Test it running `python test_conversion.py`, does it fail?
* Checkout the code version just before the last commit, does it still fail? How do you go back to the last commit?

## 2) Identify the commit which caused the bug

* Identify the commit causing the bug with `git bisect`, see <https://git-scm.com/docs/git-bisect>
* `bisect` is rarely useful in practice, let's skip it, it is in the solution if you are interested, now assume we know that the problematic commit is `363a`

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
* Add your **fork** of the repository as a remote named `fork` to the repository on Expanse
* `git push fork` your `fix_bug` to your repository
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
