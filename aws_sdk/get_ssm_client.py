import boto3

def aws_get_ssm_client(credentials_profile, region_name):
    if (credentials_profile):
        boto3.setup_default_session(profile_name=credentials_profile)
    ssm_client = boto3.client('ssm',region_name=region_name)
    
    return ssm_client
