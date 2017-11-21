# git-tutorial
A repo to demonstrate the git workflow 

## Introduction

In this tutorial we are going to demonstrate one simple git workflow that can be used in moderately large projects from software dev teams. The working example will be the implementation of a toy calculator in Python.

More concretely we are going to demonstrate:  
1. Branching, Creating and merging a PR  
2. Rebasing and Merge conflict resolution  
3. Commit squashing  

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

Now we developed an initial version of our calculator in a new branch. We can go into our VCS UI (in this case github) and create a pull request. When this PR passes the CI tests and the other dev reviews it can be merged from the UI.


