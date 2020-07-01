# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetRegistryImageResult:
    """
    A collection of values returned by getRegistryImage.
    """
    def __init__(__self__, id=None, name=None, sha256_digest=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if sha256_digest and not isinstance(sha256_digest, str):
            raise TypeError("Expected argument 'sha256_digest' to be a str")
        __self__.sha256_digest = sha256_digest
class AwaitableGetRegistryImageResult(GetRegistryImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryImageResult(
            id=self.id,
            name=self.name,
            sha256_digest=self.sha256_digest)

def get_registry_image(name=None,opts=None):
    """
    Reads the image metadata from a Docker Registry. Used in conjunction with the
    [docker\_image](https://www.terraform.io/docs/providers/docker/r/image.html) resource to keep an image up
    to date on the latest available version of the tag.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_docker as docker

    ubuntu_registry_image = docker.get_registry_image(name="ubuntu:precise")
    ubuntu_remote_image = docker.RemoteImage("ubuntuRemoteImage",
        name=ubuntu_registry_image.name,
        pull_triggers=[ubuntu_registry_image.sha256_digest])
    ```


    :param str name: The name of the Docker image, including any tags. e.g. `alpine:latest`
    """
    __args__ = dict()


    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('docker:index/getRegistryImage:getRegistryImage', __args__, opts=opts).value

    return AwaitableGetRegistryImageResult(
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        sha256_digest=__ret__.get('sha256Digest'))
