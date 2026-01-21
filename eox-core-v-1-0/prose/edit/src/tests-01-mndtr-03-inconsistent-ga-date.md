### Inconsistent GA Date

It MUST be tested that the `general_availability` is earlier than or equal to any other date value in the OpenEoX Core Information.
The property `last_updated` is ignored in this test.
As the timestamps might use different timezones, the sorting MUST take timezones into account.
The test MUST be skipped if the value of `general_availability` is `tba`.
Except for `general_availability`, any property of type `eox_timestamp_t` with value `tba` MUST be ignored in the comparison.

The relevant path for this test is:

```
    /general_availability
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "end_of_security_support": "2025-11-19T16:00:00Z",
    "general_availability": "2026-01-21T17:00:00Z",
    // ...
  }
```

> The `general_availability` is later than the `end_of_security_support`.
