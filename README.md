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

## Detailed walkthrough

* Clone the repository to comet with:

        git clone https://github.com/zonca/conversion_tofix

* `cd` into the folder, test it running `python test_conversion.py`, it fails with `AssertionError`, one of the test fails
* Identify the commit causing the bug with `git bisect`, see <https://git-scm.com/docs/git-bisect>

## 2) Bisect

    git bisect start
    
mark the current (last) commit as bad

    git bisect bad
    
now you need to identify a good commit, just open `git log` and take the initial commit, copy its hash

    git bisect good HASH
    
now bisect is going to checkout a code version in the middle of your history, test it with:

    python test_conversion.py
    
if it fails, type

    git bisect bad
    
if it works, type

    git bisect good
    
after 3-4 steps it will have identified the wrong commit which is:

    "Remove extra digits"
 
 Do `git show HASH` of that commit to check that it is removing digits from the conversion factor that should instead be there.
 
## 3) Fix in branch
 
* Create a new branch `fix_bug`

        git checkout -b fix_bug
        
* Undo it with `git revert` <https://git-scm.com/docs/git-revert>, it is currently just a copy of master, now revert the bad commit with `git revert HASH` this creates a new commit at the end of history that makes changes opposite to the ones in the bad commit. This is **NOT** modifying the past history. It is equivalent to just making the change yourself in `conversion.py` and add/commit the result.

## 4) Create Pull Request

* Try to push it back to the original repository with `git push origin fix_bug`, does it work? No, you don't have permissions to do that.
* Fork the repository under your Github account through the Github website, use the Fork button
* Rename the `origin` remote to `upstream` <https://help.github.com/articles/renaming-a-remote/>
* Add your **fork** of the repository as a remote to the repository on Comet

        git remote add origin https://github.com/yourusername/conversion_tofix
        
* `git push` your `fix_bug` to your repository

        git push origin fix_bug
        
* Go to <https://github.com/zonca/conversion_tofix>, create a Pull Request! Click on New Pull Request and choose to Compare `zonca:master` branch to `yourusername:fix_bug` branch.

## 5) Synchronize upstream

**I created a new commit in my repository**

you can reference my `add_one_commit` branch on Github, https://github.com/zonca/conversion_tofix/tree/add_one_commit

by checking it out locally

    git fetch upstream
    git checkout -b add_one_commit upstream/add_one_commit
    
**Create 2 branches, test `rebase` in one and `merge` in the other**

create 2 branches from `fix_bug`:

    git checkout fix_bug
    git checkout -b fix_bug_rebase
    git checkout -b fix_bug_merge
    
Now test the 2 methods you can use to synchronize with upstream changes.

    git checkout fix_bug_rebase
    git rebase add_one_commit
    
    git checkout fix_bug_merge
    git merge add_one_commit
    
**After this, inspect with `git log --graph --oneline`**

You see that `rebase` creates a cleaner history because your last commit fixing the bug is applied on top of the last  version from master.
The issue is that you are now rewriting history, this is not a problem in the current case because you are the only one working on this branch.
So to update the remote branch and have a cleaner pull request you do:

    git checkout fix_bug
    
now we want to either replicate the rebase on the `fix_bug` branch. But a shortcut is just to force the `fix_bug` branch to the same status of `fix_bug_rebase`.
So:

    git reset --hard fix_bug_rebase
    
Now our `fix_bug` is rebased on master and we can push it but we need to force it with `-f` because `git` doesn't allow us to rewrite history otherwise.

    git push -f origin fix_bug
    
Now our pull request will be update to this status.

Instead if we do a merge, then we see that there is a merge commit of `master` into our `fix_bug_merge`, so this is not very clean if we make a pull request we will have this extra merge commit that is not harmful per se but that makes history more complicated.
However this does have the advantage that you are **not** rewriting history because you are adding extra commits on top of the previous state of `fix_bug`.
Therefore it is better to merge if you are working on a branch with other collaborators and you don't want to rewrite history and make it very difficult for them to merge any change that they have been working on.

## 6) Synchronize upstream with conflicts

* I will create a new commit in my repository with a conflict
* Do a rebase and handle conflicts

## 7) Erase commit

* Use `git rebase` to completely wipe the commit from history
* Try to push

## 8) Hard reset

* Wipe the last commit with `git reset --hard`
