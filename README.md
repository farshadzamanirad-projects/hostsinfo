# Hostsinfo
With this ansible script we can have nice report which will include :

|IP|Hostname|OS|OS_Version|Users with UID>999|
|----|----|----|----|----|

and it will create csv and xlsx files based on date and even mail it for you!

### Prerequisites:
- [ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- python3-pip (apt -y install python3-pip, yum -y install python3-pip)
- [pandas](https://pypi.org/project/pandas/)
- mailx (apt -y install bsd-mailx, yum -y install bsd-mailx)

### Fire up!
```
ansible-playbook -i hosts info.yaml
```
> Note:

>  Please change <YOUR_DESIRED_RECIPIENT> inside [roles/local/tasks/main.yaml](https://github.com/farshadzamanirad-projects/hostsinfo/blob/main/roles/local/tasks/main.yaml) to fit your desire.

>  Please change hosts from `192.168.56.[1:254]` and credentials to fit your environment inside [hosts](https://github.com/farshadzamanirad-projects/hostsinfo/blob/main/hosts).
Ansible is awsome , Have fun!
