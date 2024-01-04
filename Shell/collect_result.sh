#!/bin/bash

echo "1. Collect results from worker machines"
cd ~/UCL_COMP0235_BIOCHEM_PROJECT/Ansible/
ansible-playbook --private-key=~/.ssh/project_identity -i inventory.yaml collect_result.yaml

echo "2. Compile results and compute summary statistics"
cd ~/UCL_COMP0235_BIOCHEM_PROJECT/Coursework/
python3 compile_results.py