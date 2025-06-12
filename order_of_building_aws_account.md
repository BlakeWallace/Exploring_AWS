#Instructions for starting out with a new AWS account.

1. **Set up an AWS account and create an administrator user** -  
[Set up an AWS account and create an administrator user](https://docs.aws.amazon.com/streams/latest/dev/setting-up.html#:~:text=To%20create%20an%20IAM%20user,and%20AWS%20Management%20Console%20access.)  
[Create an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)  
https://324037306813.signin.aws.amazon.com/console/  
   
    1. Create an account - Initially a Root User account
    1. Create an administrator user for yourself.  This makes it possible to avoid using the Root User credentials for each login.

1. **Set up the AWS Command Line Interface (AWS CLI)** -  
[Set up the AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/streams/latest/dev/setup-awscli.html)  
[awscli](https://pypi.org/project/awscli/)  
[Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)  
[Setting up the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)  
    1. open terminal
        1. run `aws --version`
        1. if it isn't found, run the following:
            1. `curl "https://awscli.amazonaws.com/AWSCLIV2-2.16.12.pkg" -o "AWSCLIV2.pkg"`
            1. `sudo installer -pkg ./AWSCLIV2.pkg -target /`
                1. if this does not work in the current virtualenv, deactivate the env and run the command as the superuser.  Then check to see that the correct version of aws is available from the activated virtualenv.
        1. Create access tokens
        1. Enable IAM Identity Center or IAM Instance
        1. https://d-9a67624af5.awsapps.com/start <- AWS access portal URL
        1. run `aws configure` to set access tokens and start url value
      
1. Instanciate an EC2 instance
    1. Instantiate Instance
        1. Current instructions are for an Ubuntu instance
        2. [visit](https://us-east-2.console.aws.amazon.com/ec2/home?region=us-east-2#Instances)
        3. Select: Launch Instances
        4. Name Instance
        5. Select AMI Ubuntu
        6. t2.micro is the Free Tier elegible instance
        7. Select/create a Key pair
        8. Configure Storage (If you stay at 8 GiGs, there will not be enough space to install Anaconda.  Up to 30 GiGs in the Free Tier.)
        9. Select Launch Instance
        10. Select Instances at the top of the page and refresh the Window
        11. Select the instance in the list
        12. Select Connect
        13. Open a terminal window and navigate to the directory housing the SSH pem key associated with the instance
        14. Run 'ssh -i "\<private_key>.pem" \<instance_type>@\<DNS>'
        15. "The authenticity of host 'ec2-3-17-80-93.us-east-2.compute.amazonaws.com (3.17.80.93)' can't be established. ECDSA key fingerprint is SHA256:E1uSoPJNRL2SDNm3UghhhuY77/tgJm8sicZIUVyAnDQ.  Are you sure you want to continue connecting (yes/no)?" - Type: **yes** 

    1. Anaconda install
        1. Run "sudo apt update"
        1. Run "wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh" (2024.10-1 is the version in this example)
        1. Run "bash Anaconda3-2024.10-1-Linux-x86_64.sh"
            1. Hit "Enter, ctrl+C," then "Enter"
            1. Type: "yes," and hit "Enter"
            1. Hit "Enter" to confirm the name of the directory where Anaconda will be stored
        1. Try: "conda create -n data scipy"
            1. If conda cannot be found then conda must be added to the PATH
            1. These instructions are from the Medium post [here](https://medium.com/@sawepeter6/conda-command-not-found-ac28bea24291#:~:text=The%20%E2%80%9Cconda%20command%20not%20found,to%20add%20the%20PATH%20manually.)  
                1. ls - to check that Anaconda has been installed
                1. ls ~/anaconda3/bin - check to see is conda is in this list
                1. nano ~/.bashrc - open the system directory
                1. export PATH=~/anaconda3/bin:$PATH - add this line to the end of the file
                1. Hit ctrl+X, y, Enter
                1. source ~/.bashrc - apply the changes 
                1. conda create -n data scipy ...
                1. conda activate data
                1. conda install jupyter python numpy pandas matplotlib

    1. Connect to the instance in your browser using jupyter
        1. Run jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser
        1. Open new terminal window
        1. Navigate to the directory housing the ssh key
        1. Run ssh -i \<key> -N -f -L 8888:localhost:8888 ubuntu@\<DNS>
        1. Open browser and go to localhost:8888
        1. enter the Token

    1. Push information from computer into EC2 instance
        1. Navigate to the directory housing the .pem file
        1. run "scp -i ~/Downloads/file.pem local_image_file user@ec2_elastic_ip:/home/user/images/" substituting appropriate elements
           