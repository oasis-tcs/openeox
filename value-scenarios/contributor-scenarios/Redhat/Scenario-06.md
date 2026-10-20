# Scenario 06

### Title

Audit lifecycle/security-support compliance across a product portfolio

### Used definitions

- `End-of-Life (EoL)`: as defined in OpenEoX
- `End-of-Security-Support (EoSSec)`: as defined in OpenEoX
- `product`: as defined in [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#12-terminology)
- `vendor`: as defined in [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#12-terminology)

### Description

As a regulator, auditor, or internal compliance/ProdSec team, I want a reliable, standardized source of
lifecycle information for every product and version in a portfolio, so that I can check whether any
product in scope (e.g. in critical infrastructure, or subject to a regulatory directive) has no
security support or has already reached End-of-Life, without relying on inconsistent names or dates
copied by hand from multiple vendor web pages, ticketing systems, or internal catalogs that frequently
disagree with each other.

### OpenEoX today

**Supported.** `end_of_life` and `end_of_security_support` are both mandatory, machine-readable fields,
and `last_updated` lets an auditor confirm data freshness. A standardized, cross-vendor OpenEoX feed is
exactly the kind of canonical, single source of truth this use case needs, and is directly in scope of
the current OpenEoX Core schema with no gaps identified for the compliance-reporting case itself (the
gap identified in [Scenario 02](Scenario-02.md) affects the *granularity* of what can be audited —
intermediate support-phase transitions — not whether basic EoL/EoSSec auditing is possible).
