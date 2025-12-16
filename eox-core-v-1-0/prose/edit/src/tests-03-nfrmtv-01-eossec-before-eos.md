### EoSSec before EoS

It MUST be tested that if `end_of_sales` is present, its value is before or equal to the value of `end_of_security_support`.
As the timestamps might use different timezones, the sorting MUST take timezones into account.
The test MUST be skipped, if `end_of_sales` is set to `tba`.


The relevant path for this test is:

```
    /end_of_sales
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "end_of_sales": "2025-12-31T12:00:00Z",
    "end_of_security_support": "2025-11-19T16:00:00Z",
    // ...
  }
```

> The `end_of_security_support` is earlier than the `end_of_sales`.
