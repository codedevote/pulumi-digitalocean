// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a DigitalOcean Cloud Firewall resource. This can be used to create,
 * modify, and delete Firewalls.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as digitalocean from "@pulumi/digitalocean";
 * 
 * const webDroplet = new digitalocean.Droplet("web", {
 *     image: "ubuntu-18-04-x64",
 *     region: "nyc3",
 *     size: "s-1vcpu-1gb",
 * });
 * const webFirewall = new digitalocean.Firewall("web", {
 *     dropletIds: [webDroplet.id],
 *     inboundRules: [
 *         {
 *             portRange: "22",
 *             protocol: "tcp",
 *             sourceAddresses: [
 *                 "192.168.1.0/24",
 *                 "2002:1:2::/48",
 *             ],
 *         },
 *         {
 *             portRange: "80",
 *             protocol: "tcp",
 *             sourceAddresses: [
 *                 "0.0.0.0/0",
 *                 "::/0",
 *             ],
 *         },
 *         {
 *             portRange: "443",
 *             protocol: "tcp",
 *             sourceAddresses: [
 *                 "0.0.0.0/0",
 *                 "::/0",
 *             ],
 *         },
 *         {
 *             protocol: "icmp",
 *             sourceAddresses: [
 *                 "0.0.0.0/0",
 *                 "::/0",
 *             ],
 *         },
 *     ],
 *     outboundRules: [
 *         {
 *             destinationAddresses: [
 *                 "0.0.0.0/0",
 *                 "::/0",
 *             ],
 *             portRange: "53",
 *             protocol: "tcp",
 *         },
 *         {
 *             destinationAddresses: [
 *                 "0.0.0.0/0",
 *                 "::/0",
 *             ],
 *             portRange: "53",
 *             protocol: "udp",
 *         },
 *         {
 *             destinationAddresses: [
 *                 "0.0.0.0/0",
 *                 "::/0",
 *             ],
 *             protocol: "icmp",
 *         },
 *     ],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/firewall.html.markdown.
 */
export class Firewall extends pulumi.CustomResource {
    /**
     * Get an existing Firewall resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallState, opts?: pulumi.CustomResourceOptions): Firewall {
        return new Firewall(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'digitalocean:index/firewall:Firewall';

    /**
     * Returns true if the given object is an instance of Firewall.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Firewall {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Firewall.__pulumiType;
    }

    /**
     * A time value given in ISO8601 combined date and time format
     * that represents when the Firewall was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The list of the IDs of the Droplets assigned
     * to the Firewall.
     */
    public readonly dropletIds!: pulumi.Output<number[] | undefined>;
    /**
     * The inbound access rule block for the Firewall.
     * The `inbound_rule` block is documented below.
     */
    public readonly inboundRules!: pulumi.Output<{ portRange?: string, protocol: string, sourceAddresses?: string[], sourceDropletIds?: number[], sourceLoadBalancerUids?: string[], sourceTags?: string[] }[] | undefined>;
    /**
     * The Firewall name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The outbound access rule block for the Firewall.
     * The `outbound_rule` block is documented below.
     */
    public readonly outboundRules!: pulumi.Output<{ destinationAddresses?: string[], destinationDropletIds?: number[], destinationLoadBalancerUids?: string[], destinationTags?: string[], portRange?: string, protocol: string }[] | undefined>;
    /**
     * An list of object containing the fields, "droplet_id",
     * "removing", and "status".  It is provided to detail exactly which Droplets
     * are having their security policies updated.  When empty, all changes
     * have been successfully applied.
     */
    public /*out*/ readonly pendingChanges!: pulumi.Output<{ dropletId?: number, removing?: boolean, status?: string }[]>;
    /**
     * A status string indicating the current state of the Firewall.
     * This can be "waiting", "succeeded", or "failed".
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * The names of the Tags assigned to the Firewall.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;

    /**
     * Create a Firewall resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: FirewallArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FirewallArgs | FirewallState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as FirewallState | undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["dropletIds"] = state ? state.dropletIds : undefined;
            inputs["inboundRules"] = state ? state.inboundRules : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["outboundRules"] = state ? state.outboundRules : undefined;
            inputs["pendingChanges"] = state ? state.pendingChanges : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as FirewallArgs | undefined;
            inputs["dropletIds"] = args ? args.dropletIds : undefined;
            inputs["inboundRules"] = args ? args.inboundRules : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["outboundRules"] = args ? args.outboundRules : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["createdAt"] = undefined /*out*/;
            inputs["pendingChanges"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        }
        super(Firewall.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Firewall resources.
 */
export interface FirewallState {
    /**
     * A time value given in ISO8601 combined date and time format
     * that represents when the Firewall was created.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The list of the IDs of the Droplets assigned
     * to the Firewall.
     */
    readonly dropletIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * The inbound access rule block for the Firewall.
     * The `inbound_rule` block is documented below.
     */
    readonly inboundRules?: pulumi.Input<pulumi.Input<{ portRange?: pulumi.Input<string>, protocol: pulumi.Input<string>, sourceAddresses?: pulumi.Input<pulumi.Input<string>[]>, sourceDropletIds?: pulumi.Input<pulumi.Input<number>[]>, sourceLoadBalancerUids?: pulumi.Input<pulumi.Input<string>[]>, sourceTags?: pulumi.Input<pulumi.Input<string>[]> }>[]>;
    /**
     * The Firewall name
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The outbound access rule block for the Firewall.
     * The `outbound_rule` block is documented below.
     */
    readonly outboundRules?: pulumi.Input<pulumi.Input<{ destinationAddresses?: pulumi.Input<pulumi.Input<string>[]>, destinationDropletIds?: pulumi.Input<pulumi.Input<number>[]>, destinationLoadBalancerUids?: pulumi.Input<pulumi.Input<string>[]>, destinationTags?: pulumi.Input<pulumi.Input<string>[]>, portRange?: pulumi.Input<string>, protocol: pulumi.Input<string> }>[]>;
    /**
     * An list of object containing the fields, "droplet_id",
     * "removing", and "status".  It is provided to detail exactly which Droplets
     * are having their security policies updated.  When empty, all changes
     * have been successfully applied.
     */
    readonly pendingChanges?: pulumi.Input<pulumi.Input<{ dropletId?: pulumi.Input<number>, removing?: pulumi.Input<boolean>, status?: pulumi.Input<string> }>[]>;
    /**
     * A status string indicating the current state of the Firewall.
     * This can be "waiting", "succeeded", or "failed".
     */
    readonly status?: pulumi.Input<string>;
    /**
     * The names of the Tags assigned to the Firewall.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Firewall resource.
 */
export interface FirewallArgs {
    /**
     * The list of the IDs of the Droplets assigned
     * to the Firewall.
     */
    readonly dropletIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * The inbound access rule block for the Firewall.
     * The `inbound_rule` block is documented below.
     */
    readonly inboundRules?: pulumi.Input<pulumi.Input<{ portRange?: pulumi.Input<string>, protocol: pulumi.Input<string>, sourceAddresses?: pulumi.Input<pulumi.Input<string>[]>, sourceDropletIds?: pulumi.Input<pulumi.Input<number>[]>, sourceLoadBalancerUids?: pulumi.Input<pulumi.Input<string>[]>, sourceTags?: pulumi.Input<pulumi.Input<string>[]> }>[]>;
    /**
     * The Firewall name
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The outbound access rule block for the Firewall.
     * The `outbound_rule` block is documented below.
     */
    readonly outboundRules?: pulumi.Input<pulumi.Input<{ destinationAddresses?: pulumi.Input<pulumi.Input<string>[]>, destinationDropletIds?: pulumi.Input<pulumi.Input<number>[]>, destinationLoadBalancerUids?: pulumi.Input<pulumi.Input<string>[]>, destinationTags?: pulumi.Input<pulumi.Input<string>[]>, portRange?: pulumi.Input<string>, protocol: pulumi.Input<string> }>[]>;
    /**
     * The names of the Tags assigned to the Firewall.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}
