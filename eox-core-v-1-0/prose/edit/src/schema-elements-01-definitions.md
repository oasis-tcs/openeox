## Definitions

The definitions (`$defs`) introduce the following domain specific types into the OpenEoX language:
OpenEoX Core Schema (`schema_t`) and Timestamp (`timestamp_t`).

```
  "$defs": {
    "schema_t": {
      // ...
    },
    "timestamp_t": {
      // ...
    }
  },
```

### OpenEoX Core Schema Type

The OpenEoX Core Schema (`schema_t`) type of value type `string` and `const` specifies the schema the JSON object must be valid against.
The single valid value for this `const` is:

```
  https://docs.oasis-open.org/openeox/v1.0/schema/core.json
```

> This value allows for tools to identify that a JSON document is meant to be valid against this schema.
> Tools can use that to support users by automatically checking whether the OpenEoX Core Object adheres to the JSON schema identified by this URL.

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
