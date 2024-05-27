         title: "EOL and EOS Information"
       package: "https://docs.oasis-open.org/openeox/tbd/schema/shell"
   description: "A draft schema for representing End-of-Life (EOL) and End-of-Support (EOS) information in OpenEoX."
    namespaces: {"c": "https://docs.oasis-open.org/openeox/tbd/schema/core"}
       exports: ["Shell"]
        config: {"$TypeName": "^[$A-Z][-_$A-Za-z0-9]{0,63}$"}

**Type: Shell (Record)**

| ID | Name           | Type         | \#    | Description                            |
|----|----------------|--------------|-------|----------------------------------------|
| 1  | **schema**     | Schema_shell | 1     |                                        |
| 2  | **statements** | Statement    | 1..\* | Contains a list of statement elements. |

**********

Specifies the schema the JSON object must be valid against.

**Type: Schema_shell (Enumerated)**

| ID | Item                                                          | Description |
|----|---------------------------------------------------------------|-------------|
| 1  | **https://docs.oasis-open.org/openeox/tbd/schema/shell.json** |             |

**********

Statements contain the single OpenEoX entries.

**Type: Statement (Record)**

| ID | Name               | Type             | \# | Description |
|----|--------------------|------------------|----|-------------|
| 1  | **core**           | c:Core           | 1  |             |
| 2  | **productName**    | ProductName_t    | 1  |             |
| 3  | **productVersion** | ProductVersion_t | 1  |             |
| 4  | **supplierName**   | SupplierName_t   | 1  |             |

**********

| Type Name         | Type Definition | Description                       |
|-------------------|-----------------|-----------------------------------|
| **ProductName_t** | String          | Contains the name of the product. |

**********

| Type Name            | Type Definition | Description                                     |
|----------------------|-----------------|-------------------------------------------------|
| **ProductVersion_t** | String          | Contains the version or release of the product. |

**********

| Type Name          | Type Definition | Description                                            |
|--------------------|-----------------|--------------------------------------------------------|
| **SupplierName_t** | String          | Contains the name of the supplier or service provider. |

**********
