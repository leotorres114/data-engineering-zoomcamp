# Terraform: Infrastructure as Code (IaC)
Terraform is an infrastructure as code (IaC) tool that allows you to build, change, and version infrastructure safely and efficiently. [source](https://www.terraform.io/intro)

In essence, one can manage cloud/container infrastructures via four simple CLI commands: 

Initialize a working directory with `.tf` configuration files with
```bash
terraform init
```
Create an execution plan, preview infrastructure that Terraform will make:
```bash
terraform plan
```
Execute actions proposed in Terraform plan: 
```bash
terraform apply
```
Destroy all cloud/container objects associated with a Terraform plan: 
```bash
terraform destroy
```
