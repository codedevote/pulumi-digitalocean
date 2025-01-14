# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

__config__ = pulumi.Config('digitalocean')

api_endpoint = __config__.get('apiEndpoint') or (utilities.get_env('DIGITALOCEAN_API_URL') or 'https://api.digitalocean.com')
"""
The URL to use for the DigitalOcean API.
"""

spaces_access_id = __config__.get('spacesAccessId') or utilities.get_env('SPACES_ACCESS_KEY_ID')
"""
The access key ID for Spaces API operations.
"""

spaces_secret_key = __config__.get('spacesSecretKey') or utilities.get_env('SPACES_SECRET_ACCESS_KEY')
"""
The secret access key for Spaces API operations.
"""

token = __config__.get('token') or utilities.get_env('DIGITALOCEAN_TOKEN')
"""
The token key for API operations.
"""

