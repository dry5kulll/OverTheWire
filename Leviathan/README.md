# Leviathan
Leviathan is a wargame that doesn't require any knowledge about programming - just a bit of common sense and some knowledge about basic *nix commands.

## Summary:
- Difficulty: 1/10
- Levels: 8
- Platform: Linux/x86

## Description:
Leviathan’s levels are called leviathan0, leviathan1, … etc. and can be accessed on leviathan.labs.overthewire.org through SSH on port 2223.

To log in to the first level use:
- Username: `leviathan0`
- Password: `leviathan0`

Data for the levels can be found in the homedirectories. You can look at `/etc/leviathan_pass` for the various level passwords.

## Solutions:

### Leviathan 0:
- **Description:**
    - There is a `bookmarks.html` file in the hidden backup directory which has lots of content. I used grep to extract the password string from the file.
- **Commands:**
    - `cat .backup/bookmarks.html | grep password`

### Leviathan 1:

- **Description:**
    - In this challenge, there is an executable file named `check` with the setuid bit set. When executed, it prompts the user for a password and returns some output. Since the correct password is unknown, I utilized the [ltrace](https://man7.org/linux/man-pages/man1/ltrace.1.html) tool to observe the actions performed by the executable.
    - During the trace, I saw a string comparison operation `(strcmp("pas", "sex"))` where the entered value is compared against the string `sex`. I used this information & entered `sex` as the password. Upon successful entry, a new terminal is spawned, and checking the user information with the id command confirms that I am now leviathan2.
    - To proceed to the next level, I retrieved the password from the `/etc/leviathan_pass/leviathan2` file.
- **Commands**:
    - `ltrace ./check`
    - `cat /etc/leviathan_pass/leviathan2`

### Leviathan 2:

- **Description:**
    - In this challenge, there is an executable file `printfile` that prints the content of any file that is specified. I tried to get the password for the next level for it but it didn't allow me to read that file.
    - Next, I used ltrace command to see what library calls are made & found that it was using cat command to read the file.
- Commands:
    - 

### Leviathan 3:

- Description:
- Commands:

### Leviathan 4:

- Description:
- Commands:

### Leviathan 5:

- Description:
- Commands:

### Leviathan 6:

- Description: [Provide a brief description of the solution for this level]
- Command(s): [Specify the commands or steps required to solve the level]


