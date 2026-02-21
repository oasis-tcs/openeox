
![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------

# OpenEoX Core Schema Version 1.0

## Committee Specification Draft 01

## 18 February 2026

### This Version

https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.md (Authoritative) \
https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.html \
https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.pdf

### Previous Version

N/A

### Latest Version

https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.md (Authoritative) \
https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.html \
https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.pdf

### Technical Committee

[OASIS OpenEoX TC](https://www.oasis-open.org/tc-openeox/)

### Chairs
Justin Murphy (justin.murphy@mail.cisa.dhs.gov), [DHS Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov) \
Omar Santos (osantos@cisco.com), [Cisco Systems](https://cisco.com/) \

### Secretaries

Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/)

### Editors

Jautau White (jaywhite@microsoft.com), Microsoft Corporation \
Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/) \
Thomas Schmidt (thomas.schmidt@bsi.bund.de), [Federal Office for Information Security (BSI) Germany](https://www.bsi.bund.de/)

### Additional Artifacts

This prose specification is one component of a Work Product that also includes:

* OpenEoX Core JSON schema: https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/schema/eox-core.json. \
Latest stage: https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json.
* OpenEoX Meta JSON schema: https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/schema/meta.json. \
Latest stage: https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json.

### Declared JSON namespaces

* [https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json](https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json)
* [https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json](https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json)

### Abstract

The OpenEoX Core Schema defines the core schema for the OpenEoX unified machine-readable approach to
managing and sharing General Availability (GA), End-of-Sales (EoS), End-of-Life (EoL), and
End-of-Security-Support (EoSSec) information for commercial and open source software and hardware.

### Citation Format

When referencing this document, the following citation format should be used:

**\[EoX-Core-v1.0]**

_OpenEoX Core Schema Version 1.0_.
Edited by Jautau White, Stefan Hagen, and Thomas Schmidt.
18 February 2026.
OASIS Committee Specification Draft 01.
https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.html.\
Latest stage: https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.html

### Related Work

This document replaces or supersedes:

N/A

This document is related to:

N/A

## License, Document Status, and Notices

Copyright &copy; OASIS Open 2026. All Rights Reserved.

For license and copyright information, and complete status, please see [Annex A](#annex-a)
which contains the License, Document Status and Notices.

-------

# Table of Contents

1. [Scope](#scope)  
2. [Definitions and Acronyms](#definitions-and-acronyms)  
	2.1 [Abbreviations and Acronyms](#abbreviations-and-acronyms)  
	2.2 [Definitions](#definitions)  
		2.2.1 [Terms Defined Elsewhere](#terms-defined-elsewhere)  
		2.2.2 [Terms Defined in this Document](#terms-defined-in-this-document)  
3. [Document Conventions](#document-conventions)  
	3.1 [Key Words](#key-words)  
	3.2 [Typographical Conventions](#typographical-conventions)  
4. [Introduction](#introduction)  
	4.1 [Design Considerations](#design-considerations)  
		4.1.1 [OpenEoX Architecture](#openeox-architecture)  
			4.1.1.1 [OpenEoX Core (this specification)](#openeox-core-this-specification)  
			4.1.1.2 [OpenEoX Shell](#openeox-shell)  
			4.1.1.3 [OpenEoX API](#openeox-api)  
		4.1.2 [Design Principles](#design-principles)  
			4.1.2.1 [Standardization and Interoperability](#standardization-and-interoperability)  
			4.1.2.2 [Security-First Approach](#security-first-approach)  
		4.1.3 [Industry Applications](#industry-applications)  
			4.1.3.1 [Vendor Perspectives](#vendor-perspectives)  
			4.1.3.2 [Consumer Perspectives](#consumer-perspectives)  
		4.1.4 [Construction Principles](#construction-principles)  
		4.1.5 [Format Validation](#format-validation)  
		4.1.6 [Date and Time](#date-and-time)  
	4.2 [Changes From the Previous Version](#changes-from-the-previous-version)  
5. [Taxonomy](#taxonomy)  
	5.1 [End-of-Life](#end-of-life)  
	5.2 [End-of-Sales](#end-of-sales)  
	5.3 [End-of-Security-Support](#end-of-security-support)  
	5.4 [General Availability](#general-availability)  
	5.5 [Product](#product)  
	5.6 [Product Life Cycle](#product-life-cycle)  
	5.7 [Vendor](#vendor)  
6. [Schema Elements](#schema-elements)  
	6.1 [Definitions](#schema-elements---definitions)  
		6.1.1 [EoX Timestamp Type](#eox-timestamp-type)  
	6.2 [Properties](#properties)  
		6.2.1 [Schema Property](#schema-property)  
		6.2.2 [End-of-Life Property](#end-of-life-property)  
		6.2.3 [End-of-Sales Property](#end-of-sales-property)  
		6.2.4 [End-of-Security-Support Property](#end-of-security-support-property)  
		6.2.5 [General Availability Property](#general-availability-property)  
		6.2.6 [Last Updated Property](#last-updated-property)  
7. [Tests](#tests)  
	7.1 [Mandatory Tests](#mandatory-tests)  
		7.1.1 [Inconsistent EoL Date](#inconsistent-eol-date)  
		7.1.2 [Date and Time](#mandatory-tests--date-and-time)  
		7.1.3 [Inconsistent GA Date](#inconsistent-ga-date)  
	7.2 [Recommended Tests](#recommended-tests)  
		7.2.1 [Use of `tba` where Date is set for EoL](#use-of-tba-where-date-is-set-for-eol)  
		7.2.2 [Use of `tba` for GA where other Date is set](#use-of-tba-for-ga-where-other-date-is-set)  
	7.3 [Informative Tests](#informative-tests)  
		7.3.1 [EoSSec before EoS](#eossec-before-eos)  
8. [Safety, Security and Data Protection](#safety-security-and-data-protection)  
9. [Conformance](#conformance)  
	9.1 [Conformance Targets](#conformance-targets)  
		9.1.1 [Conformance Clause 1: OpenEoX Core Information](#conformance-clause-1-openeox-core-information)  
		9.1.2 [Conformance Clause 2: OpenEoX Core Producer](#conformance-clause-2-openeox-core-producer)  
		9.1.3 [Conformance Clause 3: OpenEoX Core Consumer](#conformance-clause-3-openeox-core-consumer)  
		9.1.4 [Conformance Clause 4: OpenEoX Core Basic Validator](#conformance-clause-4-openeox-core-basic-validator)  
		9.1.5 [Conformance Clause 5: OpenEoX Core Extended Validator](#conformance-clause-5-openeox-core-extended-validator)  
		9.1.6 [Conformance Clause 6: OpenEoX Core Full Validator](#conformance-clause-6-openeox-core-full-validator)  
		9.1.7 [Conformance Clause 7: OpenEoX Core Library](#conformance-clause-7-openeox-core-library)  
		9.1.8 [Conformance Clause 8: OpenEoX Core Library with Basic Validation](#conformance-clause-8-openeox-core-library-with-basic-validation)  
		9.1.9 [Conformance Clause 9: OpenEoX Core Library with Extended Validation](#conformance-clause-9-openeox-core-library-with-extended-validation)  
		9.1.10 [Conformance Clause 10: OpenEoX Core Library with Full Validation](#conformance-clause-10-openeox-core-library-with-full-validation)  
		9.1.11 [Conformance Clause 11: OpenEoX Core Differ](#conformance-clause-11-openeox-core-differ)  
		9.1.12 [Conformance Clause 12: OpenEoX Core Comparator](#conformance-clause-12-openeox-core-comparator)  
		9.1.13 [Conformance Clause 13: OpenEoX Core Sorter](#conformance-clause-13-openeox-core-sorter)  
		9.1.14 [Conformance Clause 14: OpenEoX Core Merger](#conformance-clause-14-openeox-core-merger)  

Annex A [License, Document Status and Notices](#annex-a)  
A.1. [Document Status](#document-status)  
A.2. [License and Notices](#license-and-notices)  
Annex B [References](#references)  
	B.1 [Normative References](#normative-references)  
	B.2 [Informative References](#informative-references)  
Appendix 1 [Acknowledgments](#acknowledgments)  
 [Leadership](#leadership)  
	 [Special Thanks](#special-thanks)  
	 [Participants](#participants)  
Appendix 2 [Changes From Previous Version](#changes-from-previous-version)  
 [Revision History](#revision-history)  
-------

# 1. Scope <a id='scope'></a>

TODO: add scope (see [#165](https://github.com/oasis-tcs/openeox/issues/165))

-------

# 2. Definitions and Acronyms <a id='definitions-and-acronyms'></a>

## 2.1 Abbreviations and Acronyms <a id='abbreviations-and-acronyms'></a>

This document uses the following abbreviations and acronyms:

* EoL: End-of-Life.  
* EoS: End-of-Sales.  
* EoSSec: End-of-Security-Support.
* EoX: End-of-X.
* GA: General Availability.

------

## 2.2 Definitions <a id='definitions'></a>

### 2.2.1 Terms Defined Elsewhere <a id='terms-defined-elsewhere'></a>

This document uses the following terms defined elsewhere:

<dl>
  <dt id="def;embedded-link-csaf-v2-1">Embedded Link [CSAF-v2.1]</dt>
  <dd>syntactic construct which enables a message string to refer to a location mentioned in the document.</dd>
  <dt id="def;empty-array-csaf-v2-1">Empty Array: [CSAF-v2.1]</dt>
  <dd>array that contains no elements, and so has a length of zero.</dd>
  <dt id="def;empty-object-csaf-v2-1">Empty Object [CSAF-v2.1]</dt>
  <dd>object that contains no properties.</dd>
  <dt id="def;empty-string-csaf-v2-1">Empty String [CSAF-v2.1]</dt>
  <dd>string that contains no characters, and so has a length of zero.</dd>
  <dt id="def;end-user-csaf-v2-1">(End) User [CSAF-v2.1]</dt>
  <dd>person who uses the information in a document to investigate, triage, or resolve results.</dd>
  <dt id="def;product-csaf-v2-1">Product [CSAF-v2.1]</dt>
  <dd>is any deliverable (e.g. software, hardware, specification, or service) which can be referred to with a name.
      This applies regardless of the origin, the license model, or the mode of distribution of the deliverable.</dd>
  <dt id="def;property-csaf-v2-1">Property [CSAF-v2.1]</dt>
  <dd>attribute of an object consisting of a name and a value associated with the name.</dd>
  <dt id="def;triage-csaf-v2-1">Triage [CSAF-v2.1]</dt>
  <dd>decide whether a result indicates a problem that needs to be corrected.</dd>
  <dt id="def;user-csaf-v2-1">User [CSAF-v2.1]</dt>
  <dd>see end user.</dd>
  <dt id="def;vendor-csaf-v2-1">Vendor [CSAF-v2.1]</dt>
  <dd>the community, individual, or organization that created or maintains a product (including open source software and hardware providers).</dd>
  <dt id="def;white-space-csaf-v2-1">White Space [CSAF-v2.1]</dt>
  <dd>code point used to improve text readability or token separation as defined in section 12.2 of <a href="#ECMA-262">cite</a>.</dd>
</dl>

### 2.2.2 Terms Defined in this Document <a id='terms-defined-in-this-document'></a>

This document defines the following terms:

<dl>
  <dt id="def;end-of-life-eol">End-of-Life (EoL)</dt>
  <dd>indicates the last day when the particular product (or the product version/release) is officially supported in any way by the vendor.</dd>
  <dt id="def;end-of-sales-eos">End-of-Sales (EoS)</dt>
  <dd>indicates the last day when a particular product (or the product version/release) may be ordered by customers from vendor sales channels.</dd>
  <dt id="def;end-of-security-support-eossec">End-of-Security-Support (EoSSec)</dt>
  <dd>indicates the last day when the vendor has committed to providing security remediations for the particular product (or the product version/release).</dd>
  <dt id="def;general-availability-ga">General Availability (GA)</dt>
  <dd>indicates the first day when the particular product (or the product version/release) is officially launched and made accessible to the general public or through its intended distribution channels.</dd>
  <dt id="def;product-life-cycle">Product Life Cycle</dt>
  <dd>describes for a product type (software, hardware, managed service and other deliverables) the model it can be associated with.
      It can contain definitions of various support models (different levels of maintenance) in association to the product versioning convention.</dd>
  <dt id="def;openeox-core-basic-validator">OpenEoX Core Basic Validator</dt>
  <dd>A program that reads a JSON object and checks it against the JSON schema and performs mandatory tests.</dd>
  <dt id="def;openeox-core-comparator">OpenEoX Core Comparator</dt>
  <dd>A program that compares OpenEoX Core Information and returns the newer one.</dd>
  <dt id="def;openeox-core-consumer">OpenEoX Core Consumer</dt>
  <dd>A program that reads and interprets OpenEoX Core Information.</dd>
  <dt id="def;openeox-core-differ">OpenEoX Core Differ</dt>
  <dd>A program that compares OpenEoX Core Information and calculates the changes.</dd>
  <dt id="def;openeox-core-extended-validator">OpenEoX Core Extended Validator</dt>
  <dd>A OpenEoX Core Basic Validator that additionally performs recommended tests.</dd>
  <dt id="def;openeox-core-full-validator">OpenEoX Core Full Validator</dt>
  <dd>A OpenEoX Core Extended Validator that additionally performs guidance tests.</dd>
  <dt id="def;openeox-core-information">OpenEoX Core Information</dt>
  <dd>An EoX information in the format defined by this document.</dd>
  <dt id="def;openeox-core-library">OpenEoX Core Library</dt>
  <dd>A library that implements OpenEoX Core data capabilities.</dd>
  <dt id="def;openeox-core-library-with-basic-validation">OpenEoX Core Library with Basic Validation</dt>
  <dd>A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Basic Validator".</dd>
  <dt id="def;openeox-core-library-with-extended-validation">OpenEoX Core Library with Extended Validation</dt>
  <dd>A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Extended Validator".</dd>
  <dt id="def;openeox-core-library-with-full-validation">OpenEoX Core Library with Full Validation</dt>
  <dd>A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Full Validator".</dd>
  <dt id="def;openeox-core-merger">OpenEoX Core Merger</dt>
  <dd>A program that combines OpenEoX Core Information.</dd>
  <dt id="def;openeox-core-producer">OpenEoX Core Producer</dt>
  <dd>A program which emits output in the OpenEoX Core format.</dd>
  <dt id="def;openeox-core-sorter">OpenEoX Core Sorter</dt>
  <dd>A program that sorts OpenEoX Core Information from newest to oldest or vice versa.</dd>
  <dt id="def;redactable-property">Redactable Property</dt>
  <dd>property that potentially contains sensitive information that a OpenEoX Producer might wish to redact.</dd>
  <dt id="def;taxonomy">Taxonomy</dt>
  <dd>classification of product life cycle stages into a set of categories.</dd>
</dl>

# 3. Document Conventions <a id='document-conventions'></a>

## 3.1 Key Words <a id='key-words'></a>

The key words "**MUST**", "**MUST NOT**", "**REQUIRED**", "**SHALL**", "**SHALL NOT**", "**SHOULD**", "**SHOULD NOT**", "**RECOMMENDED**", "**NOT RECOMMENDED**", "**MAY**", and "**OPTIONAL**" in this document are to be interpreted as described in BCP 14 \[[RFC2119](#RFC2119)\] \[[RFC8174](#RFC8174)\] when,
and only when, they appear in all capitals, as shown here.

## 3.2 Typographical Conventions <a id='typographical-conventions'></a>

Keywords defined by this specification use this `monospaced` font.

```
    Normative source code uses this paragraph style.
```

Some sections of this specification are illustrated with non-normative examples introduced with "Example" or "Examples" like so:

*Example 1:*<a id='typographical-conventions-eg-1'></a><a id='sec-3-2-eg-1'></a><a id='example-4321'></a>

```
    Informative examples also use this paragraph style but preceded by the text "Example(s)".
```

All examples in this document are informative only.

All other text is normative unless otherwise labeled e.g. like the following informative comment:

> This is a pure informative comment that may be present, because the information conveyed is deemed useful advice or
> common pitfalls learned from implementer or operator experience and often given including the rationale.

-------

# 4. Introduction <a id='introduction'></a>

## 4.1 Design Considerations <a id='design-considerations'></a>

The OpenEoX provides the vocabulary for exchanging standardized End-of-X (EoX) life cycle data for any product.
This includes, but is not limited to hardware, software and specifications, as well as all supplier-consumer
relationships, services and offerings.

### 4.1.1 OpenEoX Architecture <a id='openeox-architecture'></a>

The OpenEoX standard is architected as a modular three-layer framework:

#### 4.1.1.1 OpenEoX Core (this specification) <a id='openeox-core-this-specification'></a>

The OpenEoX Core specification contains the fundamental EoX life cycle information elements and is
designed to be imported by other standards or integrated directly into product responses.
The Core schema establishes one part of the essential data elements required for any EoX statement:

**Required fields:**

- `end_of_life`: The definitive timestamp when all vendor support ceases
- `end_of_security_support`: The critical timestamp when security remediation commitments end
- `last_updated`: The timestamp tracking for data freshness and change management

Optionally, the standard also conveys additional life cycle events.

The core information can be provided independently when the product context is available through
other means, such as SNMP responses, HTTPS API responses.

#### 4.1.1.2 OpenEoX Shell <a id='openeox-shell'></a>

The OpenEoX Shell specification provides the binding mechanism that combines OpenEoX Core life cycle
information to specific product identifications.
This combination is called an "OpenEoX statement" - a complete, standalone representation of life cycle
information for a specific product.
The Shell forms the standalone mode in OpenEoX, enabling complete life cycle statements that can be
processed independently without external context.

#### 4.1.1.3 OpenEoX API <a id='openeox-api'></a>

The OpenEoX API specification addresses the distribution, discovery, and consumption of OpenEoX Core
and Shell data across vendor ecosystems and consumer applications.
The API specification defines standardized endpoints, query mechanisms, and data exchange patterns
that enable automated integration.

### 4.1.2 Design Principles <a id='design-principles'></a>

#### 4.1.2.1 Standardization and Interoperability <a id='standardization-and-interoperability'></a>

OpenEoX addresses the current industry challenge where vendors use proprietary, inconsistent formats
for communicating life cycle information.
By establishing a common JSON-based format, OpenEoX enables:

- Automated processing and integration across vendor ecosystems
- Consistent interpretation of life cycle stages regardless of vendor
- Reduced operational overhead in managing multi-vendor environments
- Enhanced accuracy in infrastructure life cycle planning

#### 4.1.2.2 Security-First Approach <a id='security-first-approach'></a>

Recognition that End-of-Security-Support represents a critical inflection point for infrastructure
security has influenced the OpenEoX design.
The mandatory `end_of_security_support` field ensures that security life cycle information is
always available, supporting:

- Proactive vulnerability management planning
- Compliance with security frameworks requiring current support status
- Risk assessment for critical infrastructure components
- Automated alerting when security support approaches termination

### 4.1.3 Industry Applications <a id='industry-applications'></a>

#### 4.1.3.1 Vendor Perspectives <a id='vendor-perspectives'></a>

**OpenEoX enables vendors to:**

- Standardize EoX communication across all product lines and channels
- Reduce support inquiries related to life cycle confusion
- Demonstrate proactive customer stewardship through clear life cycle communication
- Support automated customer notification systems
- Facilitate integration with partner and reseller systems

#### 4.1.3.2 Consumer Perspectives <a id='consumer-perspectives'></a>

**Organizations consuming OpenEoX information benefit through:**

- Automated discovery of life cycle status across multi-vendor environments
- Proactive planning for product refreshes and migrations
- Enhanced compliance reporting for security and regulatory frameworks
- Reduced operational risk from unexpected support terminations
- Streamlined asset management and inventory tracking

The OpenEoX architecture ensures that organizations can adopt OpenEoX in a manner
that aligns with their existing infrastructure and operational models while preserving
the ability to enhance integration over time.

### 4.1.4 Construction Principles <a id='construction-principles'></a>

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

The chosen data format and version "JSON Schema Draft 2020-12" \[[JSON-Schema-Core](#JSON-Schema-Core)\] allows
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

\[[RFC3339](#RFC3339)\]
:    Date and time format specification for timestamp representation

\[[JSON-Schema-Core](#JSON-Schema-Core)\]
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

### 4.1.5 Format Validation <a id='format-validation'></a>

The JSON schema 2020-12 dialect per default uses the `format` keyword just as annotation.
To be able to ensure that the format constraints are validated as intended, the following metaschema is defined.

```
  {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json",
    "$dynamicAnchor": "meta",
    "$vocabulary": {
      "https://json-schema.org/draft/2020-12/vocab/core": true,
      "https://json-schema.org/draft/2020-12/vocab/applicator": true,
      "https://json-schema.org/draft/2020-12/vocab/unevaluated": true,
      "https://json-schema.org/draft/2020-12/vocab/validation": true,
      "https://json-schema.org/draft/2020-12/vocab/meta-data": true,
      "https://json-schema.org/draft/2020-12/vocab/format-assertion": true,
      "https://json-schema.org/draft/2020-12/vocab/content": true
    },
    "allOf": [
      { "$ref": "https://json-schema.org/draft/2020-12/meta/core" },
      { "$ref": "https://json-schema.org/draft/2020-12/meta/applicator" },
      { "$ref": "https://json-schema.org/draft/2020-12/meta/unevaluated" },
      { "$ref": "https://json-schema.org/draft/2020-12/meta/validation" },
      { "$ref": "https://json-schema.org/draft/2020-12/meta/meta-data" },
      { "$ref": "https://json-schema.org/draft/2020-12/meta/format-assertion" },
      { "$ref": "https://json-schema.org/draft/2020-12/meta/content" }
    ]
  }
```

> All vocabularies that can be used are defined in this metaschema as JSON schema 2020-12 dialect has the rule of
> non-inheritability of vocabularies.

It is then consequently used in all JSON schemas defined in this standard and replaces the reference to the JSON schema 2020-12.

```
  {
    "$schema": "https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json",
    // ...
  }
```

The format validation is enforced by setting the corresponding vocabulary as required.

> If a library used to parse, modify or create OpenEoX content is unable to deal with this meta schema, it could reach the objective by
> interpreting the schema as JSON schema 2020-12 dialect and enforcing the format validation via its implementation.

### 4.1.6 Date and Time <a id='date-and-time'></a>

This standard uses the `date-time` format as defined in JSON Schema Draft 2020-12 Section 7.3.1.
In accordance with \[[RFC3339](#RFC3339)\] and \[[ISO8601-1](#ISO8601-1)\], the following rules apply:

* The letter `T` separating the date and time SHALL be upper case.
* The separator between date and time MUST be the letter `T`.
* The letter `Z` indicating the timezone UTC SHALL be upper case.
* Fractions of seconds are allowed as specified in the standards mention above with the full stop (`.`) as separator.
* Empty timezones MUST NOT be used.
* The ABNF of \[[RFC3339](#RFC3339)\], section 5.6 applies.

In contrast to the aforementioned standards, leap seconds MUST NOT be used.

  > While a full support of \[[RFC3339](#RFC3339)\] would be preferred, significant challenges have been mentioned by implementers
  > as most libraries are lacking the support for leap seconds.
  > To ensure interoperability, the decision was made to prohibit leap seconds.

## 4.2 Changes From the Previous Version <a id='changes-from-the-previous-version'></a>

The list of changes from the previous version and any revision history can be found in [Appendix 2](#revision-history).

------

# 5. Taxonomy <a id='taxonomy'></a>

The following subsections describe the taxonomy defining and explaining all terms the standard is build upon.

## 5.1 End-of-Life <a id='end-of-life'></a>

The End-of-Life (EoL) indicates the last day when the particular product (or the product version/release) is officially
supported in any way by the vendor.
After this date there shouldn’t be more development, updates or any type of support expected from the vendor.
The existing customers are also impacted by this product life cycle stage and should consider migration to the
still supported product version or release.

## 5.2 End-of-Sales <a id='end-of-sales'></a>

The End-of-Sales (EoS) indicates the last day when a particular product (or the product version/release) may be ordered
by customers from vendor sales channels.
After this date, the product is no longer for sale.
However, there might be other sources where the product is still available.
Once the product reaches the EoS life cycle stage, it may still be supported by the vendor, based on the official or
dedicated vendor life cycle model for this product, for existing customers.
The implications for existing customers regarding license renewals, updates, upgrades to newer versions or ongoing
technical support can vary depending on the vendor's specific policies.

## 5.3 End-of-Security-Support <a id='end-of-security-support'></a>

The End-of-Security-Support (EoSSec) indicates the last day when the vendor has committed to providing
security remediations for the particular product (or the product version/release).

## 5.4 General Availability <a id='general-availability'></a>

The General Availability (GA) indicates the first day when the particular product (or the product version/release)
is officially launched and made accessible to the general public or through its intended distribution channels.

## 5.5 Product <a id='product'></a>

Product is any deliverable (e.g. software, hardware, specification, or service) which can be referred to with a name.
This applies regardless of the origin, the license model, or the mode of distribution of the deliverable.

## 5.6 Product Life Cycle <a id='product-life-cycle'></a>

Every product type (software, hardware, managed service and other deliverables) can be associated with a life cycle model.
It can contain definitions of various support models (different levels of maintenance) in association to the product versioning convention.
The life cycle support model can be dynamic and may change over time, from the product's initial release (General Availability)
to its discontinuation (End-of-Life).
During the product life cycle, support models may switch from one state to another and may even run in parallel to meet individual requirements.
Those requirements may depend on the product type, the vendor offerings, as well as geographical related regulations.

## 5.7 Vendor <a id='vendor'></a>

Vendor refers to the community, individual, or organization that created or maintains a product (software, hardware,
managed service and other deliverables).
This includes, but is not limited to, open-source software and hardware providers.

# 6. Schema Elements <a id='schema-elements'></a>

The OpenEoX Core schema describes how to represent OpenEoX core information as a JSON document.

The OpenEoX Core schema Version 1.0 builds on the JSON Schema draft 2020-12 rules extended by the format validation
enforcement (see [4.1.5](#format-validation)).

```
  "$schema": "https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json",
```

The schema identifier is:

```
  "$id": "https://docs.oasis-open.org/openeox/v1.0/schema/core.json",
```

The further documentation of the schema is organized via Definitions and Properties.

* Definitions provide types that extend the JSON schema model
* Properties use these types to support assembling OpenEoX core information

Types and properties together provide the vocabulary for the domain specific language supporting OpenEoX information.

The four mandatory properties are `$schema`, `end_of_life`, `end_of_security_support`, and `last_updated`.
The additional property, `end_of_sales`, is optional.

## 6.1 Definitions <a id='schema-elements---definitions'></a>

The definitions (`$defs`) introduce the following domain specific types into the OpenEoX language:
EoX Timestamp (`eox_timestamp_t`).

```
  "$defs": {
    "eox_timestamp_t": {
      // ...
    }
  },
```

### 6.1.1 EoX Timestamp Type <a id='eox-timestamp-type'></a>

The EoX Timestamp (`eox_timestamp_t`) type of value type `string` contains the timestamp at which the product reaches the specified stage or the indicator that this is still 'to be announced'.

```
    "oneOf": [
      {
        "format": "date-time"
      },
      {
        "const": "tba"
      }
    ]
```

Therefore, it MUST either be a `string` with format `date-time` or use the constant value `tba`.

OpenEoX Consumer MUST treat `tba` as a date greater than the maximum date.
In any semantic interpretation, the value `tba` MUST be treated as 'not yet announced'.

## 6.2 Properties <a id='properties'></a>

The following subsections document the five properties of a OpenEoX Core JSON.
The four mandatory properties are `$schema`, `end_of_life`, `end_of_security_support`, and `last_updated`.
The properties `end_of_sales` and `general_availability` are optional.

### 6.2.1 Schema Property <a id='schema-property'></a>

The OpenEoX Core Schema (`$schema`) of value type `string` and `const` specifies the schema the JSON object must be valid against.
The single valid value for this `const` is:

```
  https://docs.oasis-open.org/openeox/v1.0/schema/core.json
```

> This value allows for tools to identify that a JSON document is meant to be valid against this schema.
> Tools can use that to support users by automatically checking whether the OpenEoX Core Object adheres to the JSON schema identified by this URL.

### 6.2.2 End-of-Life Property <a id='end-of-life-property'></a>

End-of-Life (`end_of_life`) of value type `eox_timestamp_t` indicates the last day when the particular product
is officially supported in any way by the vendor.

### 6.2.3 End-of-Sales Property <a id='end-of-sales-property'></a>

End-of-Sales (`end_of_sales`) of value type `eox_timestamp_t` indicates the last day when a particular product may be
ordered by customers from vendor sales channels.

### 6.2.4 End-of-Security-Support Property <a id='end-of-security-support-property'></a>

End-of-Security-Support (`end_of_security_support`) of value type `eox_timestamp_t` indicates the last day when the vendor
has committed to providing security remediations for the particular product.

### 6.2.5 General Availability Property <a id='general-availability-property'></a>

General Availability (`general_availability`) of value type `eox_timestamp_t` indicates the first day when the particular product
is officially launched and made accessible to the general public or through its intended distribution channels.

The following special cases are defined:

* If the value of `general_availability` is equal to the value of `end_of_security_support`, this implies that the product is not supported.
  However, the product may be before its EoL.
* If a product is sunset (in terms of EoL) before its GA,
  the `general_availability` entry SHALL be removed and just the EoL entry kept in the OpenEoX record.
* If the value of `general_availability` is equal to the value of `end_of_life`,
  this implies that the product was published but is not maintained at all.
  
  > An example could be the publication of source code as open source without the intend to maintain it.
  > The clear communication allows others to take over the development as well as to assess the risks associated with using the product.

### 6.2.6 Last Updated Property <a id='last-updated-property'></a>

Timestamp of last change (`last_updated`) of value type `string` with format `date-time` contains the RFC 3339 timestamp when
the record was last updated.

# 7. Tests <a id='tests'></a>

The following subsections list a number of tests which all will have a short description and an excerpt of an example which fails the test.

## 7.1 Mandatory Tests <a id='mandatory-tests'></a>

Mandatory tests MUST NOT fail at a valid OpenEoX Core Information.
A program MUST handle a test failure as an error.

### 7.1.1 Inconsistent EoL Date <a id='inconsistent-eol-date'></a>

It MUST be tested that the `end_of_life` is later than or equal to any other date value in the OpenEoX Core Information.
The property `last_updated` is ignored in this test.
As the timestamps might use different timezones, the sorting MUST take timezones into account.
Except for `end_of_life`, any property of type `eox_timestamp_t` with value `tba` MUST be ignored in the comparison.

The relevant path for this test is:

```
    /end_of_life
```

*Example 1 (which fails the test):*<a id='inconsistent-eol-date-eg-1'></a><a id='sec-7-1-1-eg-1'></a><a id='example-1'></a>

```
  {
    // ...
    "end_of_life": "2025-11-19T16:00:00Z",
    "end_of_security_support": "2025-12-31T12:00:00Z",
    // ...
  }
```

> The `end_of_security_support` is later than the `end_of_life`.

### 7.1.2 Date and Time <a id='mandatory-tests--date-and-time'></a>

For each item of type `string` and format `date-time` it MUST be tested that it conforms to the rules given in section [4.1.6](#date-and-time).
Any property with the value `tba` is ignored in this comparison.

The relevant path for this test is:

```
  /end_of_life
  /end_of_sales
  /end_of_security_support
  /general_availability
  /last_updated
```

*Example 1 (which fails the test):*<a id='mandatory-tests--date-and-time-eg-1'></a><a id='sec-7-1-2-eg-1'></a><a id='example-2'></a>

```
  "end_of_life": "2025-12-31 12:00:00Z",
```

> The `end_of_life` uses a white space as separator instead the letter `T`.

### 7.1.3 Inconsistent GA Date <a id='inconsistent-ga-date'></a>

It MUST be tested that the `general_availability` is earlier than or equal to any other date value in the OpenEoX Core Information.
The property `last_updated` is ignored in this test.
As the timestamps might use different timezones, the sorting MUST take timezones into account.
The test MUST be skipped if the value of `general_availability` is `tba`.
Except for `general_availability`, any property of type `eox_timestamp_t` with value `tba` MUST be ignored in the comparison.

The relevant path for this test is:

```
    /general_availability
```

*Example 1 (which fails the test):*<a id='inconsistent-ga-date-eg-1'></a><a id='sec-7-1-3-eg-1'></a><a id='example-3'></a>

```
  {
    // ...
    "end_of_security_support": "2025-11-19T16:00:00Z",
    "general_availability": "2026-01-21T17:00:00Z",
    // ...
  }
```

> The `general_availability` is later than the `end_of_security_support`.

## 7.2 Recommended Tests <a id='recommended-tests'></a>

Recommended tests SHOULD NOT fail at a valid OpenEoX Core Information without a good reason.
Failing such a test does not make the OpenEoX Core Information invalid.
These tests may include information about features which are still supported but expected to be deprecated in a future version of OpenEoX.
A program MUST handle a test failure as a warning.

### 7.2.1 Use of `tba` where Date is set for EoL <a id='use-of-tba-where-date-is-set-for-eol'></a>

For each property of type `eox_timestamp_t`, it MUST be tested that it does not contain the value `tba` if the `end_of_life` value is set to a date.

The relevant path for this test is:

```
  /end_of_sales
  /end_of_security_support
  /general_availability
```

*Example 1 (which fails the test):*<a id='use-of-tba-where-date-is-set-for-eol-eg-1'></a><a id='sec-7-2-1-eg-1'></a><a id='example-4'></a>

```
  {
    // ...
    "end_of_life": "2025-09-01T12:00:00Z",
    "end_of_security_support": "tba",
    // ...
  }
```

> The `end_of_security_support` is set to `tba` but `end_of_life` already has a date.

> A tool MAY set the `end_of_security_support` to the same value as `end_of_life` as a quick fix.

### 7.2.2 Use of `tba` for GA where other Date is set <a id='use-of-tba-for-ga-where-other-date-is-set'></a>

It MUST be tested that `general_availability` does not contain the value `tba` if any other property of type `eox_timestamp_t` is set to a date.

The relevant path for this test is:

```
  /general_availability
```

*Example 1 (which fails the test):*<a id='use-of-tba-for-ga-where-other-date-is-set-eg-1'></a><a id='sec-7-2-2-eg-1'></a><a id='example-5'></a>

```
  {
    // ...
    "end_of_security_support": "2025-06-17T14:00:00Z",
    "general_availability": "tba",
    // ...
  }
```

> The `general_availability` is set to `tba` but `end_of_security_support` already has a date.

> A tool MAY remove the `general_availability` as a quick fix.

## 7.3 Informative Tests <a id='informative-tests'></a>

Informative tests provide insights in common mistakes and bad practices.
They MAY fail at a valid OpenEoX Core Information.
It is up to the issuing party to decide whether this was an intended behavior and can be ignore or should be treated.
These tests MAY include information about recommended usage.
A program MUST handle a test failure as a information.

### 7.3.1 EoSSec before EoS <a id='eossec-before-eos'></a>

It MUST be tested that if `end_of_sales` is present, its value is before or equal to the value of `end_of_security_support`.
As the timestamps might use different timezones, the sorting MUST take timezones into account.
The test MUST be skipped, if `end_of_sales` is set to `tba`.


The relevant path for this test is:

```
    /end_of_sales
```

*Example 1 (which fails the test):*<a id='eossec-before-eos-eg-1'></a><a id='sec-7-3-1-eg-1'></a><a id='example-6'></a>

```
  {
    // ...
    "end_of_sales": "2025-12-31T12:00:00Z",
    "end_of_security_support": "2025-11-19T16:00:00Z",
    // ...
  }
```

> The `end_of_security_support` is earlier than the `end_of_sales`.

# 8. Safety, Security and Data Protection <a id='safety-security-and-data-protection'></a>

All safety, security, and data protection requirements relevant to the context in which OpenEoX information items are used MUST
be translated into, and consistently enforced through, OpenEoX implementations and processes.

OpenEoX information items are based on JSON, thus the security considerations of \[[RFC8259](#RFC8259)\] apply and
are repeated here as service for the reader:

> Generally, there are security issues with scripting languages.  JSON is a subset of JavaScript but excludes assignment and invocation.
>
> Since JSON's syntax is borrowed from JavaScript, it is possible to use that language's `eval()` function to parse most JSON texts
> (but not all; certain characters such as `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript).
> This generally constitutes an unacceptable security risk, since the text could contain executable code along with data declarations.
> The same consideration applies to the use of eval()-like functions in any other programming language in which JSON texts conform to that language's syntax.

-------

# 9. Conformance <a id='conformance'></a>

The single subsection of this section lists the conformance targets and clauses.
The clauses directly corresponding to the targets are listed in separate sub-subsections of the target list subsection.

> The order in which targets, and their corresponding clauses appear is somewhat arbitrary as there is
> no natural order on such diverse roles participating in the EoX exchanging ecosystem.

## 9.1 Conformance Targets <a id='conformance-targets'></a>

This document defines requirements for the file format and for certain software components that interact with it.
The entities ("conformance targets") for which this document defines requirements are:

* **OpenEoX Core Information**: An EoX information in the format defined by this document.
* **OpenEoX Core Producer**: A program which emits output in the OpenEoX Core format.
* **OpenEoX Core Consumer**: A program that reads and interprets OpenEoX Core Information.
* **OpenEoX Core Basic Validator**: A program that reads a JSON object and checks it against the JSON schema and performs mandatory tests.
* **OpenEoX Core Extended Validator**: A OpenEoX Core Basic Validator that additionally performs recommended tests.
* **OpenEoX Core Full Validator**: A OpenEoX Core Extended Validator that additionally performs guidance tests.
* **OpenEoX Core Library**: A library that implements OpenEoX Core data capabilities.
* **OpenEoX Core Library with Basic Validation**: A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Basic Validator".
* **OpenEoX Core Library with Extended Validation**: A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Extended Validator".
* **OpenEoX Core Library with Full Validation**: A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Full Validator".
* **OpenEoX Core Differ**: A program that compares OpenEoX Core Information and calculates the changes.
* **OpenEoX Core Comparator**: A program that compares OpenEoX Core Information and returns the newer one.
* **OpenEoX Core Sorter**: A program that sorts OpenEoX Core Information from newest to oldest or vice versa.
* **OpenEoX Core Merger**: A program that combines OpenEoX Core Information.

### 9.1.1 Conformance Clause 1: OpenEoX Core Information <a id='conformance-clause-1-openeox-core-information'></a>

A text file or data stream satisfies the "OpenEoX Core Information" conformance profile if it:

* conforms to the syntax and semantics defined in section [4.1.5](#format-validation).
* conforms to the syntax and semantics defined in section [4.1.6](#date-and-time).
* conforms to the syntax and semantics defined in section [6](#schema-elements).
* does not fail any mandatory test defined in section [7.1](#mandatory-tests).

### 9.1.2 Conformance Clause 2: OpenEoX Core Producer <a id='conformance-clause-2-openeox-core-producer'></a>

A program satisfies the "OpenEoX Core Producer" conformance profile if the program:

* produces output in the OpenEoX Core format, according to the conformance profile "OpenEoX Core Information".
* satisfies those normative requirements in section [6](#schema-elements) and
  [8](#safety-security-and-data-protection) that are designated as applying to OpenEoX Producers.

### 9.1.3 Conformance Clause 3: OpenEoX Core Consumer <a id='conformance-clause-3-openeox-core-consumer'></a>

A processor satisfies the "OpenEoX Core Consumer" conformance profile if the processor:

* reads OpenEoX Core Information and interprets them according to the semantics defined in section [6](#schema-elements).
* satisfies those normative requirements in section [6](#schema-elements) and
  [8](#safety-security-and-data-protection) that are designated as applying to OpenEoX Consumers.

### 9.1.4 Conformance Clause 4: OpenEoX Core Basic Validator <a id='conformance-clause-4-openeox-core-basic-validator'></a>

A program satisfies the "OpenEoX Core Basic Validator" conformance profile if the program:

* reads JSON objects and performs a check against the JSON schema.
* performs all mandatory tests as given in section [7.1](#mandatory-tests).
* does not change the OpenEoX Core Information.

A OpenEoX Core Basic Validator MAY provide one or more additional functions:

* Only run one or more selected mandatory tests.
* Apply quick fixes as specified in the standard.
* Apply additional quick fixes as implemented by the vendor.

### 9.1.5 Conformance Clause 5: OpenEoX Core Extended Validator <a id='conformance-clause-5-openeox-core-extended-validator'></a>

A OpenEoX Core Basic Validator satisfies the "OpenEoX Core Extended Validator" conformance profile if the OpenEoX Core Basic Validator:

* satisfies the "OpenEoX Core Basic Validator" conformance profile.
* additionally performs all recommended tests as given in section [7.2](#recommended-tests).
* provides a function that allows to specify tests for which test results of warning are reported as error.

A OpenEoX Core Extended Validator MAY provide an additional function to only run one or more selected recommended tests.

### 9.1.6 Conformance Clause 6: OpenEoX Core Full Validator <a id='conformance-clause-6-openeox-core-full-validator'></a>

A OpenEoX Core Extended Validator satisfies the "OpenEoX Core Full Validator" conformance profile if the OpenEoX Core Extended Validator:

* satisfies the "OpenEoX Core Extended Validator" conformance profile.
* additionally performs all guidance tests as given in section [7.3](#informative-tests).
* provides a function that allows to specify tests for which test results of information are reported as warning.
* provides a function that allows to specify tests for which test results of information are reported as error.

A OpenEoX Core Full Validator MAY provide an additional function to only run one or more selected guidance tests.

### 9.1.7 Conformance Clause 7: OpenEoX Core Library <a id='conformance-clause-7-openeox-core-library'></a>

A library satisfies the "OpenEoX Core Library" conformance profile if the library:

* implements all elements as data structures conforming to the syntax and semantics defined in sections
  [4.1.5](#format-validation), [4.1.6](#date-and-time) and [6](#schema-elements).
* checks all elements according to the patterns provided in the JSON schema.
* has a function that reads OpenEoX Core Information into the data structure from a
  * file system.
  * URL.
  * data stream.
* provides function for sorting the keys and sorts the keys automatically on output.
* has a function that outputs the data structure as OpenEoX Core Information
  * on the file system.
  * as string.
  * into a data stream.

The library MAY implement an option to retrieve the keys unsorted.

### 9.1.8 Conformance Clause 8: OpenEoX Core Library with Basic Validation <a id='conformance-clause-8-openeox-core-library-with-basic-validation'></a>
-1
A OpenEoX Core Library satisfies the "OpenEoX Core Library with Basic Validation" conformance profile if the OpenEoX Core Library:

* satisfies the "OpenEoX Core Library" conformance profile.
* satisfies the "OpenEoX Core Basic Validator" conformance profile.
* validates the OpenEoX Core Information before output according to the "OpenEoX Core Basic Validator" and
  presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "OpenEoX Core Basic Validator"
  and presents the validation result accordingly.

A OpenEoX Core Library does not satisfies the "OpenEoX Core Library with Basic Validation" conformance profile if the OpenEoX Core
Library uses an external library or program for the "OpenEoX Core Basic Validator" part and does not enforce its presence.

### 9.1.9 Conformance Clause 9: OpenEoX Core Library with Extended Validation <a id='conformance-clause-9-openeox-core-library-with-extended-validation'></a>

A OpenEoX Core Library satisfies the "OpenEoX Core Library with Extended Validation" conformance profile if the OpenEoX Core Library:

* satisfies the "OpenEoX Core Library" conformance profile.
* satisfies the "OpenEoX Core Extended Validator" conformance profile.
* validates the OpenEoX Core Information before output according to the "OpenEoX Core Extended Validator" and
  presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "OpenEoX Core Extended Validator"
  and presents the validation result accordingly.

A OpenEoX Core Library does not satisfies the "OpenEoX Core Library with Extended Validation" conformance profile if the OpenEoX Core
Library uses an external library or program for the "OpenEoX Core Extended Validator" part and does not enforce its presence.

### 9.1.10 Conformance Clause 10: OpenEoX Core Library with Full Validation <a id='conformance-clause-10-openeox-core-library-with-full-validation'></a>

A OpenEoX Core Library satisfies the "OpenEoX Core Library with Extended Validation" conformance profile if the OpenEoX Core Library:

* satisfies the "OpenEoX Core Library" conformance profile.
* satisfies the "OpenEoX Core Full Validator" conformance profile.
* validates the OpenEoX Core Information before output according to the "OpenEoX Core Full Validator" and
  presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "OpenEoX Core Full Validator" and
  presents the validation result accordingly.

A OpenEoX Core Library does not satisfies the "OpenEoX Core Library with Full Validation" conformance profile if the OpenEoX Core
Library uses an external library or program for the "OpenEoX Core Full Validator" part and does not enforce its presence.

### 9.1.11 Conformance Clause 11: OpenEoX Core Differ <a id='conformance-clause-11-openeox-core-differ'></a>

A program satisfies the "OpenEoX Core Differ" conformance profile if the program:

* satisfies the "OpenEoX Core Consumer" conformance profile.
* calculates the difference between two OpenEoX Core Information JSON Objects and presents it as JSON Diff.

A OpenEoX Core Differ MAY choose to make that information also available in other data formats.

### 9.1.12 Conformance Clause 12: OpenEoX Core Comparator <a id='conformance-clause-12-openeox-core-comparator'></a>

A program satisfies the "OpenEoX Core Comparator" conformance profile if the program:

* satisfies the "OpenEoX Core Consumer" conformance profile.
* provides a function to compares two OpenEoX Core Information Objects `a` and `b` based on their `last_updated` value and returns:
  * `-1` if `a["last_updated"] < b["last_updated"]`
  * `0` if `a["last_updated"] = b["last_updated"]`
  * `1` if `a["last_updated"] > b["last_updated"]`
* provides a function to compares two OpenEoX Core Information Objects `a` and `b` based on their `last_updated` value and returns:
  * `b` if `a["last_updated"] < b["last_updated"]`
  * `a` if `a["last_updated"] = b["last_updated"]`
  * `a` if `a["last_updated"] > b["last_updated"]`
* takes timezones into account.

A OpenEoX Core Comparator MAY choose to make that information also available in other data formats.

### 9.1.13 Conformance Clause 13: OpenEoX Core Sorter <a id='conformance-clause-13-openeox-core-sorter'></a>

A program satisfies the "OpenEoX Core Sorter" conformance profile if the program:

* satisfies the "OpenEoX Core Consumer" conformance profile.
* provides a function to sort an arbitrary number of OpenEoX Core Information Objects `last_updated` value with that value descending (default).
* provides a function to sort an arbitrary number of OpenEoX Core Information Objects `last_updated` value with that value ascending.
* takes timezones into account.

A OpenEoX Core Sorter MAY choose to make that information also available in other data formats.

### 9.1.14 Conformance Clause 14: OpenEoX Core Merger <a id='conformance-clause-14-openeox-core-merger'></a>

A program satisfies the "OpenEoX Core Merger" conformance profile if the program:

* satisfies the "OpenEoX Core Consumer" conformance profile.
* provides a function to merge OpenEoX Core Information into a single OpenEoX Core Information Object by overwriting all old values
  of keys present in newer OpenEoX Core Information Objects with the values from newer objects.

  > This includes the value of `last_updated`.

* provides a function to merge OpenEoX Core Information into a single OpenEoX Core Information Object by overwriting all old values
  of keys present in newer OpenEoX Core Information Objects with the values from newer objects but treating `tba` as not present during
  the overwrite process.

  > This includes the value of `last_updated`.
  > Ignoring `tba` while overwriting ensures that a date value is never overwritten by `tba`.

* provides a function to merge OpenEoX Core Information into a single OpenEoX Core Information Object by taking the newest as base
  and iterative appending keys that are not present in that object while iterating over the OpenEoX Core Information from newest to oldest.

  > As `last_updated` is a required field, it is not changed during the process.
  > Values of keys that are inserted are never changed in that process.

* takes timezones into account.

A program MAY implement other algorithms than defined here, if and only if, the results are guaranteed to be the same.

A OpenEoX Core Merger MAY choose to make that information also available in other data formats.

-------


# Annex A License, Document Status and Notices <a id='annex-a'></a>

(This annex forms an integral part of this Specification.)


## A.1. Document Status <a id='document-status'></a>

This document was last revised or approved by the OASIS OpenEoX TC on the above date. The level of approval is also listed above. Check the "Latest version" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at <https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=26350f39-9c7b-4bf2-a422-018dc7d3f5aa>.

TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at <https://www.oasis-open.org/committees/openeox/>.

NOTE: any machine-readable content (Computer Language Definitions) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.


## A.2. License and Notices <a id='license-and-notices'></a>

<!-- Required section. Do not modify. -->

Copyright &copy; OASIS Open 2026. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full Policy, which governs the licensure of this document, may be found at the OASIS website: [[https://www.oasis-open.org/policies-guidelines/ipr/](https://www.oasis-open.org/policies-guidelines/ipr/)]

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns, as provided in the OASIS IPR Policy.

This document is provided under the “Non-Assertion” IPR mode that was chosen when the project was established, as defined in the IPR Policy. For information on whether any patents have been disclosed that may be essential to implementing this document, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the project’s web page ([https://www.oasis-open.org/committees/openeox/ipr.php](https://www.oasis-open.org/committees/openeox/ipr.php)).

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. OASIS AND ITS MEMBERS WILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF ANY USE OF THIS DOCUMENT OR ANY PART THEREOF.

As stated in the OASIS IPR Policy, the following three paragraphs in brackets apply to OASIS Standards Final Deliverable documents (Committee Specifications, OASIS Standards, or Approved Errata).

OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this deliverable.

OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this OASIS Standards Final Deliverable. OASIS may include such claims on its website, but disclaims any obligation to do so.

OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this OASIS Standards Final Deliverable or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Standards Final Deliverable, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.

The name "OASIS" is a trademark of OASIS, the owner and developer of this document, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, its documents, while reserving the right to enforce its marks against misleading uses. Please see [https://www.oasis-open.org/policies-guidelines/trademark/](https://www.oasis-open.org/policies-guidelines/trademark/) for guidance.

-------

# Annex B References <a id='references'></a>

(This annex forms an integral part of this Specification.)

This section contains the normative and informative references that are used in this document.

Normative references are specific (identified by date of publication and/or edition number or version number) and Informative references are either specific or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the reference document (including any amendments) applies. While any hyperlinks included in this section were valid at the time of publication, OASIS cannot guarantee their long term validity.

## B.1 Normative References <a id='normative-references'></a>

The following documents are referenced in such a way that some or all of their content constitutes requirements of this document.

**\[**<span id="ECMA-262" class="anchor"></span>**ECMA-262\]** _ECMAScript® 2024 Language Specification_, ECMA-262, 15th edition, June 2024, <https://262.ecma-international.org/15.0/>

**\[**<span id="ISO8601-1" class="anchor"></span>**ISO8601-1\]** _Date and time — Representations for information interchangePart 1: Basic rules_, International Standard, ISO 8601-1:2019(E), February 25, 2019, <https://www.iso.org/standard/70907.html>.

**\[**<span id="JSON-Schema-Core" class="anchor"></span>**JSON-Schema-Core\]** _JSON Schema: A Media Type for Describing JSON Documents_, draft-bhutton-json-schema-00, December 2020, <https://datatracker.ietf.org/doc/html/draft-bhutton-json-schema-00>.

**\[**<span id="JSON-Schema-Validation" class="anchor"></span>**JSON-Schema-Validation\]** _JSON Schema Validation: A Vocabulary for Structural Validation of JSON_, draft-bhutton-json-schema-validation-00, December 2020, <https://datatracker.ietf.org/doc/html/draft-bhutton-json-schema-validation-00>.

**\[**<span id="JSON-Hyper-Schema" class="anchor"></span>**JSON-Hyper-Schema\]** _JSON Hyper-Schema: A Vocabulary for Hypermedia Annotation of JSON_, draft-handrews-json-schema-hyperschema-02, September 2019, <https://json-schema.org/draft/2019-09/json-schema-hypermedia.html>.

**\[**<span id="Relative-JSON-Pointers" class="anchor"></span>**Relative-JSON-Pointers\]** _Relative JSON Pointers_, draft-bhutton-relative-json-pointer-00, December 2020, <https://datatracker.ietf.org/doc/html/draft-bhutton-relative-json-pointer-00>.

**\[**<span id="RFC2119" class="anchor"></span>**RFC2119\]** Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, <https://www.rfc-editor.org/info/rfc2119>.

**\[**<span id="RFC3339" class="anchor"></span>**RFC3339\]** Klyne, G. and C. Newman, "Date and Time on the Internet: Timestamps", RFC 3339, DOI 10.17487/RFC3339, July 2002, <https://www.rfc-editor.org/info/rfc3339>.

**\[**<span id="RFC4180" class="anchor"></span>**RFC4180\]** Shafranovich, Y., "Common Format and MIME Type for Comma-Separated Values (CSV) Files", RFC 4180, DOI 10.17487/RFC4180, October 2005, <https://www.rfc-editor.org/info/rfc4180>.

**\[**<span id="RFC7230" class="anchor"></span>**RFC7230\]** Roy T. Fielding and Julian Reschke, "Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing", RFC 7230, DOI 10.17487/RFC7230, June 2014, <https://www.rfc-editor.org/info/rfc7230>.

**\[**<span id="RFC7464" class="anchor"></span>**RFC7464\]** Williams, N., "JavaScript Object Notation (JSON) Text Sequences", RFC 7464, DOI 10.17487/RFC7464, February 2015, <https://www.rfc-editor.org/info/rfc7464>.

**\[**<span id="RFC8174" class="anchor"></span>**RFC8174\]** Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, <https://www.rfc-editor.org/info/rfc8174>.

**\[**<span id="RFC8259" class="anchor"></span>**RFC8259\]** T. Bray, Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 8259, DOI 10.17487/RFC8259, December 2017, <https://www.rfc-editor.org/info/rfc8259>.

**\[**<span id="RFC9562" class="anchor"></span>**RFC9562\]** Davis, K., Peabody, B., and P. Leach, "Universally Unique IDentifiers (UUIDs)", RFC 9562, DOI 10.17487/RFC9562, May 2024, <https://www.rfc-editor.org/info/rfc9562>.

**\[**<span id="SPDX301" class="anchor"></span>**SPDX301\]** _The System Package Data Exchange® (SPDX®) Specification Version 3.0.1_, Linux Foundation and its Contributors, 2024, <https://spdx.github.io/spdx-spec/>.

## B.2 Informative References <a id='informative-references'></a>

The following referenced documents are not required for the application of this document but may assist the reader with regard to a particular subject area.

**\[**<span id="CSAF-v2.1" class="anchor"></span>**CSAF-v2.1\]** _Common Security Advisory Framework Version 2.1_. Edited by Stefan Hagen, and Thomas Schmidt. 28 May 2025. OASIS Committee Specification Draft 01. https://docs.oasis-open.org/csaf/csaf/v2.1/csd01/csaf-v2.1-csd01.html. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html.

# Appendix 1 Acknowledgments <a id='acknowledgments'></a>

(This appendix does not form an integral part of this Specification and is informational.)

The following individuals were members of the OASIS OpenEoX Technical Committee during the creation of this specification and their contributions are gratefully acknowledged:

## Leadership <a id='leadership'></a>

The following individuals have had significant leadership positions during the development of this document, not just this version of the document, and they are gratefully acknowledged:

* Chairs:
  * Co-Chair, Justin Murphy (justin.murphy@mail.cisa.dhs.gov), [DHS Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov)
  * Co-Chair, Omar Santos (osantos@cisco.com), [Cisco Systems](https://cisco.com/)

* Secretaries:
  * Secretary, Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/)

* Editors
  * Editor, Jautau White (jaywhite@microsoft.com), Microsoft Corporation
  * Editor, Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/)
  * Editor, Thomas Schmidt (thomas.schmidt@bsi.bund.de), [Federal Office for Information Security (BSI) Germany](https://www.bsi.bund.de/)

## Special Thanks <a id='special-thanks'></a>

The following individuals have made substantial contributions to this document, not just this version of the document, and their contributions are gratefully acknowledged:

tbd

## Participants <a id='participants'></a>

The following individuals were members of this committee during the creation of this document, not just this version of the document, and their contributions are gratefully acknowledged:

tbd

-------

# Appendix 2 Changes From Previous Version <a id='changes-from-previous-version'></a>

(This appendix does not form an integral part of this Specification and is informational.)

N/A.

##  Revision History <a id='revision-history'></a>

| Revision                     | Date       | Editor                                         | Changes Made                      |
|:-----------------------------|:-----------|:-----------------------------------------------|:----------------------------------|
| eox-core-v1.0-wd20250716-dev | 2025-07-16 | Jautau White, Stefan Hagen, and Thomas Schmidt | Preparing initial Editor Revision |
| eox-core-v1.0-wd20250820-dev | 2025-08-20 | Jautau White, Stefan Hagen, and Thomas Schmidt | Editor Revision with first structure |
| eox-core-v1.0-wd20251119-dev | 2025-11-19 | Jautau White, Stefan Hagen, and Thomas Schmidt | Editor Revision for TC review     |
| eox-core-v1.0-wd20260121-dev | 2026-01-21 | Jautau White, Stefan Hagen, and Thomas Schmidt | Editor Revision for TC review     |
| eox-core-v1.0-wd20260218-dev | 2026-02-18 | Jautau White, Stefan Hagen, and Thomas Schmidt | Editor Revision for TC review     |

-------

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
