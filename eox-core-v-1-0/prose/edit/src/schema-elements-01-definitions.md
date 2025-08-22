## Definitions

The definitions (`$defs`) introduce the following domain specific types into the OpenEoX language:
Timestamp (`timestamp_t`).

```
  "$defs": {
    "timestamp_t": {
      // ...
    }
  },
```

### Timestamp Type

The Timestamp (`timestamp_t`) type of value type `string` contains the timestamp at which the product reaches the specified stage or the indicator that this is still 'to be announced'.

```
    "oneOf": [
      {
        "format": "date-time"
      },
      {
        "const": "tba"
      }
    ]
```

Therefore, it MUST either be a `string` with format `date-time` or use the constant value `tba`.
