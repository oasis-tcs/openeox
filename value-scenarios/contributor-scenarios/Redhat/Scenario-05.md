# Scenario 05

### Title

Map a vulnerable component to its product, version, and End-of-Security-Support status

### Used definitions

- `End-of-Security-Support (EoSSec)`: as defined in OpenEoX
- `product`: as defined in [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#12-terminology)
- `vendor`: as defined in [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#12-terminology)

### Description

As a Security Engineer, I want to map a vulnerable component (identified e.g. by CPE or PURL) to the
correct product and version, and then check whether that product/version is still inside its committed
End-of-Security-Support (EoSSec) window, so that I can correctly prioritize vulnerability remediation,
generate accurate VEX/CSAF documents, and avoid wasting effort chasing fixes for a stream that is
already past its End-of-Security-Support date.

### OpenEoX today

**Supported.** Resolving a CPE/PURL to a product/version via `product_identification_helper` and
checking it against `end_of_security_support` is fully expressible with the current OpenEoX Core/Shell
schemas. Finer-grained distinctions in security-fix *scope* across intermediate support phases (e.g.
Full Support vs. Maintenance Support vs. Extended Update Support) are a separate concern, already
covered by [Scenario 02](Scenario-02.md).
