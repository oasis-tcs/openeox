# Design Considerations

The OpenEoX framework is a comprehensive language to exchange End-of-X (EoX) lifecycle information formulated in JSON, addressing the critical industry need for standardized communication of product lifecycle stages across commercial and open-source software and hardware.

## Framework Architecture

The OpenEoX standard is architected as a modular three-layer framework:

### OpenEoX Core (this specification)
Contains the fundamental EoX lifecycle information elements and is designed to be imported by other standards or integrated directly into product responses. The core schema establishes the essential data elements required for any EoX statement:

- **end_of_life**: The definitive timestamp when all vendor support ceases
- **end_of_security_support**: The critical timestamp when security remediation commitments end
- **end_of_sales**: The commercial availability termination timestamp (optional)
- **last_updated**: RFC 3339 timestamp tracking for data freshness and change management

The core information can be provided independently when the product context is available through other means, such as SNMP responses, HTTPS API responses.

### OpenEoX Shell
Provides the binding mechanism that combines OpenEoX core lifecycle information to specific product identifications. This combination is called an "OpenEoX statement" - a complete, standalone representation of lifecycle information for a specific product.

The Shell schema supports multiple product types through specialized identification schemas:
- **Software Products**: Identified by vendor name, product name, and version
- **Hardware Products**: Identified by vendor name, product name, model, and serial number ranges
- **Hardware with Software Products**: Combined identification supporting both hardware and embedded software components

The Shell forms the standalone mode in OpenEoX, enabling complete lifecycle statements that can be processed independently without external context.

### OpenEoX API
Addresses the distribution, discovery, and consumption of OpenEoX Core and Shell data across vendor ecosystems and consumer applications. The API specification defines standardized endpoints, query mechanisms, and data exchange patterns that enable automated integration.

## Design Principles

### Standardization and Interoperability
The framework addresses the current industry challenge where vendors use proprietary, inconsistent formats for communicating lifecycle information. By establishing a common JSON-based format, OpenEoX enables:
- Automated processing and integration across vendor ecosystems
- Consistent interpretation of lifecycle stages regardless of vendor
- Reduced operational overhead in managing multi-vendor environments
- Enhanced accuracy in infrastructure lifecycle planning

### Granular Product Identification
Care has been taken to design product identification containers that support fine-grained mapping of EoX statements onto specific product-platform-version combinations while minimizing data duplication through well-defined referencing structures. The modular approach separates lifecycle data from product identification concerns, enabling reuse across different product types while maintaining schema validity.

### Security-First Approach
Recognition that End-of-Security-Support represents a critical inflection point for infrastructure security has influenced the framework design. The mandatory **end_of_security_support** field ensures that security lifecycle information is always available, supporting:
- Proactive vulnerability management planning
- Compliance with security frameworks requiring current support status
- Risk assessment for critical infrastructure components
- Automated alerting when security support approaches termination

## Industry Applications

### Vendor Perspectives
The framework enables vendors to:
- Standardize EoX communication across all product lines and channels
- Reduce support inquiries related to lifecycle confusion
- Demonstrate proactive customer stewardship through clear lifecycle communication
- Support automated customer notification systems
- Facilitate integration with partner and reseller systems

### Consumer Perspectives
Organizations consuming EoX information benefit through:
- Automated discovery of lifecycle status across multi-vendor environments
- Proactive planning for product refreshes and migrations
- Enhanced compliance reporting for security and regulatory frameworks
- Reduced operational risk from unexpected support terminations
- Streamlined asset management and inventory tracking

The OpenEoX framework ensures that organizations can adopt OpenEoX in a manner that aligns with their existing infrastructure and operational models while preserving the ability to enhance integration over time.
