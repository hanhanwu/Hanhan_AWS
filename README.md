# Hanhan_AWS

### [EC2 Relevant Commands & Troubleshooting][1]

### Load S3 data
Check the code here: https://github.com/hanhanwu/Hanhan_AWS/blob/master/load_s3_data.py

### AWS Glue
* [Glue configuration][2]
  * Change worker numbers, worker type could improve the performance
* [Glue Pricing][3]

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


## AWS Training
* Don't quite like following the steps and lots of times, there were settings problems, not sure why am I creating all these settings. But, take a note of these training resources.
* Data Streaming and database: https://dataprocessing.wildrydes.com/streaming-aggregation.html
* Serverless workshops: https://github.com/aws-samples/aws-serverless-workshops

## AWS Sagemaker Training
* Sagemaker iPython Examples: https://github.com/awslabs/amazon-sagemaker-examples
* Hypterparam Tuning
  * Hyperparam tuning example: https://github.com/awslabs/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/xgboost_random_log/hpo_xgboost_random_log.ipynb
  * Analyze Hyper Tuning results example: https://github.com/awslabs/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/analyze_results/HPO_Analyze_TuningJob_Results.ipynb
    * Through AWS Sagemaker console, on the left side bar, there is "Hyperparameter Tuning", click on that to find the names of those jobs. You just need to replace the `tuning_job_name` here, and later `sage_client` will call `describe_hyper_parameter_tuning_job`
    * After hyperparam tuning, you can also create model with the optimized params, the instructor said you can just call `create_model` through `sage_client` with the `tuning_job_name`, didn't try this
  * Model deployment example: https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/random_cut_forest/random_cut_forest.ipynb
    * `Inference` will deploy the model you have trained. 
      * It also supports AB deployment. Deploy 1 version on production, test other version(s) on staging environment
    * "billable seconds" shows how much time you need to pay for
    * "endpoint configuration"
      * It's where you can check deployment progress
      * delete the endnpoint throgh notebook, otherwise you need to pay more
  * Save iPython notebook in "SageMaker" folder, if you save things in home directory, after restart, everything will be gone.
  * Elastic Inference example: https://github.com/awslabs/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/tensorflow_serving_using_elastic_inference_with_your_own_model/tensorflow_serving_pretrained_model_elastic_inference.ipynb
    * In sagemaker, 10% cost is training model, 90% is inference deployment. 
    * "Amazon Elastic Inference (EI) is a resource you can attach to your Amazon EC2 instances to accelerate your deep learning (DL) inference workloads. EI allows you to add inference acceleration to an Amazon SageMaker hosted endpoint or Jupyter notebook for a fraction of the cost of using a full GPU instance." Especially useful in deep learning.
    * `accelerator_type='ml.eia1.medium'` in deploy function, you can also choose large accelerator type
  * Ground Truth example: https://github.com/aws-samples/sagemaker-horovod-distributed-training/blob/master/notebooks/GndTruth/from_unlabeled_data_to_deployed_machine_learning_model_ground_truth_demo_image_classification.ipynb
    * Ground Truth is a tool that allows human to label some of the data, normally that's the low confidence records after model training.
  * Reinforcement example: https://github.com/awslabs/amazon-sagemaker-examples/blob/master/reinforcement_learning/rl_portfolio_management_coach_customEnv/rl_portfolio_management_coach_customEnv.ipynb
  * Other info & resources
    * `boto 3`: it’s the AWS python SDK, through which you can all methods in python
    * Sagemaker SDK (where you check all the methods you can call)
https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/sagemaker.html
    * Params, support GPU/CPU, check https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html
    * Lambda is used to execute functions, 15 mins time limit, better to be used for short time execution. When lambda is not available, better to use step function, but not everything can be achieved through step function for now.
    
## Training - Process Model: CRISP-DM on the AWS Stack
### Data Understanding Tools
* S3 raw data ->  Glue stores schema only -> Athena do SQL query for basic analysis -> QuickSight for visualization
### Data Preparation & Modeling
* To make it simple, you can just use EC2 + Ipython, even no need above data understanding tools
* They also suggest
  * EMR + Spark
  * EC2 + Deep Learning AMI
### Planning Deployment
* Runtime
  * Amazon EC2
  * Amazon EC2 Container Service
  * AWS Lambda
* Infrastructure Deployment
  * AWS CloudFormation
  * AWS OpsWorks
  * AWS Elastic Beanstalk
* Code Management
  * AWS CodeCommit
  * AWS CodePipeline
  * AWS Elastic Beanstalk
* Monitoring
  * Amazon CloudWatch
  * AWS CloudTrail
  * AWS Elastic Beanstalk
  
## Training - Developing Machine Learning Applications
* SageMaker Neo
  * Neo is a new capability of Amazon SageMaker that enables machine learning models to train once and run anywhere in the cloud and at the edge.
  * Neo Compilation IPython Examples: https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_neo_compilation_jobs


[1]:https://github.com/hanhanwu/Basic_But_Useful/blob/master/RA_command_lines.md#aws-ec2-troubleshooting
[2]:https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html
[3]:https://aws.amazon.com/glue/pricing/
