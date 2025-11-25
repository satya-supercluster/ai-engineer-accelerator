# Complete Linux Learning Guide

## Chapter 1: Introduction to Linux

### 1.1 What is Linux?

Linux is a free, open-source operating system that powers everything from smartphones (Android) to supercomputers, web servers, and desktop computers.

**Real-world analogy:** If Windows is like buying a pre-built house you can't modify, Linux is like getting the blueprints to build and customize your house exactly how you want it.

### 1.2 Why Learn Linux?

- **Server dominance**: 96.3% of the world's top 1 million servers run Linux
- **Career opportunities**: DevOps, Cloud Computing, Cybersecurity all require Linux
- **Free and open-source**: No licensing costs, complete transparency
- **Powerful command line**: Automate repetitive tasks efficiently
- **Stability and security**: Fewer viruses, more control over your system

### 1.3 Linux Distributions (Distros)

Think of distributions as different flavors of ice cream - same base, different toppings:

**Beginner-friendly:**

- **Ubuntu**: Most popular, great for beginners
- **Linux Mint**: Windows-like interface, easy transition
- **Pop!_OS**: Great for gaming and developers

**Advanced:**

- **Arch Linux**: Build your system from scratch
- **Gentoo**: Maximum customization

**Server-focused:**

- **CentOS/Rocky Linux**: Enterprise stability
- **Debian**: Rock-solid, used by many servers
- **Red Hat Enterprise Linux (RHEL)**: Commercial support

### 1.4 Linux Architecture

```
┌─────────────────────────────────────┐
│      Applications & Programs        │
│   (Firefox, VS Code, Terminal)      │
└─────────────────────────────────────┘
                 ↕
┌─────────────────────────────────────┐
│          Shell (Bash/Zsh)           │
│      (Command interpreter)          │
└─────────────────────────────────────┘
                 ↕
┌─────────────────────────────────────┐
│        Linux Kernel (Core)          │
│  (Hardware communication layer)     │
└─────────────────────────────────────┘
                 ↕
┌─────────────────────────────────────┐
│      Hardware (CPU, RAM, Disk)      │
└─────────────────────────────────────┘
```

---

## Chapter 2: Getting Started with Linux

### 2.1 Installation Options

**Option 1: Virtual Machine (Recommended for beginners)**  

```bash
# Download VirtualBox or VMware
# Download Ubuntu ISO
# Create new VM with 2GB RAM, 20GB disk
# Install Ubuntu in VM
```

**Option 2: Dual Boot**  

- Keep Windows and Linux on same computer
- Choose which OS at startup
- Requires partitioning hard drive

**Option 3: WSL (Windows Subsystem for Linux)**  

```powershell
# In Windows PowerShell (as Administrator)
wsl --install
# Restart computer
# Ubuntu installs automatically
```

**Option 4: Cloud Linux**  

- AWS EC2, DigitalOcean, or Linode
- Practice on remote servers

### 2.2 First Login

After installation:

```bash
# You'll see a prompt like:
username@hostname:~$ 

# Breaking it down:
# username: Your login name
# hostname: Computer name
# ~: Current directory (home directory)
# $: Regular user (# means root user)
```

### 2.3 Basic Command Structure

```bash
command [options] [arguments]

# Example:
ls -la /home
│  │   │
│  │   └─ Argument (what to act on)
│  └───── Option (how to act)
└──────── Command (what to do)
```

---

## Chapter 3: Navigating the File System

### 3.1 Linux Directory Structure

```
/                          (Root - everything starts here)
├── home/                  (User home directories)
│   ├── nobita/           (Your personal files)
│   └── gian/
├── root/                  (Root user's home)
├── etc/                   (System configuration files)
├── var/                   (Variable data - logs, databases)
├── usr/                   (User programs and applications)
├── bin/                   (Essential commands)
├── tmp/                   (Temporary files)
└── dev/                   (Device files)
```

**Windows vs Linux paths:**

```bash
# Windows
C:\Users\Nobita\Documents\file.txt

# Linux
/home/nobita/Documents/file.txt
```

### 3.2 Essential Navigation Commands

```bash
# Print working directory (where am I?)
pwd
# Output: /home/nobita

# List files
ls                    # Simple list
ls -l                # Long format (detailed)
ls -a                # Show hidden files
ls -lh               # Human-readable sizes
ls -lah              # Combine options
ls -R                # Recursive (show subdirectories)

# Change directory
cd /home/nobita/Documents    # Absolute path
cd Documents                  # Relative path
cd ..                        # Go up one level
cd ../..                     # Go up two levels
cd ~                         # Go to home directory
cd -                         # Go to previous directory
cd /                         # Go to root directory
```

**Practical scenario:**

```bash
# You're in /home/nobita
pwd
# Output: /home/nobita

# Go to Documents folder
cd Documents
pwd
# Output: /home/nobita/Documents

# Go back to home
cd ~
pwd
# Output: /home/nobita

# Go to system folder
cd /etc
pwd
# Output: /etc

# Return to previous location
cd -
pwd
# Output: /home/nobita
```

### 3.3 Understanding Paths

```bash
# Absolute path (starts with /)
cd /home/nobita/projects/website

# Relative path (from current location)
# If you're in /home/nobita:
cd projects/website

# Special path shortcuts
~     # Home directory (/home/nobita)
.     # Current directory
..    # Parent directory
-     # Previous directory
```

**Example workflow:**

```bash
# Create a project structure
cd ~
pwd  # /home/nobita

cd ./projects  # Go to projects (relative)
pwd  # /home/nobita/projects

cd ../Documents  # Go to Documents (up one, then down)
pwd  # /home/nobita/Documents

cd /var/log  # Absolute path to logs
pwd  # /var/log

cd -  # Back to Documents
pwd  # /home/nobita/Documents
```

---

## Chapter 4: Working with Files and Directories

### 4.1 Creating Files and Directories

```bash
# Create empty file
touch file.txt
touch index.html style.css script.js

# Create file with content
echo "Hello Linux" > greeting.txt

# Create multiple files
touch file1.txt file2.txt file3.txt

# Create directory
mkdir projects
mkdir -p websites/portfolio/images  # Create nested directories

# Create multiple directories
mkdir dir1 dir2 dir3
```

**Real scenario - Setting up a web project:**

```bash
# Create project structure
mkdir -p ~/projects/ecommerce/{src,tests,docs}
cd ~/projects/ecommerce
touch src/index.html src/style.css src/app.js
touch README.md

# View structure
tree
# Output:
# ecommerce/
# ├── docs/
# ├── src/
# │   ├── app.js
# │   ├── index.html
# │   └── style.css
# ├── tests/
# └── README.md
```

### 4.2 Viewing File Contents

```bash
# View entire file
cat filename.txt

# View with line numbers
cat -n filename.txt

# View first 10 lines
head filename.txt
head -n 20 filename.txt  # First 20 lines

# View last 10 lines
tail filename.txt
tail -n 5 filename.txt   # Last 5 lines
tail -f /var/log/syslog  # Follow log file (live updates)

# View one page at a time
less filename.txt
# Inside less:
# Space: Next page
# b: Previous page
# /search: Search forward
# q: Quit

# View with scrolling
more filename.txt
```

**Practical example:**

```bash
# Check system log
tail -f /var/log/syslog
# Useful for monitoring server issues in real-time

# View large file
less large_database_dump.sql
# Navigate easily through huge files

# Quick peek at config file
head -n 10 /etc/ssh/sshd_config
```

### 4.3 Copying Files and Directories

```bash
# Copy file
cp source.txt destination.txt

# Copy to directory
cp file.txt /home/nobita/backup/

# Copy multiple files
cp file1.txt file2.txt file3.txt /backup/

# Copy directory (recursive)
cp -r projects/ projects_backup/

# Copy with progress (preserve attributes)
cp -av source/ destination/

# Copy only if newer
cp -u source.txt destination.txt

# Interactive (ask before overwrite)
cp -i file.txt existing_file.txt
```

**Scenario - Backing up a project:**

```bash
# Create backup of website
cp -r ~/projects/website ~/backups/website_backup_$(date +%Y%m%d)

# Copy config files
cp /etc/nginx/nginx.conf ~/backups/nginx.conf.backup

# Copy only modified files
cp -u ~/projects/website/* ~/backups/website/
```

### 4.4 Moving and Renaming

```bash
# Rename file
mv oldname.txt newname.txt

# Move file to directory
mv file.txt /home/nobita/Documents/

# Move multiple files
mv file1.txt file2.txt file3.txt /destination/

# Move directory
mv old_folder/ new_location/

# Move and rename
mv ~/Downloads/report.pdf ~/Documents/annual_report_2024.pdf

# Interactive move
mv -i file.txt /destination/
```

**Example workflow:**

```bash
# Organize downloads
cd ~/Downloads
mv *.pdf ~/Documents/PDFs/
mv *.jpg ~/Pictures/
mv *.zip ~/Archives/

# Rename project
mv old_project_name new_project_name

# Move to parent directory
mv file.txt ../
```

### 4.5 Deleting Files and Directories

```bash
# Delete file
rm file.txt

# Delete multiple files
rm file1.txt file2.txt file3.txt

# Delete all .txt files
rm *.txt

# Interactive delete (ask confirmation)
rm -i important_file.txt

# Delete directory and contents
rm -r folder_name/

# Force delete (no confirmation)
rm -rf folder_name/  # ⚠️ DANGEROUS!

# Delete empty directory
rmdir empty_folder/
```

**⚠️ Important Safety Tips:**

```bash
# NEVER run these without being absolutely sure:
rm -rf /        # Deletes everything (requires --no-preserve-root)
rm -rf ~        # Deletes your entire home directory
rm -rf *        # Deletes everything in current directory

# Safe practices:
# 1. Always check current directory
pwd

# 2. List files before deleting
ls *.txt
# Then delete
rm *.txt

# 3. Use interactive mode for important files
rm -i sensitive_data.txt

# 4. Move to trash instead of deleting
mv unwanted_file.txt ~/.local/share/Trash/
```

**Practical scenario:**

```bash
# Clean up old log files
cd /var/log
sudo rm -i *.log.old

# Remove build artifacts
cd ~/projects/website
rm -rf node_modules/
rm -rf dist/

# Clean temporary files
rm -rf /tmp/*
```

---

## Chapter 5: File Permissions and Ownership

### 5.1 Understanding Permissions

Every file has permissions for three groups:

- **Owner (u)**: The file creator
- **Group (g)**: Users in the file's group
- **Others (o)**: Everyone else

Three types of permissions:

- **Read (r)**: View contents (value: 4)
- **Write (w)**: Modify contents (value: 2)
- **Execute (x)**: Run as program (value: 1)

```bash
# View permissions
ls -l file.txt
# Output: -rw-r--r-- 1 nobita users 1234 Nov 26 10:00 file.txt
          │││││││││
          │││││││└┴┴─ Others permissions (r--)
          │││││└┴┴─── Group permissions (r--)
          ││└┴┴───── Owner permissions (rw-)
          │└────────── Number of hard links
          └─────────── File type (- = regular file, d = directory)
```

### 5.2 Changing Permissions (chmod)

**Symbolic method:**

```bash
# Give owner execute permission
chmod u+x script.sh

# Remove write permission from others
chmod o-w file.txt

# Give group read and write
chmod g+rw document.txt

# Set exact permissions
chmod u=rwx,g=rx,o=r file.txt

# Add execute to all
chmod +x script.py

# Remove write from all
chmod -w readonly.txt
```

**Numeric method:**

```bash
# Calculate permission number:
# Read (4) + Write (2) + Execute (1)

chmod 755 script.sh
# 7 (4+2+1) = rwx for owner
# 5 (4+1)   = r-x for group
# 5 (4+1)   = r-x for others

chmod 644 file.txt
# 6 (4+2) = rw- for owner
# 4 (4)   = r-- for group
# 4 (4)   = r-- for others

chmod 600 private.key
# 6 (4+2) = rw- for owner only
# 0       = --- for group
# 0       = --- for others
```

**Common permission patterns:**

```bash
chmod 777 file.txt    # Everyone can do everything (INSECURE!)
chmod 755 script.sh   # Standard executable script
chmod 644 document.txt # Standard readable file
chmod 600 secret.txt  # Private file (owner only)
chmod 700 private_dir/ # Private directory
```

**Real-world scenario:**

```bash
# Make script executable
chmod +x deploy.sh
./deploy.sh  # Now you can run it

# Secure SSH key
chmod 600 ~/.ssh/id_rsa
# SSH requires private keys to be read-only by owner

# Set website permissions
chmod 755 ~/public_html/
chmod 644 ~/public_html/*.html
chmod 755 ~/public_html/cgi-bin/*.cgi

# Recursive permission change
chmod -R 755 /var/www/html/
```

### 5.3 Changing Ownership (chown)

```bash
# Change owner
sudo chown nobita file.txt

# Change owner and group
sudo chown nobita:users file.txt

# Change only group
sudo chown :webdev file.txt
# Or
sudo chgrp webdev file.txt

# Recursive change
sudo chown -R nobita:users /home/nobita/projects/

# Change multiple files
sudo chown nobita file1.txt file2.txt file3.txt
```

**Practical scenarios:**

```bash
# Fix ownership after copying files as root
sudo cp /root/backup.tar.gz /home/nobita/
sudo chown nobita:nobita /home/nobita/backup.tar.gz

# Set web server ownership
sudo chown -R www-data:www-data /var/www/html/

# Give ownership to different user
sudo chown gian:gian /home/nobita/shared_project/
```

### 5.4 Special Permissions

```bash
# Setuid (runs as file owner)
chmod u+s /usr/bin/passwd
chmod 4755 file

# Setgid (runs as file group)
chmod g+s directory/
chmod 2755 directory

# Sticky bit (only owner can delete)
chmod +t /tmp/
chmod 1777 shared_directory/
```

**Understanding special permissions:**

```bash
# Sticky bit on /tmp
ls -ld /tmp
# drwxrwxrwt  # The 't' means sticky bit
# Anyone can create files, but only owner can delete their own files

# Setuid on passwd command
ls -l /usr/bin/passwd
# -rwsr-xr-x  # The 's' allows users to change their password
# even though password file requires root access
```

---

## Chapter 6: Text Processing and Searching

### 6.1 Searching for Files (find)

```bash
# Find by name
find /home/nobita -name "*.txt"

# Find by type
find . -type f    # Files only
find . -type d    # Directories only

# Find by size
find . -size +100M     # Larger than 100MB
find . -size -1K       # Smaller than 1KB
find . -size 50M       # Exactly 50MB

# Find by modification time
find . -mtime -7       # Modified in last 7 days
find . -mtime +30      # Modified more than 30 days ago
find . -mmin -60       # Modified in last 60 minutes

# Find and execute command
find . -name "*.log" -delete
find . -name "*.txt" -exec cat {} \;
find . -type f -name "*.jpg" -exec cp {} /backup/ \;

# Find by permissions
find . -perm 777       # Exactly 777
find . -perm -644      # At least 644

# Find by owner
find /home -user nobita
```

**Real-world examples:**

```bash
# Find large files eating disk space
find / -type f -size +500M 2>/dev/null

# Find recently modified config files
find /etc -name "*.conf" -mtime -1

# Find and remove old log files
find /var/log -name "*.log" -mtime +30 -delete

# Find all PHP files in website
find /var/www -name "*.php"

# Find files with wrong permissions
find /var/www -type f ! -perm 644
```

### 6.2 Searching File Contents (grep)

```bash
# Basic search
grep "error" logfile.txt

# Case-insensitive search
grep -i "error" logfile.txt

# Show line numbers
grep -n "error" logfile.txt

# Search recursively in directory
grep -r "TODO" ~/projects/

# Invert match (show non-matching lines)
grep -v "success" logfile.txt

# Count occurrences
grep -c "error" logfile.txt

# Show surrounding context
grep -A 3 "error" logfile.txt  # 3 lines after
grep -B 3 "error" logfile.txt  # 3 lines before
grep -C 3 "error" logfile.txt  # 3 lines before and after

# Search multiple files
grep "function" *.js

# Search with regex
grep -E "error|warning|critical" logfile.txt
```

**Practical scenarios:**

```bash
# Find errors in logs
grep -i "error" /var/log/syslog

# Find function definition in code
grep -rn "def calculate_total" ~/projects/

# Check if service is running
ps aux | grep nginx

# Find IP address in logs
grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" access.log

# Search for TODO comments
grep -rn "TODO" --include="*.py" ~/projects/

# Find failed login attempts
grep "Failed password" /var/log/auth.log

# Exclude certain directories
grep -r "import" ~/projects/ --exclude-dir=node_modules
```

### 6.3 Text Stream Processing

**cat - Concatenate and display:**

```bash
# Display file
cat file.txt

# Concatenate multiple files
cat file1.txt file2.txt > combined.txt

# Number lines
cat -n file.txt

# Show non-printing characters
cat -A file.txt
```

**sort - Sort lines:**

```bash
# Sort alphabetically
sort names.txt

# Sort numerically
sort -n numbers.txt

# Reverse sort
sort -r names.txt

# Sort by column
sort -k2 data.txt  # Sort by 2nd column

# Remove duplicates while sorting
sort -u names.txt
```

**uniq - Remove duplicates:**

```bash
# Remove adjacent duplicates (requires sorted input)
sort names.txt | uniq

# Count occurrences
sort names.txt | uniq -c

# Show only duplicates
sort names.txt | uniq -d

# Show only unique lines
sort names.txt | uniq -u
```

**wc - Word count:**

```bash
# Count lines, words, characters
wc file.txt

# Count only lines
wc -l file.txt

# Count only words
wc -w file.txt

# Count multiple files
wc -l *.txt
```

**cut - Extract columns:**

```bash
# Extract characters
cut -c1-5 file.txt    # Characters 1-5

# Extract fields (default delimiter: tab)
cut -f1,3 data.txt    # Fields 1 and 3

# Custom delimiter
cut -d"," -f2 data.csv  # 2nd field in CSV

# Example with /etc/passwd
cut -d":" -f1,7 /etc/passwd  # Username and shell
```

**tr - Translate characters:**

```bash
# Convert lowercase to uppercase
echo "hello" | tr 'a-z' 'A-Z'

# Delete characters
echo "hello123" | tr -d '0-9'

# Squeeze repeated characters
echo "hello    world" | tr -s ' '

# Replace characters
echo "hello" | tr 'el' '31'  # h31lo
```

**Real-world text processing pipeline:**

```bash
# Find most common IP addresses in access log
cut -d" " -f1 access.log | sort | uniq -c | sort -rn | head -10

# Count unique users in log
cut -d":" -f1 /etc/passwd | wc -l

# Find top 5 largest files
find . -type f -exec du -h {} \; | sort -rh | head -5

# Extract email addresses from file
grep -Eo "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" contacts.txt | sort -u
```

---

## Chapter 7: Redirection and Pipes

### 7.1 Understanding Streams

Linux has three data streams:

- **stdin (0)**: Standard input (keyboard)
- **stdout (1)**: Standard output (screen)
- **stderr (2)**: Standard error (screen)

### 7.2 Output Redirection

```bash
# Redirect stdout to file (overwrite)
ls > file_list.txt

# Redirect stdout to file (append)
ls >> file_list.txt

# Redirect stderr to file
ls /nonexistent 2> errors.txt

# Redirect both stdout and stderr
ls /home /nonexistent > output.txt 2>&1

# Modern syntax for both
ls /home /nonexistent &> output.txt

# Discard output
ls > /dev/null

# Discard errors
ls /nonexistent 2> /dev/null

# Discard everything
ls /home /nonexistent &> /dev/null
```

**Practical examples:**

```bash
# Save command output for later
df -h > disk_usage_$(date +%Y%m%d).txt

# Log script errors
./backup_script.sh 2> backup_errors.log

# Keep log of successful commands only
apt update > /var/log/apt_update.log 2> /dev/null

# Save both output and errors
python script.py &> script_output.log
```

### 7.3 Input Redirection

```bash
# Read from file instead of keyboard
sort < unsorted.txt

# Use here document
cat << EOF > new_file.txt
Line 1
Line 2
Line 3
EOF

# Use here string
grep "error" <<< "This is an error message"
```

**Examples:**

```bash
# Send email with file contents
mail -s "Report" user@example.com < report.txt

# Use here document for multi-line input
mysql -u root -p << EOF
USE database_name;
SELECT * FROM users;
EOF
```

### 7.4 Pipes (|)

Pipes send output from one command as input to another:

```bash
# Basic pipe
ls -l | less

# Multiple pipes
cat access.log | grep "404" | wc -l

# Complex pipeline
ps aux | grep nginx | grep -v grep | awk '{print $2}'
```

**Real-world pipelines:**

```bash
# Find top 10 largest files
du -ah /home/nobita | sort -rh | head -10

# Count running processes
ps aux | wc -l

# Find most common error in logs
grep "error" /var/log/syslog | cut -d" " -f5- | sort | uniq -c | sort -rn | head -5

# Monitor live log and filter errors
tail -f /var/log/application.log | grep --color=auto "ERROR"

# List users logged in
who | cut -d" " -f1 | sort -u

# Find files modified today
find /home -mtime 0 | wc -l

# Disk usage by directory
du -sh /var/* | sort -rh | head -10

# Monitor network connections
netstat -tuln | grep LISTEN

# Find process using most memory
ps aux | sort -rnk 4 | head -5

# Count lines of code in project
find ~/projects -name "*.py" | xargs wc -l | sort -rn
```

### 7.5 tee Command

Write to file AND display on screen:

```bash
# Save and display
ls -l | tee file_list.txt

# Append instead of overwrite
ls -l | tee -a file_list.txt

# Multiple outputs
echo "Log entry" | tee -a log1.txt log2.txt log3.txt

# Use in pipeline
cat access.log | grep "error" | tee errors.txt | wc -l
```

**Practical uses:**

```bash
# Monitor and save script output
./long_running_script.sh | tee script_output.log

# Save intermediate results
cat data.txt | sort | tee sorted.txt | uniq > unique.txt

# Log apt updates
sudo apt update | tee apt_update.log
```

---

## Chapter 8: Process Management

### 8.1 Viewing Processes

```bash
# List all processes
ps aux

# Tree view of processes
ps auxf
pstree

# Real-time process viewer
top
htop  # More user-friendly (install first)

# List processes for current user
ps -u nobita

# Find specific process
ps aux | grep nginx

# Show process hierarchy
ps -ejH
```

**Understanding ps output:**

```bash
ps aux
# USER  PID  %CPU %MEM    VSZ   RSS TTY STAT START   TIME COMMAND
# nobita 1234 0.5  2.1 123456 67890 ?   Ss   10:00   0:05 /usr/bin/python

# PID: Process ID
# %CPU: CPU usage
# %MEM: Memory usage
# VSZ: Virtual memory size
# RSS: Resident memory size
# TTY: Terminal
# STAT: Process state (S=sleeping, R=running, Z=zombie)
# START: Start time
# TIME: CPU time used
# COMMAND: Command name
```

### 8.2 Managing Processes

```bash
# Run command in background
long_command &

# List background jobs
jobs

# Bring job to foreground
fg %1

# Send job to background
bg %1

# Suspend current process (Ctrl+Z)
# Then resume in background
bg
```

**Example workflow:**

```bash
# Start server in background
python -m http.server 8000 &
# [1] 12345

# List jobs
jobs
# [1]+  Running  python -m http.server 8000 &

# Bring to foreground
fg %1

# Suspend with Ctrl+Z
# Resume in background
bg %1

# Continue working while server runs
```

### 8.3 Killing Processes

```bash
# Kill by PID
kill 1234

# Force kill
kill -9 1234
# Or
kill -SIGKILL 1234

# Kill by name
killall firefox
pkill firefox

# Interactive process killer
htop  # Press F9 to kill selected process

# Kill all processes for user
killall -u nobita

# Kill gracefully (allow cleanup)
kill -15 1234
kill -SIGTERM 1234
```

**Common signals:**

```bash
kill -l  # List all signals

# Most used:
kill -1 PID   # SIGHUP (reload config)
kill -2 PID   # SIGINT (Ctrl+C)
kill -9 PID   # SIGKILL (force kill, can't be caught)
kill -15 PID  # SIGTERM (graceful termination)
kill -18 PID  # SIGCONT (continue suspended process)
kill -19 PID  # SIGSTOP (suspend process)
```

**Real-world scenarios:**

```bash
# Find and kill hung process
ps aux | grep "hung_program"
kill -9 12345

# Reload nginx configuration
sudo kill -HUP $(cat /var/run/nginx.pid)
# Or
sudo nginx -s reload

# Kill all Chrome processes
killall -9 chrome

# Force quit unresponsive application
pkill -9 -f "unresponsive_app"

# Stop all user processes
killall -u temporary_user
```

### 8.4 Process Priority (nice and renice)

Priority ranges from -20 (highest) to 19 (lowest):

```bash
# Start with low priority
nice -n 10 ./cpu_intensive_task.sh

# Start with high priority (requires root)
sudo nice -n -10 ./important_task.sh

# Change priority of running process
renice -n 5 -p 1234

# Set priority by user
sudo renice -n 10 -u nobita
```

**Practical examples:**

```bash
# Run backup with low priority
nice -n 19 tar czf backup.tar.gz /home/nobita

# Run video encoding in background with low priority
nice -n 15 ffmpeg -i input.mp4 output.mp4 &

# Increase priority of database process
sudo renice -n -5 -p $(pgrep mysql)
```

### 8.5 nohup and screen

**nohup - Run command immune to hangups:**

```bash
# Run command that survives logout
nohup python long_script.py &

# Output goes to nohup.out by default
nohup python script.py > custom_output.log 2>&1 &
```

**screen - Terminal multiplexer:**

```bash
# Start new screen session
screen

# Start named session
screen -S mysession

# Detach from session (Ctrl+A then D)

# List sessions
screen -ls

# Reattach to session
screen -r mysession

# Kill session
screen -X -S mysession quit
```

**tmux - Modern alternative to screen:**

```bash
# Start new session
tmux

# Create named session
tmux new -s mysession

# Detach (Ctrl+B then D)

# List sessions
tmux ls

# Attach to session
tmux attach -t mysession

# Kill session
tmux kill-session -t mysession
```

**Real-world usage:**

```bash
# Run long backup on remote server
ssh server
screen -S backup
./backup_script.sh
# Press Ctrl+A then D to detach
# Logout from SSH - script continues running

# Later, reattach to check progress
ssh server
screen -r backup
```

---

## Chapter 9: Package Management

### 9.1 APT (Debian/Ubuntu)

```bash
# Update package lists
sudo apt update

# Upgrade all packages
sudo apt upgrade

# Full upgrade (handles dependencies better)
sudo apt full-upgrade

# Install package
sudo apt install nginx

# Install multiple packages
sudo apt install nginx mysql-server php

# Remove package
sudo apt remove nginx

# Remove package and config files
sudo apt purge nginx

# Remove unused dependencies
sudo apt autoremove

# Search for package
apt search nginx

# Show package info
apt show nginx

# List installed packages
apt list --installed

# List upgradable packages
apt list --upgradable
```

**Practical scenarios:**

```bash
# Set up web server
sudo apt update
sudo apt install nginx mysql-server php-fpm
sudo systemctl start nginx

# Install development tools
sudo apt install build-essential git curl wget

# Clean up system
sudo apt autoremove
sudo apt autoclean

# Fix broken packages
sudo apt --fix-broken install
```

### 9.2 YUM/DNF (RedHat/CentOS/Fedora)

```bash
# Update package lists
sudo dnf check-update

# Install package
sudo dnf install nginx

# Update all packages
sudo dnf upgrade

# Remove package
sudo dnf remove nginx

# Search for package
dnf search nginx

# Show package info
dnf info nginx

# List installed packages
dnf list installed

# Clean cache
sudo dnf clean all
```

### 9.3 Snap (Universal packages)

```bash
# Install snap
sudo apt install snapd

# Find packages
snap find vlc

# Install package
sudo snap install vlc

# List installed snaps
snap list

# Update all snaps
sudo snap refresh

# Remove snap
sudo snap remove vlc
```

### 9.4 Downloading and Installing from Source

```bash
# Download source
wget https://example.com/software-1.0.tar.gz

# Extract
tar xzf software-1.0.tar.gz
cd software-1.0

# Configure, compile, install
./configure
make
sudo make install

# Install dependencies first
sudo apt install build-essential
```

---

## Chapter 10: User and Group Management

### 10.1 User Management

```bash
# Add new user
sudo adduser gian

# Add user with specific UID
sudo useradd -u 1500 shizuka

# Create user with home directory
sudo useradd -m -s /bin/bash nobita

# Change user password
sudo passwd gian

# Change your own password
passwd

# Delete user
sudo userdel gian

# Delete user and home directory
sudo userdel -r gian

# Modify user
sudo usermod -l new_name old_name

# Add user to group
sudo usermod -aG sudo nobita

# Lock user account
sudo usermod -L gian

# Unlock user account
sudo usermod -U gian

# View user info
id nobita
finger nobita
```

**Real-world scenarios:**

```bash
# Create developer user
sudo adduser dev_user
sudo usermod -aG sudo,www-data dev_user

# Create user for deployment
sudo useradd -m -s /bin/bash deploy
sudo mkdir /home/deploy/.ssh
sudo cp authorized_keys /home/deploy/.ssh/
sudo chown -R deploy:deploy /home/deploy/.ssh

# Disable user temporarily
sudo usermod -L temporary_contractor

# View all users
cat /etc/passwd
cut -d: -f1 /etc/passwd
```

### 10.2 Group Management

```bash
# Create group
sudo groupadd developers

# Delete group
sudo groupdel developers

# Add user to group
sudo usermod -aG developers nobita

# Remove user from group
sudo gpasswd -d nobita developers

# View user groups
groups nobita

# View group members
getent group developers

# Change file group
sudo chgrp developers project_folder
```

**Practical example - Setting up shared project:**

```bash
# Create developers group
sudo groupadd developers

# Add team members
sudo usermod -aG developers nobita
sudo usermod -aG developers gian
sudo usermod -aG developers shizuka

# Create shared directory
sudo mkdir /opt/projects
sudo chgrp developers /opt/projects
sudo chmod 2775 /opt/projects

# Now all developers can collaborate in /opt/projects
```

### 10.3 Sudo and Root Access

```bash
# Run command as root
sudo apt update

# Switch to root user
sudo su
# Or
sudo -i

# Run command as different user
sudo -u www-data whoami

# Edit sudoers file (safely)
sudo visudo

# View sudo log
sudo tail /var/log/auth.log
```

**Sudoers configuration:**

```bash
# Edit sudoers
sudo visudo

# Allow user to run all commands
nobita ALL=(ALL:ALL) ALL

# Allow without password
nobita ALL=(ALL) NOPASSWD: ALL

# Allow specific commands
nobita ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx

# Allow group
%developers ALL=(ALL:ALL) ALL
```

---

## Chapter 11: Networking Basics

### 11.1 Network Configuration

```bash
# View IP addresses
ip addr show
# Or short form
ip a

# View network interfaces
ifconfig  # Older command
ip link show

# View routing table
ip route show
route -n

# View DNS configuration
cat /etc/resolv.conf

# Test connectivity
ping google.com
ping -c 4 8.8.8.8  # Send 4 packets

# Trace route
traceroute google.com

# DNS lookup
nslookup google.com
dig google.com

# View network statistics
netstat -tuln  # All listening ports
ss -tuln       # Modern alternative
```

**Practical examples:**

```bash
# Check if service is accessible
ping -c 3 192.168.1.100

# Find your IP address
ip addr show | grep inet

# Test website response
curl -I https://example.com

# Download file
wget https://example.com/file.zip
curl -O https://example.com/file.zip

# Test port connection
telnet example.com 80
nc -zv example.com 80
```

### 11.2 Firewall (ufw)

```bash
# Enable firewall
sudo ufw enable

# Disable firewall
sudo ufw disable

# Check status
sudo ufw status
sudo ufw status verbose

# Allow port
sudo ufw allow 22
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Deny port
sudo ufw deny 3306

# Allow from specific IP
sudo ufw allow from 192.168.1.100

# Allow specific IP to specific port
sudo ufw allow from 192.168.1.100 to any port 22

# Delete rule
sudo ufw delete allow 80

# Reset firewall
sudo ufw reset
```

**Common setup for web server:**

```bash
# Allow SSH, HTTP, HTTPS
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status
```

### 11.3 SSH (Secure Shell)

```bash
# Connect to remote server
ssh username@server_ip

# Connect with specific port
ssh -p 2222 username@server_ip

# Copy file to remote
scp file.txt username@server:/path/to/destination

# Copy from remote
scp username@server:/path/file.txt ./

# Copy directory
scp -r folder username@server:/path/

# Generate SSH key
ssh-keygen -t rsa -b 4096

# Copy public key to server
ssh-copy-id username@server

# SSH with key
ssh -i ~/.ssh/private_key username@server
```

**Setting up passwordless SSH:**

```bash
# On local machine
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# Press Enter to accept defaults

# Copy to server
ssh-copy-id nobita@192.168.1.100

# Now you can login without password
ssh nobita@192.168.1.100
```

**SSH config file:**

```bash
# Edit ~/.ssh/config
nano ~/.ssh/config

# Add:
Host myserver
    HostName 192.168.1.100
    User nobita
    Port 22
    IdentityFile ~/.ssh/id_rsa

# Now you can simply use:
ssh myserver
```

---

## Chapter 12: System Monitoring and Logs

### 12.1 System Information

```bash
# System information
uname -a          # All system info
hostnamectl       # Hostname and OS info

# CPU information
lscpu
cat /proc/cpuinfo

# Memory information
free -h
cat /proc/meminfo

# Disk usage
df -h             # Disk space
du -sh /home/*    # Directory sizes
ncdu /home        # Interactive disk usage

# Hardware information
lshw              # Detailed hardware
lspci             # PCI devices
lsusb             # USB devices
lsblk             # Block devices
```

### 12.2 System Monitoring

```bash
# Real-time process viewer
top
htop

# System activity
vmstat 1          # Every second
iostat            # I/O statistics
sar               # System activity reporter

# Memory usage
free -h
watch -n 1 free -h  # Update every second

# Disk I/O
iotop             # Like top for disk I/O

# Network monitoring
iftop             # Network bandwidth
nethogs           # Network by process
```

**Monitoring script example:**

```bash
#!/bin/bash
# System monitoring script

echo "=== System Monitoring ==="
echo "Date: $(date)"
echo

echo "=== CPU Usage ==="
top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'

echo
echo "=== Memory Usage ==="
free -h

echo
echo "=== Disk Usage ==="
df -h | grep -v tmpfs

echo
echo "=== Top 5 Processes by CPU ==="
ps aux --sort=-%cpu | head -6

echo
echo "=== Top 5 Processes by Memory ==="
ps aux --sort=-%mem | head -6
```

### 12.3 Log Files

**Important log locations:**

```bash
/var/log/syslog       # System log
/var/log/auth.log     # Authentication log
/var/log/kern.log     # Kernel log
/var/log/apache2/     # Apache logs
/var/log/nginx/       # Nginx logs
/var/log/mysql/       # MySQL logs
```

**Viewing logs:**

```bash
# View log file
sudo tail -f /var/log/syslog

# Last 100 lines
sudo tail -n 100 /var/log/syslog

# Search in logs
sudo grep "error" /var/log/syslog

# View with journalctl (systemd)
sudo journalctl           # All logs
sudo journalctl -u nginx  # Specific service
sudo journalctl -f        # Follow mode
sudo journalctl --since "1 hour ago"
sudo journalctl --since "2024-11-26 10:00:00"
```

**Log analysis examples:**

```bash
# Find failed login attempts
sudo grep "Failed password" /var/log/auth.log

# Count 404 errors in web server
sudo grep "404" /var/log/nginx/access.log | wc -l

# Find IP addresses with most requests
sudo awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head

# Monitor errors in real-time
sudo tail -f /var/log/syslog | grep -i error

# Check disk space from logs
sudo grep "No space left" /var/log/syslog
```

---

## Chapter 13: Bash Scripting Basics

### 13.1 Creating Your First Script

```bash
#!/bin/bash
# My first script

echo "Hello, Linux!"
echo "Current user: $USER"
echo "Home directory: $HOME"
echo "Current directory: $(pwd)"
```

**Make it executable and run:**

```bash
chmod +x script.sh
./script.sh
```

### 13.2 Variables

```bash
#!/bin/bash

# String variable
name="Nobita"
echo "Hello, $name"

# Number variable
age=10
echo "Age: $age"

# Command substitution
current_date=$(date)
echo "Today is: $current_date"

# User input
echo "What's your name?"
read user_name
echo "Hello, $user_name!"

# Environment variables
echo "Path: $PATH"
echo "User: $USER"
echo "Home: $HOME"
```

### 13.3 Conditionals

```bash
#!/bin/bash

# If statement
age=18
if [ $age -ge 18 ]; then
    echo "You are an adult"
else
    echo "You are a minor"
fi

# Multiple conditions
score=85
if [ $score -ge 90 ]; then
    echo "Grade: A"
elif [ $score -ge 80 ]; then
    echo "Grade: B"
elif [ $score -ge 70 ]; then
    echo "Grade: C"
else
    echo "Grade: F"
fi

# File checks
if [ -f "file.txt" ]; then
    echo "File exists"
fi

if [ -d "directory" ]; then
    echo "Directory exists"
fi

# String comparison
name="Nobita"
if [ "$name" == "Nobita" ]; then
    echo "Hello Nobita!"
fi
```

**Comparison operators:**

```bash
# Numeric comparisons
-eq  # Equal
-ne  # Not equal
-gt  # Greater than
-lt  # Less than
-ge  # Greater than or equal
-le  # Less than or equal

# String comparisons
==   # Equal
!=   # Not equal
-z   # Empty string
-n   # Non-empty string

# File checks
-f   # Regular file exists
-d   # Directory exists
-r   # Readable
-w   # Writable
-x   # Executable
```

### 13.4 Loops

**For loop:**

```bash
#!/bin/bash

# Loop through list
for name in Nobita Gian Shizuka Suneo; do
    echo "Hello, $name"
done

# Loop through numbers
for i in {1..5}; do
    echo "Number: $i"
done

# C-style for loop
for ((i=1; i<=5; i++)); do
    echo "Count: $i"
done

# Loop through files
for file in *.txt; do
    echo "Processing: $file"
done
```

**While loop:**

```bash
#!/bin/bash

# Basic while loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Read file line by line
while IFS= read -r line; do
    echo "Line: $line"
done < input.txt

# Infinite loop
while true; do
    echo "Press Ctrl+C to stop"
    sleep 1
done
```

### 13.5 Functions

```bash
#!/bin/bash

# Simple function
greet() {
    echo "Hello, World!"
}

# Call function
greet

# Function with parameters
greet_user() {
    echo "Hello, $1!"
}

greet_user "Nobita"

# Function with return value
add_numbers() {
    local sum=$(($1 + $2))
    echo $sum
}

result=$(add_numbers 5 3)
echo "Sum: $result"

# Function with multiple parameters
create_user() {
    local username=$1
    local fullname=$2
    
    echo "Creating user: $username"
    echo "Full name: $fullname"
    sudo useradd -m -c "$fullname" "$username"
}

create_user "nobita" "Nobita Nobi"
```

### 13.6 Practical Script Examples

**Backup script:**

```bash
#!/bin/bash

# Backup script
SOURCE="/home/nobita/projects"
DEST="/backup"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_$DATE.tar.gz"

echo "Starting backup..."
tar -czf "$DEST/$BACKUP_FILE" "$SOURCE"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "File: $DEST/$BACKUP_FILE"
else
    echo "Backup failed!"
    exit 1
fi
```

**System monitor script:**

```bash
#!/bin/bash

# System monitoring script
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80

# Check CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')

# Check memory usage
memory_usage=$(free | grep Mem | awk '{print ($3/$2) * 100.0}')

echo "CPU Usage: ${cpu_usage}%"
echo "Memory Usage: ${memory_usage}%"

# Alert if thresholds exceeded
if (( $(echo "$cpu_usage > $CPU_THRESHOLD" | bc -l) )); then
    echo "WARNING: High CPU usage!"
fi

if (( $(echo "$memory_usage > $MEMORY_THRESHOLD" | bc -l) )); then
    echo "WARNING: High memory usage!"
fi
```

**Deployment script:**

```bash
#!/bin/bash

# Web application deployment script

echo "Starting deployment..."

# Pull latest code
cd /var/www/myapp
git pull origin main

# Install dependencies
npm install

# Build application
npm run build

# Restart services
sudo systemctl restart nginx
sudo systemctl restart myapp

# Check status
if systemctl is-active --quiet myapp; then
    echo "Deployment successful!"
else
    echo "Deployment failed!"
    exit 1
fi
```

---

## Chapter 14: Automation with Cron

### 14.1 Understanding Cron

Cron syntax:

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, Sunday=0 or 7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

### 14.2 Managing Cron Jobs

```bash
# Edit crontab
crontab -e

# List cron jobs
crontab -l

# Remove all cron jobs
crontab -r

# Edit crontab for specific user
sudo crontab -u nobita -e
```

### 14.3 Cron Examples

```bash
# Run every minute
* * * * * /path/to/script.sh

# Run every hour
0 * * * * /path/to/script.sh

# Run every day at 2:30 AM
30 2 * * * /path/to/backup.sh

# Run every Monday at 9:00 AM
0 9 * * 1 /path/to/weekly_report.sh

# Run first day of every month
0 0 1 * * /path/to/monthly_task.sh

# Run every 5 minutes
*/5 * * * * /path/to/script.sh

# Run on weekdays at 6 PM
0 18 * * 1-5 /path/to/script.sh

# Run multiple times
0 6,12,18 * * * /path/to/script.sh
```

**Practical cron jobs:**

```bash
# Daily backup at 2 AM
0 2 * * * /home/nobita/scripts/backup.sh >> /var/log/backup.log 2>&1

# Clear /tmp every Sunday at midnight
0 0 * * 0 rm -rf /tmp/*

# Check disk space every hour
0 * * * * df -h | mail -s "Disk Usage Report" admin@example.com

# Update system every night
0 3 * * * sudo apt update && sudo apt upgrade -y

# Restart service daily
0 4 * * * sudo systemctl restart myapp
```

### 14.4 Anacron

For tasks that don't require precise timing:

```bash
# Edit anacrontab
sudo nano /etc/anacrontab

# Format: period delay job-identifier command
1  5  daily-backup  /home/nobita/scripts/backup.sh
7  10 weekly-clean  /home/nobita/scripts/cleanup.sh
```

---

## Chapter 15: Best Practices and Tips

### 15.1 Security Best Practices

```bash
# Keep system updated
sudo apt update && sudo apt upgrade

# Use strong passwords
passwd  # Change regularly

# Disable root SSH login
sudo nano /etc/ssh/sshd_config
# Set: PermitRootLogin no
sudo systemctl restart sshd

# Use SSH keys instead of passwords
ssh-keygen -t rsa -b 4096

# Enable firewall
sudo ufw enable
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443

# Regular backups
# Automate with cron

# Monitor logs
sudo tail -f /var/log/auth.log

# Set file permissions correctly
chmod 600 sensitive_file
chmod 755 public_directory
```

### 15.2 Performance Tips

```bash
# Clean package cache
sudo apt autoclean
sudo apt autoremove

# Find large files
find / -type f -size +100M 2>/dev/null

# Monitor resource usage
htop
iotop

# Disable unnecessary services
sudo systemctl disable bluetooth
sudo systemctl stop bluetooth

# Use lighter alternatives
# Instead of Firefox, use Midori
# Instead of LibreOffice, use AbiWord
```

### 15.3 Useful Aliases

Add to `~/.bashrc`:

```bash
# Navigation aliases
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -lah'
alias la='ls -A'

# Safety aliases
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Git aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'

# System aliases
alias update='sudo apt update && sudo apt upgrade'
alias ports='netstat -tulanp'
alias meminfo='free -h'
alias diskinfo='df -h'

# Quick edit configs
alias bashrc='nano ~/.bashrc'
alias reload='source ~/.bashrc'
```

Apply changes:

```bash
source ~/.bashrc
```

---

## Quick Reference Cheat Sheet

```bash
# File Operations
ls -lah              # List files with details
cd /path             # Change directory
pwd                  # Print working directory
mkdir dirname        # Create directory
touch file.txt       # Create file
cp source dest       # Copy
mv source dest       # Move/rename
rm file              # Delete file
rm -r dir            # Delete directory

# File Viewing
cat file             # View file
less file            # Page through file
head -n 10 file      # First 10 lines
tail -f file         # Follow file (live)

# File Permissions
chmod 755 file       # Change permissions
chown user file      # Change owner
chgrp group file     # Change group

# Search
find / -name file    # Find file
grep "text" file     # Search in file
which command        # Find command location

# Process Management
ps aux               # List processes
top                  # Real-time processes
kill PID             # Kill process
killall name         # Kill by name

# Network
ping host            # Test connectivity
ifconfig             # Network interfaces
netstat -tuln        # Network connections
ssh user@host        # Remote login

# Package Management (Ubuntu/Debian)
sudo apt update      # Update package lists
sudo apt install pkg # Install package
sudo apt remove pkg  # Remove package
sudo apt upgrade     # Upgrade all packages

# System Information
uname -a             # System info
df -h                # Disk usage
free -h              # Memory usage
lscpu                # CPU info

# User Management
sudo adduser name    # Add user
sudo passwd user     # Change password
sudo usermod -aG grp user  # Add to group

# File Compression
tar -czf file.tar.gz dir/  # Compress
tar -xzf file.tar.gz       # Extract
zip -r file.zip dir/       # Zip
unzip file.zip             # Unzip

# Text Processing
sort file            # Sort lines
uniq file            # Remove duplicates
wc -l file           # Count lines
cut -d: -f1 file     # Extract column

# Redirection
command > file       # Redirect output
command >> file      # Append output
command 2> file      # Redirect errors
command | command2   # Pipe to another command
```

---

This comprehensive Linux guide covers everything from basic navigation to advanced automation. Practice these commands regularly, and you'll become proficient in Linux system administration!
