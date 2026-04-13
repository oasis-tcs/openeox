# Schema Elements

The OpenEoX Core schema describes how to represent OpenEoX core information as a JSON document.

The OpenEoX Core schema Version 1.0 builds on the JSON Schema draft 2020-12 rules extended by the format validation
enforcement (see [sec](#format-validation)).

```
  "$schema": "https://docs.oasis-open.org/openeox/eox-core/v1.0/schema/meta.json",
```

The schema identifier is:

```
  "$id": "https://docs.oasis-open.org/openeox/v1.0/schema/core.json",
```

The further documentation of the schema is organized via Definitions and Properties.

* Definitions provide types that extend the JSON schema model
* Properties use these types to support assembling OpenEoX core information

Types and properties together provide the vocabulary for the domain specific language supporting OpenEoX information.

The four mandatory properties are `$schema`, `end_of_life`, `end_of_security_support`, and `last_updated`.
The additional property, `end_of_sales`, is optional.
