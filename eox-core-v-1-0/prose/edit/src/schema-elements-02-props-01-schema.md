### Schema Property

The OpenEoX Core Schema (`$schema`) of value type `string` and `const` specifies the schema the JSON object must be valid against.
The single valid value for this `const` is:

```
  https://docs.oasis-open.org/openeox/v1.0/schema/core.json
```

> This value allows for tools to identify that a JSON document is meant to be valid against this schema.
> Tools can use that to support users by automatically checking whether the OpenEoX Core Object adheres to the JSON schema identified by this URL.
