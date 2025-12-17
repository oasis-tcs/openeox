### Use of `tba` where Date is set for EoL

For each property of type `eox_timestamp_t`, it MUST be tested that it does not contain the value `tba` if the `end_of_life` value is set to a date.

The relevant path for this test is:

```
  /end_of_sales
  /end_of_security_support
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "end_of_life": "2025-09-01T12:00:00Z",
    "end_of_security_support": "tba",
    // ...
  }
```

> The `end_of_security_support` is set to `tba` but `end_of_life` already has a date.

> A tool MAY set the `end_of_security_support` to the same value as `end_of_life` as a quick fix.
