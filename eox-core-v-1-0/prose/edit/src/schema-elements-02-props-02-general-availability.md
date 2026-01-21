### General Availability Property

General Availability (`general_availability`) of value type `eox_timestamp_t` indicates the first day when the particular product
is officially launched and made accessible to the general public or through its intended distribution channels.

The following special cases are defined:

* If the value of `general_availability` is equal to the value of `end_of_security_support`, this implies that the product is not supported.
  However, the product may be before its EoL.
* If a product is sunset (in terms of EoL) before its GA,
  the `general_availability` entry SHALL be removed and just the EoL entry kept in the OpenEoX record.
* If the value of `general_availability` is equal to the value of `end_of_life`,
  this implies that the product was published but is not maintained at all.
  
  > An example could be the publication of source code as open source without the intend to maintain it.
  > The clear communication allows others to take over the development as well as to assess the risks associated with using the product.
