// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Digitalocean
{
    public static partial class Invokes
    {
        /// <summary>
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/tag.html.markdown.
        /// </summary>
        public static Task<GetTagResult> GetTag(GetTagArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTagResult>("digitalocean:index/getTag:getTag", args, options.WithVersion());
    }

    public sealed class GetTagArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the tag.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetTagArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetTagResult
    {
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetTagResult(
            string name,
            string id)
        {
            Name = name;
            Id = id;
        }
    }
}
