// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Outputs
{

    [OutputType]
    public sealed class ContainerNetworkData
    {
        /// <summary>
        /// *Deprecated:* Use `network_data` instead. The network gateway of the container as read from its
        /// NetworkSettings.
        /// </summary>
        public readonly string? Gateway;
        /// <summary>
        /// *Deprecated:* Use `network_data` instead. The IP address of the container's first network it.
        /// </summary>
        public readonly string? IpAddress;
        /// <summary>
        /// *Deprecated:* Use `network_data` instead. The IP prefix length of the container as read from its
        /// NetworkSettings.
        /// </summary>
        public readonly int? IpPrefixLength;
        public readonly string? NetworkName;

        [OutputConstructor]
        private ContainerNetworkData(
            string? gateway,

            string? ipAddress,

            int? ipPrefixLength,

            string? networkName)
        {
            Gateway = gateway;
            IpAddress = ipAddress;
            IpPrefixLength = ipPrefixLength;
            NetworkName = networkName;
        }
    }
}
