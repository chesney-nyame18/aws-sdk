import boto3

def aws_get_s3_client(credentials_profile):
    if (credentials_profile):
        boto3.setup_default_session(profile_name=credentials_profile)
    s3_client = boto3.client('s3')
    
    return s3_client
