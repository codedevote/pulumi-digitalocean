// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package digitalocean

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Retrieves information about droplet sizes that DigitalOcean supports. This data source provides all of droplet size properties, with the ability to filter and sort the results.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/sizes.html.markdown.
func LookupSizes(ctx *pulumi.Context, args *GetSizesArgs) (*GetSizesResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["sorts"] = args.Sorts
	}
	outputs, err := ctx.Invoke("digitalocean:index/getSizes:getSizes", inputs)
	if err != nil {
		return nil, err
	}
	return &GetSizesResult{
		Filters: outputs["filters"],
		Sizes: outputs["sizes"],
		Sorts: outputs["sorts"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getSizes.
type GetSizesArgs struct {
	// Filter the results.
	// The `filter` block is documented below.
	Filters interface{}
	// Sort the results.
	// The `sort` block is documented below.
	Sorts interface{}
}

// A collection of values returned by getSizes.
type GetSizesResult struct {
	Filters interface{}
	Sizes interface{}
	Sorts interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
