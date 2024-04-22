# 0x0E. Web stack debugging #1 

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg" />
</p>


# Web stack debugging #1

This was the second in a series of web stack debugging projects. In these
projects, I was given broken/bugged webstacks in isolated containers,
and tasked with fixing the web stack to a working state. For each
task, I wrote a script automating the commands necessary to fix the
web stack.

## Tasks :page_with_curl:

* **0. Nginx likes port 80**
  * [0-nginx_likes_port_80](./0-nginx_likes_port_80): Bash script that
  configures Nginx to run and listen to port 80 on all of a server's active IPv4's.

* **1. Make it sweet and short**
  * [1-debugging_made_short](./1-debugging_made_short): Bash script that
  configures Nginx to listen to port 80 without running on all of a server's
  active IPv4's.
##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   Your Puppet manifests must pass `Shellcheck` version 0.3.7 without any errors.
*   All your Bash script files must be executable.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.
*   You can’t use `systemctl` for restarting a process.
*   You are not allowed to use `wget`.

## Project Description.
Learn what is the main role of a web server.
What is a child process.
Why web servers usually have a parent process and child processes.
What are the main HTTP requests.
What DNS stands for and its main role.
