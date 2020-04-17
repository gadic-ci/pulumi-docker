// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class NetworkIpamConfigArgs : Pulumi.ResourceArgs
    {
        [Input("auxAddress")]
        private InputMap<object>? _auxAddress;
        public InputMap<object> AuxAddress
        {
            get => _auxAddress ?? (_auxAddress = new InputMap<object>());
            set => _auxAddress = value;
        }

        [Input("gateway")]
        public Input<string>? Gateway { get; set; }

        [Input("ipRange")]
        public Input<string>? IpRange { get; set; }

        [Input("subnet")]
        public Input<string>? Subnet { get; set; }

        public NetworkIpamConfigArgs()
        {
        }
    }
}
