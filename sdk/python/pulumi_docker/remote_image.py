# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class RemoteImage(pulumi.CustomResource):
    keep_locally: pulumi.Output[bool]
    """
    If true, then the Docker image won't be
    deleted on destroy operation. If this is false, it will delete the image from
    the docker local storage on destroy operation.
    """
    latest: pulumi.Output[str]
    name: pulumi.Output[str]
    """
    The name of the Docker image, including any tags or SHA256 repo digests.
    """
    pull_trigger: pulumi.Output[str]
    """
    **Deprecated**, use `pull_triggers` instead.
    """
    pull_triggers: pulumi.Output[list]
    """
    List of values which cause an
    image pull when changed. This is used to store the image digest from the
    registry when using the `getRegistryImage` [data source](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
    to trigger an image update.
    """
    def __init__(__self__, resource_name, opts=None, keep_locally=None, name=None, pull_trigger=None, pull_triggers=None, __props__=None, __name__=None, __opts__=None):
        """
        Pulls a Docker image to a given Docker host from a Docker Registry.

        This resource will *not* pull new layers of the image automatically unless used in
        conjunction with [`getRegistryImage`](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
        data source to update the `pull_triggers` field.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        # Find the latest Ubuntu precise image.
        ubuntu = docker.RemoteImage("ubuntu", name="ubuntu:precise")
        ```
        ### Dynamic image

        ```python
        import pulumi
        import pulumi_docker as docker

        ubuntu_registry_image = docker.get_registry_image(name="ubuntu:precise")
        ubuntu_remote_image = docker.RemoteImage("ubuntuRemoteImage",
            name=ubuntu_registry_image.name,
            pull_triggers=[ubuntu_registry_image.sha256_digest])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] keep_locally: If true, then the Docker image won't be
               deleted on destroy operation. If this is false, it will delete the image from
               the docker local storage on destroy operation.
        :param pulumi.Input[str] name: The name of the Docker image, including any tags or SHA256 repo digests.
        :param pulumi.Input[str] pull_trigger: **Deprecated**, use `pull_triggers` instead.
        :param pulumi.Input[list] pull_triggers: List of values which cause an
               image pull when changed. This is used to store the image digest from the
               registry when using the `getRegistryImage` [data source](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
               to trigger an image update.
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

            __props__['keep_locally'] = keep_locally
            if name is None:
                raise TypeError("Missing required property 'name'")
            __props__['name'] = name
            if pull_trigger is not None:
                warnings.warn("Use field pull_triggers instead", DeprecationWarning)
                pulumi.log.warn("pull_trigger is deprecated: Use field pull_triggers instead")
            __props__['pull_trigger'] = pull_trigger
            __props__['pull_triggers'] = pull_triggers
            __props__['latest'] = None
        super(RemoteImage, __self__).__init__(
            'docker:index/remoteImage:RemoteImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, keep_locally=None, latest=None, name=None, pull_trigger=None, pull_triggers=None):
        """
        Get an existing RemoteImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] keep_locally: If true, then the Docker image won't be
               deleted on destroy operation. If this is false, it will delete the image from
               the docker local storage on destroy operation.
        :param pulumi.Input[str] name: The name of the Docker image, including any tags or SHA256 repo digests.
        :param pulumi.Input[str] pull_trigger: **Deprecated**, use `pull_triggers` instead.
        :param pulumi.Input[list] pull_triggers: List of values which cause an
               image pull when changed. This is used to store the image digest from the
               registry when using the `getRegistryImage` [data source](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
               to trigger an image update.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["keep_locally"] = keep_locally
        __props__["latest"] = latest
        __props__["name"] = name
        __props__["pull_trigger"] = pull_trigger
        __props__["pull_triggers"] = pull_triggers
        return RemoteImage(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
