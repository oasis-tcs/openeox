# Scenario 01

### Title

Discover all currently supported product streams for a product family

### Used definitions

- `Product`: as defined in OpenEoX
- `Vendor`: as defined in OpenEoX
- `product`: as defined in [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#12-terminology)

### Description

As a Security Engineer or Engineer, I want to list all currently supported release streams of a given product, 
so that I know which streams I must still track for security advisories, bug tracking, and SBOM/CSAF/VEX generation, 
and which ones I can ignore because they are no longer supported.

For example: for Red Hat OpenShift Container Platform (OCP) 4, this means retrieving the full set of
y-stream releases (4.1 through the current latest) together with each one's published/supported status,
in a single machine-readable query, instead of parsing vendor lifecycle web pages by hand.

### OpenEoX today

Supported. A single `eox-shell` document with one `statement` per release stream (each carrying its own
`core` block and `product_identification_helper`) already lets a consumer enumerate every stream and its
`end_of_life`/`end_of_security_support` dates. Red Hat OpenShift Container Platform (OCP) 4, with
release streams 4.1 through the current latest, is a concrete worked example of this.
