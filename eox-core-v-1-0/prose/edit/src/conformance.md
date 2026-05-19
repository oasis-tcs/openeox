# Conformance

The single subsection of this section lists the conformance targets and clauses.
The clauses directly corresponding to the targets are listed in separate sub-subsections of the target list subsection.

> The order in which targets, and their corresponding clauses appear is somewhat arbitrary as there is
> no natural order on such diverse roles participating in the EoX exchanging ecosystem.

## Conformance Targets

This document defines requirements for the file format and for certain software components that interact with it.
The entities ("conformance targets") for which this document defines requirements are:

* **EoX Core Information**: Information about end-of-anything in the format defined by this document.
* **EoX Core Producer**: A program which emits output in the EoX Core format.
* **EoX Core Consumer**: A program that reads and interprets EoX Core Information.
* **EoX Core Viewer**: An EoX Consumer that reads EoX Core Information, displays a list of the results it contains,
  and allows an end user to view each result in the context of the artifact in which it occurs.
* **EoX Core Recommending Viewer**: An EoX Viewer that provides actionable interpretations by mapping life cycle events to recommended actions.
* **EoX Core Basic Validator**: A program that reads a JSON object and checks it against the JSON schema and performs mandatory tests.
* **EoX Core Extended Validator**: A EoX Core Basic Validator that additionally performs recommended tests.
* **EoX Core Full Validator**: A EoX Core Extended Validator that additionally performs guidance tests.
* **EoX Core Library**: A library that implements EoX Core data capabilities.
* **EoX Core Library with Basic Validation**: A EoX Core Library that also satisfies the conformance target "EoX Core Basic Validator".
* **EoX Core Library with Extended Validation**: A EoX Core Library that also satisfies the conformance target "EoX Core Extended Validator".
* **EoX Core Library with Full Validation**: A EoX Core Library that also satisfies the conformance target "EoX Core Full Validator".
* **EoX Core Differ**: A program that compares EoX Core Information and calculates the changes.
* **EoX Core Comparator**: A program that compares EoX Core Information and returns the newer one.
* **EoX Core Sorter**: A program that sorts EoX Core Information from newest to oldest or vice versa.
* **EoX Core Merger**: A program that combines EoX Core Information.

### Conformance Clause 1: EoX Core Information

A text file or data stream satisfies the "EoX Core Information" conformance profile if it:

* conforms to the syntax and semantics defined in section [sec](#format-validation).
* conforms to the syntax and semantics defined in section [sec](#date-and-time).
* conforms to the syntax and semantics defined in section [sec](#schema-elements).
* does not fail any mandatory test defined in section [sec](#mandatory-tests).

### Conformance Clause 2: EoX Core Producer

A program satisfies the "EoX Core Producer" conformance profile if the program:

* produces output in the EoX Core format, according to the conformance profile "EoX Core Information".
* satisfies those normative requirements in section [sec](#schema-elements) and
  [sec](#safety-security-and-data-protection) that are designated as applying to EoX Producers.

### Conformance Clause 3: EoX Core Consumer

A processor satisfies the "EoX Core Consumer" conformance profile if the processor:

* reads EoX Core Information and interprets them according to the semantics defined in section [sec](#schema-elements).
* satisfies those normative requirements in section [sec](#schema-elements) and
  [sec](#safety-security-and-data-protection) that are designated as applying to EoX Consumers.

### Conformance Clause 4: EoX Core Viewer

A viewer satisfies the "EoX Core Viewer" conformance profile if the viewer fulfills the following two groups of requirements:

The viewer:

* satisfies the "EoX Consumer" conformance profile.
* satisfies the normative requirements given below.

For each value of type `/$defs/eox_timestamp_t` that does not conform to [cite](#RFC3339) the viewer:

* SHOULD output the raw string value if the value is not `tba`.
* SHOULD display a value that is understandable to the user as a replacement for the technical value `tba`.

> A tool MAY provide an option to suppress dates with value `tba`.

### Conformance Clause 5: EoX Core Recommending Viewer

A viewer satisfies the "EoX Core Recommending Viewer" conformance profile if the viewer fulfills the following groups of requirements:

The viewer:

* satisfies the "EoX Core Viewer" conformance profile.
* provides an interpretation view for each life cycle event that additionally answers:
  1. at what date the event occurs.
  2. what lifecycle state changes at that date. 
  3. which actions are needed.
  
  > For this specification, the first two answers are directly derived from property semantics and their values.
  > The third answer (needed actions) is not explicitly represented by a dedicated EoX Core property and therefore
  > requires a defined action mapping by specification, profile, implementation, or deployment policy.

* still provides the date and change interpretation, if no action mapping is available.

The EoX Core Actionable Viewer SHOULD: 

* indicate that the action is not specified by this specification, if no action mapping is available.

* use the following action mapping as default:

  * EoS: Product can no longer be ordered from vendor sales channels.
    _Recommended action_: evaluate and initiate replacement procurement plans for successor offerings.
  * EoSSec: Vendor no longer commits to security remediations.
    _Recommended action_: complete upgrade or migration to a supported product version and apply risk treatment until migration is complete.
  * EoL: All vendor support ends.
    _Recommended action_: complete replacement or decommissioning of affected deployments.

An EoX Core Recommending Viewer MAY use different action mappings or expand on the recommended actions. 
  

### Conformance Clause 6: EoX Core Basic Validator

A program satisfies the "EoX Core Basic Validator" conformance profile if the program:

* reads JSON objects and performs a check against the JSON schema.
* performs all mandatory tests as given in section [sec](#mandatory-tests).
* does not change the EoX Core Information.

A EoX Core Basic Validator MAY provide one or more additional functions:

* Only run one or more selected mandatory tests.
* Apply quick fixes as specified in the standard.
* Apply additional quick fixes as implemented by the vendor.

### Conformance Clause 7: EoX Core Extended Validator

A EoX Core Basic Validator satisfies the "EoX Core Extended Validator" conformance profile if the EoX Core Basic Validator:

* satisfies the "EoX Core Basic Validator" conformance profile.
* additionally performs all recommended tests as given in section [sec](#recommended-tests).
* provides a function that allows to specify tests for which test results of warning are reported as error.

A EoX Core Extended Validator MAY provide an additional function to only run one or more selected recommended tests.

### Conformance Clause 8: EoX Core Full Validator

A EoX Core Extended Validator satisfies the "EoX Core Full Validator" conformance profile if the EoX Core Extended Validator:

* satisfies the "EoX Core Extended Validator" conformance profile.
* additionally performs all guidance tests as given in section [sec](#informative-tests).
* provides a function that allows to specify tests for which test results of information are reported as warning.
* provides a function that allows to specify tests for which test results of information are reported as error.

A EoX Core Full Validator MAY provide an additional function to only run one or more selected guidance tests.

### Conformance Clause 9: EoX Core Library

A library satisfies the "EoX Core Library" conformance profile if the library:

* implements all elements as data structures conforming to the syntax and semantics defined in sections
  [sec](#format-validation), [sec](#date-and-time) and [sec](#schema-elements).
* checks all elements according to the patterns provided in the JSON schema.
* has a function that reads EoX Core Information into the data structure from a
  * file system.
  * URL.
  * data stream.
* provides function for sorting the keys and sorts the keys automatically on output.
* has a function that outputs the data structure as EoX Core Information
  * on the file system.
  * as string.
  * into a data stream.

The library MAY implement an option to retrieve the keys unsorted.

### Conformance Clause 10: EoX Core Library with Basic Validation
A EoX Core Library satisfies the "EoX Core Library with Basic Validation" conformance profile if the EoX Core Library:

* satisfies the "EoX Core Library" conformance profile.
* satisfies the "EoX Core Basic Validator" conformance profile.
* validates the EoX Core Information before output according to the "EoX Core Basic Validator" and
  presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "EoX Core Basic Validator"
  and presents the validation result accordingly.

A EoX Core Library does not satisfies the "EoX Core Library with Basic Validation" conformance profile if the EoX Core
Library uses an external library or program for the "EoX Core Basic Validator" part and does not enforce its presence.

### Conformance Clause 11: EoX Core Library with Extended Validation

A EoX Core Library satisfies the "EoX Core Library with Extended Validation" conformance profile if the EoX Core Library:

* satisfies the "EoX Core Library" conformance profile.
* satisfies the "EoX Core Extended Validator" conformance profile.
* validates the EoX Core Information before output according to the "EoX Core Extended Validator" and
  presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "EoX Core Extended Validator"
  and presents the validation result accordingly.

A EoX Core Library does not satisfies the "EoX Core Library with Extended Validation" conformance profile if the EoX Core
Library uses an external library or program for the "EoX Core Extended Validator" part and does not enforce its presence.

### Conformance Clause 12: EoX Core Library with Full Validation

A EoX Core Library satisfies the "EoX Core Library with Extended Validation" conformance profile if the EoX Core Library:

* satisfies the "EoX Core Library" conformance profile.
* satisfies the "EoX Core Full Validator" conformance profile.
* validates the EoX Core Information before output according to the "EoX Core Full Validator" and
  presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "EoX Core Full Validator" and
  presents the validation result accordingly.

A EoX Core Library does not satisfies the "EoX Core Library with Full Validation" conformance profile if the EoX Core
Library uses an external library or program for the "EoX Core Full Validator" part and does not enforce its presence.

### Conformance Clause 13: EoX Core Differ

A program satisfies the "EoX Core Differ" conformance profile if the program:

* satisfies the "EoX Core Consumer" conformance profile.
* calculates the difference between two EoX Core Information JSON Objects and presents it as JSON Diff.

A EoX Core Differ MAY choose to make that information also available in other data formats.

### Conformance Clause 14: EoX Core Comparator

A program satisfies the "EoX Core Comparator" conformance profile if the program:

* satisfies the "EoX Core Consumer" conformance profile.
* provides a function to compares two EoX Core Information Objects `a` and `b` based on their `last_updated` value and returns:
  * `-1` if `a["last_updated"] < b["last_updated"]`
  * `0` if `a["last_updated"] = b["last_updated"]`
  * `1` if `a["last_updated"] > b["last_updated"]`
* provides a function to compares two EoX Core Information Objects `a` and `b` based on their `last_updated` value and returns:
  * `b` if `a["last_updated"] < b["last_updated"]`
  * `a` if `a["last_updated"] = b["last_updated"]`
  * `a` if `a["last_updated"] > b["last_updated"]`
* takes timezones into account.

A EoX Core Comparator MAY choose to make that information also available in other data formats.

### Conformance Clause 15: EoX Core Sorter

A program satisfies the "EoX Core Sorter" conformance profile if the program:

* satisfies the "EoX Core Consumer" conformance profile.
* provides a function to sort an arbitrary number of EoX Core Information Objects `last_updated` value with that value descending (default).
* provides a function to sort an arbitrary number of EoX Core Information Objects `last_updated` value with that value ascending.
* takes timezones into account.

A EoX Core Sorter MAY choose to make that information also available in other data formats.

### Conformance Clause 16: EoX Core Merger

A program satisfies the "EoX Core Merger" conformance profile if the program:

* satisfies the "EoX Core Consumer" conformance profile.
* provides a function to merge EoX Core Information into a single EoX Core Information Object by overwriting all old values
  of keys present in newer EoX Core Information Objects with the values from newer objects.

  > This includes the value of `last_updated`.

* provides a function to merge EoX Core Information into a single EoX Core Information Object by overwriting all old values
  of keys present in newer EoX Core Information Objects with the values from newer objects but treating `tba` as not present during
  the overwrite process.

  > This includes the value of `last_updated`.
  > Ignoring `tba` while overwriting ensures that a date value is never overwritten by `tba`.

* provides a function to merge EoX Core Information into a single EoX Core Information Object by taking the newest as base
  and iterative appending keys that are not present in that object while iterating over the EoX Core Information from newest to oldest.

  > As `last_updated` is a required field, it is not changed during the process.
  > Values of keys that are inserted are never changed in that process.

* takes timezones into account.

A program MAY implement other algorithms than defined here, if and only if, the results are guaranteed to be the same.

An EoX Core Merger MAY choose to make that information also available in other data formats.

-------
