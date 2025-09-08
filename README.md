# Automation_OPENPR
This PR introduces a Python script that automates the workflow of reviewing Simulink models linked to GitHub pull requests.

# What you need first?

**download gh cli**

https://cli.github.com/


**auth gh cli in your git bash**

put in git terminal:

gh.exe auth login

follow the proccess through web when asked


**have python in your computer**

https://www.python.org/


**considering that you already have matlab, run these commands in git bash to test the resources**

gh --version
python --version


**ok, good to go**


**get a pr from your choice that has a .slx or .sldd as changes**


**run in git bash**

python \c\...\yourpath\script.py <your_pr_url>


**if you want a smaller command, must do first**

nano ~/.bashrc

inside of it, put: alias openpr='python /c/...yourpath/script.py'

ctrl+O then ctrl+X

source ~/.bashrc


**OK, now you can just put in terminal**

openpr <your_pr_url>



