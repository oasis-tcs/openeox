### Construction Principles

The OpenEoX Core specification describes a map for well-known named transition events (like end-of-life) to dates.
Producers use this mapping to bind products to this minimal set of life cycle events.

Other schemata provide models to add the data needed for product identification.
Examples for such schemata are:

- OpenEoX Shell
- OpenEoX API
- integration into the product itself (for example via SNMP calls or HTTPS requests)
- integration into other standards (for example CSAF)

This separation provides consistent, interoperable, actionable, structured, and validated life cycle information
with the goal to offer complete automation.

The chosen data format and version "JSON Schema Draft 2020-12" [cite](#JSON-Schema-Core) allows
validation and delegation to providers of referenced schemata.
The latter enables separation of concerns as it allows other standards, specifications,
and product-specific implementations to import and reference the OpenEoX Core schema.
This enables consistency and interoperability across different implementations.

The OpenEoX Core schema is defined at <https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json>

The schema elements and their expected usage patterns are detailed in subsequent sections.

Linking and integration of the OpenEoX Core schema with product identification schema information may lead to inconsistencies.
The producers of OpenEoX information items have to ensure the intended semantics.
For example, that life cycle dates are ordered logically.
Semantic validation is out of scope for this OpenEoX Core specification.

The OpenEoX Core schema is designed to be self-contained with minimal external dependencies, utilizing only:

[cite](#RFC3339)
:    Date and time format specification for timestamp representation

[cite](#JSON-Schema-Core)
:    Schema validation and structure definition

OpenEoX information items SHOULD only contain members where the value is an OpenEoX life cycle date.
The use of placeholders or `null` values is discouraged and any compliant OpenEoX implementation SHOULD ignore such members.

> In combination, these to preceding requirements maximize clarity and simplify automation.
<!-- TODO(sthagen): Where and when did we decide on date references, like v25 will be end-of-support when v27 is GA? -->

OpenEoX information items SHOULD NOT contain additional properties in themselves or as part of
referenced schema instances.
Suggestions for new fields or values SHOULD be made through issues in the TC's GitHub.
The JSON schemas defined in this standard do not allow the use of additional properties and custom keywords.

> The standardized fields allow for scalability across different issuing parties and dramatically reduce the human effort and
> need for dedicated parsers as well as other tools on the side of the consuming parties.
