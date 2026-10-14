# Comment Resolution Log: OpenEoX Core Schema v1.0 CSD01 (DRAFT)

30-day public review, 14 July to 13 August 2026 (23:59 UTC). Eleven comments from two
reviewers. Prepared by the OASIS TC Administrator, 27 August 2026, from both archives;
the companion file carries every comment verbatim.

The **TC disposition** and **Resolution** columns are the TC's to complete. Everything
else is filled. Both source archives are readable without a login.

Sources:

- openeox-comment facility: [review thread](https://groups.oasis-open.org/discussion/invitation-to-comment-on-openeox-core-schema-v10-csd01-30-day-public-review-ends-13-august-2026)
- OpenEoX TC community: [review thread, TC mirror](https://groups.oasis-open.org/discussion/invitation-to-comment-on-openeox-core-schema-v10-csd01-30-day-public-review-ends-13-august-2026-1)

## Comments from Aleksei Chirkunov, openeox-comment facility, 21 July 2026

| ID | Section(s) | Comment | TC disposition | Resolution | Status |
|---|---|---|---|---|---|
| AC-01 | 2.2.2, 7.3, 9.1.8 | "Guidance tests" (2.2.2, 9.1.8) and "Informative Tests" (7.3) appear to name the same category; one name throughout would remove the ambiguity. | | | Open |
| AC-02 | 4.1.4, 7.1 | Internal contradiction: 4.1.4 places semantic validation out of scope, using date ordering as the example, while 7.1 makes date ordering checks mandatory. Suggests narrowing 4.1.4 to say exactly which semantic checks are outside Core. | | | Open |
| AC-03 | 6.2.6, 9.1.14, 9.1.16 | last_updated decides which record is newer, but no rule requires Producers to update it when lifecycle data changes, and equal timestamps with different content silently return record a. Suggests requiring last_updated to change with the record and treating equal timestamps with different content as a conflict. | | | Open |
| AC-04 | 8 | Section 8 covers unsafe JSON parsing but the data itself needs a trust model: source authentication, record integrity, freshness, and Consumer behaviour when a record cannot be verified. A forged or replayed record could hide the end of security support. | | | Open |
| AC-05 | 9.1.6, 7.1 | Internal contradiction: Validator Basic is required to run all mandatory tests from 7.1, then permitted to run selected tests only. Suggests partial runs be clearly marked and not produce a full conformance result. | | | Open |
| AC-06 | 9.1.12 | Copy and paste error: the "Library with Full Validation" clause opens with "Library with Extended Validation". The rest of the clause refers to Validator Full. | | | Open |

## Comments from Jay White (Microsoft), OpenEoX TC community, 12 August 2026

Mapped against the Azure Service Tree; framed by the commenter as future work that
should not block the current draft.

| ID | Section(s) | Comment | TC disposition | Resolution | Status |
|---|---|---|---|---|---|
| JW-01 | Core schema | More guidance and examples for records where End of Security Support and End of Life differ, are unknown, or are announced at different times. | | | Open |
| JW-02 | Core schema | Retirement granularity: platforms retire an API, feature, SKU, or regional instance while the parent service stays active. Suggests a way to identify the target of a lifecycle event and its parent relationship, possibly a future version or extension. | | | Open |
| JW-03 | Core schema | An optional link from a lifecycle record to a successor offering, replacement service, or migration path. | | | Open |
| JW-04 | Core model | Private Preview and Public Preview as lifecycle milestones: future extension or companion model, not a Core v1.0 blocker. | | | Open |
| JW-05 | Core model | Keep breaking change events separate from Core lifecycle facts; a companion model referencing OpenEoX records may fit better than expanding Core. | | | Open |
