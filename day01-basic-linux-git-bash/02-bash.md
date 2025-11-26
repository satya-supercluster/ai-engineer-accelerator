# Complete Bash Scripting & Command Line Guide

## Enterprise-Level Linux/Unix Shell Mastery

---

## Chapter 1: Introduction to Bash and Shell

### 1.1 What is Bash?

**Bash (Bourne Again Shell)** is a command-line interface and scripting language used to interact with Unix/Linux systems. It's the default shell on most Linux distributions and macOS.

**Why learn Bash for enterprise work:**

- Automate repetitive tasks (save hours daily)
- Manage servers and cloud infrastructure
- Process large datasets efficiently
- Deploy applications and manage CI/CD pipelines
- Debug production issues quickly
- Essential for DevOps, SRE, and Backend Engineering roles

**Real-world scenario:** A DevOps engineer needs to restart 50 application servers, check their logs, and verify they're running correctly. Without Bash, this could take hours. With Bash: 2 minutes.

### 1.2 Shell vs Terminal vs Console

- **Shell**: The program that interprets commands (bash, zsh, fish)
- **Terminal**: The application that runs the shell (Terminal.app, iTerm2, GNOME Terminal)
- **Console**: Physical hardware or virtual interface for system access

```bash
# Check your current shell
echo $SHELL
# Output: /bin/bash or /bin/zsh

# Check Bash version
bash --version

# List available shells
cat /etc/shells
```

### 1.3 Types of Shells

```bash
# Common shells
sh          # Original Bourne Shell
bash        # Bourne Again Shell (most common)
zsh         # Z Shell (macOS default since Catalina)
fish        # Friendly Interactive Shell
ksh         # Korn Shell
dash        # Debian Almquist Shell
```

---

## Chapter 2: Essential Command Line Navigation

### 2.1 File System Structure

```bash
# Linux/Unix file system hierarchy
/                    # Root directory
├── bin             # Essential user binaries
├── boot            # Boot loader files
├── dev             # Device files
├── etc             # System configuration files
├── home            # User home directories
├── lib             # Shared libraries
├── opt             # Optional software
├── root            # Root user's home
├── tmp             # Temporary files
├── usr             # User programs
└── var             # Variable data (logs, databases)
```

### 2.2 Navigation Commands

```bash
# Print working directory
pwd
# Output: /home/username/projects

# List directory contents
ls                  # Basic listing
ls -l              # Long format (permissions, owner, size, date)
ls -la             # Include hidden files (starting with .)
ls -lh             # Human-readable file sizes
ls -lt             # Sort by modification time
ls -lS             # Sort by file size
ls -R              # Recursive listing

# Change directory
cd /var/log        # Absolute path
cd projects        # Relative path
cd ..              # Parent directory
cd ~               # Home directory
cd -               # Previous directory
cd                 # Home directory (shortcut)

# Create directories
mkdir new-project
mkdir -p parent/child/grandchild  # Create nested directories
mkdir -p project/{src,tests,docs} # Create multiple directories
```

**Enterprise scenario:**

```bash
# Navigate to application logs
cd /var/log/nginx

# Check latest error logs
ls -lt | head -5

# Go back to your project
cd ~/projects/ecommerce-api
```

### 2.3 File Operations

```bash
# Create files
touch newfile.txt                    # Create empty file
touch file1.txt file2.txt file3.txt  # Multiple files

# Copy files and directories
cp source.txt destination.txt        # Copy file
cp -r source-dir/ dest-dir/         # Copy directory recursively
cp -p file.txt backup.txt           # Preserve attributes
cp *.txt backup/                    # Copy all .txt files

# Move/Rename
mv oldname.txt newname.txt          # Rename file
mv file.txt /path/to/destination/   # Move file
mv *.log archive/                   # Move multiple files

# Delete files and directories
rm file.txt                         # Remove file
rm -f file.txt                      # Force remove (no prompt)
rm -r directory/                    # Remove directory recursively
rm -rf directory/                   # Force remove directory
rm -i *.txt                        # Interactive (prompt for each)

# View file contents
cat file.txt                        # Display entire file
less file.txt                       # View with pagination (q to quit)
more file.txt                       # View with pagination (older)
head file.txt                       # First 10 lines
head -n 20 file.txt                # First 20 lines
tail file.txt                       # Last 10 lines
tail -n 50 file.txt                # Last 50 lines
tail -f application.log            # Follow file (live updates)
```

**Real-world example:**

```bash
# Monitoring production logs in real-time
tail -f /var/log/application/error.log

# Check last 100 lines of specific error
tail -n 100 /var/log/nginx/error.log | grep "500 Internal"

# Copy production config to backup
cp -p /etc/nginx/nginx.conf /backup/nginx.conf.$(date +%Y%m%d)
```

---

## Chapter 3: Text Processing and Manipulation

### 3.1 Grep - Search Text

```bash
# Basic grep
grep "error" application.log                # Search for "error"
grep -i "error" application.log            # Case insensitive
grep -r "TODO" .                           # Recursive search
grep -n "function" script.sh               # Show line numbers
grep -v "debug" application.log            # Invert match (exclude)
grep -c "error" application.log            # Count matches
grep -A 3 "error" application.log          # Show 3 lines after
grep -B 3 "error" application.log          # Show 3 lines before
grep -C 3 "error" application.log          # Show 3 lines context

# Advanced patterns
grep "error\|warning" app.log              # OR condition
grep -E "error|warning" app.log            # Extended regex (same)
grep "^Error" app.log                      # Lines starting with
grep "Error$" app.log                      # Lines ending with
grep "\[ERROR\]" app.log                   # Escape special characters

# Practical examples
grep -r "password" /etc/                   # Find config files with passwords
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" access.log  # Find IP addresses
```

**Enterprise scenario:**

```bash
# Find all failed login attempts in the last hour
grep "Failed password" /var/log/auth.log | tail -n 1000

# Find all API endpoints returning 500 errors
grep "HTTP/1.1\" 500" /var/log/nginx/access.log | awk '{print $7}' | sort | uniq -c

# Search for memory leaks in application logs
grep -i "out of memory\|memory leak" /var/log/application/*.log
```

### 3.2 Awk - Pattern Scanning and Processing

```bash
# Basic awk
awk '{print $1}' file.txt              # Print first column
awk '{print $1, $3}' file.txt          # Print columns 1 and 3
awk '{print $NF}' file.txt             # Print last column
awk -F: '{print $1}' /etc/passwd       # Custom delimiter (colon)

# Conditional processing
awk '$3 > 100 {print $1, $3}' data.txt            # If column 3 > 100
awk '$5 == "FAILED" {print $0}' test-results.txt  # If column 5 equals FAILED
awk 'NR > 1 {print}' file.txt                     # Skip header (line 1)

# Calculations
awk '{sum += $3} END {print sum}' sales.txt       # Sum column 3
awk '{sum += $3} END {print sum/NR}' sales.txt    # Average of column 3

# Built-in variables
# NR  = Current record (line) number
# NF  = Number of fields in current record
# $0  = Entire line
# $1,$2,etc = Individual fields
```

**Enterprise examples:**

```bash
# Extract request times from nginx access logs
awk '{print $NF}' /var/log/nginx/access.log | \
  awk '{sum+=$1; count++} END {print "Avg:", sum/count}'

# Find top 10 IP addresses by request count
awk '{print $1}' /var/log/nginx/access.log | \
  sort | uniq -c | sort -rn | head -10

# Calculate total sales from CSV
awk -F',' '{sum += $4} END {print "Total: $" sum}' sales.csv

# Monitor memory usage by process
ps aux | awk '{sum+=$6} END {print "Total memory: " sum/1024 "MB"}'
```

### 3.3 Sed - Stream Editor

```bash
# Substitution
sed 's/old/new/' file.txt              # Replace first occurrence per line
sed 's/old/new/g' file.txt             # Replace all occurrences
sed 's/old/new/gi' file.txt            # Case insensitive replace
sed -i 's/old/new/g' file.txt          # Edit file in-place
sed -i.bak 's/old/new/g' file.txt      # Create backup before editing

# Delete lines
sed '/pattern/d' file.txt              # Delete lines matching pattern
sed '1d' file.txt                      # Delete first line
sed '1,5d' file.txt                    # Delete lines 1-5
sed '$d' file.txt                      # Delete last line

# Insert and append
sed '1i\Header Line' file.txt          # Insert before line 1
sed '1a\New Line' file.txt             # Append after line 1
sed '/pattern/a\New Line' file.txt     # Append after pattern match

# Multiple operations
sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt
sed 's/foo/bar/; s/baz/qux/' file.txt  # Same as above
```

**Production use cases:**

```bash
# Update configuration files
sed -i 's/max_connections = 100/max_connections = 500/' /etc/mysql/my.cnf

# Remove empty lines from logs
sed '/^$/d' application.log > cleaned.log

# Replace all localhost with production domain
sed -i 's/localhost:3000/api.company.com/g' config.js

# Mask sensitive data in logs before sharing
sed 's/password=[^&]*/password=REDACTED/g' application.log

# Update version in multiple files
find . -name "package.json" -exec sed -i 's/"version": "1.0.0"/"version": "1.1.0"/' {} \;
```

### 3.4 Cut - Extract Sections

```bash
# Cut by delimiter
cut -d':' -f1 /etc/passwd              # Extract usernames
cut -d',' -f1,3 data.csv               # Extract columns 1 and 3
cut -d' ' -f2-4 file.txt               # Extract fields 2 through 4

# Cut by character position
cut -c1-10 file.txt                    # Extract characters 1-10
cut -c5- file.txt                      # Extract from character 5 onward

# Practical examples
cut -d',' -f2 sales.csv | sort | uniq  # Get unique products
```

### 3.5 Sort and Uniq

```bash
# Sort
sort file.txt                          # Alphabetical sort
sort -n numbers.txt                    # Numeric sort
sort -r file.txt                       # Reverse sort
sort -k2 data.txt                      # Sort by 2nd column
sort -t',' -k3 -n data.csv             # Sort CSV by 3rd column numerically
sort -u file.txt                       # Sort and remove duplicates

# Uniq (requires sorted input)
sort file.txt | uniq                   # Remove duplicate lines
sort file.txt | uniq -c                # Count occurrences
sort file.txt | uniq -d                # Show only duplicates
sort file.txt | uniq -u                # Show only unique lines
```

**Enterprise scenario:**

```bash
# Find most common errors in logs
grep "ERROR" app.log | sort | uniq -c | sort -rn | head -10

# Get unique IP addresses accessing the server
awk '{print $1}' /var/log/nginx/access.log | sort -u

# Find duplicate entries in database export
cut -d',' -f1 users.csv | sort | uniq -d
```

---

## Chapter 4: Redirection and Pipes

### 4.1 Input/Output Redirection

```bash
# Output redirection
command > file.txt                     # Overwrite file
command >> file.txt                    # Append to file
command 2> error.log                   # Redirect errors
command > output.txt 2>&1              # Redirect both stdout and stderr
command &> output.txt                  # Same as above (shorthand)

# Input redirection
command < input.txt                    # Read from file
command << EOF                         # Here document
line 1
line 2
EOF

# Examples
ls -la > directory-listing.txt
cat file1.txt file2.txt > combined.txt
echo "Log entry" >> application.log
find / -name "*.log" 2> /dev/null     # Suppress errors
```

### 4.2 Pipes

Pipes (`|`) send output of one command as input to another:

```bash
# Basic pipes
ls -l | less                           # Page through long output
cat file.txt | grep "error"            # Search in file
ps aux | grep nginx                    # Find nginx processes

# Chaining multiple commands
cat access.log | grep "404" | wc -l    # Count 404 errors
cat data.txt | sort | uniq | wc -l     # Count unique lines

# Complex pipelines
ps aux | awk '{print $2, $11}' | sort -k2 | head -10
```

**Real-world pipelines:**

```bash
# Monitor top memory-consuming processes
ps aux | sort -k4 -rn | head -10

# Find largest files in current directory
du -ah . | sort -rh | head -20

# Extract email addresses from file
grep -Eo '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' contacts.txt | sort -u

# Monitor active connections by IP
netstat -an | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn

# Check disk usage by directory
du -sh /var/* | sort -rh | head -10
```

### 4.3 Tee Command

Save output to file AND display it:

```bash
# Basic tee
command | tee output.txt               # Overwrite
command | tee -a output.txt            # Append

# Multiple files
command | tee file1.txt file2.txt

# Examples
ls -la | tee directory-list.txt        # Save and display
./deploy.sh | tee deploy.log           # Save deployment output
```

---

## Chapter 5: Process Management

### 5.1 Viewing Processes

```bash
# List processes
ps                                     # Current shell processes
ps aux                                 # All processes (detailed)
ps -ef                                 # All processes (different format)
ps aux | grep nginx                    # Find specific process

# Top - interactive process viewer
top                                    # Real-time process monitor
htop                                   # Enhanced version (if installed)

# Process tree
pstree                                 # Show process hierarchy
pstree -p                              # Include PIDs

# Get process info
ps -p 1234                            # Info for specific PID
ps -u username                        # Processes by user
```

**Important ps columns:**

```
USER       PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      1234  2.5  1.3  45678  9876 ?        Ss   10:00   0:05 nginx
```

### 5.2 Managing Processes

```bash
# Foreground and background
command                               # Run in foreground
command &                             # Run in background
Ctrl + Z                              # Suspend current process
bg                                    # Resume in background
fg                                    # Bring to foreground
jobs                                  # List background jobs

# Process control
kill PID                              # Terminate process (SIGTERM)
kill -9 PID                           # Force kill (SIGKILL)
kill -15 PID                          # Graceful termination (SIGTERM)
killall process_name                  # Kill by name
pkill -f "pattern"                    # Kill by pattern

# Priority control
nice -n 10 command                    # Run with lower priority
renice -n 5 -p PID                    # Change priority of running process
```

**Common signals:**

```bash
kill -l                               # List all signals
kill -1 PID     # SIGHUP  (reload config)
kill -2 PID     # SIGINT  (Ctrl+C)
kill -9 PID     # SIGKILL (force kill - cannot be caught)
kill -15 PID    # SIGTERM (graceful termination - default)
kill -18 PID    # SIGCONT (continue process)
kill -19 PID    # SIGSTOP (stop process)
```

**Enterprise scenarios:**

```bash
# Restart application gracefully
pkill -HUP nginx                      # Reload nginx config

# Find and kill memory-hogging processes
ps aux | sort -k4 -rn | head -5       # Identify culprits
kill -15 $(ps aux | grep "memory_leak_app" | awk '{print $2}')

# Monitor specific process
watch -n 1 "ps aux | grep nginx"

# Kill all processes by user
pkill -u username

# Gracefully stop application with fallback to force kill
kill -15 1234 && sleep 5 || kill -9 1234
```

### 5.3 System Monitoring

```bash
# CPU and memory
free -h                               # Memory usage (human-readable)
vmstat 1                              # Virtual memory stats (every 1 sec)
iostat                                # CPU and I/O stats
mpstat                                # CPU usage per processor

# Disk usage
df -h                                 # Disk space by filesystem
du -sh /var/log/*                     # Directory sizes
du -sh * | sort -rh | head -10        # Top 10 largest items

# Network
netstat -tuln                         # Listening ports
netstat -an | grep ESTABLISHED        # Active connections
ss -tuln                              # Socket statistics (faster than netstat)
ifconfig                              # Network interface info
ip addr show                          # Network interfaces (modern)

# System load
uptime                                # System uptime and load average
w                                     # Who is logged in and what they're doing
last                                  # Recent login history
```

**Load average explained:**

```bash
uptime
# Output: 14:30:00 up 5 days, 3:25, 2 users, load average: 0.50, 0.75, 1.20
#                                                          1min  5min  15min
# Load < CPU cores = Good
# Load = CPU cores = Fully utilized
# Load > CPU cores = Overloaded
```

**Real-time monitoring script:**

```bash
# Create a monitoring dashboard
watch -n 2 "echo 'CPU Usage:'; top -bn1 | head -15; \
echo ''; echo 'Memory:'; free -h; \
echo ''; echo 'Disk:'; df -h /"
```

---

## Chapter 6: File Permissions and Ownership

### 6.1 Understanding Permissions

```bash
# Permission structure
ls -l file.txt
# -rw-r--r-- 1 user group 1234 Jan 15 10:30 file.txt
# │││││││││
# ││││││││└─ Others execute
# │││││││└── Others write
# ││││││└─── Others read
# │││││└──── Group execute
# ││││└───── Group write
# │││└────── Group read
# ││└─────── Owner execute
# │└──────── Owner write
# └───────── Owner read
```

**Permission types:**

- `r` (read) = 4
- `w` (write) = 2
- `x` (execute) = 1

```bash
# Permission calculation
rwx = 4+2+1 = 7
rw- = 4+2+0 = 6
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
```

### 6.2 Changing Permissions

```bash
# Symbolic mode
chmod u+x script.sh                   # Add execute for owner
chmod g+w file.txt                    # Add write for group
chmod o-r file.txt                    # Remove read for others
chmod a+r file.txt                    # Add read for all
chmod u+x,g+w file.txt                # Multiple changes

# Numeric mode
chmod 755 script.sh                   # rwxr-xr-x
chmod 644 file.txt                    # rw-r--r--
chmod 600 private.key                 # rw-------
chmod 777 file.txt                    # rwxrwxrwx (dangerous!)

# Recursive
chmod -R 755 directory/               # Apply to all files/subdirs

# Special permissions
chmod +t directory                    # Sticky bit
chmod g+s directory                   # SetGID
chmod u+s binary                      # SetUID
```

**Common permission sets:**

```bash
644  # Regular files (rw-r--r--)
755  # Executable files/directories (rwxr-xr-x)
600  # Private files (rw-------)
700  # Private executables (rwx------)
777  # World-writable (dangerous! avoid in production)
```

### 6.3 Changing Ownership

```bash
# Change owner
chown user file.txt                   # Change owner
chown user:group file.txt             # Change owner and group
chown -R user:group directory/        # Recursive

# Change group only
chgrp group file.txt                  # Change group
chgrp -R group directory/             # Recursive

# Copy permissions from another file
chmod --reference=source.txt target.txt
chown --reference=source.txt target.txt
```

**Enterprise scenarios:**

```bash
# Set up web application permissions
chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html
chmod -R 644 /var/www/html/*.html

# Secure SSH keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 644 ~/.ssh/authorized_keys

# Set up log directory
mkdir /var/log/myapp
chown myapp:myapp /var/log/myapp
chmod 755 /var/log/myapp

# Make scripts executable for team
chmod 754 /opt/scripts/deploy.sh
chgrp developers /opt/scripts/deploy.sh
```

### 6.4 Special Permissions

```bash
# Sticky bit (t)
chmod +t /tmp                         # Only owner can delete files
# Useful for shared directories

# SetGID (s on group)
chmod g+s /shared/project             # New files inherit directory group
# Useful for team collaboration

# SetUID (s on user)
chmod u+s /usr/bin/passwd             # Run with owner's privileges
# Use with extreme caution!
```

---

## Chapter 7: Environment Variables

### 7.1 Understanding Environment Variables

```bash
# View all environment variables
env
printenv

# View specific variable
echo $HOME
echo $PATH
echo $USER
echo $SHELL

# Common environment variables
$HOME          # User's home directory
$PATH          # Command search paths
$USER          # Current username
$PWD           # Present working directory
$OLDPWD        # Previous directory
$SHELL         # Current shell
$HOSTNAME      # Machine hostname
$LANG          # Locale settings
```

### 7.2 Setting Variables

```bash
# Local variable (current shell only)
NAME="John Doe"
echo $NAME

# Environment variable (available to child processes)
export API_KEY="abc123xyz"
export DATABASE_URL="postgresql://localhost/mydb"

# Set multiple variables
export VAR1="value1" VAR2="value2"

# Unset variable
unset VAR1

# Temporary for one command
API_KEY="temp123" ./script.sh
```

### 7.3 PATH Management

```bash
# View current PATH
echo $PATH
# Output: /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# Add to PATH (temporary)
export PATH=$PATH:/opt/custom/bin

# Add to beginning of PATH
export PATH=/opt/custom/bin:$PATH

# Make permanent (add to ~/.bashrc or ~/.bash_profile)
echo 'export PATH=$PATH:/opt/custom/bin' >> ~/.bashrc
source ~/.bashrc
```

### 7.4 Configuration Files

```bash
# System-wide configuration
/etc/profile                          # Login shell config
/etc/bash.bashrc                      # Interactive shell config

# User-specific configuration
~/.bash_profile                       # Login shell (runs once)
~/.bashrc                             # Interactive shell (runs for each shell)
~/.bash_logout                        # Executed on logout
~/.profile                            # Read by Bourne-compatible shells

# Load order for bash login shell:
# 1. /etc/profile
# 2. ~/.bash_profile (or ~/.bash_login or ~/.profile)
# 3. ~/.bashrc (usually sourced from ~/.bash_profile)
```

**Best practice configuration:**

```bash
# ~/.bash_profile
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# ~/.bashrc
# Aliases
alias ll='ls -lah'
alias gs='git status'
alias dc='docker-compose'

# Environment variables
export EDITOR=vim
export VISUAL=vim
export PAGER=less

# Custom PATH
export PATH="$HOME/bin:$PATH"
export PATH="/opt/company/tools:$PATH"

# Application-specific
export JAVA_HOME=/usr/lib/jvm/java-11
export MAVEN_HOME=/opt/maven
export PATH="$MAVEN_HOME/bin:$PATH"

# Database connections
export DB_HOST="db.company.com"
export DB_PORT="5432"

# API keys (better to use .env file or secrets manager)
# export API_KEY="your-key-here"

# Custom functions
function mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Prompt customization
export PS1="\u@\h:\w\$ "
```

---

## Chapter 8: Bash Scripting Fundamentals

### 8.1 Your First Script

```bash
#!/bin/bash
# This is a comment

echo "Hello, World!"
echo "Current user: $USER"
echo "Current directory: $PWD"
```

**Save as `hello.sh` and run:**

```bash
chmod +x hello.sh
./hello.sh
```

### 8.2 Variables

```bash
#!/bin/bash

# Variable assignment (no spaces around =)
NAME="Alice"
AGE=30
IS_ACTIVE=true

# Using variables
echo "Name: $NAME"
echo "Age: $AGE"
echo "Name: ${NAME}"  # Alternative syntax

# Command substitution
CURRENT_DATE=$(date +%Y-%m-%d)
FILE_COUNT=$(ls | wc -l)
echo "Date: $CURRENT_DATE"
echo "Files: $FILE_COUNT"

# Read input
echo "Enter your name:"
read USER_INPUT
echo "Hello, $USER_INPUT!"

# Read with prompt
read -p "Enter your age: " USER_AGE
echo "You are $USER_AGE years old"

# Read password (hidden input)
read -sp "Enter password: " PASSWORD
echo
echo "Password saved"
```

### 8.3 Command-Line Arguments

```bash
#!/bin/bash

# Special variables
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
echo "Exit status of last command: $?"
echo "Process ID: $$"

# Example usage
# ./script.sh arg1 arg2 arg3
```

**Practical example:**

```bash
#!/bin/bash
# deploy.sh - Deployment script

if [ $# -ne 2 ]; then
    echo "Usage: $0 <environment> <version>"
    echo "Example: $0 production 1.2.3"
    exit 1
fi

ENVIRONMENT=$1
VERSION=$2

echo "Deploying version $VERSION to $ENVIRONMENT..."
# Deployment logic here
```

### 8.4 Conditionals

```bash
#!/bin/bash

# If-else statement
if [ condition ]; then
    # code
elif [ condition ]; then
    # code
else
    # code
fi

# String comparisons
if [ "$NAME" = "Alice" ]; then
    echo "Hello Alice"
fi

if [ "$NAME" != "Bob" ]; then
    echo "Not Bob"
fi

if [ -z "$NAME" ]; then
    echo "Variable is empty"
fi

if [ -n "$NAME" ]; then
    echo "Variable is not empty"
fi

# Numeric comparisons
if [ $AGE -eq 30 ]; then echo "Equal to 30"; fi
if [ $AGE -ne 30 ]; then echo "Not equal to 30"; fi
if [ $AGE -gt 30 ]; then echo "Greater than 30"; fi
if [ $AGE -lt 30 ]; then echo "Less than 30"; fi
if [ $AGE -ge 30 ]; then echo "Greater or equal to 30"; fi
if [ $AGE -le 30 ]; then echo "Less or equal to 30"; fi

# File tests
if [ -f "file.txt" ]; then echo "File exists"; fi
if [ -d "directory" ]; then echo "Directory exists"; fi
if [ -r "file.txt" ]; then echo "File is readable"; fi
if [ -w "file.txt" ]; then echo "File is writable"; fi
if [ -x "script.sh" ]; then echo "File is executable"; fi
if [ -s "file.txt" ]; then echo "File is not empty"; fi

# Logical operators
if [ $AGE -gt 18 ] && [ $AGE -lt 65 ]; then
    echo "Working age"
fi

if [ "$STATUS" = "active" ] || [ "$STATUS" = "pending" ]; then
    echo "Valid status"
fi

if [ ! -f "file.txt" ]; then
    echo "File does not exist"
fi

# Modern test syntax [[ ]] (preferred)
if [[ $NAME == "Alice" ]]; then
    echo "Hello Alice"
fi

if [[ $NAME == Ali* ]]; then
    echo "Name starts with Ali"
fi

if [[ $AGE -gt 18 && $AGE -lt 65 ]]; then
    echo "Working age"
fi
```

**Real-world example:**

```bash
#!/bin/bash
# check_service.sh - Monitor service health

SERVICE_NAME="nginx"

if systemctl is-active --quiet $SERVICE_NAME; then
    echo "✓ $SERVICE_NAME is running"
    exit 0
else
    echo "✗ $SERVICE_NAME is not running"
    echo "Attempting to restart..."
    
    if systemctl restart $SERVICE_NAME; then
        echo "✓ $SERVICE_NAME restarted successfully"
        exit 0
    else
        echo "✗ Failed to restart $SERVICE_NAME"
        echo "Sending alert..."
        # Alert logic here
        exit 1
    fi
fi
```

### 8.5 Loops

```bash
#!/bin/bash

# For loop - list
for item in apple banana cherry; do
    echo "Fruit: $item"
done

# For loop - range
for i in {1..5}; do
    echo "Number: $i"
done

# For loop - C-style
for ((i=1; i<=5; i++)); do
    echo "Count: $i"
done

# For loop - files
for file in *.txt; do
    echo "Processing: $file"
done

# For loop - command output
for user in $(cat users.txt); do
    echo "User: $user"
done

# While loop
COUNT=1
while [ $COUNT -le 5 ]; do
    echo "Count: $COUNT"
    ((COUNT++))
done

# While loop - reading file
while read line; do
    echo "Line: $line"
done < file.txt

# Until loop (opposite of while)
COUNT=1
until [ $COUNT -gt 5 ]; do
    echo "Count: $COUNT"
    ((COUNT++))
done

# Break and continue
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue  # Skip 5
    fi
    if [ $i -eq 8 ]; then
        break     # Stop at 8
    fi
    echo $i
done
```

**Enterprise examples:**

```bash
#!/bin/bash
# backup_databases.sh - Backup all databases

DATABASES=$(mysql -e "SHOW DATABASES;" | grep -v Database | grep -v information_schema | grep -v performance_schema)
BACKUP_DIR="/backup/mysql/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR

for db in $DATABASES; do
    echo "Backing up database: $db"
    mysqldump $db > "$BACKUP_DIR/$db.sql"
    
    if [ $? -eq 0 ]; then
        echo "✓ $db backed up successfully"
        gzip "$BACKUP_DIR/$db.sql"
    else
        echo "✗ Failed to backup $db"
    fi
done

echo "Backup completed"
```

```bash
#!/bin/bash
# monitor_servers.sh - Check multiple servers

SERVERS=("web1.company.com" "web2.company.com" "db1.company.com")

for server in "${SERVERS[@]}"; do
    echo "Checking $server..."
    
    if ping -c 1 -W 2 $server &> /dev/null; then
        echo "✓ $server is reachable"
        
        # Check SSH
        if ssh -o ConnectTimeout=5 $server "exit" 2>/dev/null; then
            echo "✓ SSH is working"
        else
            echo "✗ SSH failed"
        fi
    else
        echo "✗ $server is unreachable"
        # Send alert
    fi
    echo "---"
done
```

### 8.6 Functions

```bash
#!/bin/bash

# Basic function
greet() {
    echo "Hello, World!"
}

# Function with parameters
greet_user() {
    local name=$1  # local variable
    echo "Hello, $name!"
}

# Function with return value
add_numbers() {
    local sum=$(($1 + $2))
    echo $sum  # Return via echo
}

# Function with explicit return code
check_file() {
    if [ -f "$1" ]; then
        return 0  # Success
    else
        return 1  # Failure
    fi
}

# Using functions
greet
greet_user "Alice"

result=$(add_numbers 5 10)
echo "Sum: $result"

if check_file "config.txt"; then
    echo "Config file exists"
else
    echo "Config file missing"
fi
```

**Enterprise function library:**

```bash
#!/bin/bash
# lib/utils.sh - Reusable functions

# Logging functions
log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_error() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') - $1" >&2
}

log_warning() {
    echo "[WARNING] $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Error handling
die() {
    log_error "$1"
    exit 1
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Retry mechanism
retry() {
    local max_attempts=$1
    shift
    local cmd="$@"
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        log_info "Attempt $attempt of $max_attempts: $cmd"
        
        if eval $cmd; then
            log_info "Command succeeded"
            return 0
        fi
        
        log_warning "Command failed, retrying..."
        ((attempt++))
        sleep 2
    done
    
    log_error "Command failed after $max_attempts attempts"
    return 1
}

# Send notification (Slack example)
send_slack_notification() {
    local message=$1
    local webhook_url=$SLACK_WEBHOOK_URL
    
    curl -X POST -H 'Content-type: application/json' \
        --data "{\"text\":\"$message\"}" \
        $webhook_url
}

# Backup with rotation
backup_with_rotation() {
    local source=$1
    local dest=$2
    local keep_days=$3
    
    # Create backup
    local backup_file="$dest/backup-$(date +%Y%m%d-%H%M%S).tar.gz"
    tar -czf $backup_file $source
    
    # Remove old backups
    find $dest -name "backup-*.tar.gz" -mtime +$keep_days -delete
}

# Usage in main script:
# source lib/utils.sh
# log_info "Starting deployment"
# retry 3 ./deploy.sh
```

### 8.7 Arrays

```bash
#!/bin/bash

# Declare array
fruits=("apple" "banana" "cherry")

# Access elements
echo ${fruits[0]}      # apple
echo ${fruits[1]}      # banana
echo ${fruits[@]}      # All elements
echo ${#fruits[@]}     # Array length

# Add element
fruits+=("date")

# Iterate array
for fruit in "${fruits[@]}"; do
    echo $fruit
done

# Array with indices
for i in "${!fruits[@]}"; do
    echo "Index $i: ${fruits[$i]}"
done

# Associative arrays (key-value pairs)
declare -A config
config[host]="localhost"
config[port]="3306"
config[user]="admin"

echo ${config[host]}

# Iterate associative array
for key in "${!config[@]}"; do
    echo "$key: ${config[$key]}"
done
```

**Real-world example:**

```bash
#!/bin/bash
# deploy_multiple.sh - Deploy to multiple environments

declare -A environments
environments[dev]="dev.company.com"
environments[staging]="staging.company.com"
environments[production]="prod.company.com"

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

for env in "${!environments[@]}"; do
    server=${environments[$env]}
    
    echo "Deploying version $VERSION to $env ($server)..."
    
    ssh $server "cd /var/www && \
                 git fetch && \
                 git checkout $VERSION && \
                 ./deploy.sh"
    
    if [ $? -eq 0 ]; then
        echo "✓ Deployed to $env successfully"
    else
        echo "✗ Failed to deploy to $env"
        exit 1
    fi
done

echo "All deployments completed"
```

---

## Chapter 9: Advanced Bash Scripting

### 9.1 Error Handling

```bash
#!/bin/bash

# Exit on error
set -e  # Exit if any command fails
set -u  # Exit if undefined variable is used
set -o pipefail  # Exit if any command in pipe fails

# Combine all
set -euo pipefail

# Trap errors
trap 'echo "Error on line $LINENO"' ERR

# Cleanup on exit
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/tempfile
}
trap cleanup EXIT

# Handle specific signals
trap 'echo "Interrupted"; exit 130' INT  # Ctrl+C
trap 'echo "Terminated"; exit 143' TERM

# Check command success
if ! command_that_might_fail; then
    echo "Command failed"
    exit 1
fi

# Alternative
command_that_might_fail || {
    echo "Command failed"
    exit 1
}

# Safe execution
safe_execute() {
    local cmd="$@"
    
    if ! $cmd; then
        log_error "Failed to execute: $cmd"
        return 1
    fi
}
```

**Production-ready error handling:**

```bash
#!/bin/bash
# deploy.sh - Production deployment script

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="/var/log/deployment.log"
LOCK_FILE="/var/lock/deploy.lock"

# Logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

error_exit() {
    log "ERROR: $1"
    exit 1
}

# Cleanup function
cleanup() {
    log "Cleaning up..."
    rm -f $LOCK_FILE
    
    if [ $? -ne 0 ]; then
        log "Deployment failed. Rolling back..."
        # Rollback logic
    fi
}

trap cleanup EXIT
trap 'error_exit "Deployment interrupted"' INT TERM

# Lock mechanism
if [ -f $LOCK_FILE ]; then
    error_exit "Another deployment is in progress"
fi

touch $LOCK_FILE

# Main deployment logic
log "Starting deployment..."

# Pre-deployment checks
log "Running pre-deployment checks..."
./scripts/pre_deploy_check.sh || error_exit "Pre-deployment checks failed"

# Backup
log "Creating backup..."
./scripts/backup.sh || error_exit "Backup failed"

# Deploy
log "Deploying application..."
git pull origin main || error_exit "Git pull failed"

# Install dependencies
log "Installing dependencies..."
npm install --production || error_exit "Dependency installation failed"

# Run migrations
log "Running database migrations..."
npm run migrate || error_exit "Database migration failed"

# Restart services
log "Restarting services..."
systemctl restart myapp || error_exit "Service restart failed"

# Health check
log "Running health check..."
sleep 5
curl -f http://localhost:3000/health || error_exit "Health check failed"

log "Deployment completed successfully"
```

### 9.2 Debugging

```bash
#!/bin/bash

# Enable debug mode
set -x  # Print each command before execution
set -v  # Print shell input lines

# Conditional debugging
DEBUG=${DEBUG:-0}

debug() {
    if [ $DEBUG -eq 1 ]; then
        echo "[DEBUG] $1"
    fi
}

# Usage
debug "Checking configuration..."

# Run script with debugging
# DEBUG=1 ./script.sh

# Or with bash -x
# bash -x script.sh

# Disable debug for specific section
set +x
# commands without debug
set -x

# Check syntax without executing
bash -n script.sh
```

### 9.3 Options Parsing

```bash
#!/bin/bash
# script.sh - Script with options

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Options:
    -h, --help          Show this help message
    -v, --version       Show version
    -e, --environment   Environment (dev|staging|prod)
    -f, --file         Input file
    -d, --debug        Enable debug mode
EOF
    exit 0
}

# Default values
ENVIRONMENT=""
INPUT_FILE=""
DEBUG=0

# Parse options
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            ;;
        -v|--version)
            echo "Version 1.0.0"
            exit 0
            ;;
        -e|--environment)
            ENVIRONMENT="$2"
            shift 2
            ;;
        -f|--file)
            INPUT_FILE="$2"
            shift 2
            ;;
        -d|--debug)
            DEBUG=1
            shift
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# Validate required options
if [ -z "$ENVIRONMENT" ]; then
    echo "Error: Environment is required"
    usage
fi

# Main script logic
echo "Environment: $ENVIRONMENT"
echo "Input file: $INPUT_FILE"
echo "Debug mode: $DEBUG"
```

**Using getopts (standard approach):**

```bash
#!/bin/bash

while getopts "e:f:dvh" opt; do
    case $opt in
        e)
            ENVIRONMENT=$OPTARG
            ;;
        f)
            FILE=$OPTARG
            ;;
        d)
            DEBUG=1
            ;;
        v)
            VERBOSE=1
            ;;
        h)
            usage
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            usage
            ;;
    esac
done

# Shift processed options
shift $((OPTIND-1))

# Remaining arguments
echo "Remaining args: $@"
```

### 9.4 Working with JSON

```bash
#!/bin/bash

# Using jq (JSON processor)
# Install: apt-get install jq

# Parse JSON
JSON='{"name":"Alice","age":30,"city":"NYC"}'

# Extract value
NAME=$(echo $JSON | jq -r '.name')
echo $NAME  # Alice

# Extract nested value
JSON='{"user":{"name":"Bob","email":"bob@example.com"}}'
EMAIL=$(echo $JSON | jq -r '.user.email')

# Array handling
JSON='{"users":[{"name":"Alice"},{"name":"Bob"}]}'
NAMES=$(echo $JSON | jq -r '.users[].name')

# Read JSON file
CONFIG=$(cat config.json)
DATABASE=$(echo $CONFIG | jq -r '.database.host')

# Create JSON
jq -n \
  --arg name "Alice" \
  --arg email "alice@example.com" \
  '{name: $name, email: $email}'

# Modify JSON
cat config.json | jq '.database.port = 5432' > config.json.tmp
mv config.json.tmp config.json
```

**Real-world API interaction:**

```bash
#!/bin/bash
# api_client.sh - Interact with REST API

API_URL="https://api.company.com"
API_KEY="your-api-key"

# GET request
get_users() {
    curl -s -H "Authorization: Bearer $API_KEY" \
         "$API_URL/users" | jq '.'
}

# POST request
create_user() {
    local name=$1
    local email=$2
    
    curl -s -X POST \
         -H "Authorization: Bearer $API_KEY" \
         -H "Content-Type: application/json" \
         -d "{\"name\":\"$name\",\"email\":\"$email\"}" \
         "$API_URL/users" | jq '.'
}

# Check API health
check_api_health() {
    response=$(curl -s -w "%{http_code}" "$API_URL/health")
    http_code="${response: -3}"
    
    if [ $http_code -eq 200 ]; then
        echo "✓ API is healthy"
        return 0
    else
        echo "✗ API is unhealthy (HTTP $http_code)"
        return 1
    fi
}

# Extract specific data
get_user_emails() {
    curl -s -H "Authorization: Bearer $API_KEY" \
         "$API_URL/users" | jq -r '.[].email'
}

# Usage
check_api_health
create_user "John Doe" "john@example.com"
get_users
```

### 9.5 Parallel Execution

```bash
#!/bin/bash

# Run commands in background
command1 &
command2 &
command3 &
wait  # Wait for all background jobs

# GNU Parallel (if installed)
# apt-get install parallel

# Process multiple items in parallel
cat servers.txt | parallel -j 10 "ping -c 1 {}"

# Process files in parallel
find . -name "*.log" | parallel gzip {}

# Run function in parallel
export -f process_server
parallel process_server ::: web1 web2 web3 db1 db2
```

**Parallel deployment example:**

```bash
#!/bin/bash
# parallel_deploy.sh - Deploy to multiple servers simultaneously

SERVERS=("web1.company.com" "web2.company.com" "web3.company.com")
VERSION=$1

deploy_to_server() {
    local server=$1
    local version=$2
    
    echo "Deploying to $server..."
    
    ssh $server "cd /var/www/app && \
                 git fetch && \
                 git checkout $version && \
                 ./deploy.sh" \
    && echo "✓ $server deployed successfully" \
    || echo "✗ $server deployment failed"
}

# Export function for parallel execution
export -f deploy_to_server

# Deploy in parallel
printf "%s\n" "${SERVERS[@]}" | \
    parallel -j 3 deploy_to_server {} $VERSION

echo "All deployments completed"
```

---

## Chapter 10: System Administration Tasks

### 10.1 User Management

```bash
# List users
cat /etc/passwd
cut -d: -f1 /etc/passwd  # Just usernames

# Add user
sudo useradd username
sudo useradd -m -s /bin/bash username  # With home dir and shell

# Set password
sudo passwd username

# Modify user
sudo usermod -aG sudo username        # Add to sudo group
sudo usermod -s /bin/zsh username     # Change shell

# Delete user
sudo userdel username
sudo userdel -r username              # Remove home directory too

# List groups
cat /etc/group
groups username                       # Groups for specific user

# Add group
sudo groupadd developers

# Add user to group
sudo usermod -aG developers username

# List logged-in users
who
w
last                                  # Login history
```

**Automated user provisioning:**

```bash
#!/bin/bash
# provision_users.sh - Bulk user creation

USERS_FILE="users.csv"  # Format: username,fullname,email

while IFS=, read -r username fullname email; do
    echo "Creating user: $username"
    
    # Create user
    sudo useradd -m -s /bin/bash -c "$fullname" $username
    
    # Set temporary password
    echo "$username:TempPassword123!" | sudo chpasswd
    
    # Force password change on first login
    sudo chage -d 0 $username
    
    # Add to developers group
    sudo usermod -aG developers $username
    
    # Create SSH directory
    sudo mkdir -p /home/$username/.ssh
    sudo chmod 700 /home/$username/.ssh
    
    # Send welcome email
    echo "Welcome to the company!" | mail -s "Account Created" $email
    
    echo "✓ User $username created"
done < $USERS_FILE
```

### 10.2 Service Management (systemd)

```bash
# Start/stop/restart service
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx           # Reload config without restart

# Enable/disable service (start at boot)
sudo systemctl enable nginx
sudo systemctl disable nginx

# Check status
systemctl status nginx
systemctl is-active nginx
systemctl is-enabled nginx

# List all services
systemctl list-units --type=service
systemctl list-units --type=service --state=running

# View logs
journalctl -u nginx                   # All logs for service
journalctl -u nginx -f                # Follow logs
journalctl -u nginx --since "1 hour ago"
journalctl -u nginx --since "2024-01-01"
```

**Create custom systemd service:**

```bash
# /etc/systemd/system/myapp.service

[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=myapp
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/bin/start.sh
ExecStop=/opt/myapp/bin/stop.sh
Restart=on-failure
RestartSec=10
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=myapp

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
sudo systemctl status myapp
```

### 10.3 Cron Jobs (Scheduled Tasks)

```bash
# Edit crontab
crontab -e                            # Current user
sudo crontab -e -u username           # Specific user

# List crontab
crontab -l

# Crontab syntax
# * * * * * command
# │ │ │ │ │
# │ │ │ │ └─ Day of week (0-7, 0 and 7 are Sunday)
# │ │ │ └─── Month (1-12)
# │ │ └───── Day of month (1-31)
# │ └─────── Hour (0-23)
# └───────── Minute (0-59)

# Examples
0 2 * * * /backup/daily.sh            # Daily at 2 AM
*/15 * * * * /monitor/check.sh        # Every 15 minutes
0 0 * * 0 /backup/weekly.sh           # Weekly on Sunday
0 0 1 * * /backup/monthly.sh          # Monthly on 1st
0 9-17 * * 1-5 /check/business_hours.sh  # Weekdays 9AM-5PM

# Special strings
@reboot /startup/init.sh              # At boot
@daily /backup/daily.sh               # Once a day
@hourly /monitor/check.sh             # Once an hour
@weekly /backup/weekly.sh             # Once a week
@monthly /reports/generate.sh         # Once a month
```

**Production cron job with logging:**

```bash
# Crontab entry with proper logging
0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1

# /opt/scripts/backup.sh
#!/bin/bash

set -euo pipefail

LOG_FILE="/var/log/backup.log"
BACKUP_DIR="/backup/$(date +\%Y\%m\%d)"

log() {
    echo "[$(date '+\%Y-\%m-\%d \%H:\%M:\%S')] $1" >> $LOG_FILE
}

log "Starting backup"

mkdir -p $BACKUP_DIR

# Backup database
log "Backing up database..."
mysqldump --all-databases | gzip > "$BACKUP_DIR/databases.sql.gz"

# Backup files
log "Backing up files..."
tar -czf "$BACKUP_DIR/files.tar.gz" /var/www/html

# Upload to S3
log "Uploading to S3..."
aws s3 sync $BACKUP_DIR s3://company-backups/$(date +\%Y\%m\%d)/

# Cleanup old backups
log "Cleaning up old backups..."
find /backup -type d -mtime +30 -exec rm -rf {} \;

log "Backup completed"
```

### 10.4 Log Management

```bash
# View logs
tail -f /var/log/syslog                # System log
tail -f /var/log/auth.log              # Authentication
tail -f /var/log/nginx/access.log      # Web server access
tail -f /var/log/nginx/error.log       # Web server errors

# Search logs
grep "error" /var/log/application.log
grep -i "failed" /var/log/auth.log

# Log rotation configuration
# /etc/logrotate.d/myapp

/var/log/myapp/*.log {
    daily                    # Rotate daily
    rotate 30                # Keep 30 days
    compress                 # Compress old logs
    delaycompress           # Compress on next rotation
    missingok               # Don't error if log missing
    notifempty              # Don't rotate if empty
    create 0640 myapp myapp # Create new log with permissions
    sharedscripts
    postrotate
        systemctl reload myapp > /dev/null
    endscript
}
```

**Log analysis script:**

```bash
#!/bin/bash
# analyze_logs.sh - Daily log analysis

LOG_FILE="/var/log/nginx/access.log"
REPORT_FILE="/var/log/reports/daily-$(date +%Y%m%d).txt"

{
    echo "Daily Log Report - $(date)"
    echo "================================"
    echo ""
    
    echo "Top 10 IP Addresses:"
    awk '{print $1}' $LOG_FILE | sort | uniq -c | sort -rn | head -10
    echo ""
    
    echo "Top 10 Requested URLs:"
    awk '{print $7}' $LOG_FILE | sort | uniq -c | sort -rn | head -10
    echo ""
    
    echo "HTTP Status Codes:"
    awk '{print $9}' $LOG_FILE | sort | uniq -c | sort -rn
    echo ""
    
    echo "Error 4xx Count:"
    awk '$9 ~ /^4/ {count++} END {print count}' $LOG_FILE
    echo ""
    
    echo "Error 5xx Count:"
    awk '$9 ~ /^5/ {count++} END {print count}' $LOG_FILE
    echo ""
    
    echo "Total Requests:"
    wc -l < $LOG_FILE
    
} > $REPORT_FILE

echo "Report generated: $REPORT_FILE"
```

### 10.5 Disk and File System Management

```bash
# Disk usage
df -h                                  # Filesystem usage
df -h /var                            # Specific mount point
df -i                                 # Inode usage

# Directory size
du -sh /var/log                       # Total size
du -sh /var/log/*                     # Each subdirectory
du -h --max-depth=1 /var | sort -rh   # Sorted by size

# Find large files
find / -type f -size +100M            # Files > 100MB
find / -type f -size +1G -exec ls -lh {} \; 2>/dev/null

# Disk space monitoring
THRESHOLD=90
USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ $USAGE -gt $THRESHOLD ]; then
    echo "Warning: Disk usage is ${USAGE}%"
    # Send alert
fi

# Mount filesystem
sudo mount /dev/sdb1 /mnt/data
sudo umount /mnt/data

# List block devices
lsblk
blkid

# Filesystem check
sudo fsck /dev/sdb1
```

**Automated disk cleanup:**

```bash
#!/bin/bash
# cleanup.sh - Automated disk space management

LOG_DIR="/var/log"
TEMP_DIR="/tmp"
BACKUP_DIR="/backup"

echo "Starting cleanup..."

# Remove old logs (older than 30 days)
find $LOG_DIR -name "*.log.*" -mtime +30 -delete
echo "✓ Old logs removed"

# Remove old temp files (older than 7 days)
find $TEMP_DIR -type f -mtime +7 -delete
echo "✓ Temp files cleaned"

# Compress old backups (older than 7 days, not compressed)
find $BACKUP_DIR -name "*.sql" -mtime +7 -exec gzip {} \;
echo "✓ Old backups compressed"

# Remove very old backups (older than 60 days)
find $BACKUP_DIR -name "*.gz" -mtime +60 -delete
echo "✓ Very old backups removed"

# Clean package cache (Ubuntu/Debian)
sudo apt-get clean
sudo apt-get autoclean
echo "✓ Package cache cleaned"

# Clean Docker (if installed)
if command -v docker &> /dev/null; then
    docker system prune -af --volumes
    echo "✓ Docker cleaned"
fi

# Report disk usage
echo ""
echo "Current Disk Usage:"
df -h / | awk 'NR==2 {print "Root: " $5 " used"}'
df -h /var | awk 'NR==2 {print "/var: " $5 " used"}'

echo "Cleanup completed"
```

---

## Chapter 11: Networking and Remote Operations

### 11.1 Network Commands

```bash
# Network interfaces
ifconfig                              # Legacy command
ip addr show                          # Modern alternative
ip link show                          # Network devices

# Network connectivity
ping google.com                       # Test connectivity
ping -c 4 google.com                  # Send 4 packets
traceroute google.com                 # Trace route
mtr google.com                        # Combined ping/traceroute

# DNS lookup
nslookup google.com
dig google.com
host google.com

# Network statistics
netstat -tuln                         # Listening ports
netstat -an                           # All connections
ss -tuln                              # Modern alternative
ss -s                                 # Statistics summary

# Active connections
lsof -i                               # Files using network
lsof -i :80                           # What's using port 80
netstat -anp | grep :3000             # Check specific port

# Download files
wget https://example.com/file.txt
wget -O custom-name.txt https://example.com/file.txt
curl -O https://example.com/file.txt
curl -o custom-name.txt https://example.com/file.txt

# Test HTTP endpoints
curl -I https://example.com           # Headers only
curl -X POST -d "data=value" https://api.example.com
curl -H "Authorization: Bearer token" https://api.example.com
```

**Network monitoring script:**

```bash
#!/bin/bash
# monitor_network.sh - Monitor network connectivity

HOSTS=("8.8.8.8" "google.com" "api.company.com")
LOG_FILE="/var/log/network-monitor.log"

for host in "${HOSTS[@]}"; do
    if ping -c 1 -W 2 $host &> /dev/null; then
        echo "[$(date)] ✓ $host is reachable" >> $LOG_FILE
    else
        echo "[$(date)] ✗ $host is unreachable" >> $LOG_FILE
        # Send alert
        echo "Alert: $host is down" | mail -s "Network Alert" admin@company.com
    fi
done
```

### 11.2 SSH (Secure Shell)

```bash
# Connect to remote server
ssh user@hostname
ssh user@192.168.1.100
ssh -p 2222 user@hostname             # Custom port

# Run command on remote server
ssh user@hostname "ls -la"
ssh user@hostname "cat /var/log/syslog | tail -n 50"

# Copy files (scp)
scp file.txt user@hostname:/remote/path/
scp user@hostname:/remote/file.txt ./local/
scp -r directory/ user@hostname:/remote/path/
scp -P 2222 file.txt user@hostname:/path/  # Custom port

# Sync directories (rsync - preferred)
rsync -avz /local/dir/ user@hostname:/remote/dir/
rsync -avz --delete /local/dir/ user@hostname:/remote/dir/
rsync -avz -e "ssh -p 2222" /local/ user@hostname:/remote/

# SSH keys
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
ssh-copy-id user@hostname
cat ~/.ssh/id_rsa.pub | ssh user@hostname "cat >> ~/.ssh/authorized_keys"

# SSH config (~/.ssh/config)
Host myserver
    HostName server.company.com
    User myusername
    Port 22
    IdentityFile ~/.ssh/id_rsa

# Now you can simply: ssh myserver

# SSH tunneling
ssh -L 8080:localhost:80 user@hostname  # Local port forward
ssh -R 8080:localhost:80 user@hostname  # Remote port forward
ssh -D 8080 user@hostname              # SOCKS proxy
```

**Automated deployment via SSH:**

```bash
#!/bin/bash
# remote_deploy.sh - Deploy to remote server

SERVER="prod.company.com"
USER="deploy"
REMOTE_DIR="/var/www/app"
LOCAL_DIR="./dist"

echo "Deploying to $SERVER..."

# Create backup on remote
ssh $USER@$SERVER "cd $REMOTE_DIR && tar -czf backup-$(date +%Y%m%d-%H%M%S).tar.gz ."

# Sync files
rsync -avz --delete \
    --exclude 'node_modules' \
    --exclude '.git' \
    $LOCAL_DIR/ $USER@$SERVER:$REMOTE_DIR/

# Run post-deployment commands
ssh $USER@$SERVER << 'EOF'
    cd /var/www/app
    npm install --production
    npm run build
    sudo systemctl restart myapp
    echo "Deployment completed"
EOF

# Verify deployment
if curl -f http://$SERVER/health; then
    echo "✓ Deployment successful"
else
    echo "✗ Deployment failed"
    exit 1
fi
```

### 11.3 Firewall Management (ufw/iptables)

```bash
# UFW (Uncomplicated Firewall - Ubuntu/Debian)
sudo ufw status                       # Check status
sudo ufw enable                       # Enable firewall
sudo ufw disable                      # Disable firewall

# Allow/Deny
sudo ufw allow 22/tcp                 # Allow SSH
sudo ufw allow 80/tcp                 # Allow HTTP
sudo ufw allow 443/tcp                # Allow HTTPS
sudo ufw allow from 192.168.1.0/24    # Allow from subnet
sudo ufw deny 23                      # Deny telnet

# Application profiles
sudo ufw app list
sudo ufw allow 'Nginx Full'
sudo ufw allow 'OpenSSH'

# Delete rules
sudo ufw delete allow 80/tcp

# Reset firewall
sudo ufw reset

# iptables (lower-level)
sudo iptables -L                      # List rules
sudo iptables -L -n -v                # Detailed list

# Allow incoming SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Save rules
sudo iptables-save > /etc/iptables/rules.v4
```

---

## Chapter 12: Docker and Containers

### 12.1 Docker Basics

```bash
# Container management
docker ps                             # Running containers
docker ps -a                          # All containers
docker run ubuntu                     # Run container
docker run -d nginx                   # Run detached
docker run -p 8080:80 nginx          # Port mapping
docker run --name myapp nginx        # Named container

# Stop/start/restart
docker stop container_id
docker start container_id
docker restart container_id

# Remove containers
docker rm container_id
docker rm -f container_id            # Force remove running

# Execute commands in container
docker exec -it container_id bash
docker exec container_id ls /var/log

# View logs
docker logs container_id
docker logs -f container_id          # Follow logs
docker logs --tail 100 container_id  # Last 100 lines

# Image management
docker images                         # List images
docker pull nginx:latest             # Download image
docker build -t myapp:1.0 .          # Build from Dockerfile
docker rmi image_id                  # Remove image

# Inspect container
docker inspect container_id
docker stats                         # Resource usage
docker top container_id              # Running processes
```

**Docker cleanup script:**

```bash
#!/bin/bash
# docker_cleanup.sh - Clean up Docker resources

echo "Cleaning up Docker..."

# Stop all running containers
echo "Stopping containers..."
docker stop $(docker ps -q) 2>/dev/null

# Remove stopped containers
echo "Removing stopped containers..."
docker container prune -f

# Remove unused images
echo "Removing unused images..."
docker image prune -a -f

# Remove unused volumes
echo "Removing unused volumes..."
docker volume prune -f

# Remove unused networks
echo "Removing unused networks..."
docker network prune -f

# Show disk usage
echo ""
echo "Current Docker disk usage:"
docker system df

echo "Cleanup completed"
```

### 12.2 Docker Compose

```bash
# docker-compose.yml example
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - api
  
  api:
    build: ./api
    environment:
      - DATABASE_URL=postgresql://db:5432/mydb
    ports:
      - "3000:3000"
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

```bash
# Docker Compose commands
docker-compose up                     # Start services
docker-compose up -d                  # Start detached
docker-compose down                   # Stop and remove
docker-compose ps                     # List services
docker-compose logs                   # View logs
docker-compose logs -f web            # Follow specific service
docker-compose exec web bash          # Execute command
docker-compose build                  # Build images
docker-compose restart                # Restart services
```

**Deployment script with Docker:**

```bash
#!/bin/bash
# deploy_docker.sh - Deploy using Docker Compose

set -euo pipefail

ENVIRONMENT=$1
COMPOSE_FILE="docker-compose.${ENVIRONMENT}.yml"

if [ ! -f "$COMPOSE_FILE" ]; then
    echo "Error: $COMPOSE_FILE not found"
    exit 1
fi

echo "Deploying to $ENVIRONMENT..."

# Pull latest images
docker-compose -f $COMPOSE_FILE pull

# Build custom images
docker-compose -f $COMPOSE_FILE build

# Stop old containers
docker-compose -f $COMPOSE_FILE down

# Start new containers
docker-compose -f $COMPOSE_FILE up -d

# Wait for health check
echo "Waiting for services to be healthy..."
sleep 10

# Verify
if docker-compose -f $COMPOSE_FILE ps | grep -q "Up"; then
    echo "✓ Deployment successful"
else
    echo "✗ Deployment failed"
    docker-compose -f $COMPOSE_FILE logs
    exit 1
fi

# Cleanup old images
docker image prune -f

echo "Deployment completed"
```

---

## Chapter 13: Enterprise Bash Patterns

### 13.1 Configuration Management

```bash
# config.sh - Centralized configuration

# Environment-specific configs
ENVIRONMENTS=("dev" "staging" "production")

# Load environment config
load_config() {
    local env=$1
    local config_file="config/${env}.conf"
    
    if [ -f "$config_file" ]; then
        source "$config_file"
    else
        echo "Error: Config file $config_file not found"
        exit 1
    fi
}

# config/production.conf
DB_HOST="prod-db.company.com"
DB_PORT="5432"
DB_NAME="production"
API_URL="https://api.company.com"
LOG_LEVEL="ERROR"
MAX_CONNECTIONS=100

# config/dev.conf
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="development"
API_URL="http://localhost:3000"
LOG_LEVEL="DEBUG"
MAX_CONNECTIONS=10

# Usage in script
ENV=${1:-dev}
source ./config.sh
load_config $ENV

echo "Connecting to $DB_HOST:$DB_PORT"
```

### 13.2 Secrets Management

```bash
# secrets.sh - Secure secrets handling

# Use environment variables
export DATABASE_PASSWORD="${DATABASE_PASSWORD}"

# Or load from encrypted file
load_secrets() {
    if [ -f ".secrets.enc" ]; then
        # Decrypt using gpg or openssl
        openssl enc -d -aes-256-cbc -in .secrets.enc -out /tmp/secrets
        source /tmp/secrets
        rm -f /tmp/secrets
    fi
}

# Or use external secrets manager
get_secret() {
    local secret_name=$1
    
    # AWS Secrets Manager
    aws secretsmanager get-secret-value \
        --secret-id $secret_name \
        --query SecretString \
        --output text
    
    # Or Vault
    # vault kv get -field=value secret/$secret_name
}

# Usage
DB_PASSWORD=$(get_secret "prod/database/password")
```

### 13.3 Logging Framework

```bash
# logger.sh - Structured logging

LOG_FILE="/var/log/myapp/app.log"
LOG_LEVEL=${LOG_LEVEL:-INFO}  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Log levels
LOG_LEVELS=([DEBUG]=0 [INFO]=1 [WARNING]=2 [ERROR]=3 [CRITICAL]=4)

should_log() {
    local level=$1
    local current_level_value=${LOG_LEVELS[$LOG_LEVEL]}
    local message_level_value=${LOG_LEVELS[$level]}
    
    [ $message_level_value -ge $current_level_value ]
}

log() {
    local level=$1
    shift
    local message="$@"
    
    if should_log $level; then
        local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        local log_entry="$timestamp [$level] $message"
        
        echo "$log_entry" | tee -a $LOG_FILE
        
        # Send critical errors to monitoring
        if [ "$level" = "CRITICAL" ]; then
            send_alert "$message"
        fi
    fi
}

log_debug() { log DEBUG "$@"; }
log_info() { log INFO "$@"; }
log_warning() { log WARNING "$@"; }
log_error() { log ERROR "$@"; }
log_critical() { log CRITICAL "$@"; }

# Usage
log_info "Application started"
log_error "Database connection failed"
log_critical "System out of memory"
```

### 13.4 Health Check Framework

```bash
# healthcheck.sh - Comprehensive health checks

#!/bin/bash

set -euo pipefail

CHECKS_PASSED=0
CHECKS_FAILED=0

# Health check functions
check_service() {
    local service=$1
    
    if systemctl is-active --quiet $service; then
        log_info "✓ $service is running"
        ((CHECKS_PASSED++))
        return 0
    else
        log_error "✗ $service is not running"
        ((CHECKS_FAILED++))
        return 1
    fi
}

check_port() {
    local host=$1
    local port=$2
    
    if nc -z -w2 $host $port 2>/dev/null; then
        log_info "✓ Port $port on $host is open"
        ((CHECKS_PASSED++))
        return 0
    else
        log_error "✗ Port $port on $host is closed"
        ((CHECKS_FAILED++))
        return 1
    fi
}

check_disk_space() {
    local path=$1
    local threshold=$2
    
    local usage=$(df -h $path | awk 'NR==2 {print $5}' | sed 's/%//')
    
    if [ $usage -lt $threshold ]; then
        log_info "✓ Disk usage for $path is ${usage}%"
        ((CHECKS_PASSED++))
        return 0
    else
        log_error "✗ Disk usage for $path is ${usage}% (threshold: ${threshold}%)"
        ((CHECKS_FAILED++))
        return 1
    fi
}

check_url() {
    local url=$1
    local expected_code=$2
    
    local response=$(curl -s -o /dev/null -w "%{http_code}" $url)
    
    if [ "$response" = "$expected_code" ]; then
        log_info "✓ $url returned $response"
        ((CHECKS_PASSED++))
        return 0
    else
        log_error "✗ $url returned $response (expected: $expected_code)"
        ((CHECKS_FAILED++))
        return 1
    fi
}

check_database() {
    if psql -h localhost -U myapp -d mydb -c "SELECT 1" &>/dev/null; then
        log_info "✓ Database is accessible"
        ((CHECKS_PASSED++))
        return 0
    else
        log_error "✗ Database is not accessible"
        ((CHECKS_FAILED++))
        return 1
    fi
}

# Run all checks
main() {
    log_info "Starting health checks..."
    
    check_service nginx
    check_service postgresql
    check_port localhost 80
    check_port localhost 5432
    check_disk_space / 90
    check_disk_space /var 90
    check_url "http://localhost/health" "200"
    check_database
    
    log_info "Health check summary:"
    log_info "Passed: $CHECKS_PASSED"
    log_info "Failed: $CHECKS_FAILED"
    
    if [ $CHECKS_FAILED -gt 0 ]; then
        log_error "Health checks failed"
        exit 1
    else
        log_info "All health checks passed"
        exit 0
    fi
}

main
```

---

## Chapter 14: Performance and Optimization

### 14.1 Script Performance

```bash
# Measure execution time
time ./script.sh

# Or within script
START_TIME=$(date +%s)
# ... script logic ...
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
echo "Execution time: $DURATION seconds"

# Profile script execution
bash -x script.sh 2>&1 | ts '[%Y-%m-%d %H:%M:%%.S]' > profile.log

# Find slow commands
PS4='+ $(date "+%s.%N")\011 '
set -x
# commands to profile
set +x
```

### 14.2 Optimization Techniques

```bash
# Use built-in commands instead of external
# Bad
filename=$(basename $path)
# Good
filename="${path##*/}"

# Avoid unnecessary subshells
# Bad
count=$(cat file.txt | wc -l)
# Good
count=$(wc -l < file.txt)

# Use arrays for multiple items
# Bad
for file in $(ls *.txt); do
    echo $file
done

# Good
files=(*.txt)
for file in "${files[@]}"; do
    echo "$file"
done

# Process large files efficiently
# Bad - loads entire file into memory
content=$(cat large_file.txt)

# Good - process line by line
while IFS= read -r line; do
    # process line
done < large_file.txt

# Parallel processing for independent tasks
for item in {1..100}; do
    process_item $item &
done
wait

# Limit parallel jobs
max_jobs=10
for item in {1..100}; do
    while [ $(jobs -r | wc -l) -ge $max_jobs ]; do
        sleep 0.1
    done
    process_item $item &
done
wait
```

---

## Chapter 15: Quick Reference & Best Practices

### 15.1 Bash Scripting Best Practices

```bash
#!/bin/bash

# Always use shebang
# Always use set options
set -euo pipefail

# Use meaningful variable names
# Bad
x="file.txt"
# Good
INPUT_FILE="file.txt"

# Quote variables
# Bad
rm -rf $directory
# Good
rm -rf "$directory"

# Use [[ ]] for tests (more powerful)
# Bad
if [ "$var" = "value" ]; then
# Good
if [[ $var == "value" ]]; then

# Check if variable is set
if [[ -z ${VAR:-} ]]; then
    echo "VAR is not set"
fi

# Use functions for repeated code
# Avoid global variables
# Use local for function variables

# Document your scripts
# Add comments for complex logic
# Include usage function

# Validate input
if [ $# -lt 1 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

# Clean up on exit
trap cleanup EXIT

# Log important actions
# Handle errors gracefully
# Test scripts before production use
```

### 15.2 Common Pitfalls

```bash
# Pitfall 1: Not quoting variables
file="my file.txt"
cat $file         # Wrong - expands to: cat my file.txt
cat "$file"       # Correct

# Pitfall 2: Using ls in scripts
# Wrong
for file in $(ls *.txt); do
    echo $file
done

# Correct
for file in *.txt; do
    echo "$file"
done

# Pitfall 3: Not checking command success
cd /some/directory
rm -rf *  # Dangerous if cd failed!

# Correct
cd /some/directory || exit 1
rm -rf *

# Or
if cd /some/directory; then
    rm -rf *
fi

# Pitfall 4: Parsing ls output
# Wrong
size=$(ls -l file.txt | awk '{print $5}')

# Correct
size=$(stat -f%z file.txt)  # macOS
size=$(stat -c%s file.txt)  # Linux

# Pitfall 5: Not handling spaces in filenames
find . -name "*.txt" -exec rm {} \;  # Wrong
find . -name "*.txt" -exec rm {} +   # Better
find . -name "*.txt" -delete          # Best

# Pitfall 6: Using == in [ ]
if [ $var == "value" ]; then  # Not POSIX compliant
if [ "$var" = "value" ]; then  # Correct
if [[ $var == "value" ]]; then  # Also correct (bash specific)
```

### 15.3 Essential One-Liners

```bash
# Find and replace in multiple files
find . -name "*.txt" -exec sed -i 's/old/new/g' {} +

# Find large files
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null

# Monitor file changes
watch -n 1 'ls -lh file.txt'

# Count files in directory
find . -type f | wc -l

# Find duplicate files
find . -type f -exec md5sum {} + | sort | uniq -w32 -dD

# Kill processes by name
pkill -f "process_name"

# Get public IP
curl ifconfig.me

# Download entire website
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://example.com

# Monitor bandwidth
iftop -i eth0

# Find files modified in last N days
find . -mtime -7

# Sort files by size
du -sh * | sort -rh

# Extract specific column from CSV
cut -d',' -f3 data.csv

# Remove duplicate lines
sort -u file.txt

# Generate random password
openssl rand -base64 32

# JSON pretty print
cat file.json | python -m json.tool

# Create directory and cd into it
mkdir -p new/nested/dir && cd $_

# Last command's exit code
echo $?

# Previous command with sudo
sudo !!

# Replace in last command
^old^new^
```

### 15.4 Bash Scripting Cheat Sheet

```bash
# VARIABLES
var="value"                    # Assignment (no spaces!)
echo $var                      # Access
echo ${var}                    # Alternative syntax
readonly var="value"           # Constant
unset var                      # Delete variable

# SPECIAL VARIABLES
$0          # Script name
$1-$9       # Arguments 1-9
${10}       # Argument 10+
$#          # Number of arguments
$@          # All arguments (array)
$*          # All arguments (string)
$?          # Exit status of last command
$$          # Process ID
$!          # PID of last background job

# STRING OPERATIONS
${#var}                        # Length
${var:start:length}            # Substring
${var/old/new}                 # Replace first
${var//old/new}                # Replace all
${var#prefix}                  # Remove shortest prefix
${var##prefix}                 # Remove longest prefix
${var%suffix}                  # Remove shortest suffix
${var%%suffix}                 # Remove longest suffix
${var:-default}                # Use default if unset
${var:=default}                # Assign default if unset

# ARRAYS
arr=("item1" "item2")          # Declaration
${arr[0]}                      # First element
${arr[@]}                      # All elements
${#arr[@]}                     # Array length
arr+=("item3")                 # Append

# CONDITIONS
if [[ condition ]]; then
    # code
elif [[ condition ]]; then
    # code
else
    # code
fi

# LOOPS
for item in list; do done
for ((i=0; i<10; i++)); do done
while [[ condition ]]; do done
until [[ condition ]]; do done

# FUNCTIONS
func() {
    local var=$1
    echo "result"
    return 0
}

# FILE TESTS
-f    # File exists
-d    # Directory exists
-r    # Readable
-w    # Writable
-x    # Executable
-s    # Not empty
-e    # Exists (any type)

# COMPARISON
==, !=                  # String equality
-eq, -ne               # Numeric equality
-lt, -le, -gt, -ge     # Numeric comparison
&&, ||                 # Logical AND, OR
!                      # Logical NOT

# REDIRECTION
>     # Redirect output
>>    # Append output
<     # Redirect input
2>    # Redirect stderr
&>    # Redirect both
|     # Pipe

# PROCESS CONTROL
&       # Run in background
Ctrl+Z  # Suspend
bg      # Resume in background
fg      # Resume in foreground
wait    # Wait for background jobs
kill    # Send signal to process
```

---

## Conclusion

This guide covers Bash scripting from fundamentals to enterprise-level usage. Key takeaways:

1. **Master the basics**: File operations, text processing, pipes
2. **Write robust scripts**: Error handling, logging, validation
3. **Automate everything**: Deployments, monitoring, backups
4. **Follow best practices**: Quoting, error checking, documentation
5. **Learn incrementally**: Start simple, build complexity
6. **Test thoroughly**: Validate in dev before production
7. **Keep scripts maintainable**: Clear naming, modular functions, comments

**Next Steps:**

- Practice writing scripts for daily tasks
- Study existing production scripts
- Contribute to shell script projects
- Read system administration guides
- Experiment with different tools (awk, sed, grep)
- Learn about cloud CLI tools (AWS CLI, gcloud, az)

Remember: The best way to learn Bash is by doing. Start automating your repetitive tasks today!
