# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Firewall(pulumi.CustomResource):
    created_at: pulumi.Output[str]
    """
    A time value given in ISO8601 combined date and time format
    that represents when the Firewall was created.
    """
    droplet_ids: pulumi.Output[list]
    """
    The list of the IDs of the Droplets assigned
    to the Firewall.
    """
    inbound_rules: pulumi.Output[list]
    """
    The inbound access rule block for the Firewall.
    The `inbound_rule` block is documented below.
    
      * `portRange` (`str`) - The ports on which traffic will be allowed
        specified as a string containing a single port, a range (e.g. "8000-9000"),
        or "1-65535" to open all ports for a protocol. Required for when protocol is
        `tcp` or `udp`.
      * `protocol` (`str`) - The type of traffic to be allowed.
        This may be one of "tcp", "udp", or "icmp".
      * `sourceAddresses` (`list`) - An array of strings containing the IPv4
        addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs from which the
        inbound traffic will be accepted.
      * `sourceDropletIds` (`list`) - An array containing the IDs of
        the Droplets from which the inbound traffic will be accepted.
      * `sourceLoadBalancerUids` (`list`) - An array containing the IDs
        of the Load Balancers from which the inbound traffic will be accepted.
      * `sourceTags` (`list`) - An array containing the names of Tags
        corresponding to groups of Droplets from which the inbound traffic
        will be accepted.
    """
    name: pulumi.Output[str]
    """
    The Firewall name
    """
    outbound_rules: pulumi.Output[list]
    """
    The outbound access rule block for the Firewall.
    The `outbound_rule` block is documented below.
    
      * `destinationAddresses` (`list`) - An array of strings containing the IPv4
        addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the
        outbound traffic will be allowed.
      * `destinationDropletIds` (`list`) - An array containing the IDs of
        the Droplets to which the outbound traffic will be allowed.
      * `destinationLoadBalancerUids` (`list`) - An array containing the IDs
        of the Load Balancers to which the outbound traffic will be allowed.
      * `destinationTags` (`list`) - An array containing the names of Tags
        corresponding to groups of Droplets to which the outbound traffic will
        be allowed.
        traffic.
      * `portRange` (`str`) - The ports on which traffic will be allowed
        specified as a string containing a single port, a range (e.g. "8000-9000"),
        or "1-65535" to open all ports for a protocol. Required for when protocol is
        `tcp` or `udp`.
      * `protocol` (`str`) - The type of traffic to be allowed.
        This may be one of "tcp", "udp", or "icmp".
    """
    pending_changes: pulumi.Output[list]
    """
    An list of object containing the fields, "droplet_id",
    "removing", and "status".  It is provided to detail exactly which Droplets
    are having their security policies updated.  When empty, all changes
    have been successfully applied.
    
      * `droplet_id` (`float`)
      * `removing` (`bool`)
      * `status` (`str`) - A status string indicating the current state of the Firewall.
        This can be "waiting", "succeeded", or "failed".
    """
    status: pulumi.Output[str]
    """
    A status string indicating the current state of the Firewall.
    This can be "waiting", "succeeded", or "failed".
    """
    tags: pulumi.Output[list]
    """
    The names of the Tags assigned to the Firewall.
    """
    def __init__(__self__, resource_name, opts=None, droplet_ids=None, inbound_rules=None, name=None, outbound_rules=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a DigitalOcean Cloud Firewall resource. This can be used to create,
        modify, and delete Firewalls.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] droplet_ids: The list of the IDs of the Droplets assigned
               to the Firewall.
        :param pulumi.Input[list] inbound_rules: The inbound access rule block for the Firewall.
               The `inbound_rule` block is documented below.
        :param pulumi.Input[str] name: The Firewall name
        :param pulumi.Input[list] outbound_rules: The outbound access rule block for the Firewall.
               The `outbound_rule` block is documented below.
        :param pulumi.Input[list] tags: The names of the Tags assigned to the Firewall.
        
        The **inbound_rules** object supports the following:
        
          * `portRange` (`pulumi.Input[str]`) - The ports on which traffic will be allowed
            specified as a string containing a single port, a range (e.g. "8000-9000"),
            or "1-65535" to open all ports for a protocol. Required for when protocol is
            `tcp` or `udp`.
          * `protocol` (`pulumi.Input[str]`) - The type of traffic to be allowed.
            This may be one of "tcp", "udp", or "icmp".
          * `sourceAddresses` (`pulumi.Input[list]`) - An array of strings containing the IPv4
            addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs from which the
            inbound traffic will be accepted.
          * `sourceDropletIds` (`pulumi.Input[list]`) - An array containing the IDs of
            the Droplets from which the inbound traffic will be accepted.
          * `sourceLoadBalancerUids` (`pulumi.Input[list]`) - An array containing the IDs
            of the Load Balancers from which the inbound traffic will be accepted.
          * `sourceTags` (`pulumi.Input[list]`) - An array containing the names of Tags
            corresponding to groups of Droplets from which the inbound traffic
            will be accepted.
        
        The **outbound_rules** object supports the following:
        
          * `destinationAddresses` (`pulumi.Input[list]`) - An array of strings containing the IPv4
            addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the
            outbound traffic will be allowed.
          * `destinationDropletIds` (`pulumi.Input[list]`) - An array containing the IDs of
            the Droplets to which the outbound traffic will be allowed.
          * `destinationLoadBalancerUids` (`pulumi.Input[list]`) - An array containing the IDs
            of the Load Balancers to which the outbound traffic will be allowed.
          * `destinationTags` (`pulumi.Input[list]`) - An array containing the names of Tags
            corresponding to groups of Droplets to which the outbound traffic will
            be allowed.
            traffic.
          * `portRange` (`pulumi.Input[str]`) - The ports on which traffic will be allowed
            specified as a string containing a single port, a range (e.g. "8000-9000"),
            or "1-65535" to open all ports for a protocol. Required for when protocol is
            `tcp` or `udp`.
          * `protocol` (`pulumi.Input[str]`) - The type of traffic to be allowed.
            This may be one of "tcp", "udp", or "icmp".

        > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/firewall.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['droplet_ids'] = droplet_ids
            __props__['inbound_rules'] = inbound_rules
            __props__['name'] = name
            __props__['outbound_rules'] = outbound_rules
            __props__['tags'] = tags
            __props__['created_at'] = None
            __props__['pending_changes'] = None
            __props__['status'] = None
        super(Firewall, __self__).__init__(
            'digitalocean:index/firewall:Firewall',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, created_at=None, droplet_ids=None, inbound_rules=None, name=None, outbound_rules=None, pending_changes=None, status=None, tags=None):
        """
        Get an existing Firewall resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: A time value given in ISO8601 combined date and time format
               that represents when the Firewall was created.
        :param pulumi.Input[list] droplet_ids: The list of the IDs of the Droplets assigned
               to the Firewall.
        :param pulumi.Input[list] inbound_rules: The inbound access rule block for the Firewall.
               The `inbound_rule` block is documented below.
        :param pulumi.Input[str] name: The Firewall name
        :param pulumi.Input[list] outbound_rules: The outbound access rule block for the Firewall.
               The `outbound_rule` block is documented below.
        :param pulumi.Input[list] pending_changes: An list of object containing the fields, "droplet_id",
               "removing", and "status".  It is provided to detail exactly which Droplets
               are having their security policies updated.  When empty, all changes
               have been successfully applied.
        :param pulumi.Input[str] status: A status string indicating the current state of the Firewall.
               This can be "waiting", "succeeded", or "failed".
        :param pulumi.Input[list] tags: The names of the Tags assigned to the Firewall.
        
        The **inbound_rules** object supports the following:
        
          * `portRange` (`pulumi.Input[str]`) - The ports on which traffic will be allowed
            specified as a string containing a single port, a range (e.g. "8000-9000"),
            or "1-65535" to open all ports for a protocol. Required for when protocol is
            `tcp` or `udp`.
          * `protocol` (`pulumi.Input[str]`) - The type of traffic to be allowed.
            This may be one of "tcp", "udp", or "icmp".
          * `sourceAddresses` (`pulumi.Input[list]`) - An array of strings containing the IPv4
            addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs from which the
            inbound traffic will be accepted.
          * `sourceDropletIds` (`pulumi.Input[list]`) - An array containing the IDs of
            the Droplets from which the inbound traffic will be accepted.
          * `sourceLoadBalancerUids` (`pulumi.Input[list]`) - An array containing the IDs
            of the Load Balancers from which the inbound traffic will be accepted.
          * `sourceTags` (`pulumi.Input[list]`) - An array containing the names of Tags
            corresponding to groups of Droplets from which the inbound traffic
            will be accepted.
        
        The **outbound_rules** object supports the following:
        
          * `destinationAddresses` (`pulumi.Input[list]`) - An array of strings containing the IPv4
            addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the
            outbound traffic will be allowed.
          * `destinationDropletIds` (`pulumi.Input[list]`) - An array containing the IDs of
            the Droplets to which the outbound traffic will be allowed.
          * `destinationLoadBalancerUids` (`pulumi.Input[list]`) - An array containing the IDs
            of the Load Balancers to which the outbound traffic will be allowed.
          * `destinationTags` (`pulumi.Input[list]`) - An array containing the names of Tags
            corresponding to groups of Droplets to which the outbound traffic will
            be allowed.
            traffic.
          * `portRange` (`pulumi.Input[str]`) - The ports on which traffic will be allowed
            specified as a string containing a single port, a range (e.g. "8000-9000"),
            or "1-65535" to open all ports for a protocol. Required for when protocol is
            `tcp` or `udp`.
          * `protocol` (`pulumi.Input[str]`) - The type of traffic to be allowed.
            This may be one of "tcp", "udp", or "icmp".
        
        The **pending_changes** object supports the following:
        
          * `droplet_id` (`pulumi.Input[float]`)
          * `removing` (`pulumi.Input[bool]`)
          * `status` (`pulumi.Input[str]`) - A status string indicating the current state of the Firewall.
            This can be "waiting", "succeeded", or "failed".

        > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/firewall.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["created_at"] = created_at
        __props__["droplet_ids"] = droplet_ids
        __props__["inbound_rules"] = inbound_rules
        __props__["name"] = name
        __props__["outbound_rules"] = outbound_rules
        __props__["pending_changes"] = pending_changes
        __props__["status"] = status
        __props__["tags"] = tags
        return Firewall(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

