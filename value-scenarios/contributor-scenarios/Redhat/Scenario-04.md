# Scenario 04

### Title

Get notified ahead of a lifecycle or support-phase transition

### Used definitions

- `End-of-Life (EoL)`: as defined in OpenEoX
- `End-of-Security-Support (EoSSec)`: as defined in OpenEoX
- `Product Life Cycle`: as defined in OpenEoX

### Description

As a consumer (an Engineer, Product Manager, or automated system), I want to track the lifecycle states
and transition dates for all the products I use, so that I can automatically trigger replacement or
upgrade-planning notifications ahead of End-of-Life, End-of-Security-Support, or any other support-phase
narrowing event, rather than discovering the transition after it has already happened.

### OpenEoX today

**Partially supported.** `end_of_life` and `end_of_security_support` are both machine-readable and
`last_updated` allows a consumer to detect when a record changed, so a polling/diffing client can already
build EoL/EoSSec notifications today. However, notifications ahead of *intermediate* support-phase
transitions (e.g. "Full Support ends in 30 days") are blocked by the same gap described in
[Scenario 02](Scenario-02.md) — those intermediate dates cannot be represented yet. There is also no
standardized subscription/webhook mechanism defined by OpenEoX itself; this is left to consuming systems
and is out of scope for `eox-core`/`eox-shell` but may be relevant for a future `eox-api` deliverable.
