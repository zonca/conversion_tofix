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

### Use bisect

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
 
* Create a new branch `fix_bug`

        git checkout -b fix_bug
        
* Undo it with `git revert` <https://git-scm.com/docs/git-revert>, it is currently just a copy of master, now revert the bad commit with `git revert HASH` this creates a new commit at the end of history that makes changes opposite to the ones in the bad commit. This is **NOT** modifying the past history. It is equivalent to just making the change yourself in `conversion.py` and add/commit the result.

* Try to push it back to the original repository with `git push origin fix_bug`, does it work? No, you don't have permissions to do that.
* Fork the repository under your Github account through the Github website, use the Fork button
* Rename the `origin` remote to `upstream` <https://help.github.com/articles/renaming-a-remote/>
* Add your **fork** of the repository as a remote to the repository on Comet

        git remote add origin https://github.com/yourusername/conversion_tofix
        
* `git push` your `fix_bug` to your repository

        git push origin fix_bug
        
* Go to <https://github.com/zonca/conversion_tofix>, create a Pull Request! Click on New Pull Request and choose to Compare `zonca:master` branch to `yourusername:fix_bug` branch.
