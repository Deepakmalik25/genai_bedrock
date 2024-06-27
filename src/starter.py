import pprint   # for pretty printing
import sys      # for command line arguments
import os       # for file operations
import boto3    # for AWS S3 operations
import json     # for JSON operations
import time     # for time operations
import logging  # for logging


bedrock = boto3.client(
    service_name='bedrock',
    region_name='eu-central-1',)

pp = pprint.PrettyPrinter(depth=4)

models=bedrock.list_foundation_models()
for model in models['modelSummaries']:
    pp.pprint(models)