// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ServiceTaskSpecPlacementPlatformArgs : Pulumi.ResourceArgs
    {
        [Input("architecture", required: true)]
        public Input<string> Architecture { get; set; } = null!;

        [Input("os", required: true)]
        public Input<string> Os { get; set; } = null!;

        public ServiceTaskSpecPlacementPlatformArgs()
        {
        }
    }
}
