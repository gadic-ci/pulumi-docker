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
    public sealed class ServiceTaskSpec
    {
        /// <summary>
        /// See ContainerSpec below for details.
        /// </summary>
        public readonly Outputs.ServiceTaskSpecContainerSpec ContainerSpec;
        /// <summary>
        /// A counter that triggers an update even if no relevant parameters have been changed. See [Docker Spec](https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126).
        /// </summary>
        public readonly int? ForceUpdate;
        /// <summary>
        /// See Log Driver below for details.
        /// </summary>
        public readonly Outputs.ServiceTaskSpecLogDriver? LogDriver;
        /// <summary>
        /// Ids of the networks in which the container will be put in.
        /// </summary>
        public readonly ImmutableArray<string> Networks;
        /// <summary>
        /// See Placement below for details.
        /// </summary>
        public readonly Outputs.ServiceTaskSpecPlacement? Placement;
        /// <summary>
        /// See Resources below for details.
        /// </summary>
        public readonly Outputs.ServiceTaskSpecResources? Resources;
        /// <summary>
        /// See Restart Policy below for details.
        /// </summary>
        public readonly Outputs.ServiceTaskSpecRestartPolicy? RestartPolicy;
        /// <summary>
        /// Runtime is the type of runtime specified for the task executor. See [Docker Runtime](https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go).
        /// </summary>
        public readonly string? Runtime;

        [OutputConstructor]
        private ServiceTaskSpec(
            Outputs.ServiceTaskSpecContainerSpec containerSpec,

            int? forceUpdate,

            Outputs.ServiceTaskSpecLogDriver? logDriver,

            ImmutableArray<string> networks,

            Outputs.ServiceTaskSpecPlacement? placement,

            Outputs.ServiceTaskSpecResources? resources,

            Outputs.ServiceTaskSpecRestartPolicy? restartPolicy,

            string? runtime)
        {
            ContainerSpec = containerSpec;
            ForceUpdate = forceUpdate;
            LogDriver = logDriver;
            Networks = networks;
            Placement = placement;
            Resources = resources;
            RestartPolicy = restartPolicy;
            Runtime = runtime;
        }
    }
}