# Hanhan_AWS


### Create IPython Notebook on AWS
  1. I am following this link to create the IPython NoteBook (don't check that video, just copy the code in the webpage will keep you from more troubles):   http://blog.impiyush.me/2015/02/running-ipython-notebook-server-on-aws.html
  2. Make sure when you are modify the security-group, use the AWS launch-... one, NOT the new group created by yourself.

### Upload file into AWS S3 and read the file to my AWS IPython
  1. Upload the file to S3 is easy.
  2. When you are reading S3 data to your AWS IPython through boto3, after installing this library in your AWS EC2 instance terminal, you also need to modify AWS configure. Get the Access Key, Access ID from your AWS EC2 homepage, click the top right corner and you will find them.
  3. Then install AWS CLI and modify do "aws configure" like this: http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

### aws_ipython.py
  1. Create IPython NoteBook in AWS.
  2. Upload file to S3.
  3. Read S3 file to your AWS IPython and do some operations, the output is saved as .txt file.
  4. Upload your .txtx file to S3.
  5. Check the S3 files through AWS IPython.
  * <b>In fact, in jupyter notebook, we can just run aws command line to upload/download files from/into S3</b>
    * `aws --profile [profile_name] s3 cp ~/Desktop/my_file.csv s3://my_bucket/my_file.csv`, repalce "profile_name" with the profile name
    
### Choosing EC2 Instance
* EC2 Instances Types & Price: https://aws.amazon.com/ec2/instance-types/
  * Instances start with "m" are memory optimized, those start with "c" are computation optimized. When running the code multi-threading, the instance starts with "m" may work better than those start with "c"
