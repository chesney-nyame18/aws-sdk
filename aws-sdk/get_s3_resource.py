import boto3

def aws_get_s3_resource(credentials_profile):
    if (credentials_profile):
        boto3.setup_default_session(profile_name=credentials_profile)
    s3_resource = boto3.resource('s3')
    
    return s3_resource
