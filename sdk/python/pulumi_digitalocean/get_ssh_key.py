# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetSshKeyResult:
    """
    A collection of values returned by getSshKey.
    """
    def __init__(__self__, fingerprint=None, name=None, public_key=None, id=None):
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        __self__.fingerprint = fingerprint
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        __self__.public_key = public_key
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetSshKeyResult(GetSshKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshKeyResult(
            fingerprint=self.fingerprint,
            name=self.name,
            public_key=self.public_key,
            id=self.id)

def get_ssh_key(name=None,opts=None):
    """
    Use this data source to access information about an existing resource.
    
    :param str name: The name of the ssh key.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/ssh_key.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getSshKey:getSshKey', __args__, opts=opts).value

    return AwaitableGetSshKeyResult(
        fingerprint=__ret__.get('fingerprint'),
        name=__ret__.get('name'),
        public_key=__ret__.get('publicKey'),
        id=__ret__.get('id'))
