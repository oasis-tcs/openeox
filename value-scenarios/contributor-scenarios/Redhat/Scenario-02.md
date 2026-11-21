# Scenario 02

### Title

Track the full support-phase schedule of a product version

### Used definitions

- `General Availability (GA)`: as defined in OpenEoX
- `End-of-Life (EoL)`: as defined in OpenEoX
- `End-of-Security-Support (EoSSec)`: as defined in OpenEoX
- `Product Life Cycle`: as defined in OpenEoX

### Description

As an Engineer, I want to list **all** lifecycle/support phases for a given product version — not only
its first (GA) and last (EoL) milestones — so that I can tell customers and internal tooling exactly when
support scope changes (for example when a release moves from full bug-fix support to security-fixes-only
maintenance, or into a separately-entitled extended-support period), and so that I can plan upgrades
before support scope narrows, not only before EoL.

For example: Red Hat OpenShift Container Platform (OCP) y-stream releases move through General
Availability → Full Support → Maintenance Support → Extended Update Support (EUS) Term 1 → EUS Term 2 →
End-of-Life, each with its own start/end date. A consumer needs all of these transition dates, not just
the first and last, to make informed support and upgrade decisions.

### OpenEoX today

**Gap.** `eox-core` only defines four possible named milestones per statement
(`general_availability`, `end_of_sales`, `end_of_security_support`, `end_of_life`). There is no way to
express an arbitrary-length, ordered list of intermediate named support phases (e.g. "Full Support",
"Maintenance Support", "EUS Term 1", "EUS Term 2"). This forces a producer to either drop the
intermediate transitions entirely, or collapse them into `end_of_security_support` /
`end_of_life`, losing information that is material to the consumer's upgrade planning.

This gap is already tracked by the TC in
[issue #22](https://github.com/oasis-tcs/openeox/issues/22),
[issue #29](https://github.com/oasis-tcs/openeox/issues/29),
[issue #31](https://github.com/oasis-tcs/openeox/issues/31), and in particular
[issue #67](https://github.com/oasis-tcs/openeox/issues/67) ("Single fields vs. scope for End of
Maintenance"), which proposes exactly this kind of phase/scope list. Red Hat OpenShift Container
Platform (OCP) 4's six-phase model (GA, Full Support, Maintenance Support, EUS Term 1, EUS Term 2, EoL)
is a concrete worked example of this gap.
