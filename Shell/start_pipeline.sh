#!/bin/bash

echo "1. On host machine, split the 6000 IDs to 5 parts"
cd ~/UCL_COMP0235_BIOCHEM_PROJECT/Coursework
python3 ~/UCL_COMP0235_BIOCHEM_PROJECT/Coursework/distribute_ids.py

echo "2. Upload data from local Coursework folder to S3 bucket"
aws s3 sync ~/UCL_COMP0235_BIOCHEM_PROJECT/Coursework s3://comp0235-ucabkk1/Coursework

echo "3. Download data from S3 bucket"
cd ~/UCL_COMP0235_BIOCHEM_PROJECT/Ansible/
ansible-playbook --private-key=~/.ssh/project_identity -i inventory.yaml s3_bucket.yaml

echo "4. Start the ML pipeline"
ansible-playbook --private-key=~/.ssh/project_identity -i inventory.yaml distribute_work.yaml

