#!/bin/bash

cd ~/UCL_COMP0235_BIOCHEM_PROJECT/Ansible/

echo "1. Mount Block Storage"
ansible-playbook --private-key=~/.ssh/project_identity -i inventory.yaml mount_volume.yaml

echo "2. Install Packages"
ansible-playbook --private-key=~/.ssh/project_identity -i inventory.yaml setup.yaml

echo "3. Setup Node Exporter service"
ansible-playbook --private-key=~/.ssh/project_identity -i inventory.yaml node_exporter.yaml

