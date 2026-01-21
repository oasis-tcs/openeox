### Use of `tba` for GA where other Date is set{#use-of-tba-for-ga-where-other-date-is-set}

It MUST be tested that `general_availability` does not contain the value `tba` if any other property of type `eox_timestamp_t` is set to a date.

The relevant path for this test is:

```
  /general_availability
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "end_of_security_support": "2025-06-17T14:00:00Z",
    "general_availability": "tba",
    // ...
  }
```

> The `general_availability` is set to `tba` but `end_of_security_support` already has a date.

> A tool MAY remove the `general_availability` as a quick fix.
