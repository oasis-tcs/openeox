
![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------

# OpenEOX Core Schema Version 1.0

## Committee Specification Draft 01

## 16 July 2025

#### This stage:
https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.md (Authoritative) \
https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.html \
https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.pdf

#### Previous stage:
N/A

#### Latest stage:
https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.md (Authoritative) \
https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.html \
https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.pdf

#### Technical Committee:
[OASIS OpenEOX TC](https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=26350f39-9c7b-4bf2-a422-018dc7d3f5aa)

#### Chairs:
Justin Murphy (justin.murphy@mail.cisa.dhs.gov), [DHS Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov) \
Omar Santos (osantos@cisco.com), [Cisco Systems](https://cisco.com/) \

#### Editors:
Jautau White (jaywhite@microsoft.com), Microsoft Corporation \
Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/) \
Thomas Schmidt (thomas.schmidt@bsi.bund.de), [Federal Office for Information Security (BSI) Germany](https://www.bsi.bund.de/)

#### Additional artifacts:
This prose specification is one component of a Work Product that also includes:

* OpenEOX Core JSON schema: https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/schema/eox-core.json. \
Latest stage: https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json.

#### Related work:
This specification is related to

* ...

#### Declared JSON namespaces:

* [https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json](https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/eox-core.json)


#### Abstract:
The OpenEoX Core Schema defines the core schema for the OpenEOX unified machine-readable approach to
managing and sharing End-of-Life (EOL) and End-of-Support (EOS) information for commercial and open source software and hardware.

#### Status:
This document was last revised or approved by the OASIS OpenEOX TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=26350f39-9c7b-4bf2-a422-018dc7d3f5aa.

TC members should send comments on this specification to the TC's email list. Any individual may submit comments by following the instructions listed at https://groups.oasis-open.org/communities/community-home?CommunityKey=c9295ed5-b5f9-4a51-8893-018f5aa7fc09. 

This specification is provided under the [Non-Assertion Mode](https://www.oasis-open.org/policies-guidelines/ipr/#Non-Assertion-Mode) of the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/), the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page (https://www.oasis-open.org/committees/tosca/ipr.php).

Note that any machine-readable content ([Computer Language Definitions](https://www.oasis-open.org/policies-guidelines/tc-process-2017-05-26/#wpComponentsCompLang)) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.

#### Key Words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 \[[RFC2119](#RFC2119)\] and \[[RFC8174](#RFC8174)\] when, and only when, they appear in all capitals, as shown here.

#### Citation format:
When referencing this specification the following citation format should be used:

**[EOX-Core-v1.0]**

_OpenEOX Core Schema Version 1.0_.
Edited by Jautau White, Stefan Hagen, and Thomas Schmidt.
DD MONTH 2025.
OASIS Committee Specification Draft 01.
https://docs.oasis-open.org/openeox/eox-core/v1.0/csd01/eox-core-v1.0-csd01.html. Latest stage: https://docs.oasis-open.org/openeox/eox-core/v1.0/eox-core-v1.0.html

#### Notices

Copyright &copy; OASIS Open 2025. All Rights Reserved.

Distributed under the terms of the OASIS [IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/).

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs.

For complete copyright information please see the full Notices section in [Appendix E](#appendix-e-notices).

-------

-------

# Table of Contents

1. [Introduction](#introduction)  
	1.1 [Typographical Conventions](#typographical-conventions)  
2. [Overview](#overview)  
3. [Conformance](#conformance)  

Appendix A. [References](#references)  
	A.1 [Normative References](#normative-references)  
	A.2 [Informative References](#informative-references)  
Appendix B. [Safety, Security and Data Protection](#safety-security-and-data-protection)  
Appendix C. [Acknowledgments](#acknowledgments)  
Appendix D. [Revision History](#revision-history)  
Appendix E. [Notices](#notices)  
-------

# 1. Introduction <a id='introduction'></a>

## 1.1 Typographical Conventions <a id='typographical-conventions'></a>

Keywords defined by this specification use this `monospaced` font.

```
    Normative source code uses this paragraph style.
```

Some sections of this specification are illustrated with non-normative examples introduced with "Example" or "Examples" like so:

*Example 1:*<a id='typographical-conventions-eg-1'></a><a id='sec-1-1-eg-1'></a><a id='example-4321'></a>

```
    Informative examples also use this paragraph style but preceded by the text "Example(s)".
```

All examples in this document are informative only.

All other text is normative unless otherwise labeled e.g. like the following informative comment:

> This is a pure informative comment that may be present, because the information conveyed is deemed useful advice or
> common pitfalls learned from implementer or operator experience and often given including the rationale.

-------

# 2. Overview <a id='overview'></a>

TBD

# 3. Conformance <a id='conformance'></a>

TBD

-------

# Appendix A. References <a id='references'></a>

This appendix contains the normative and informative references that are used in this document.

While any hyperlinks included in this appendix were valid at the time of publication, OASIS cannot guarantee their long-term validity.

## A.1 Normative References <a id='normative-references'></a>

The following documents are referenced in such a way that some or all of their content constitutes requirements of this document.

ECMA-262
:    _ECMAScript® 2024 Language Specification_, ECMA-262, 15th edition, June 2024,
<https://262.ecma-international.org/15.0/>

ISO8601-1
:    _Date and time — Representations for information interchangePart 1: Basic rules_, International Standard, ISO 8601-1:2019(E), February 25, 2019,
<https://www.iso.org/standard/70907.html>.

JSON-Schema-Core
:    _JSON Schema: A Media Type for Describing JSON Documents_, draft-bhutton-json-schema-00, December 2020, 
<https://datatracker.ietf.org/doc/html/draft-bhutton-json-schema-00>.

JSON-Schema-Validation
:    _JSON Schema Validation: A Vocabulary for Structural Validation of JSON_, draft-bhutton-json-schema-validation-00, December 2020, <https://datatracker.ietf.org/doc/html/draft-bhutton-json-schema-validation-00>.

JSON-Hyper-Schema
:    _JSON Hyper-Schema: A Vocabulary for Hypermedia Annotation of JSON_, draft-handrews-json-schema-hyperschema-02, September 2019, <https://json-schema.org/draft/2019-09/json-schema-hypermedia.html>.

Relative-JSON-Pointers
:    _Relative JSON Pointers_, draft-bhutton-relative-json-pointer-00, December 2020,
<https://datatracker.ietf.org/doc/html/draft-bhutton-relative-json-pointer-00>.

RFC2119
:    Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997,
<https://www.rfc-editor.org/info/rfc2119>.

RFC3339
:    Klyne, G. and C. Newman, "Date and Time on the Internet: Timestamps", RFC 3339, DOI 10.17487/RFC3339, July 2002,
<https://www.rfc-editor.org/info/rfc3339>.

RFC4180
:    Shafranovich, Y., "Common Format and MIME Type for Comma-Separated Values (CSV) Files", RFC 4180, DOI 10.17487/RFC4180, October 2005,
<https://www.rfc-editor.org/info/rfc4180>.

RFC7230
:    Roy T. Fielding and Julian Reschke, "Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing", RFC 7230, DOI 10.17487/RFC7230, June 2014,
<https://www.rfc-editor.org/info/rfc7230>.

RFC7464
:    Williams, N., "JavaScript Object Notation (JSON) Text Sequences", RFC 7464, DOI 10.17487/RFC7464, February 2015,
<https://www.rfc-editor.org/info/rfc7464>.

RFC8174
:    Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017,
<https://www.rfc-editor.org/info/rfc8174>.

RFC8259
:    T. Bray, Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 8259, DOI 10.17487/RFC8259, December 2017,
<https://www.rfc-editor.org/info/rfc8259>.

RFC9562
:    Davis, K., Peabody, B., and P. Leach, "Universally Unique IDentifiers (UUIDs)", RFC 9562, DOI 10.17487/RFC9562, May 2024,
<https://www.rfc-editor.org/info/rfc9562>.

SPDX301
:    _The System Package Data Exchange® (SPDX®) Specification Version 3.0.1_, Linux Foundation and its Contributors, 2024,
<https://spdx.github.io/spdx-spec/>.

## A.2 Informative References <a id='informative-references'></a>

TBD

# Appendix B. Safety, Security and Data Protection <a id='safety-security-and-data-protection'></a>

TBD

-------

# Appendix C. Acknowledgments <a id='acknowledgments'></a>

The following individuals were members of the OASIS OpenEOX Technical Committee during the creation of this specification and their contributions are gratefully acknowledged:

**OASIS OpenEOX TC Members:**

| First Name | Last Name        | Company                                                    |
|:-----------|:-----------------|:-----------------------------------------------------------|
| Denny      | Page             | TIBCO Software Inc.                                        |
| Feng       | Cao              | Oracle                                                     |
| Jautau     | White            | Microsoft Corporation                                      |
| Justin     | Murphy           | DHS Cybersecurity and Infrastructure Security Agency(CISA) |
| Langley    | Rock             | Red Hat                                                    |
| Martin     | Prpic            | Red Hat                                                    |
| Omar       | Santos           | Cisco Systems                                              |
| Stefan     | Hagen            | Individual                                                 |
| Thomas     | Schmidt          | Federal Office for Information Security (BSI) Germany      |
| ...        | ...              | ...                                                        |

-------

# Appendix D. Revision History <a id='revision-history'></a>

| Revision                     | Date       | Editor                                         | Changes Made                      |
|:-----------------------------|:-----------|:-----------------------------------------------|:----------------------------------|
| eox-core-v1.0-wd20250716-dev | 2025-07-16 | Jautau White, Stefan Hagen, and Thomas Schmidt | Preparing initial Editor Revision |

-------

# Appendix E. Notices <a id='notices'></a>

<!-- Required section. Do not modify. -->

Copyright &copy; OASIS Open 2025. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr/) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

As stated in the OASIS IPR Policy, the following three paragraphs in brackets apply to OASIS Standards Final Deliverable documents (Committee Specification, Candidate OASIS Standard, OASIS Standard, or Approved Errata).

[OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this deliverable.]

[OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this OASIS Standards Final Deliverable. OASIS may include such claims on its website, but disclaims any obligation to do so.]

[OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this OASIS Standards Final Deliverable or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Standards Final Deliverable, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.]

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark/ for above guidance.

-------
