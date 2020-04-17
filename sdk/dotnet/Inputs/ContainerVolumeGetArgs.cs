// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ContainerVolumeGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The path in the container where the
        /// device will be binded.
        /// </summary>
        [Input("containerPath")]
        public Input<string>? ContainerPath { get; set; }

        /// <summary>
        /// The container where the volume is
        /// coming from.
        /// </summary>
        [Input("fromContainer")]
        public Input<string>? FromContainer { get; set; }

        /// <summary>
        /// The path on the host where the device
        /// is located.
        /// </summary>
        [Input("hostPath")]
        public Input<string>? HostPath { get; set; }

        /// <summary>
        /// If true, this volume will be readonly.
        /// Defaults to false.
        /// </summary>
        [Input("readOnly")]
        public Input<bool>? ReadOnly { get; set; }

        /// <summary>
        /// The name of the docker volume which
        /// should be mounted.
        /// </summary>
        [Input("volumeName")]
        public Input<string>? VolumeName { get; set; }

        public ContainerVolumeGetArgs()
        {
        }
    }
}
