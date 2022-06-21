#! /bin/bash

apt update --option Acquire::HTTPS::Proxy=https://contractorproxyeast.northgrum.com:80

installed_py_ver=$(python3 --version)
if [[ $installed_py_ver != *"3.8."* ]] ; then
  apt-get -y install python3
fi

apt-get -y install virtualenv
virtualenv --python=python3.8 /home/sleipnir_pipeline/py3.8
apt-get -y install flake8
pip install pytest coverage pytest-cov
pip install robot==5.0.1
