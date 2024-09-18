# Dell's Use Case and Value Scenarios
- Contributor: Langley, Dell
- Originally discussed in [Issue #14](https://github.com/oasis-tcs/openeox/issues/14)


Companies including our own may speak in terms of End of Sale, End of Standard Support, End of Security Support/Life, End of Life, End of Service Life.  These terms might not match the use case of other vendors.
 
Because of this, a flexible schema is anticipated as being needed.
 
Below is a proposed standalone & hopefully universal schema that addresses some known use cases.
 
```
{
Vendor, 
    // required
    // Name of vendor 
    // arbitrary text
Email,
    // required
    // contact address for vendor
    // email formatted text
Website,
    // required
    // Primary Vendor URL 
    // URL text
ID, 
    // required
    // with the Notification Date, will form a primary key
    // incremental ID starting with 001
Label, 
    // required
    // label the vendor uses for the type of communication. 
    // e.g., "End of Sale", "End of Life", "End of Support", "End of Security Support"
Description, 
    // optional
    // describe what this means to the end user and provide other notes as needed
    // arbitrary text field
Notification_Date, 
    // required
    // date this is published.  
    // ISO 8601 format
Effective_Date, 
    // required
    // date when the policy comes into effect.  
    // ISO 8601 format
End_Date, 
    // optional
    // date when policy is no longer effective (e.g., partial to none for support). 
    // ISO 8601 format
Category, 
    // required
    // category of EoX to allow cross-vendor grouping of different "Label" values 
    // One of ["Sales"|"Support"|"Security Support"|"Other"]
Support_Term, 
    // optional
    // alternative to End_date if the term is based on date of sale (e.g., 3 years)
    // arbitrary text
Support_Coverage, 
    // required (if support);
    // Extent of support; 
    // One of ["None"|"Partial"|"Full"]
Policy_URLs, 
    // optional
    // delimited list of links to where the formal policies are found
    // Arbitrary vendor URLs 
Previous_Reference, 
    // optional
    // list of previous record(s) this replaces
    // Notification_Date+ID 
Affected_Products 
    // required
    // min. 1
    // record structure
    {
    Product_Name, 
        // required
        // name of the product
        // arbitrary vendor product name
    Product_Version, 
        // required
        // string of one or more versions
        // arbitrary text, or "All"
    Product_URLs 
        // optional; 
        // delimited list of product pages and other relevant info
        // arbitrary vendor URLs for specific products
    }
}

```

