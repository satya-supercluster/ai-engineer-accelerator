# Complete Git & GitHub Learning Guide

## Chapter 1: Introduction to Version Control

### 1.1 What is Git?

Git is a distributed version control system that tracks changes in your code over time. Think of it as a "time machine" for your projects that allows you to:

- Save snapshots of your work at different points
- Go back to previous versions if something breaks
- Work on new features without affecting the main code
- Collaborate with others seamlessly

**Real-world scenario:** Imagine you're writing a novel. Without Git, you might save files like `novel_v1.doc`, `novel_v2_final.doc`, `novel_v2_final_ACTUAL.doc`. With Git, you have one file with a complete history of all changes.

### 1.2 Git vs GitHub

- **Git**: The version control tool that runs on your computer
- **GitHub**: A cloud platform for hosting Git repositories and collaborating with others

**Analogy:** Git is like your personal photo album, while GitHub is like Instagram where you share those photos with others.

---

## Chapter 2: Setting Up Git

### 2.1 Installing Git

**Windows:**

```bash
# Download from git-scm.com and run installer
# Verify installation
git --version
```

**Mac:**

```bash
# Using Homebrew
brew install git

# Verify
git --version
```

**Linux:**

```bash
# Ubuntu/Debian
sudo apt-get install git

# Verify
git --version
```

### 2.2 Configuring Git (First-Time Setup)

```bash
# Set your identity globally
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# View all configurations
git config --list

# View specific config
git config user.name
```

**Why this matters:** Every commit you make will be tagged with this information, creating accountability in team projects.

### 2.3 Getting Help

```bash
# General help
git help

# Help for specific command
git help commit
git commit --help

# Short summary
git commit -h
```

---

## Chapter 3: Taking Snapshots (Basic Workflow)

### 3.1 Initializing a Repository

```bash
# Create a new project folder
mkdir my-ecommerce-project
cd my-ecommerce-project

# Initialize Git repository
git init

# Check status
git status
```

**What happens:** Git creates a hidden `.git` folder that tracks all changes.

### 3.2 Understanding the Git Workflow

Git has three main areas:

1. **Working Directory**: Where you edit files
2. **Staging Area** (Index): Where you prepare files for commit
3. **Repository**: Where committed snapshots are stored

```
Working Directory → (git add) → Staging Area → (git commit) → Repository
```

**Scenario:** You're building an e-commerce site:

```bash
# Create files
echo "Welcome to our store" > homepage.html
echo "body { color: blue; }" > styles.css

# Check what Git sees
git status
# Shows: Untracked files (in Working Directory)
```

### 3.3 Staging Files

```bash
# Stage a single file
git add homepage.html

# Stage multiple files
git add homepage.html styles.css

# Stage all files
git add .

# Stage all files with specific extension
git add *.css

# Check status after staging
git status
```

**Example workflow:**

```bash
# You've modified three files
git status
# Modified: product.html, cart.js, styles.css

# You only want to commit product.html and cart.js
git add product.html cart.js

git status
# Changes to be committed: product.html, cart.js
# Changes not staged: styles.css
```

### 3.4 Committing Changes

```bash
# Commit with message
git commit -m "Add homepage and basic styling"

# Commit with detailed message (opens editor)
git commit
```

**Best practices for commit messages:**

```bash
# Bad commits
git commit -m "fixed stuff"
git commit -m "changes"

# Good commits
git commit -m "Fix login button alignment on mobile"
git commit -m "Add user authentication endpoint"
git commit -m "Remove deprecated payment gateway code"
```

**Multi-line commit message:**

```bash
git commit -m "Add shopping cart functionality

- Implement add to cart button
- Create cart summary component
- Add cart persistence with localStorage"
```

### 3.5 Skipping the Staging Area

```bash
# Commit all tracked files directly (skip staging)
git add .
git commit -m "Quick update to all files"

# Or shortcut for modified files only
git commit -am "Update existing files"
```

**Warning:** `-am` only works for files Git already tracks, not new files.

### 3.6 Viewing History

```bash
# View commit history
git log

# Compact view (one line per commit)
git log --oneline

# View with graph
git log --oneline --graph --all

# View last 3 commits
git log -3

# View commits by author
git log --author="John"

# View commits with specific word in message
git log --grep="bugfix"
```

**Example output:**

```
a1b2c3d (HEAD -> main) Add checkout page
e4f5g6h Implement product search
i7j8k9l Create product catalog
```

---

## Chapter 4: Managing Files

### 4.1 Removing Files

```bash
# Remove file from working directory and stage deletion
git rm products.html

# Remove from Git but keep in working directory
git rm --cached secrets.txt

# Remove entire folder
git rm -r old-components/
```

**Scenario:**

```bash
# You accidentally committed sensitive data
git rm --cached config/api-keys.txt
git commit -m "Remove API keys from repository"
# File still exists locally but won't be tracked
```

### 4.2 Renaming/Moving Files

```bash
# Rename a file
git mv oldname.js newname.js

# Move file to different folder
git mv homepage.html pages/homepage.html

# This is equivalent to:
mv homepage.html pages/homepage.html
git rm homepage.html
git add pages/homepage.html
```

### 4.3 Ignoring Files

Create a `.gitignore` file:

```bash
# .gitignore file content

# Dependencies
node_modules/
vendor/

# Environment files
.env
.env.local

# Build outputs
dist/
build/
*.log

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db

# Specific files
config/secrets.json
```

**Common patterns:**

```bash
# Ignore all .txt files
*.txt

# But track this one
!important.txt

# Ignore all files in any directory named temp
**/temp/

# Ignore files only in root directory
/config.json
```

---

## Chapter 5: Viewing Changes

### 5.1 Checking Status

```bash
# Detailed status
git status

# Short status
git status -s
```

**Short status output:**

```
M  modified-file.js      # Modified, staged
 M unstaged-file.js      # Modified, not staged
A  new-file.js           # Added (new file staged)
D  deleted-file.js       # Deleted
?? untracked.js          # Untracked
```

### 5.2 Viewing Differences

```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged

# View changes in specific file
git diff homepage.html

# Compare two commits
git diff a1b2c3d e4f5g6h

# View changes between branches
git diff main feature-branch
```

**Example scenario:**

```bash
# You modified product.js
git diff product.js

# Output shows:
-const price = 10;
+const price = 15;

# This shows you changed the price from 10 to 15
```

### 5.3 Viewing Specific Commits

```bash
# View details of latest commit
git show

# View specific commit
git show a1b2c3d

# View files changed in a commit
git show --name-only a1b2c3d

# View commit statistics
git show --stat a1b2c3d
```

---

## Chapter 6: Undoing Changes

### 6.1 Unstaging Files

```bash
# Unstage a specific file
git restore --staged product.js

# Unstage all files
git restore --staged .

# Old way (still works)
git reset HEAD product.js
```

**Scenario:**

```bash
# You accidentally staged a secret file
git add .
git status
# Shows: config/api-keys.txt staged

git restore --staged config/api-keys.txt
# Now it's unstaged
```

### 6.2 Discarding Local Changes

```bash
# Discard changes in working directory
git restore product.js

# Discard all changes
git restore .

# Old way
git checkout -- product.js
```

**⚠️ Warning:** This permanently deletes your uncommitted changes!

### 6.3 Restoring Files to Earlier Versions

```bash
# Restore file from last commit
git restore --source=HEAD~1 product.js

# Restore from specific commit
git restore --source=a1b2c3d product.js

# Restore entire project to previous commit
git restore --source=a1b2c3d .
```

### 6.4 Using Git Reset

Git reset has three modes:

```bash
# Soft reset - keeps changes staged
git reset --soft HEAD~1
# Use case: You want to modify the last commit

# Mixed reset (default) - keeps changes unstaged
git reset HEAD~1
# Use case: You want to uncommit but keep your work

# Hard reset - discards all changes
git reset --hard HEAD~1
# Use case: You want to completely undo recent commits
```

**Example workflow:**

```bash
# Your last 3 commits:
# c3: "Add payment"
# c2: "Add cart"  
# c1: "Add products"

# You want to undo "Add payment" but keep the code
git reset --soft HEAD~1
# Now you can modify and recommit

# You want to completely remove last 2 commits
git reset --hard HEAD~2
# Back to "Add products" commit, all other work gone!
```

---

## Chapter 7: Branching and Merging

### 7.1 Understanding Branches

Branches allow you to work on different features simultaneously without affecting the main code.

```bash
# View all branches
git branch

# Create new branch
git branch feature-login

# Switch to branch
git checkout feature-login

# Create and switch in one command
git checkout -b feature-payment

# New way (Git 2.23+)
git switch feature-login
git switch -c feature-payment
```

**Scenario - E-commerce development:**

```bash
# Main branch has stable code
git checkout main

# Developer 1 works on login
git checkout -b feature-login

# Developer 2 works on cart
git checkout -b feature-cart

# Developer 3 fixes bug
git checkout -b bugfix-header
```

### 7.2 Branch Workflow

```bash
# Create feature branch
git checkout -b feature-user-profile

# Make changes
echo "User Profile Page" > profile.html
git add profile.html
git commit -m "Create user profile page"

# Make more commits
echo "Add avatar upload" >> profile.html
git commit -am "Add avatar upload feature"

# View branch history
git log --oneline --graph
```

### 7.3 Merging Branches

#### Fast-Forward Merge

When there are no changes on the main branch:

```bash
# Switch to main
git checkout main

# Merge feature branch
git merge feature-user-profile

# Result: Fast-forward merge (no merge commit created)
```

**Visualization:**

```
Before:
main:    A---B
               \
feature:        C---D

After:
main:    A---B---C---D
```

#### Three-Way Merge

When both branches have new commits:

```bash
# Main has moved forward
git checkout main
echo "New feature" > admin.html
git add admin.html
git commit -m "Add admin panel"

# Merge feature branch
git merge feature-user-profile

# Result: Merge commit created
```

**Visualization:**

```
Before:
main:    A---B---E
               \
feature:        C---D

After:
main:    A---B---E---F (merge commit)
               \   /
feature:        C-D
```

### 7.4 Handling Merge Conflicts

Conflicts occur when the same lines are modified in both branches.

**Example conflict scenario:**

```bash
# In main branch
echo "Price: $10" > product.html
git add product.html
git commit -m "Set product price"

# In feature branch
git checkout feature-discount
echo "Price: $8" > product.html
git add product.html
git commit -m "Add discount price"

# Try to merge
git checkout main
git merge feature-discount
# CONFLICT! Git can't decide which price to keep
```

**Resolving conflicts:**

```bash
# Git marks the conflict in product.html:
<<<<<<< HEAD
Price: $10
=======
Price: $8
>>>>>>> feature-discount

# Edit the file to resolve:
Price: $10
Discount Price: $8

# Stage the resolved file
git add product.html

# Complete the merge
git commit -m "Merge feature-discount, keep both prices"
```

### 7.5 Deleting Branches

```bash
# Delete merged branch
git branch -d feature-user-profile

# Force delete unmerged branch
git branch -D experimental-feature

# Delete remote branch
git push origin --delete feature-user-profile
```

---

## Chapter 8: Git Stash

### 8.1 What is Stash?

Stash temporarily saves your uncommitted changes so you can switch branches.

**Scenario:** You're working on a feature when an urgent bug needs fixing:

```bash
# You're working on feature-payment
echo "Processing payment..." > payment.js
git status
# Shows: Modified payment.js (uncommitted)

# Urgent bug on main branch!
# Save your work temporarily
git stash

# Now working directory is clean
git status
# Nothing to commit

# Switch to main and fix bug
git checkout main
# Fix the bug...
git commit -am "Fix urgent bug"

# Go back to feature
git checkout feature-payment

# Restore your work
git stash pop
```

### 8.2 Stash Commands

```bash
# Save current changes
git stash

# Save with description
git stash push -m "WIP: payment form validation"

# List all stashes
git stash list
# Output:
# stash@{0}: WIP: payment form validation
# stash@{1}: On main: header styles

# View stash contents
git stash show stash@{0}

# Apply stash without removing it
git stash apply stash@{0}

# Apply and remove stash
git stash pop

# Remove specific stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

### 8.3 Advanced Stash Usage

```bash
# Stash including untracked files
git stash -u

# Stash including ignored files
git stash -a

# Create branch from stash
git stash branch feature-from-stash

# Apply stash to different branch
git checkout other-branch
git stash apply stash@{2}
```

---

## Chapter 9: Working with Remote Repositories

### 9.1 Connecting to GitHub

```bash
# View remote connections
git remote -v

# Add remote repository
git remote add origin https://github.com/username/repo.git

# Change remote URL
git remote set-url origin https://github.com/username/new-repo.git

# Remove remote
git remote remove origin
```

### 9.2 Pushing to Remote

```bash
# Push to remote (first time)
git push -u origin main

# After first push
git push

# Push specific branch
git push origin feature-login

# Push all branches
git push --all

# Force push (use carefully!)
git push --force
```

**Collaborative scenario:**

```bash
# Nobita creates the repository
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/nobita/ecommerce.git
git push -u origin main

# Gian clones it
git clone https://github.com/nobita/ecommerce.git
cd ecommerce
```

### 9.3 Fetching and Pulling

```bash
# Fetch updates (doesn't merge)
git fetch origin

# View fetched changes
git log origin/main

# Merge fetched changes
git merge origin/main

# Fetch and merge in one command
git pull origin main

# Pull with rebase
git pull --rebase origin main
```

**Difference between fetch and pull:**

- `git fetch`: Downloads changes but doesn't modify your working directory
- `git pull`: Downloads and immediately merges changes (`fetch` + `merge`)

### 9.4 Cloning Repositories

```bash
# Clone repository
git clone https://github.com/username/repo.git

# Clone to specific folder
git clone https://github.com/username/repo.git my-folder

# Clone specific branch
git clone -b develop https://github.com/username/repo.git

# Shallow clone (only recent history)
git clone --depth 1 https://github.com/username/repo.git
```

---

## Chapter 10: Collaboration Workflows

### 10.1 Feature Branch Workflow

```bash
# 1. Update main branch
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature-shopping-cart

# 3. Work on feature
# ... make changes ...
git add .
git commit -m "Implement add to cart"

# 4. Push feature branch
git push -u origin feature-shopping-cart

# 5. Create Pull Request on GitHub

# 6. After review, merge on GitHub

# 7. Update local main
git checkout main
git pull origin main

# 8. Delete feature branch
git branch -d feature-shopping-cart
git push origin --delete feature-shopping-cart
```

### 10.2 Handling Pull Requests

**Team workflow example:**

```bash
# Nobita creates feature
git checkout -b feature-product-filter
# ... work ...
git push origin feature-product-filter
# Creates PR on GitHub

# Gian reviews code on GitHub
# Requests changes

# Nobita makes updates
git add .
git commit -m "Address review feedback"
git push origin feature-product-filter

# Gian approves and merges on GitHub

# Both update their local main
git checkout main
git pull origin main
```

### 10.3 Resolving Conflicts in Collaboration

```bash
# Your teammate pushed changes
git pull origin main
# CONFLICT in product.js

# View conflict
cat product.js
# <<<<<<< HEAD
# Your changes
# =======
# Teammate's changes
# >>>>>>> origin/main

# Resolve manually, then:
git add product.js
git commit -m "Resolve merge conflict in product.js"
git push origin main
```

---

## Chapter 11: Advanced Git Techniques

### 11.1 Cherry-Picking

Apply specific commits from one branch to another:

```bash
# You have a bug fix in feature branch
git checkout feature-experimental
git log --oneline
# a1b2c3d Fix critical security bug

# Apply only that commit to main
git checkout main
git cherry-pick a1b2c3d
```

### 11.2 Rebasing

Rebase rewrites history to create a linear progression:

```bash
# Instead of merge
git checkout feature-branch
git rebase main

# Interactive rebase (squash commits)
git rebase -i HEAD~3
```

**⚠️ Warning:** Never rebase commits that have been pushed to shared branches!

### 11.3 Git Aliases

Create shortcuts for common commands:

```bash
# Set up aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'restore --staged'
git config --global alias.last 'log -1 HEAD'
git config --global alias.lg 'log --oneline --graph --all'

# Now you can use:
git co main
git br -a
git lg
```

---

## Chapter 12: Git Best Practices

### 12.1 Commit Guidelines

**DO:**

- Commit often with small, logical changes
- Write clear, descriptive commit messages
- Test before committing
- Keep commits focused on one task

**DON'T:**

- Commit half-finished work
- Mix multiple changes in one commit
- Commit generated files or dependencies
- Use vague messages like "fix stuff"

### 12.2 Branch Naming Conventions

```bash
# Good branch names
feature/user-authentication
bugfix/login-error
hotfix/payment-gateway
refactor/database-queries
docs/api-documentation

# Bad branch names
fix
new-stuff
asdf
branch1
```

### 12.3 Security Practices

```bash
# Never commit sensitive data
# Add to .gitignore:
.env
config/secrets.yml
*.pem
*.key

# If you accidentally committed secrets:
git rm --cached config/secrets.yml
git commit -m "Remove secrets file"

# Change the exposed credentials immediately!
```

---

## Chapter 13: Troubleshooting Common Issues

### 13.1 "Detached HEAD" State

```bash
# You checked out a specific commit
git checkout a1b2c3d
# Warning: You are in 'detached HEAD' state

# To keep changes, create a branch
git checkout -b recovered-work

# To discard and return
git checkout main
```

### 13.2 Undoing a Pushed Commit

```bash
# Create a new commit that undoes previous commit
git revert a1b2c3d
git push origin main

# DON'T use reset on shared branches!
```

### 13.3 Recovering Deleted Commits

```bash
# View reflog (history of HEAD movements)
git reflog

# Find the commit before deletion
git reflog
# a1b2c3d HEAD@{2}: commit: My deleted work

# Restore it
git checkout a1b2c3d
git checkout -b recovered-branch
```

---

## Quick Reference Cheat Sheet

```bash
# Setup
git config --global user.name "Name"
git config --global user.email "email@example.com"

# Basic Commands
git init                    # Initialize repository
git status                  # Check status
git add <file>             # Stage file
git add .                  # Stage all
git commit -m "message"    # Commit with message
git log --oneline          # View history

# Branching
git branch                 # List branches
git branch <name>          # Create branch
git checkout <name>        # Switch branch
git checkout -b <name>     # Create and switch
git merge <branch>         # Merge branch
git branch -d <name>       # Delete branch

# Remote
git remote add origin <url>    # Add remote
git push -u origin main        # Push to remote
git pull origin main           # Pull from remote
git clone <url>                # Clone repository

# Undoing
git restore <file>             # Discard changes
git restore --staged <file>    # Unstage file
git reset --soft HEAD~1        # Undo commit, keep changes
git reset --hard HEAD~1        # Undo commit, discard changes

# Stash
git stash                      # Save changes temporarily
git stash list                 # List stashes
git stash pop                  # Apply and remove stash
git stash apply                # Apply without removing
```

---

This comprehensive guide covers everything from basic Git operations to advanced collaboration techniques. Practice these concepts with real projects to solidify your understanding!
