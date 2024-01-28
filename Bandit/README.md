# OverTheWire Bandit Challenge 🎮

## Introduction 🚀
Welcome to the Bandit wargame, an engaging challenge designed for absolute beginners. This game aims to teach fundamental skills essential for playing other wargames.
If you want to explore the original website, you can find it [here](https://overthewire.org/wargames/bandit/).

## Getting Started 🛠️
The game is organized into levels, starting from Level 0. Your goal is to "beat" or "finish" each level, which unlocks information on how to proceed to the next one. The website's pages for each level contain instructions on transitioning from the previous level. You can find links to all levels and their solutions below.

## Ready to Begin? 🚀
To begin your journey with Level 0, log in via SSH using the following command:
`ssh bandit0@bandit.labs.overthewire.org -p 2220`. Password for Level 0 is `bandit0`. As you progress, the password for the next level will be revealed on each level's page.

## Table of Contents 📚
1. [Level 0](#level-0)
2. [Level 1](#level-1)
3. [Level 2](#level-2)
4. [Level 3](#level-3)
5. [Level 4](#level-4)
6. [Level 5](#level-5)
7. [Level 6](#level-6)
8. [Level 7](#level-7)
9. [Level 8](#level-8)
10. [Level 9](#level-9)
11. [Level 10](#level-10)
12. [Level 11](#level-11)
13. [Level 12](#level-12)
14. [Level 13](#level-13)
15. [Level 14](#level-14)
16. [Level 15](#level-15)
17. [Level 16](#level-16)
18. [Level 17](#level-17)
19. [Level 18](#level-18)
20. [Level 19](#level-19)
21. [Level 20](#level-20)
22. [Level 21](#level-21)
23. [Level 22](#level-22)
24. [Level 23](#level-23)
25. [Level 24](#level-24)
26. [Level 25](#level-25)
27. [Level 26](#level-26)
28. [Level 27](#level-27)
29. [Level 28](#level-28)
30. [Level 29](#level-29)
31. [Level 30](#level-30)
32. [Level 31](#level-31)
33. [Level 32](#level-32)
34. [Level 33](#level-33)


## Solution 💡
### Level 0
- **Description:**
     - There is a `readme` in the home directory which contains the password for the next level, use the cat command to display its contents.
- **Commands:**
     - `cat readme`

### Level 1
- **Description:**
     - There is a file in the home directory that has a name `-`. Use the cat command as shown below to read the contents of this file and find the password for the next level.
- **Commands:**
     - `cat ./-`

### Level 2
- **Description:**
     - This level involves a filename with spaces. Use either of the provided commands to display the contents of the file and obtain the password for Level 3.
- **Commands:**
     - `cat ./spaces\ in\ this\ filename` or `cat "spaces in this filename"`

### Level 3
- **Description:**
     - There is directory named `inhere` which contains a hiden file as its name starts with a dot. To list all the files including hidden files in a dirctory use the -a option in the ls command. Read the content of the file by cat command and get the password for the next level.
- **Commands:**
     - `ls -la inhere/`
     - `cat inhere/.hidden`

### Level 4
- **Description:**
     - There are multiple files in the `inhere` directory. Use the file command on each of those files and get their file types. Read the content of the file whose file type is `ASCII Test` and get the password of the next level.
- **Commands:**
     - `file ./inhere/`
     - `cat ./inhere/-file07`

### Level 5
- **Description:**
     - From the given description, the file size is 1033 bytes. Using find command search for all the files whose size is 1033 bytes in the directory and get the password for the next level.
- **Commands**:
     - `find . -type f -size 1033c`

### Level 6
- **Description:**
     - From the given description, the owner of the file is `bandit7` and it belongs to `bandit6` group. Use the below find command to search of the file and get the password for the next level.
- **Commands:**
     - `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null`

### Level 7
- **Description:**
     - Use the grep command to extract the line that contains the word `millionth` and get the password for the next level.
- **Commands:**
     - `cat data.txt | grep millionth`

### Level 8
- **Description:**
     - Sort the file using the sort command and list the number of occurances of each line using the uniq command. The line which has 1 written before it occurs only once in the file and that is the password for the next level.
- **Commands:**
     - `cat data.txt | sort | uniq -c`

### Level 9
- **Description:**
     -  Using strings extract the readable characters from the file and get the password for the next level.
- **Commands:**
     - `cat data.txt | strings`

### Level 10
- **Description:**
     - Decode the contents of the file using Base64 and get the password for the next level.
- **Commands:**
     - `cat data.txt  | base64 -d`

### Level 11
- **Description:**
     - The contents of the file are encoded using ROT-13 algorithm. Use [this](https://rot13.com/) website to decode the contents or use the `tr` command below.
- **Commands:**
     - `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`

### Level 12
- **Description:**
     - The password for the next level is stored in `data.txt` file which is encoded in hex format.
     - Use the `xxd` command to reverse the hex data and save the output to a new file.
     - Utilize the file command to determine the file type. If it is a compressed file, proceed with the appropriate decompression command `(gzip, bzip2, or tar)` until an ASCII text file is obtained.
     - Read the contents of the file to obtain the password for the next level.
     - **Note:** If decompression fails, attempt adding an extension to the compressed file. For instance, if the file is compressed with `gzip`, add the `.gz` extension and retry the decompression.
- **Commands:**
     - `cat ~/data.txt | xxd -r > <output_file>` (Reverse the hexdump)
     - `file <output_file>` (Check file type)
     - `bzip2 -d <output_file>` (bzip2 decompression)
     - `gzip -d <output_file>.gz` (gzip decompression)
     - `tar -xvf <output_file>` (tar decompression)
     - `cat <output_file>` (Read the password)

### Level 13
- **Description**:
     - Use the SSH Private Key to login to the login next level.
- **Commands**:
     - `ssh bandit14@localhost -i sshkey.private -p 2220`

### Level 14
- **Description**:
     - Connect to the localhost on port `30000` using `netcat` and submit the password for the current level.
     - Use the `cat` command to read the password for the current level from the etc directory.
- **Commands**:
     - `cat /etc/bandit_pass/bandit14`
     - `nc 127.0.0.1 30000`

### Level 15
- **Description**:
     - Connect to the localhost on the port `30001` using `openssl` and submit the password for the current level.
- **Commands**:
     - `openssl s_client -connect localhost:30001`

### Level 16
- **Description**:
     - Run an `nmap` scan on localhost on ports ranging between `31000 - 32000`. This will give list of open ports within the range.
     - Connect to those open ports one by one using `openssl` & submit the password for the current level, until you get the SSH Private Key for the next level.
- **Commands**:
     - `nmap localhost -p31000-32000 -v -T4`
     - `openssl s_client -connect localhost:<open_port>`

### Level 17
- **Description**:
     - In the home directory there are two files `passwords.old` & `passwords.new`.
     - Use the `diff` command to find out the difference between those two files & get the password of the next level.
- **Commands**:
     - `diff passwords.old passwords.new`

### Level 18
- **Description**:
     - The SSH shell dies after you login to this level because the `.bashrc` file is modified in that way.
     - You can just send the commands directly with the SSH connection string & it will give the output of that command.
     - Read the `readme` file in the home directory & get the output for the next level.
- **Commands**:
     - `ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"`

### Level 19
- **Description**:
     - There is a `bandit20-do` executable file which has setuid bit set.
     - The file is owned by `bandit20` user so it can run commands as that user.
     - Use is to read the password for the next level.
- **Commands**:
     - `./bandit20-do cat /etc/bandit_pass/bandit20`

### Level 20
- **Description**:
     - There is an `suconnect` executable (setuid bit set) file which connects to an open port & gives the password for the next level, if it receives the correct password for the current level.
     - Use `echo` command to display the password for the current level & pipe it to the `ncat` listener, that will open up an arbitrary port on the localhost.
     - You can either create a new SSH connection in another terminal or use the same terminal by putting the `ncat` listener in bckground as shown below.
- **Commands**:
     - `echo -n "VxCazJaVykI6W36BkBU0mJTCM8rR95XT" | ncat -lvnp 1337 &`
     - `./suconnect 1337`

### Level 21
- **Description**:
     - There is a cronjob running which you can find in the `/etc/cron.d/` directory using the command `ls -al /etc/cron.d`. There is file `cronjob_bandit22` running
       ```bash
          @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
          * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
       ```
     - The script `/usr/bin/cronjob_bandit22.sh` is executed by `bandit22` user every minute of every hour, every day of the month, every month, every day of the week.
       ```bash
          #!/bin/bash
          chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
          cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
       ```
     - 
- **Commands**:
     - `cat



### Level 22
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 23
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 24
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 25
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 26
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 27
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 28
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 29
- **Description**:
     - This
- **Commands**:
     - `cat


### Level 29
- **Description**:
     - This
- **Commands**:
     - `cat


### Level 30
- **Description**:
     - This
- **Commands**:
     - `cat

### Level 31
- **Description**:
     - This
- **Commands**:
     - `cat

### Level 32
- **Description**:
     - This
- **Commands**:
     - `cat

### Level 33
- **Description**:
     - This
- **Commands**:
     - `cat
