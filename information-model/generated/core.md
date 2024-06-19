         title: "EOL and EOS Information"
       package: "https://docs.oasis-open.org/openeox/tbd/schema/core"
   description: "A draft schema for representing End-of-Life (EOL) and End-of-Support (EOS) information in OpenEoX."
       exports: ["Core"]
        config: {"$TypeName": "^[$A-Z][-_$A-Za-z0-9]{0,63}$"}

**Type: Core (Record)**

| ID | Name             | Type        | \#    | Description                         |
|----|------------------|-------------|-------|-------------------------------------|
| 1  | **schema**       | Schema_core | 1     |                                     |
| 2  | **last_updated** | Timestamp   | 1     | Timestamp of last change            |
| 3  | **status**       | Status      | 1..\* | Contains a list of status elements. |

**********

Specifies the schema the JSON object must be valid against.

**Type: Schema_core (Enumerated)**

| ID | Item                                                    | Description |
|----|---------------------------------------------------------|-------------|
| 1  | **https://docs.oasis-open.org/openeox/tbd/schema/core** |             |

**********

| Type Name     | Type Definition | Description                     |
|---------------|-----------------|---------------------------------|
| **Timestamp** | String          | Contains the RFC 3339 timestamp |

**********

Contains a single entry in the product lifecycle.

**Type: Status (Record)**

| ID | Name          | Type            | \# | Description                                                      |
|----|---------------|-----------------|----|------------------------------------------------------------------|
| 1  | **category**  | Category        | 1  | Contains the category of the status                              |
| 2  | **timestamp** | StatusTimestamp | 1  | Contains the timestamp at which the product enters the category. |

**********

**Type: Category (Enumerated)**

| ID | Item             | Description |
|----|------------------|-------------|
| 1  | **EndOfLife**    |             |
| 2  | **EndOfSupport** |             |

**********

**Type: StatusTimestamp (Choice)**

| ID | Name           | Type       | \# | Description |
|----|----------------|------------|----|-------------|
| 1  | **timestamp**  | Timestamp  | 1  |             |
| 2  | **timeValues** | TimeValues | 1  |             |

**********

**Type: TimeValues (Enumerated)**

| ID | Item    | Description |
|----|---------|-------------|
| 1  | **tba** |             |

**********
