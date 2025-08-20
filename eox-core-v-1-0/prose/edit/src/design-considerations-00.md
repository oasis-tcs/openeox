# Design Considerations

OpenEoX is a language to exchange any End-of information formulated in JSON.

The standard is divided into 3 parts:

- OpenEoX Core (this specification): contain the OpenEoX core information and intended to be imported by other standards which will provide the
  product context needed.
  Optionally, the product context can be omitted if the product itself provides the information, e.g. through in an SNMP or HTTPS response.
- OpenEoX Shell: binding OpenEoX core information to products.
  Such combination is called an OpenEoX statement.
  The OpenEoX Shell forms the so called standalone mode in OpenEoX.
- OpenEoX API: deals with the distribution of OpenEoX Core and OpenEoX Shell data.
