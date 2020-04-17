// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package docker

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Reads the image metadata from a Docker Registry. Used in conjunction with the
// [docker\_image](https://www.terraform.io/docs/providers/docker/r/image.html) resource to keep an image up
// to date on the latest available version of the tag.
func GetRegistryImage(ctx *pulumi.Context, args *GetRegistryImageArgs, opts ...pulumi.InvokeOption) (*GetRegistryImageResult, error) {
	var rv GetRegistryImageResult
	err := ctx.Invoke("docker:index/getRegistryImage:getRegistryImage", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRegistryImage.
type GetRegistryImageArgs struct {
	// The name of the Docker image, including any tags. e.g. `alpine:latest`
	Name *string `pulumi:"name"`
}

// A collection of values returned by getRegistryImage.
type GetRegistryImageResult struct {
	// id is the provider-assigned unique ID for this managed resource.
	Id           string  `pulumi:"id"`
	Name         *string `pulumi:"name"`
	Sha256Digest string  `pulumi:"sha256Digest"`
}
