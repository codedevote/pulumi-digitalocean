# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetDropletResult:
    """
    A collection of values returned by getDroplet.
    """
    def __init__(__self__, backups=None, disk=None, image=None, ipv4_address=None, ipv4_address_private=None, ipv6=None, ipv6_address=None, ipv6_address_private=None, locked=None, memory=None, monitoring=None, name=None, price_hourly=None, price_monthly=None, private_networking=None, region=None, size=None, status=None, tags=None, urn=None, vcpus=None, volume_ids=None, id=None):
        if backups and not isinstance(backups, bool):
            raise TypeError("Expected argument 'backups' to be a bool")
        __self__.backups = backups
        """
        Whether backups are enabled.
        """
        if disk and not isinstance(disk, float):
            raise TypeError("Expected argument 'disk' to be a float")
        __self__.disk = disk
        """
        The size of the Droplets disk in GB.
        """
        if image and not isinstance(image, str):
            raise TypeError("Expected argument 'image' to be a str")
        __self__.image = image
        """
        The Droplet image ID or slug.
        """
        if ipv4_address and not isinstance(ipv4_address, str):
            raise TypeError("Expected argument 'ipv4_address' to be a str")
        __self__.ipv4_address = ipv4_address
        """
        The Droplets public IPv4 address
        """
        if ipv4_address_private and not isinstance(ipv4_address_private, str):
            raise TypeError("Expected argument 'ipv4_address_private' to be a str")
        __self__.ipv4_address_private = ipv4_address_private
        """
        The Droplets private IPv4 address
        """
        if ipv6 and not isinstance(ipv6, bool):
            raise TypeError("Expected argument 'ipv6' to be a bool")
        __self__.ipv6 = ipv6
        """
        Whether IPv6 is enabled.
        """
        if ipv6_address and not isinstance(ipv6_address, str):
            raise TypeError("Expected argument 'ipv6_address' to be a str")
        __self__.ipv6_address = ipv6_address
        """
        The Droplets public IPv6 address
        """
        if ipv6_address_private and not isinstance(ipv6_address_private, str):
            raise TypeError("Expected argument 'ipv6_address_private' to be a str")
        __self__.ipv6_address_private = ipv6_address_private
        """
        The Droplets private IPv6 address
        """
        if locked and not isinstance(locked, bool):
            raise TypeError("Expected argument 'locked' to be a bool")
        __self__.locked = locked
        """
        Whether the Droplet is locked.
        """
        if memory and not isinstance(memory, float):
            raise TypeError("Expected argument 'memory' to be a float")
        __self__.memory = memory
        """
        The amount of the Droplets memory in MB.
        """
        if monitoring and not isinstance(monitoring, bool):
            raise TypeError("Expected argument 'monitoring' to be a bool")
        __self__.monitoring = monitoring
        """
        Whether monitoring agent is installed.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if price_hourly and not isinstance(price_hourly, float):
            raise TypeError("Expected argument 'price_hourly' to be a float")
        __self__.price_hourly = price_hourly
        """
        Droplet hourly price.
        """
        if price_monthly and not isinstance(price_monthly, float):
            raise TypeError("Expected argument 'price_monthly' to be a float")
        __self__.price_monthly = price_monthly
        """
        Droplet monthly price.
        """
        if private_networking and not isinstance(private_networking, bool):
            raise TypeError("Expected argument 'private_networking' to be a bool")
        __self__.private_networking = private_networking
        """
        Whether private networks are enabled.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        The region the Droplet is running in.
        """
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        __self__.size = size
        """
        The unique slug that indentifies the type of Droplet.
        """
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        The status of the Droplet.
        """
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
        """
        A list of the tags associated to the Droplet.
        """
        if urn and not isinstance(urn, str):
            raise TypeError("Expected argument 'urn' to be a str")
        __self__.urn = urn
        """
        The uniform resource name of the Droplet
        """
        if vcpus and not isinstance(vcpus, float):
            raise TypeError("Expected argument 'vcpus' to be a float")
        __self__.vcpus = vcpus
        """
        The number of the Droplets virtual CPUs.
        """
        if volume_ids and not isinstance(volume_ids, list):
            raise TypeError("Expected argument 'volume_ids' to be a list")
        __self__.volume_ids = volume_ids
        """
        List of the IDs of each volumes attached to the Droplet.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_droplet(name=None,opts=None):
    __args__ = dict()

    __args__['name'] = name
    __ret__ = await pulumi.runtime.invoke('digitalocean:index/getDroplet:getDroplet', __args__, opts=opts)

    return GetDropletResult(
        backups=__ret__.get('backups'),
        disk=__ret__.get('disk'),
        image=__ret__.get('image'),
        ipv4_address=__ret__.get('ipv4Address'),
        ipv4_address_private=__ret__.get('ipv4AddressPrivate'),
        ipv6=__ret__.get('ipv6'),
        ipv6_address=__ret__.get('ipv6Address'),
        ipv6_address_private=__ret__.get('ipv6AddressPrivate'),
        locked=__ret__.get('locked'),
        memory=__ret__.get('memory'),
        monitoring=__ret__.get('monitoring'),
        name=__ret__.get('name'),
        price_hourly=__ret__.get('priceHourly'),
        price_monthly=__ret__.get('priceMonthly'),
        private_networking=__ret__.get('privateNetworking'),
        region=__ret__.get('region'),
        size=__ret__.get('size'),
        status=__ret__.get('status'),
        tags=__ret__.get('tags'),
        urn=__ret__.get('urn'),
        vcpus=__ret__.get('vcpus'),
        volume_ids=__ret__.get('volumeIds'),
        id=__ret__.get('id'))
