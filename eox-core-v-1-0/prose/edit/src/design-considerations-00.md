# Design Considerations

The OpenEoX provides the vocabulary for exchanging standardized End-of-X (EoX) life cycle data for any product.
This includes, but is not limited to hardware, software and specifications, as well as all supplier-consumer
relationships, services and offerings.

## OpenEoX Architecture

The OpenEoX standard is architected as a modular three-layer framework:

### OpenEoX Core (this specification)

The OpenEoX Core specification contains the fundamental EoX life cycle information elements and is
designed to be imported by other standards or integrated directly into product responses.
The Core schema establishes one part of the essential data elements required for any EoX statement:

**Required fields:**

- `end_of_life`: The definitive timestamp when all vendor support ceases
- `end_of_security_support`: The critical timestamp when security remediation commitments end
- `last_updated`: The timestamp tracking for data freshness and change management

Optionally, the standard also conveys additional life cycle events.

The core information can be provided independently when the product context is available through
other means, such as SNMP responses, HTTPS API responses.

### OpenEoX Shell

The OpenEoX Shell specification provides the binding mechanism that combines OpenEoX Core life cycle
information to specific product identifications.
This combination is called an "OpenEoX statement" - a complete, standalone representation of life cycle
information for a specific product.
The Shell forms the standalone mode in OpenEoX, enabling complete life cycle statements that can be
processed independently without external context.

### OpenEoX API

The OpenEoX API specification addresses the distribution, discovery, and consumption of OpenEoX Core
and Shell data across vendor ecosystems and consumer applications.
The API specification defines standardized endpoints, query mechanisms, and data exchange patterns
that enable automated integration.

## Design Principles

### Standardization and Interoperability

OpenEoX addresses the current industry challenge where vendors use proprietary, inconsistent formats
for communicating life cycle information.
By establishing a common JSON-based format, OpenEoX enables:

- Automated processing and integration across vendor ecosystems
- Consistent interpretation of life cycle stages regardless of vendor
- Reduced operational overhead in managing multi-vendor environments
- Enhanced accuracy in infrastructure life cycle planning

### Security-First Approach

Recognition that End-of-Security-Support represents a critical inflection point for infrastructure
security has influenced the OpenEoX design.
The mandatory `end_of_security_support` field ensures that security life cycle information is
always available, supporting:

- Proactive vulnerability management planning
- Compliance with security frameworks requiring current support status
- Risk assessment for critical infrastructure components
- Automated alerting when security support approaches termination

## Industry Applications

### Vendor Perspectives

**OpenEoX enables vendors to:**

- Standardize EoX communication across all product lines and channels
- Reduce support inquiries related to life cycle confusion
- Demonstrate proactive customer stewardship through clear life cycle communication
- Support automated customer notification systems
- Facilitate integration with partner and reseller systems

### Consumer Perspectives

**Organizations consuming OpenEoX information benefit through:**

- Automated discovery of life cycle status across multi-vendor environments
- Proactive planning for product refreshes and migrations
- Enhanced compliance reporting for security and regulatory frameworks
- Reduced operational risk from unexpected support terminations
- Streamlined asset management and inventory tracking

The OpenEoX architecture ensures that organizations can adopt OpenEoX in a manner
that aligns with their existing infrastructure and operational models while preserving
the ability to enhance integration over time.
