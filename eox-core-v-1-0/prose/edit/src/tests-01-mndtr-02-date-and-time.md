### Date and Time{#mandatory-tests--date-and-time}

For each item of type `string` and format `date-time` it MUST be tested that it conforms to the rules given in section [sec](#date-and-time).
Any property with the value `tba` is ignored in this comparison.

The relevant path for this test is:

```
  /end_of_life
  /end_of_sales
  /end_of_security_support
  /last_updated
```

*Example 1 (which fails the test):*

```
  "end_of_life": "2025-12-31 12:00:00Z",
```

> The `end_of_life` uses a white space as separator instead the letter `T`.
