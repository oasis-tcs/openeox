# Scenario 07

### Title

Discover planned future releases and their expected GA date

### Used definitions

- `General Availability (GA)`: as defined in OpenEoX
- `Product`: as defined in OpenEoX

### Description

As a Security Engineer or Engineer, I want to discover upcoming ("planned", not-yet-released) product
versions and their expected General Availability date, so that I can plan migrations, capacity, and
security-review work ahead of a release shipping, rather than reacting only after it is already
available.

### OpenEoX today

**Partially supported.** The `"tba"` literal allowed for any `eox_timestamp_t` value (including
`general_availability`) lets a producer publish a record for a known, not-yet-dated future release.
What is not expressible is the distinct concept of a "planned" release that has been announced/registered
but has no committed dates at all yet, versus a release that already has a committed GA date but whose
later milestones (EoSSec/EoL) are still `"tba"`. A dedicated release/record status (e.g. "Planned" vs.
"Released") would remove this ambiguity, but is not required for the common case of "GA date known,
later dates pending."
