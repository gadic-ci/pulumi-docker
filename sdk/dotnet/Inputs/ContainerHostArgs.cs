// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ContainerHostArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Hostname to add.
        /// </summary>
        [Input("host", required: true)]
        public Input<string> Host { get; set; } = null!;

        /// <summary>
        /// IP address this hostname should resolve to.
        /// </summary>
        [Input("ip", required: true)]
        public Input<string> Ip { get; set; } = null!;

        public ContainerHostArgs()
        {
        }
    }
}
