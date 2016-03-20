# Hanhan_AWS
using AWS


* Create IPython Notebook on AWS
  1. I am following this link to create the IPython NoteBook (don't check that video, just copy the code in the webpage will keep you from more troubles):   http://blog.impiyush.me/2015/02/running-ipython-notebook-server-on-aws.html
  2. Make sure when you are modify the security-group, use the AWS launch-... one, NOT the new group created by yourself.

* Upload file into AWS S3 and read the file to my AWS IPython
  1. Upload the file to S3 is easy.
  2. When you are reading S3 data to your AWS IPython through boto3, after installing this library in your AWS EC2 instance terminal, you also need to modify AWS configure. Get the Access Key, Access ID from your AWS EC2 homepage, click the top right corner and you will find them.
  3. Then install AWS CLI and modify do "aws configure" like this: http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

* aws_ipython.py

