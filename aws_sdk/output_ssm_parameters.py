import logging
import sys
import boto3
import botocore

from aws_sdk import aws_get_ssm_client
from logging_setup import log_init

log = logging.getLogger(__name__)

def fetch_aws_parameters(ssm_client, ssm_path, environment, region_name):

    try:
        ssm_path_with_environment = "/{}/{}/".format(environment,ssm_path)
        log.info("Getting all parameters from: {}".format(ssm_path_with_environment))
        return_vals = dict()
        next_token = ' '
        while next_token is not None:
            
            response = ssm_client.get_parameters_by_path(Path=ssm_path_with_environment, WithDecryption=True, NextToken=next_token)
            
            for param in response['Parameters']:
                name = param['Name'][param['Name'].rfind('/')+1:].upper()
                log.debug("Found paramater: {}".format(name))
                return_vals[name] = param['Value']
            
            next_token = response.get('NextToken', None)

        return return_vals

    except Exception:
        log.exception("Failure getting parameters")
    return None

def output_aws_parameters(credentials_profile, ssm_path, environment, region_name, debug, plain_text_log):
    try:
        ssm_client = aws_get_ssm_client(credentials_profile, region_name)

        log_init(log, debug, plain_text_log, sys.stderr)

        parameters = fetch_aws_parameters(ssm_client, ssm_path, environment, region_name)

        write_export_commands_to_stdOut(parameters)
    except botocore.exceptions.ProfileNotFound as ProfileError:
        log.error("Profile: {} not found".format(credentials_profile))
    except Exception:
        log.exception()

def write_export_commands_to_stdOut(parameters):
    for name, value in parameters.items():
        print("export {}='{}'".format(name,value))
