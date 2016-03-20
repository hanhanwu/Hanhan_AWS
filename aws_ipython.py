# The code ins written in different cells in IPython on AWS

# cell 1: check boto3 works and can read S3 bucket
import boto3
import botocore

s3 = boto3.resource('s3')
bucket = s3.Bucket('[your bucket name]')
exists = True
try:
    s3.meta.client.head_bucket(Bucket='[your bucket name]')
except botocore.exceptions.ClientError as e:
    # If a client error is thrown, then check that it was a 404 error.
    # If it was a 404 error, then the bucket does not exist.
    error_code = int(e.response['Error']['Code'])
    if error_code == 404:
        exists = False
        
        
# cell 2: download the s3 file to local
s3.Object('[your bucket name]', '[your zip file name]').download_file('[your zip file name]')


# cell 3: read the .zip file and write the output into a .txt file, it will saved in AWS IPython
import zipfile

def has_key_word(key_word, line):
    if key_word in line.lower():
        return True
    return False

with zipfile.ZipFile('[your zip file name]', 'r') as z:
    with z.open('[your txt file name]') as f:
        for line in f:
            if has_key_word('[a key word]', line):
                with open('[your txt file name]', 'a') as the_file:
                    the_file.write(line+'\n')


# cell 4: upload your generated txt file to S3
s3.Object('[your S3 bucket name]', '[your txt file name]').put(Body=open('[your txt file name]', 'rb'))


# cell 5: check your files in S3 through your AWS IPython
for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        print(key.key)
