## Definitions

The definitions (`$defs`) introduce the following domain specific types into the OpenEoX language:
EoX Timestamp (`eox_timestamp_t`).

```
  "$defs": {
    "eox_timestamp_t": {
      // ...
    }
  },
```

### EoX Timestamp Type

The EoX Timestamp (`eox_timestamp_t`) type of value type `string` contains the timestamp at which the product reaches the specified stage or the indicator that this is still 'to be announced'.

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

OpenEoX Consumer MUST treat `tba` as a date greater than the maximum date.
In any semantic interpretation, the value `tba` MUST be treated as 'not yet announced'.
