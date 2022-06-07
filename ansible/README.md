# Ansible

Repository for Ansible playbooks to track any infrastructure changes we need
These scripts only work on vm 10.22.1.77 since it has the master key. Connect by using sudo su -l ansible, then run ssh 10.22.1.77 and inside the /git dir you will see the repository where the makefile is.
Make file commands


- make python3.8 (Installs python on all machines)
- make git2.27 (Installs git on all machines) *Will throw errors on Install Git step, Please ignore its caused by a bad command within makefile
- make packages (Installs all required packages)
