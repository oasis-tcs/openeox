# Definitions and Acronyms

## Definitions

### Terms Defined Elsewhere

This document uses the following terms defined elsewhere:

* Embedded Link: [csaf-v2.1]:
  syntactic construct which enables a message string to refer to a location mentioned in the document.  
* Empty Array: [csaf-v2.1]:
  array that contains no elements, and so has a length of zero.
* Empty Object: [csaf-v2.1]:
  object that contains no properties.
* Empty String: [csaf-v2.1]:
  string that contains no characters, and so has a length of zero.
* (End) User: [csaf-v2.1]:
  person who uses the information in a document to investigate, triage, or resolve results.
* Product: [csaf-v2.1]:
  is any deliverable (e.g. software, hardware, specification, or service) which can be referred to with a name.
  This applies regardless of the origin, the license model, or the mode of distribution of the deliverable.
* Property: [csaf-v2.1]:
  attribute of an object consisting of a name and a value associated with the name.
* Triage: [csaf-v2.1]:
  decide whether a result indicates a problem that needs to be corrected.
* User: [csaf-v2.1]:
  see end user.
* Vendor: [csaf-v2.1]:
  the community, individual, or organization that created or maintains a product
  (including open source software and hardware providers).
* White Space: [csaf-v2.1]:
  code point used to improve text readability or token separation as defined in section 12.2 of [cite](#ECMA-262).

### Terms Defined in this Document

This document defines the following terms:

* End-of-Life (EoL):
  indicates the last day when the particular product (or the product version/release)
  is officially supported in any way by the vendor.
* End-of-Sales (EoS):
  indicates the last day when a particular product (or the product version/release)
  may be ordered by customers from vendor sales channels.
* End-of-Security-Support (EoSSec):
  indicates the last day when the vendor has committed to providing security remediations
  for the particular product (or the product version/release).
* General Availability (GA):
  indicates the first day when the particular product (or the product version/release) is officially
  launched and made accessible to the general public or through its intended distribution channels.
* Product Life Cycle:
  describes for a product type (software, hardware, managed service and other deliverables) the model it can be associated with.
  It can contain definitions of various support models (different levels of maintenance) in association to
  the product versioning convention.
* OpenEoX Core Basic Validator:
  A program that reads a JSON object and checks it against the JSON schema and performs mandatory tests.
* OpenEoX Core Comparator:
  A program that compares OpenEoX Core Information and returns the newer one.
* OpenEoX Core Consumer:
  A program that reads and interprets OpenEoX Core Information.
* OpenEoX Core Differ:
  A program that compares OpenEoX Core Information and calculates the changes.
* OpenEoX Core Extended Validator:
  A OpenEoX Core Basic Validator that additionally performs recommended tests.
* OpenEoX Core Full Validator:
  A OpenEoX Core Extended Validator that additionally performs guidance tests.
* OpenEoX Core Information:
  An EoX information in the format defined by this document.
* OpenEoX Core Library:
  A library that implements OpenEoX Core data capabilities.
* OpenEoX Core Library with Basic Validation:
  A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Basic Validator".
* OpenEoX Core Library with Extended Validation:
  A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Extended Validator".
* OpenEoX Core Library with Full Validation:
  A OpenEoX Core Library that also satisfies the conformance target "OpenEoX Core Full Validator".
* OpenEoX Core Merger:
  A program that combines OpenEoX Core Information.
* OpenEoX Core Producer:
  A program which emits output in the OpenEoX Core format.
* OpenEoX Core Sorter:
  A program that sorts OpenEoX Core Information from newest to oldest or vice versa.
* Redactable Property:
  property that potentially contains sensitive information that a OpenEoX Producer might wish to redact.
* Taxonomy:
  classification of product life cycle stages into a set of categories.

## Abbreviations and Acronyms

This document uses the following abbreviations and acronyms:

* EoL: End-of-Life.  
* EoS: End-of-Sales.  
* EoSSec: End-of-Security-Support.
* EoX: End-of-X.
* GA: General Availability.

------
