
![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------

# OpenEoX Shell Schema Version 1.0

## Committee Specification Draft 01

## 15 March 2026

### This Version

https://docs.oasis-open.org/openeox/eox-shell/v1.0/csd01/eox-shell-v1.0-csd01.md (Authoritative) \
https://docs.oasis-open.org/openeox/eox-shell/v1.0/csd01/eox-shell-v1.0-csd01.html \
https://docs.oasis-open.org/openeox/eox-shell/v1.0/csd01/eox-shell-v1.0-csd01.pdf

### Previous Version

N/A

### Latest Version

https://docs.oasis-open.org/openeox/eox-shell/v1.0/eox-shell-v1.0.md (Authoritative) \
https://docs.oasis-open.org/openeox/eox-shell/v1.0/eox-shell-v1.0.html \
https://docs.oasis-open.org/openeox/eox-shell/v1.0/eox-shell-v1.0.pdf

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

* OpenEoX SHell JSON schema: https://docs.oasis-open.org/openeox/eox-shell/v1.0/csd01/schema/eox-shell.json. \
Latest stage: https://docs.oasis-open.org/openeox/eox-shell/v1.0/schema/eox-shell.json.
* OpenEoX Meta JSON schema: https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/schema/meta.json. \
Latest stage: https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json.

### Declared JSON namespaces

* [https://docs.oasis-open.org/openeox/eox-shell/v1.0/schema/eox-shell.json](https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json)
* [https://docs.oasis-open.org/openeox/eox-shell/v1.0/schema/meta.json](https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json)

### Abstract

The OpenEoX Shell Schema defines the shell schemata for the OpenEoX unified machine-readable approach to
managing and sharing General Availability (GA), End-of-Sales (EoS), End-of-Life (EoL), and
End-of-Security-Support (EoSSec) information for commercial and open source software and hardware.

### Citation Format

When referencing this document, the following citation format should be used:

**\[EoX-Shell-v1.0]**

_OpenEoX Shell Schema Version 1.0_.
Edited by Jautau White, Stefan Hagen, and Thomas Schmidt.
15 March 2026.
OASIS Committee Specification Draft 01.
https://docs.oasis-open.org/openeox/eox-shell/v1.0/csd01/eox-shell-v1.0-csd01.html.\
Latest stage: https://docs.oasis-open.org/openeox/eox-shell/v1.0/eox-shell-v1.0.html

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
			4.1.1.1 [OpenEoX Core](#openeox-core)  
			4.1.1.2 [OpenEoX Shell (this specification)](#openeox-shell-this-specification)  
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
	6.2 [Properties](#properties)  
		6.2.1 [Schema Property](#schema-property)  
7. [Tests](#tests)  
	7.1 [Mandatory Tests](#mandatory-tests)  
	7.2 [Recommended Tests](#recommended-tests)  
	7.3 [Informative Tests](#informative-tests)  
8. [Safety, Security and Data Protection](#safety-security-and-data-protection)  
9. [Conformance](#conformance)  
	9.1 [Conformance Targets](#conformance-targets)  
		9.1.1 [Conformance Clause 1: TBC](#conformance-clause-1-tbc)  
Annex A [License, Document Status and Notices](#annex-a)  
	A.1. [Document Status](#document-status)  
	A.2. [License and Notices](#license-and-notices)  
Annex B [References](#references)  
	B.1. [Normative References](#normative-references)  
	B.2. [Informative References](#informative-references)  
Appendix 1 [Acknowledgments](#acknowledgments)  
	 [Leadership](#leadership)  
	 [Special Thanks](#special-thanks)  
	 [Participants](#participants)  
Appendix 2 [Changes From Previous Version](#changes-from-previous-version)  
	 [Revision History](#revision-history)  
-------

# 1. Scope <a id='scope'></a>

TBC

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

#### 4.1.1.1 OpenEoX Core <a id='openeox-core'></a>

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

#### 4.1.1.2 OpenEoX Shell (this specification) <a id='openeox-shell-this-specification'></a>

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
    "$id": "https://docs.oasis-open.org/openeox/eox-shell/v1.0/schema/meta.json",
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
    "$schema": "https://docs.oasis-open.org/openeox/eox-shell/v1.0/schema/meta.json",
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

TBC

## 6.1 Definitions <a id='schema-elements---definitions'></a>

TBC

## 6.2 Properties <a id='properties'></a>

TBC

### 6.2.1 Schema Property <a id='schema-property'></a>

The OpenEoX Core Schema (`$schema`) of value type `string` and `const` specifies the schema the JSON object must be valid against.
The single valid value for this `const` is:

```
  https://docs.oasis-open.org/openeox/v1.0/schema/shell.json
```

> This value allows for tools to identify that a JSON document is meant to be valid against this schema.
> Tools can use that to support users by automatically checking whether the OpenEoX Core Object adheres to the JSON schema identified by this URL.

# 7. Tests <a id='tests'></a>

The following subsections list a number of tests which all will have a short description and an excerpt of an example which fails the test.

## 7.1 Mandatory Tests <a id='mandatory-tests'></a>

Mandatory tests MUST NOT fail at a valid OpenEoX Shell Information.
A program MUST handle a test failure as an error.

## 7.2 Recommended Tests <a id='recommended-tests'></a>

Recommended tests SHOULD NOT fail at a valid OpenEoX Shell Information without a good reason.
Failing such a test does not make the OpenEoX Shell Information invalid.
These tests may include information about features which are still supported but expected to be deprecated in a future version of OpenEoX.
A program MUST handle a test failure as a warning.

## 7.3 Informative Tests <a id='informative-tests'></a>

Informative tests provide insights in common mistakes and bad practices.
They MAY fail at a valid OpenEoX Shell Information.
It is up to the issuing party to decide whether this was an intended behavior and can be ignore or should be treated.
These tests MAY include information about recommended usage.
A program MUST handle a test failure as a information.

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

TBC

### 9.1.1 Conformance Clause 1: TBC <a id='conformance-clause-1-tbc'></a>

TBC

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

## B.1. Normative References <a id='normative-references'></a>

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

## B.2. Informative References <a id='informative-references'></a>

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

## Revision History <a id='revision-history'></a>

| Revision                      | Date       | Editor                                         | Changes Made                      |
|:------------------------------|:-----------|:-----------------------------------------------|:----------------------------------|
| eox-shell-v1.0-wd20250716-dev | 2025-07-16 | Jautau White, Stefan Hagen, and Thomas Schmidt | Editor Revision for TC review     |

-------

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
