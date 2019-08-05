# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class DatabaseCluster(pulumi.CustomResource):
    database: pulumi.Output[str]
    """
    Name of the cluster's default database.
    """
    engine: pulumi.Output[str]
    """
    Database engine used by the cluster (ex. `pg` for PostreSQL).
    """
    host: pulumi.Output[str]
    """
    Database cluster's hostname.
    """
    maintenance_windows: pulumi.Output[list]
    """
    Defines when the automatic maintenance should be performed for the database cluster.
    """
    name: pulumi.Output[str]
    """
    The name of the database cluster.
    """
    node_count: pulumi.Output[float]
    """
    Number of nodes that will be included in the cluster.
    """
    password: pulumi.Output[str]
    """
    Password for the cluster's default user.
    """
    port: pulumi.Output[float]
    """
    Network port that the database cluster is listening on.
    """
    region: pulumi.Output[str]
    """
    DigitalOcean region where the cluster will reside.
    """
    size: pulumi.Output[str]
    """
    Database droplet size associated with the cluster (ex. `db-s-1vcpu-1gb`).
    """
    uri: pulumi.Output[str]
    """
    The full URI for connecting to the database cluster.
    """
    urn: pulumi.Output[str]
    """
    The uniform resource name of the database cluster.
    """
    user: pulumi.Output[str]
    """
    Username for the cluster's default user.
    """
    version: pulumi.Output[str]
    """
    Engine version used by the cluster (ex. `11` for PostgreSQL 11).
    """
    def __init__(__self__, resource_name, opts=None, engine=None, maintenance_windows=None, name=None, node_count=None, region=None, size=None, version=None, __name__=None, __opts__=None):
        """
        Provides a DigitalOcean database cluster resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] engine: Database engine used by the cluster (ex. `pg` for PostreSQL).
        :param pulumi.Input[list] maintenance_windows: Defines when the automatic maintenance should be performed for the database cluster.
        :param pulumi.Input[str] name: The name of the database cluster.
        :param pulumi.Input[float] node_count: Number of nodes that will be included in the cluster.
        :param pulumi.Input[str] region: DigitalOcean region where the cluster will reside.
        :param pulumi.Input[str] size: Database droplet size associated with the cluster (ex. `db-s-1vcpu-1gb`).
        :param pulumi.Input[str] version: Engine version used by the cluster (ex. `11` for PostgreSQL 11).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/database_cluster.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if engine is None:
            raise TypeError("Missing required property 'engine'")
        __props__['engine'] = engine

        __props__['maintenance_windows'] = maintenance_windows

        __props__['name'] = name

        if node_count is None:
            raise TypeError("Missing required property 'node_count'")
        __props__['node_count'] = node_count

        if region is None:
            raise TypeError("Missing required property 'region'")
        __props__['region'] = region

        if size is None:
            raise TypeError("Missing required property 'size'")
        __props__['size'] = size

        if version is None:
            raise TypeError("Missing required property 'version'")
        __props__['version'] = version

        __props__['database'] = None
        __props__['host'] = None
        __props__['password'] = None
        __props__['port'] = None
        __props__['uri'] = None
        __props__['urn'] = None
        __props__['user'] = None

        super(DatabaseCluster, __self__).__init__(
            'digitalocean:index/databaseCluster:DatabaseCluster',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

