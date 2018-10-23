#!/usr/bin/env bash

cat << EOF
Environment Variables:
    ftp_proxy    = ${ftp_proxy}
    http_proxy   = ${http_proxy}
    https_proxy  = ${https_proxy}
    tester_name  = ${tester_name}
    env_rel_path = ${env_rel_path}
EOF

# delimited with '='
export freecad_conda_ver=${freecad_conda_ver_major}=${freecad_conda_ver_minor}

# FIXME: although preferable, installing with apt doesn't work with python imports
## install 'add-apt-repository' utility
#apt-get update
#apt-get install -y software-properties-common
#
## add FreeCAD apt repo'
#add-apt-repository -y ppa:freecad-maintainers/freecad-daily
#apt-get update
#apt-get install -y freecad-daily python3 python3-pip
#pip3 install --upgrade pip

# Install apt packages
apt-get update
apt-get install -y python3 python3-pip wget
python3 -m pip install --upgrade pip

# using conda package management to install freecad=0.17
wget -nv https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh
bash /tmp/miniconda.sh -b -p /opt/miniconda
export PATH="$PATH:/opt/miniconda/bin"
hash -r
conda config --set always_yes yes --set changeps1 no
conda update conda
#conda info -a
conda install -c freecad -c conda-forge freecad=${freecad_conda_ver} conda

# install pip packages
python3 -m pip install ipython
