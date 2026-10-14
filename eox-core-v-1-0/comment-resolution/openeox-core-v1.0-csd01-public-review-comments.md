# OpenEoX Core Schema v1.0 CSD01: public review comments

30-day public review, 14 July to 13 August 2026 (23:59 UTC). Eleven comments from two
reviewers, held in two archives. Full text reproduced verbatim below, captured from the
Higher Logic archives on 27 August 2026.

## Source 1: openeox-comment facility

Thread: "Invitation to comment on OpenEoX Core Schema v1.0 CSD01 - 30-day public review
ends 13 August 2026"
https://groups.oasis-open.org/discussion/invitation-to-comment-on-openeox-core-schema-v10-csd01-30-day-public-review-ends-13-august-2026

### Aleksei Chirkunov, posted 21 July 2026 09:17

> Hi,
>
> Review notes:
>
> 1. Validator Full refers to "guidance tests" in sections 2.2.2 and 9.1.8, while section
> 7.3 calls them "Informative Tests". I assume these are the same category, but using one
> name throughout would remove the ambiguity.
>
> 2. Section 4.1.4 says semantic validation is out of scope and uses date ordering as an
> example. Section 7.1 then makes date ordering checks mandatory. These two parts seem to
> conflict. It would help to narrow the statement in 4.1.4 and say exactly which semantic
> checks are outside the Core specification.
>
> 3. Sections 6.2.6, 9.1.14 and 9.1.16 rely on last_updated to decide which record is
> newer, but I could not find a clear rule requiring Producers to update it whenever
> lifecycle data changes. There is also no safe outcome for two different records with the
> same timestamp. Comparator simply returns record a. That can hide a real update. I
> suggest requiring last_updated to change with the record and treating equal timestamps
> with different content as a conflict.
>
> 4. Section 8 mostly covers the risk of parsing JSON with eval-like functions. The data
> itself also needs a trust model. A forged or replayed record could hide the end of
> security support or trigger the wrong migration or decommissioning action. The section
> should cover source authentication, record integrity, freshness and what a Consumer
> should do when a record cannot be verified.
>
> 5. In section 9.1.6, Validator Basic is required to run all mandatory tests from section
> 7.1. A few lines later it is allowed to run only selected mandatory tests. That creates
> an unclear result: can a partial run still be reported as Validator Basic? I think
> partial runs should be clearly marked and should not produce a full conformance result.
>
> 6. Section 9.1.12 looks like a copy-and-paste error. The section is for "Library with
> Full Validation" but the first sentence says "Library with Extended Validation". The
> rest of the clause refers to Validator Full so the first sentence should use "Library
> with Full Validation" too.
>
> Thx

## Source 2: OpenEoX TC community

Thread: "Invitation to comment on OpenEoX Core Schema v1.0 CSD01 - 30-day public review
ends 13 August 2026" (TC mirror)
https://groups.oasis-open.org/discussion/invitation-to-comment-on-openeox-core-schema-v10-csd01-30-day-public-review-ends-13-august-2026-1

### Jay White (Microsoft), posted 12 August 2026 16:28

> Hello OpenEoX TC and Comments TC,
>
> I am sharing feedback on behalf of Microsoft and Azure Service Tree stakeholders as part
> of the public review for OpenEoX Core Schema v1.0 CSD01.
>
> We reviewed the draft against an Azure Service Tree lifecycle mapping exercise. Overall,
> the Core model is clear and useful. The separation of General Availability, End of
> Sales, End of Security Support, and End of Life gives vendors and consumers a common way
> to describe lifecycle milestones in a machine readable form.
>
> A few items stood out as areas where additional clarification or future work could help
> large cloud service providers use OpenEoX more consistently.
>
> **Clarify how End of Security Support and End of Life should be represented**
>
> The Core schema requires both end_of_life and end_of_security_support, and allows a
> value of tba when the date is not yet announced. That distinction is useful.
>
> From the Azure Service Tree review, we saw that a single retirement date is not enough
> to fully express the lifecycle state. Security support may end on a different date than
> broader support or service retirement. It would help implementers if the specification
> included more guidance and examples for records where End of Security Support and End of
> Life are different, unknown, or announced at different times.
>
> **Add clearer support for retirement scope**
>
> A key gap from the Azure Service Tree perspective is retirement granularity. Large cloud
> platforms do not always retire a full product or service. They may retire an API,
> feature, capability, SKU, dependency, or regional instance while the parent service
> remains active.
>
> It would be useful for OpenEoX to support a clear way to identify the specific target of
> a lifecycle event and, where needed, its relationship to a parent product or service.
> This could be handled in a future version or extension if it is outside the intended
> scope of Core v1.0.
>
> **Consider successor and migration guidance**
>
> Consumers need to know not only what is changing and when, but also where they should go
> next. An optional way to link a lifecycle record to a successor offering, replacement
> service, or migration path would make OpenEoX records more actionable.
>
> This is especially useful when a service, API, or capability is retired but there is a
> recommended replacement.
>
> **Treat preview lifecycle milestones as future vision, not a Core v1.0 blocker**
>
> Azure Service Tree discussions also raised Private Preview and Public Preview as
> lifecycle milestones that are important in cloud environments. These are not part of the
> current OpenEoX Core model, and I do not think they need to block the current draft.
>
> However, the TC may want to consider whether preview milestones belong in a future
> extension or companion model for cloud services.
>
> **Keep breaking change events separate from Core lifecycle facts**
>
> Breaking Change is a planned new event type in the Azure Service Tree future vision. It
> is not part of the current Service Tree schema shared for this review, and it is also
> not part of OpenEoX Core.
>
> That separation seems appropriate. A breaking change is not the same as General
> Availability, End of Sales, End of Security Support, or End of Life. It may relate to
> those milestones, but it should not be merged into the Core lifecycle model.
>
> If the TC wants to support breaking changes, deprecations, or migration notices in the
> future, a companion model that references OpenEoX lifecycle records may be a better fit
> than expanding Core directly.
>
> Thank you to everyone who contributed to this draft. The Core schema is a strong
> foundation. The feedback above is intended to help ensure it can also support the level
> of granularity that large cloud platforms need for service, feature, and API lifecycle
> management.
>
> Best regards,
>
> Jay White
> Editor, OpenEoX Technical Committee
> Microsoft
