## Construction Principles

OpenEoX Core information bound to products is created through the application of
a well-defined schema, typically by product managers or vendors making lifecycle decisions.
The focused and purposefully minimal schema contains standardized dates, while the product context is provided through neighbor specifications such as OpenEoX Shell, OpenEoX API, integration into the product itself (e.g., via SNMP calls), or integration into other standards (e.g., CSAF). This separation serves the goal of providing actionable, structured, and validated lifecycle information targeting a high degree of automation.

The format chosen is JSON Schema Draft 2020-12 which allows validation and delegation to sub-schema providers.
The latter aligns well with separation of concerns and enables the OpenEoX Core schema to be imported and referenced
by other standards, specifications, and product-specific implementations.

Technically, the use of JSON Schema Draft 2020-12 allows validation and proof of model conformance through
established schema-based validation of the declared OpenEoX Core information.

The OpenEoX Core schema structures is defined at https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json

The schema elements and their expected usage patterns are detailed in subsequent sections.
The linking and integration with product identification schemas relies on importing the OpenEoX Core schema
appropriately and thus implies that semantic validation (e.g. ensuring lifecycle dates are logically ordered)
is to be ensured by the producer and consumer of documents containing OpenEoX statements.
Such semantic validation is out of scope for the core schema specification.

The OpenEoX Core schema is designed to be self-contained with minimal external dependencies,
utilizing only:

* **RFC 3339**: Date and time format specification for timestamp representation
* **JSON Schema Draft 2020-12**: Schema validation and structure definition

When suppliers do not provide specific lifecycle dates, the corresponding fields should be omitted entirely rather than using placeholder values. This approach maintains data type integrity and avoids complications in the information model.

Even though not all - especially the referenced - JSON schemas prohibit specifically additional properties and custom keywords,
it is strongly recommended not to use them.
Suggestions for new fields or values SHOULD be made through issues in the TC's GitHub.
The JSON schemas defined in this standard do not allow the use of additional properties and custom keywords.

> The standardized fields allow for scalability across different issuing parties and dramatically reduce the human effort and
> need for dedicated parsers as well as other tools on the side of the consuming parties.

The schema elements and their detailed specifications are provided in the subsequent Schema Elements section.
Additional conventions for timestamp handling and lifecycle stage interpretations are detailed in the Additional Conventions section.
