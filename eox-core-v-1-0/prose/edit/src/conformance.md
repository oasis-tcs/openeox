# Conformance

In the only subsection of this section, the conformance targets and clauses are listed.
The clauses, matching the targets one to one, are listed in separate sub-subsections of the targets listing subsection.

Informative Comments:

> The order in which targets, and their corresponding clauses appear is somewhat arbitrary as there is
> no natural order on such diverse roles participating in the EoX exchanging ecosystem.

## Conformance Targets

This document defines requirements for the file format and for certain software components that interact with it.
The entities ("conformance targets") for which this document defines requirements are:

* **OpenEoX Core Consumer**: A program that reads and interprets OpenEoX Core Information.
* **OpenEoX Core Information**: An EoX information in the format defined by this document.
* **OpenEoX Core Library**: A library that implements OpenEoX Core data capabilities.
* **OpenEoX Core Producer**: A program which emits output in the OpenEoX Core format.

### Conformance Clause 1: OpenEoX Core Information

A text file or data stream satisfies the "OpenEoX Core Information" conformance profile if it:

* conforms to the syntax and semantics defined in section [sec](#format-validation).
* conforms to the syntax and semantics defined in section [sec](#date-and-time).
* conforms to the syntax and semantics defined in section [sec](#schema-elements).
* does not fail any mandatory test defined in section [sec](#mandatory-tests).

### Conformance Clause 2: OpenEoX Core Producer

A program satisfies the "OpenEoX Core Producer" conformance profile if the program:

* produces output in the OpenEoX Core format, according to the conformance profile "OpenEoX Core Information".
* satisfies those normative requirements in section [sec](#schema-elements) and
  [sec](#safety-security-and-data-protection-considerations) that are designated as applying to OpenEoX Producers.

### Conformance Clause 3: OpenEoX Core Consumer

A processor satisfies the "OpenEoX Core Consumer" conformance profile if the processor:

* reads OpenEoX Core Information and interprets them according to the semantics defined in section [sec](#schema-elements).
* satisfies those normative requirements in section [sec](#schema-elements) and
  [sec](#safety-security-and-data-protection-considerations) that are designated as applying to OpenEoX Consumers.

### Conformance Clause 4: OpenEoX Core Library

A library satisfies the "OpenEoX Core Library" conformance profile if the library:

* implements all elements as data structures conforming to the syntax and semantics defined in section
  [sec](#date-and-time) and [sec](#schema-elements).
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

-------
