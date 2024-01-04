#!/bin/bash

echo "1. Generate a key for inter-machine communication"

if [ ! -f ~/.ssh/project_identity ]; then
  ssh-keygen -f ~/.ssh/project_identity -N ""
else
  echo "The key already exists, not overwriting it."
fi

echo "2. Distribute the key via Ansible using the lecturer key"
cd ~/UCL_COMP0235_BIOCHEM_PROJECT/Ansible/
ansible-playbook --private-key=~/.ssh/lecturer_key -i inventory.yaml distribute_keys.yaml