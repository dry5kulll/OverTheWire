# OverTheWire Bandit Challenge 🎮

## Introduction 🚀
Welcome to the Bandit wargame, an engaging challenge designed for absolute beginners. This game aims to teach fundamental skills essential for playing other wargames.
If you want to explore the original website, you can find it [here](https://overthewire.org/wargames/bandit/).

## Getting Started 🛠️
The game is organized into levels, starting from Level 0. Your goal is to "beat" or "finish" each level, which unlocks information on how to proceed to the next one. The website's pages for each level contain instructions on transitioning from the previous level. You can find links to all levels & their solutions below.

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
     - There is is `readme` in the home directory which contains the password for the next level, use the cat command to display its contents.
- **Commands:**
     - `cat readme`

### Level 1
- **Description:**
     - There is a file in the home directory that has a name `-`. Use the cat command as shown below to read the contents of this file & find the password for the next level.
- **Commands:**
     - `cat ./-`

### Level 2
- **Description:**
     - This level involves a filename with spaces. Use either of the provided commands to display the contents of the file & obtain the password for Level 3.
- **Commands:**
     - `cat ./spaces\ in\ this\ filename` or `cat "spaces in this filename"`

### Level 3
- **Description:**
     - There is directory named `inhere` which contains a hiden file as its name starts with a dot. To list all the files including hidden files in a dirctory use the -a option in the ls command. Read the content of the file by cat command & get the password for the next level.
- **Commands:**
     - `ls -la inhere/`
     - `cat inhere/.hidden`

### Level 4
- **Description:**
     - There are multiple files in the `inhere` directory. Use the file command on each of those files & get their file types. Read the content of the file whose file type is `ASCII Test` & get the password of the next level.
- **Commands:**
     - `file ./inhere/`
     - `cat ./inhere/-file07`

### Level 5
- **Description:**
     - From the given description, the file size is 1033 bytes. Using find command search for all the files whose size is 1033 bytes in the directory & get the password for the next level.
- **Commands**:
     - `find . -type f -size 1033c`

### Level 6
- **Description:**
     - From the given description, the owner of the file is `bandit7` & it belongs to `bandit6` group. Use the below find command to search of the file & get the password for the next level.
- **Commands:**
     - `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null`

### Level 7
- **Description:**
     - Use the grep command to extract the line that contains the word `millionth` & get the password for the next level.
- **Commands:**
     - `cat data.txt | grep millionth`

### Level 8
- **Description:**
     - Sort the file using the sort command & list the number of occurances of each line using the uniq command. The line which has 1 written before it occurs only once in the file & that is the password for the next level.
- **Commands:**
     - `cat data.txt | sort | uniq -c`

### Level 9
- **Description:**
     -  Using strings extract the readable characters from the file & get the password for the next level.
- **Commands:**
     - `cat data.txt | strings`

### Level 10
- **Description:**
     - Decode the contents of the file using Base64 & get the password for the next level.
- **Commands:**
     - `cat data.txt  | base64 -d`

### Level 11
- **Description:**
     - This
- **Commands:**
     - `cat

* `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
* Explanation: Decode the contents of the file by performing a ROT-13 operation on its content, uisng the tr command & get the password for the next level.

### Level 12
- **Description:**
     - This
- **Commands:**
     - `cat

* `cat ~/data.txt | xxd -r > data`
* Explanation: The file is hexdump so to reverse the hexdump use the xxd command with r flag & save the contents into a new file. Using the file command check the type of the file.
    * It should be a compressed file. To decompress use different command like gzip, bzip, tar, etc commands until the file completely decompressed & you are left with an ASCII text file. Read the file content & get the password for the next user.
    * Note: If the decompression fails, try adding an extension to the compressed file. For e.g. if the file is "gzip" then add the ".gz" extension & then try to decompress.
  
### Level 13
- **Description**:
     - This
- **Commands**:
     - `cat

* `ssh bandit14@localhost -i sshkey.private -p 2220`
* Explanation: Use the Private Key provided to login to the next level by SSH.

### Level 14
- **Description**:
     - This
- **Commands**:
     - `cat

* `cat /etc/bandit_pass/bandit14`
* `nc 127.0.0.1 30000`
* Explanation: Get the password for the current level by reading the "/etc/bandit_pass/bandit14" file. Connect to the localhost & given port 30000 via netcat & submit the password of the current level. If the password is correct, the password for the next level will be given.

### Level 15
- **Description**:
     - This
- **Commands**:
     - `cat

* `openssl s_client -connect localhost:30001`
* Explanation: Use the OpenSSL command to connect to localhost on the given port & submit the password for the current level. If the password is correct, the password for the next level will be given.

### Level 16
- **Description**:
     - This
- **Commands**:
     - `cat

* `nmap localhost -p31000-32000 -v -T4`
* `openssl s_client -connect localhost:<PORT>`
* Explanation: Perform an nmap scan on localhost on ports between 31000 - 32000. It is display all the open ports between the range.
  * Use OpenSSL to connect to the port one by one, until one of them will accept the current users password & will give the SSH Private key for the next level.

### Level 17
- **Description**:
     - This
- **Commands**:
     - `cat

* `diff passwords.old passwords.new`
* Explanation: Use the diff command to find the difference between the two files & get the password for the next level.

### Level 18
- **Description**:
     - This
- **Commands**:
     - `cat


### Level 19
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 20
- **Description**:
     - This
- **Commands**:
     - `cat



### Level 21
- **Description**:
     - This
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
