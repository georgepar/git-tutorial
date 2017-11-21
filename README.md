# git-tutorial
A repo to demonstrate the git workflow 

## Introduction

In this tutorial we are going to demonstrate one simple git workflow that can be used in moderately large projects from software dev teams (for large projects I still advocate [gerrit](https://www.gerritcodereview.com/)).

The working example will be the implementation of a toy calculator in Python.

More concretely we are going to demonstrate:  
1. Branching, Creating and merging a PR  
2. Rebasing and Merge conflict resolution  
3. Bonus part: `git bisect`

Note that in a previous tutorial I explicitly recommended never to do `git push -f`. Well, almost never.  

## Part 1: Branching out  

In large projects direct push to master is a bad idea. Everybody knows that, even the [stackexchange people](https://softwareengineering.stackexchange.com/a/335682) :).

So everyone should incorporate branching in their dev workflow. In most cases you will create a new branch for every issue in your issue tracker. Let's see how this is done in practice:  

```
git clone https://github.com/georgepar/git-tutorial
git checkout -b TASK-1-initial-calc
# Edit run.py
git add run.py
git commit -sv -m "Add initial runner"
# Edit requirements.txt
git add requirements.txt
git commit -sv -m "Add some dummy dependencies"
git push -u origin TASK-1-initial-calc
```

Now we developed an initial version of our calculator in a new branch. 

- `run.py`
```python
import sys


def main():
    # The operation we want to perform will be passed
    # as a string in the positional command line args
    # Example: python run.py '1 + 2'
    args = sys.argv[1].strip().split()
    x, op, y = args[0], args[1], args[2]
    print(x, op, y)


if __name__ == '__main__':
    main()
```
- `requirements.txt`
```
numpy==1.7.1
requests==2.7.0
```

We can go into our VCS UI (in this case github) and create a pull request. When this PR passes the CI tests and the reviews it can be merged from the UI.

![My image](images/pr.png)

## Part 2: Rebasing

### Case 1: Two independent devs develop different features

In this case let's assume that we have 2 tasks, TASK-2-implement-addition and TASK-3-implement-multiplication.
We assign them to Alice and Bob respectively and they start developing independently.

Alice finishes first and her PR gets merged. The new code is shown below:

```python
import sys


def add(x, y):
    return x + y


def main():
    # The operation we want to perform will be passed
    # as a string in the positional command line args
    # Example: python run.py '1 + 2'
    args = sys.argv[1].strip().split()
    x, op, y = args[0], args[1], args[2]

    if op == '+':
        return add(x, y)
        

if __name__ == '__main__':
    main()
```

Now Bob finishes his task and his code looks like this:

- `run.py`
```python
import sys


def mult(x, y):
    return float(x) * float(y)


def main():
    # The operation we want to perform will be passed
    # as a string in the positional command line args
    # Example: python run.py '1 + 2'
    args = sys.argv[1].strip().split()
    x, op, y = args[0], args[1], args[2]
    if op == '*':
        print(mult(x, y))


if __name__ == '__main__':
    main()
```
- `requirements.txt`
```
numpy==1.7.1
requests==2.7.0
```

Since Alice's code was already merged he will have to rebase his branch to the upstream code by running:
```bash
git checkout master
git pull
git checkout TASK-3-implement-multiplication
git rebase master
First, rewinding head to replay your work on top of it...
Applying: Implement multiplication
Using index info to reconstruct a base tree...
M	run.py
Falling back to patching base and 3-way merge...
Auto-merging run.py
CONFLICT (content): Merge conflict in run.py
error: Failed to merge in the changes.
Patch failed at 0001 Implement multiplication
The copy of the patch that failed is found in: .git/rebase-apply/patch

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".
```

We see that we have to resolve some merge conflicts. I really recommend using [meld](http://meldmerge.org/) for this. [This excellent stackoverflow answer says all you need to know to get started](https://stackoverflow.com/a/34119867).

We can fire up meld by running:

```bash
git mergetool
```

And resolve the conflicts as shown in the following video (sorry for the bad quality):
[![meld conflict resolution](https://img.youtube.com/vi/LrQ4-sILJ7A/0.jpg)](https://www.youtube.com/watch?v=LrQ4-sILJ7A)

Let's take this step by step. What we did is a 3-way merge.  
- On the left we can see the upstream code (master)  
- On the right we can see the local branch (TASK-3-implement-multiplication)  
- In the middle we can see their common ancestor which will be the final product  

Resolving MCs then is just a matter of picking and choosing what we need from each branch.

Once we're finished we can run:  

```bash
git rebase --continue
git push -f
```

And create the PR as usual.

### Case 2: Branching out from an unmerged branch

Now let's assume that we create a new task, TASK-4-implement-division and assign it to George. George wants to base his work on Bob's work on multiplication so at some point he branches out of TASK-3-implement-multiplication.

W
