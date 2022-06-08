# Ansible

Repository for Ansible playbooks to track any infrastructure changes we need
These scripts only work on vm 10.22.1.77 since it has the master key. Connect by using sudo su -l ansible, then run ssh 10.22.1.77 and go to the dir of /git dir you will see the repository where the makefile is.
Make file commands

- make python3.8 (Installs python on all machines)
- make git2.27 (Installs git on all machines)
- make packages (Installs all required packages)
