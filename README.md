
# Engineering for Data Analysis - Protein Prediction Project
> This project employs Amazon Web Services (AWS) to establish a distributed analysis system for running a 3D protein-prediction task. The primary challenge in protein prediction is the extensive time required for accurate forecasts. By leveraging a single AWS host machine to coordinate multiple worker machines, this project aims to significantly expedite the protein structure prediction process, improving the existing process's efficiency to facilitate relevant biological and pharmaceutical research better.

## AWS Infrastructure

In this project, 6 AWS machines (EC2 instances) were employed, including 1 host machine, 1 client machine and 4 cluster machines. The host machine utilised Ansible for orchestrating operations across the network, managing file distribution, task allocation, and document control, while not participating in the protein prediction task. The client machine and 4 cluster machines were the main worker machines as they were dedicated to executing ML prediction tasks under the host machine's instructions. 

### Prerequisites
The host machine needs to have Python3, Pip and Ansible installed.

```shell
sudo yum install python3 python3-pip -y
python3 -m pip install --user ansible
```
### Setup SSH keys for inter-machine connection
On the host machine, generate project_identity key and distribute the key via Ansible ([distribute_keys.yaml](./Ansible/distribute_keys.yaml))

```shell
cd .ssh
ssh-keygen -f project_identity

# Use the lecturer_key to distribute project identity keys. 
cd ~/UCL_COMP0235_BIOCHEM_PROJECT/Ansible/
ansible-playbook --private-key=~/.ssh/lecturer_key -i inventory.yaml distribute_keys.yaml
```
### Setting up worker (client and cluster machines)
Run the shell script to setup the worker machines.

```shell
~/UCL_COMP0235_BIOCHEM_PROJECT/Shell/worker_setup.sh 
```
The shell script contains the following steps via Ansible:
- [Mount block storage](./Ansible/mount_volume.yaml)
- [Install software dependencies](./Ansible/setup.yaml)
- [Setup Node Exporter for monitoring](./Ansible/node_exporter.yaml)

### Download codebase for S4Pred and HH-suite and PDB70 dataset
```shell
~/UCL_COMP0235_BIOCHEM_PROJECT/Shell/download.sh 
```
The shell script contains the following steps via Ansible:
- [Download code fof S4Pred and HH-suite from Github](./Ansible/code_downloader.yaml)
- [Download PDB70 database](./Ansible/data_downloader.yaml)

### Features
- Feature 1
- Feature 2
- Feature 3

## Getting Started
Instructions on how to get a copy of the project up and running on a local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them.

\```
Example: pip install -r requirements.txt
\```

### Installation
Step by step series of examples that tell you how to get a development environment running.

\```
git clone https://yourproject.git
cd yourproject
\```

## Usage
Explain how to use your project with code snippets.

### Python Snippet
```python
# Python code example
print('Hello, World!')
```

### Shell Snippet
\```shell
# Shell command example
echo 'Hello, World!'
\```

### YAML Snippet
\```yaml
# YAML configuration example
greeting: 'Hello, World!'
\```

## Adding Images
You can add images to make your README visually appealing.

![Alt text](path/to/image.jpg)
![Another image](path/to/another_image.jpg)

## Contributing
Explain how others can contribute to your project.

## File References
- [Example File 1](./path/to/file1)
- [Example File 2](./path/to/file2)

## License
Describe the license under which your project is released.

## Contact
Your Name - email@example.com

Project Link: [https://github.com/your_username/your_project](https://github.com/your_username/your_project)
