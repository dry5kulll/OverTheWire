# OverTheWire Bandit Challenge

## Introduction

Welcome to the Bandit wargame, an engaging challenge designed for absolute beginners. This game aims to teach fundamental skills essential for playing other wargames. If you encounter any issues or have ideas for new levels, feel free to provide feedback.

## Getting Started

### Level Structure

The game is organized into levels, starting from Level 0. Your goal is to "beat" or "finish" each level, which unlocks information on how to proceed to the next one. The website's pages for each level contain instructions on transitioning from the previous level. You can find links to all levels in the sidemenu on the left.

### Guidance for Beginners

For those new to the game or command line usage:

- **Don't Panic:** Levels may present unfamiliar challenges, but the purpose is to learn the basics.
- **Read and Learn:** The game involves reading a lot of new information. If you're new to the command line, start with this [introduction to user commands](#).
- **Troubleshooting Tips:**
  - If you know a command but don't know how to use it, try the manual (man page) by entering `man <command>`. For example, `man ls` to learn about the "ls" command.
  - If there is no man page, the command might be a shell built-in. Use the `help <X>` command. For example, `help cd`.
  - Utilize your favorite search engine, such as Google, for additional assistance.
  - If you're still stuck, join us via [chat](#).

## Ready to Begin?

You're all set to start your journey! Begin with [Level 0](#), linked on the left side of this page. Good luck!

## Note for VM Users

If you are using a virtual machine (VM) and face issues connecting to overthewire.org via SSH with a "broken pipe error" when the network adapter is set to NAT mode, add the setting `IPQoS throughput` to `/etc/ssh/ssh_config` to resolve the issue. If the problem persists, consider changing the adapter to Bridged mode.

