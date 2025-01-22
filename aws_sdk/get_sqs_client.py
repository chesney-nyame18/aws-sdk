import boto3

def aws_get_sqs_client(credentials_profile):
    if (credentials_profile):
        boto3.setup_default_session(profile_name=credentials_profile)
    ssm_client = boto3.client('sqs')
    
    return ssm_client
