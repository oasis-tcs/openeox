### Inconsistent EoL Date

It MUST be tested that the `end_of_life` is later than or equal to any other date value in the OpenEoX Core Information.
The property `last_updated` is ignored in this test.
As the timestamps might use different timezones, the sorting MUST take timezones into account.
Except for `end_of_life`, any property of type `eox_timestamp_t` with value `tba` MUST be ignored in the comparison.

The relevant path for this test is:

```
    /end_of_life
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "end_of_life": "2025-11-19T16:00:00Z",
    "end_of_security_support": "2025-12-31T12:00:00Z",
    // ...
  }
```

> The `end_of_security_support` is later than the `end_of_life`.
