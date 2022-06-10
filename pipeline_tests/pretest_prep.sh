#! /bin/bash

installed_py_ver=$(python3 --version)
if [[ $installed_py_ver != *"3.8."* ]] ; then
  - apt update --option Acquire::HTTPS::Proxy=https://contractorproxyeast.northgrum.com:80
  - apt-get -y install python3 virtualenv flake8
  virtualenv --python=python3.8 /home/sleipnir_pipeline/py3.8
  pip install pytest coverage
else
  virtualenv --python=python3.8 /home/sleipnir_pipeline/py3.8
fi
