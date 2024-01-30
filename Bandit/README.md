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


## Solutions 💡
### Level 0
- **Description:**
     - There is a `readme` in the home directory which contains the password for the next level.
- **Solution:**
     - Use the `cat readme` command to read the password for the next level.

### Level 1
- **Description:**
     - There is a file in the home directory that has a name `-`.
- **Solution:**
     - Use the `cat ./-` command to read the password for the next level.

### Level 2
- **Description:**
     - This level involves a filename with spaces.
- **Solution:**
     - Use `cat ./spaces\ in\ this\ filename` or `cat "spaces in this filename"` command to read the password for the next level.

### Level 3
- **Description:**
     - There is directory named `inhere` which contains a hiden file as its name starts with a dot. To list all the files including hidden files in a dirctory use the -a option in the ls command. Read the content of the file by cat command and get the password for the next level.
- **Solution:**
     - `ls -la inhere/`
     - `cat inhere/.hidden`

### Level 4
- **Description:**
     - There are multiple files in the `inhere` directory. Use the file command on each of those files and get their file types. Read the content of the file whose file type is `ASCII Test` and get the password of the next level.
- **Solution:**
     - `file ./inhere/`
     - `cat ./inhere/-file07`

### Level 5
- **Description:**
     - From the given description, the file size is 1033 bytes. Using find command search for all the files whose size is 1033 bytes in the directory and get the password for the next level.
- **Solution**:
     - `find . -type f -size 1033c`

### Level 6
- **Description:**
     - From the given description, the owner of the file is `bandit7` and it belongs to `bandit6` group. Use the below find command to search of the file and get the password for the next level.
- **Solution:**
     - `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null`

### Level 7
- **Description:**
     - Use the grep command to extract the line that contains the word `millionth` and get the password for the next level.
- **Solution:**
     - `cat data.txt | grep millionth`

### Level 8
- **Description:**
     - Sort the file using the sort command and list the number of occurances of each line using the uniq command. The line which has 1 written before it occurs only once in the file and that is the password for the next level.
- **Solution:**
     - `cat data.txt | sort | uniq -c`

### Level 9
- **Description:**
     -  Using strings extract the readable characters from the file and get the password for the next level.
- **Solution:**
     - `cat data.txt | strings`

### Level 10
- **Description:**
     - Decode the contents of the file using Base64 and get the password for the next level.
- **Solution:**
     - `cat data.txt  | base64 -d`

### Level 11
- **Description:**
     - The contents of the file are encoded using ROT-13 algorithm. Use [this](https://rot13.com/) website to decode the contents or use the `tr` command below.
- **Solution:**
     - `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`

### Level 12
- **Description:**
     - The password for the next level is stored in `data.txt` file which is encoded in hex format.
     - Use the `xxd` command to reverse the hex data and save the output to a new file.
     - Utilize the file command to determine the file type. If it is a compressed file, proceed with the appropriate decompression command `(gzip, bzip2, or tar)` until an ASCII text file is obtained.
     - Read the contents of the file to obtain the password for the next level.
     - **Note:** If decompression fails, attempt adding an extension to the compressed file. For instance, if the file is compressed with `gzip`, add the `.gz` extension and retry the decompression.
- **Solution:**
     - `cat ~/data.txt | xxd -r > <output_file>` (Reverse the hexdump)
     - `file <output_file>` (Check file type)
     - `bzip2 -d <output_file>` (bzip2 decompression)
     - `gzip -d <output_file>.gz` (gzip decompression)
     - `tar -xvf <output_file>` (tar decompression)
     - `cat <output_file>` (Read the password)

### Level 13
- **Description:**
     - Use the SSH Private Key to login to the login next level.
- **Solution:**
     - `ssh bandit14@localhost -i sshkey.private -p 2220`

### Level 14
- **Description:**
     - Connect to the localhost on port `30000` using `netcat` and submit the password for the current level.
     - Use the `cat` command to read the password for the current level from the etc directory.
- **Solution:**
     - `cat /etc/bandit_pass/bandit14`
     - `nc 127.0.0.1 30000`

### Level 15
- **Description:**
     - Connect to the localhost on the port `30001` using `openssl` and submit the password for the current level.
- **Solution:**
     - `openssl s_client -connect localhost:30001`

### Level 16
- **Description:**
     - Run an `nmap` scan on localhost on ports ranging between `31000 - 32000`. This will give list of open ports within the range.
     - Connect to those open ports one by one using `openssl` & submit the password for the current level, until you get the SSH Private Key for the next level.
- **Solution:**
     - `nmap localhost -p31000-32000 -v -T4`
     - `openssl s_client -connect localhost:<open_port>`

### Level 17
- **Description:**
     - In the home directory there are two files `passwords.old` & `passwords.new`.
     - Use the `diff` command to find out the difference between those two files & get the password of the next level.
- **Solution:**
     - `diff passwords.old passwords.new`

### Level 18
- **Description:**
     - The SSH shell dies after you login to this level because the `.bashrc` file is modified in that way.
     - You can just send the Solution directly with the SSH connection string & it will give the output of that command.
     - Read the `readme` file in the home directory & get the output for the next level.
- **Solution:**
     - `ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"`

### Level 19
- **Description:**
     - There is a `bandit20-do` executable file which has setuid bit set.
     - The file is owned by `bandit20` user so it can run Solution as that user.
     - Use is to read the password for the next level.
- **Solution:**
     - `./bandit20-do cat /etc/bandit_pass/bandit20`

### Level 20
- **Description:**
     - There is an `suconnect` executable (setuid bit set) file which connects to an open port & gives the password for the next level, if it receives the correct password for the current level.
     - Use `echo` command to display the password for the current level & pipe it to the `ncat` listener, that will open up an arbitrary port on the localhost.
     - You can either create a new SSH connection in another terminal or use the same terminal by putting the `ncat` listener in bckground as shown below.
- **Solution:**
     - `echo -n "VxCazJaVykI6W36BkBU0mJTCM8rR95XT" | ncat -lvnp 1337 &`
     - `./suconnect 1337`

### Level 21
- **Description**:
     - There is a cronjob running in the `/etc/cron.d/` directory. The file `cronjob_bandit22` has the below code in it.
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
     - The script modifies the permissions on the file in the `/tmp` directory and then copies the password of the `bandit22` user into that file.
- **Solution**:
     - `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`

### Level 22
- **Description**:
     - Same as the previous level, there is a cronjob running.
     - The script `/usr/bin/cronjob_bandit23.sh` executed by `bandit23` user has the below code in it.
       ```bash
       #!/bin/bash
       myname=$(whoami)
       mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
       echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
       cat /etc/bandit_pass/$myname > /tmp/$mytarget
       ```
     - The script `/usr/bin/cronjob_bandit23.sh` is responsible for extracting the username of the executing user, appending it to the string `I am user `, generating an MD5 hash of the resulting string, and then copying the password file of the bandit23 user into a file named with the MD5 hash.
- **Solution**:
     - `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`
     - `cat /tmp/8ca319486bfbbc3663ea0fbe81326349`

### Level 23
- **Description**:
     - Same as the previous level, there is a cronjob running.
     - The script `/usr/bin/cronjob_bandit24.sh` executed by `bandit24` user has the below code in it.
       ```bash
       #!/bin/bash
       myname=$(whoami)
       cd /var/spool/$myname/foo
       echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
       for i in * .*;
       do
            if [ "$i" != "." -a "$i" != ".." ];
            then
                 echo "Handling $i"
                 owner="$(stat --format "%U" ./$i)"
                 if [ "${owner}" = "bandit23" ]; then
                      timeout -s 9 60 ./$i
                 fi
                 rm -f ./$i
            fi
       done
       ```
     - The code navigates to the `/var/spool/bandit24/foo` directory and extracts the owner of every file in that directory.
     - If the owner of the file is `bandit23` then it executes that file with a timeout of 60 seconds, if the program doesn't complete within 60 seconds, then it sends a signal `SIGKILL` (signal number 9) to terminate it.
     - Also, the directory `/var/spool/bandit24/foo` is writable & execuatble by any other user.
     - So, to get the password for the next user, I created a file with the below code, this will create a file in the `/tmp` directory, copy the password for the next user into it & make it readable, writable by everyone.
       ```bash
       #!/bin/bash
       cat /etc/bandit_pass/bandit24 > /tmp/cross
       chmod 666 /tmp/cross
       ```
- **Solution**:
     - `cat /tmp/cross`

### Level 24
- **Description**:
     - There is daemon listening in Port 30002 that accepts the password for current user along with a 4-digit code.
     - If the password & code is correct, it will give the password for the next level.
- **Solution**:
     - Create a script with the below code that will bruteforce through the entire
       ```bash
       #!/bin/bash

       for i in {0000..9999};
       do
            echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i";
       done | nc localhost 30002 | grep -vi wrong
       ```
     - Execute the script, & wait until it gives the password for next level.

### Level 25
- **Description**:
     - This
- **Solution**:
     - `cat



### Level 26
- **Description**:
     - There is an executable file `bandit27-do` that has setuid bit set on it.
     - It allows running command as another user in this case `bandit27` user as the file is owned by that user.
- **Solution**:
     - Run `./bandit27-do id` command & you will see the following output `uid=11026(bandit26) gid=11026(bandit26) euid=11027(bandit27) groups=11026(bandit26)`.
     - The effective uid (euid) is `bandit27`. So now you can run the command `./bandit27-do cat /etc/bandit_pass/bandit27` & get the password for the next level.

### Level 27
- **Description**:
     - There is a git repository at `ssh://bandit27-git@localhost/home/bandit27-git/repo` on port 2220 whose password is same as the current levels password.
- **Solution**:
     - Clone the git repo using the command `git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo`. Use the current levels password to clone the repo.
     - Navigate to the cloned repo, read the readme file & get the password for the next level.

### Level 28
- **Description**:
     - There is a git repository at `ssh://bandit28-git@localhost/home/bandit28-git/repo` on port 2220 whose password is same as the current levels password.
- **Solution**:
     - Follow the same steps from the previous level to clone the GitHub Repo, once cloned navigate into the repo.
     - There is a readme.md file that will have the below content.
       ```
       # Bandit Notes
       Some notes for level29 of bandit.

       ## credentials
       username: bandit29
       password: xxxxxxxxxx
       ```
     - Use the `git log` command to check the logs & you should see 3 commits, slong with a hash value assocaited with them.
     - Finally, use the `git show <commit_hash>` on all those commits & grab the password for the next level.

### Level 29
- **Description**:
     - There is a git repository at `ssh://bandit29-git@localhost/home/bandit29-git/repo` on port 2220 whose password is same as the current levels password.
- **Solution**:
     - Follow the same steps from the previous level to clone the GitHub Repo, once cloned navigate into the repo.
     - There is a readme.md file that will have the below content.
       ```
       # Bandit Notes
       Some notes for bandit30 of bandit.

       ## credentials
       username: bandit30
       password: <no passwords in production!>
       ```
     - Use the `git status` or `git branch` to check the current branch you are on.
     - Use the `git branch -r` command & you will find other branches along with the master branch.
       ```
       origin/HEAD -> origin/master
       origin/dev
       origin/master
       origin/sploits-dev
       ```
     - Examine each branches one by one using the `git show origin/dev` command & get the password for the next level.

### Level 30
- **Description**:
     - There is a git repository at `ssh://bandit30-git@localhost/home/bandit30-git/repo` on port 2220 whose password is same as the current levels password.
- **Solution**:
     - Follow the same steps from the previous level to clone the GitHub Repo, once cloned navigate into the repo.
     - There is a readme.md file that will have the below content.
       ```
       just an empty file... muahaha
       ```
     - There are no commits or branches.
     - Enter the command `git show <TAB>` & enter the tab button to see other options associated with the command.
     - One of the options includes `secret`. Use it to get the password for the next level.

### Level 31
- **Description**:
     - There is a git repository at `ssh://bandit31-git@localhost/home/bandit31-git/repo` on port 2220 whose password is same as the current levels password.
- **Solution**:
     - Follow the same steps from the previous level to clone the GitHub Repo, once cloned navigate into the repo.
     - There is a readme.md file that will have the below content.
       ```
       This time your task is to push a file to the remote repository.
       Details:
            File name: key.txt
            Content: 'May I come in?'
            Branch: master
       ```
     - Create a file with the same name & content.
     - git status - shows where branch is changed or updated
     - git add . -f - To force add the newly created file
     - git status - shows the changes to be committed
     - git commit -m "File Committed" - Commits the new file changes in the local repo
     - git push - Push the changes to the master branch

### Level 32
- **Description**:
     - This time after logging in, you are send 
- **Solution**:
     - Use `$0` to escape the restricted shell. After escaping, we are `bandit33` user. Grab its password from the `/etc/bandit_pass/bandit33` file.

### Level 33
- **Description**:
     - This is the last level of the challenge.
- **Solution**:
     - Read the contents of the readme.txt file and grab the final flag.
       ```
       Congratulations on solving the last level of this game!
       At this moment, there are no more levels to play in this game. However, we are constantly working on new levels and will most likely expand this game with more levels soon. Keep an eye out for an announcement on our usual communication channels! In the meantime, you could play some of our other wargames.
       If you have an idea for an awesome new level, please let us know!
       ```
