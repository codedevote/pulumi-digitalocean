// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package digitalocean

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Droplet snapshots are saved instances of a Droplet. Use this data
// source to retrieve the ID of a DigitalOcean Droplet snapshot for use in other
// resources.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/d/droplet_snapshot.html.markdown.
func LookupDropletSnapshot(ctx *pulumi.Context, args *GetDropletSnapshotArgs) (*GetDropletSnapshotResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["mostRecent"] = args.MostRecent
		inputs["name"] = args.Name
		inputs["nameRegex"] = args.NameRegex
		inputs["region"] = args.Region
	}
	outputs, err := ctx.Invoke("digitalocean:index/getDropletSnapshot:getDropletSnapshot", inputs)
	if err != nil {
		return nil, err
	}
	return &GetDropletSnapshotResult{
		CreatedAt: outputs["createdAt"],
		DropletId: outputs["dropletId"],
		MinDiskSize: outputs["minDiskSize"],
		MostRecent: outputs["mostRecent"],
		Name: outputs["name"],
		NameRegex: outputs["nameRegex"],
		Region: outputs["region"],
		Regions: outputs["regions"],
		Size: outputs["size"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getDropletSnapshot.
type GetDropletSnapshotArgs struct {
	// If more than one result is returned, use the most recent Droplet snapshot.
	MostRecent interface{}
	// The name of the Droplet snapshot.
	Name interface{}
	// A regex string to apply to the Droplet snapshot list returned by DigitalOcean. This allows more advanced filtering not supported from the DigitalOcean API. This filtering is done locally on what DigitalOcean returns.
	NameRegex interface{}
	// A "slug" representing a DigitalOcean region (e.g. `nyc1`). If set, only Droplet snapshots available in the region will be returned.
	Region interface{}
}

// A collection of values returned by getDropletSnapshot.
type GetDropletSnapshotResult struct {
	// The date and time the Droplet snapshot was created.
	CreatedAt interface{}
	// The ID of the Droplet from which the Droplet snapshot originated.
	DropletId interface{}
	// The minimum size in gigabytes required for a Droplet to be created based on this Droplet snapshot.
	MinDiskSize interface{}
	MostRecent interface{}
	Name interface{}
	NameRegex interface{}
	Region interface{}
	// A list of DigitalOcean region "slugs" indicating where the Droplet snapshot is available.
	Regions interface{}
	// The billable size of the Droplet snapshot in gigabytes.
	Size interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
