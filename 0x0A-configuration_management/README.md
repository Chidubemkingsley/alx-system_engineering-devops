# System Engineering and DevOps - Bash, Scripting, Web Stack/Web Stack Debugging, Networking & Security, CI/CD
![Repo size](https://img.shields.io/github/repo-size/4ouR04/alx-system_engineering-devops)
![Latest commit](https://img.shields.io/github/last-commit/4ouR04/alx-system_engineering-devops/master?style=round-square)

This repository contains programs written for the system engineering and DevOps
track at ALX School. In these projects, I worked with Bash and practiced
writing Bash scripts to automate tasks.
The specific list of projects
contained follows:

* [0x00. Shell, basics](./0x00-shell_basics)
* [0x01. Shell, permissions](./0x01-shell_permissions)
* [0x02. Shell, I/O Redirections and filters](./0x02-shell_redirections)
* [0x03. Shell, init files, variables and expansions](./0x03-shell_variable_expansions)
* [0x04-loops,conditions, and,parsing](./0x04-loops_conditions_and_parsing)
* [0x06-regular, expressions](./0x06-regular_expressions)
* [0x08-networking, basics, 2](./0x08-networking_basics_2)
* [0x09-web, infrastructure, design](./0x09-web_infrastructure_design)
* [0x0A-configuration, management](./00x0A-configuration_management)
* [0x0B-ssh](./0x0B-ssh)
* [0x0C-web, server](./0x0C-web_server)
* [0x0F-load, balancer](./0x0F-load_balancer)
* [attack, is,the,best, defense](./attack_is_the_best_defense)
* [0x10-https, ssl](./0x10-https_ssl)
* [Command, Line,for, the, WIn](./command_line_for_the_win)


## Acknowledgements :pray:

Click this image for more information

<a href= "https://www.alxafrica.com/"><img style="width: 100%" src="img/alx.png" alt="Alx logo"></a>

### For the project termed 0x0A. Configuration management 

####Background Context

When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.

There were 2 pieces of bad news:

    When MCollective receives nil as an argument for its filter method, it takes this to mean ‘all servers’
    The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

That was me ^_^‘: https://twitter.com/devopsreact/status/836971570136375296

###Resources

<str>Read or watch:</str>

    Intro to Configuration Management
    Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
    Puppet’s Declarative Language: Modeling Instead of Scripting
    Puppet lint
    Puppet emacs mode

###Requirements
<str>General</str>

    All your files will be interpreted on Ubuntu 20.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp


