// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Digitalocean
{
    /// <summary>
    /// Provides a DigitalOcean Project resource.
    /// 
    /// Projects allow you to organize your resources into groups that fit the way you work.
    /// You can group resources (like Droplets, Spaces, Load Balancers, domains, and Floating IPs)
    /// in ways that align with the applications you host on DigitalOcean.
    /// 
    /// The following resources can be associated with a project:
    /// 
    /// * Droplet
    /// * Load Balancer
    /// * Domain
    /// * Volume
    /// * Floating IP
    /// * Spaces Bucket
    /// 
    /// **Note:** A Terrafrom managed project cannot be set as a default project.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/project.html.markdown.
    /// </summary>
    public partial class Project : Pulumi.CustomResource
    {
        /// <summary>
        /// the date and time when the project was created, (ISO8601)
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// the description of the project
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        /// </summary>
        [Output("environment")]
        public Output<string?> Environment { get; private set; } = null!;

        /// <summary>
        /// The name of the Project
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// the id of the project owner.
        /// </summary>
        [Output("ownerId")]
        public Output<int> OwnerId { get; private set; } = null!;

        /// <summary>
        /// the unique universal identifier of the project owner.
        /// </summary>
        [Output("ownerUuid")]
        public Output<string> OwnerUuid { get; private set; } = null!;

        /// <summary>
        /// the purpose of the project, (Default: "Web Application")
        /// </summary>
        [Output("purpose")]
        public Output<string?> Purpose { get; private set; } = null!;

        /// <summary>
        /// a list of uniform resource names (URNs) for the resources associated with the project
        /// </summary>
        [Output("resources")]
        public Output<ImmutableArray<string>> Resources { get; private set; } = null!;

        /// <summary>
        /// the date and time when the project was last updated, (ISO8601)
        /// </summary>
        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;


        /// <summary>
        /// Create a Project resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Project(string name, ProjectArgs? args = null, CustomResourceOptions? options = null)
            : base("digitalocean:index/project:Project", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Project(string name, Input<string> id, ProjectState? state = null, CustomResourceOptions? options = null)
            : base("digitalocean:index/project:Project", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Project resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Project Get(string name, Input<string> id, ProjectState? state = null, CustomResourceOptions? options = null)
        {
            return new Project(name, id, state, options);
        }
    }

    public sealed class ProjectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// the description of the project
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        /// </summary>
        [Input("environment")]
        public Input<string>? Environment { get; set; }

        /// <summary>
        /// The name of the Project
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// the purpose of the project, (Default: "Web Application")
        /// </summary>
        [Input("purpose")]
        public Input<string>? Purpose { get; set; }

        [Input("resources")]
        private InputList<string>? _resources;

        /// <summary>
        /// a list of uniform resource names (URNs) for the resources associated with the project
        /// </summary>
        public InputList<string> Resources
        {
            get => _resources ?? (_resources = new InputList<string>());
            set => _resources = value;
        }

        public ProjectArgs()
        {
        }
    }

    public sealed class ProjectState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// the date and time when the project was created, (ISO8601)
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// the description of the project
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        /// </summary>
        [Input("environment")]
        public Input<string>? Environment { get; set; }

        /// <summary>
        /// The name of the Project
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// the id of the project owner.
        /// </summary>
        [Input("ownerId")]
        public Input<int>? OwnerId { get; set; }

        /// <summary>
        /// the unique universal identifier of the project owner.
        /// </summary>
        [Input("ownerUuid")]
        public Input<string>? OwnerUuid { get; set; }

        /// <summary>
        /// the purpose of the project, (Default: "Web Application")
        /// </summary>
        [Input("purpose")]
        public Input<string>? Purpose { get; set; }

        [Input("resources")]
        private InputList<string>? _resources;

        /// <summary>
        /// a list of uniform resource names (URNs) for the resources associated with the project
        /// </summary>
        public InputList<string> Resources
        {
            get => _resources ?? (_resources = new InputList<string>());
            set => _resources = value;
        }

        /// <summary>
        /// the date and time when the project was last updated, (ISO8601)
        /// </summary>
        [Input("updatedAt")]
        public Input<string>? UpdatedAt { get; set; }

        public ProjectState()
        {
        }
    }
}
