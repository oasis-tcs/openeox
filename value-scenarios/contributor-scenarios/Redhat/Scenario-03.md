# Scenario 03

### Title

Resolve dependent products lifecycle linking between a product and its base product

### Used definitions

- `Product`: as defined in OpenEoX
- `Product Life Cycle`: as defined in OpenEoX
- `product`: as defined in [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#12-terminology)

### Description

As an Engineer, I want to list the products that a given product depends on (its dependent-product
relationships), and have their lifecycles linked, so that I can automatically verify that a dependent
product's support window is never longer than the base product it is built on, and so that a change to
the base product's lifecycle can be checked for downstream violations.

For example: Red Hat OpenShift Container Platform (OCP) is a product built on top of, and dependent on,
Red Hat Enterprise Linux (RHEL). OCP's support window for a given stream must never outlive the RHEL
version/stream it was built against. Today this relationship is tracked manually; a producer could
instead reference the base product's OpenEoX record directly.

### OpenEoX today

**Gap.** Neither `eox-core` nor `eox-shell` has a construct for referencing another product's OpenEoX
record as a basis/dependency, so this relationship cannot be expressed or automatically validated today.
This exact need was raised by a Red Hat TC member in
[issue #151](https://github.com/oasis-tcs/openeox/issues/151) ("Product OpenEoX life cycle linking"),
where the proposed direction is a Shell-level, optional dependency reference inside the product object
(for example, a `based_on` reference to another product's Shell statement), enabling automatic detection
of lifecycle violations (a dependent product outliving its base product).
