# Safety, Security and Data Protection{#safety-security-and-data-protection}

All safety, security, and data protection requirements relevant to the context in which OpenEoX information items are used MUST
be translated into, and consistently enforced through, OpenEoX implementations and processes.

OpenEoX information items are based on JSON, thus the security considerations of [cite](#RFC8259) apply and
are repeated here as service for the reader:

> Generally, there are security issues with scripting languages.  JSON is a subset of JavaScript but excludes assignment and invocation.
>
> Since JSON's syntax is borrowed from JavaScript, it is possible to use that language's `eval()` function to parse most JSON texts
> (but not all; certain characters such as `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript).
> This generally constitutes an unacceptable security risk, since the text could contain executable code along with data declarations.
> The same consideration applies to the use of eval()-like functions in any other programming language in which JSON texts conform to that language's syntax.

Additional mitigation measures, such as retrieving OpenEoX Core Information only
from sources trusted by the deployment, authenticating the source, and verifying
the integrity of the information, including any available signature, before
parsing, SHOULD be in place to reduce the risk further.

The `last_updated` property is producer-supplied metadata and does not by itself
establish that an information item is current. A previously valid, signed
information item may be replayed. Consumers SHOULD apply freshness checks
appropriate to their deployment to detect stale or replayed information items.

If a Consumer cannot verify the source, integrity, or freshness of an
information item, it SHOULD treat the item as unverified, make the verification
status visible to users, and follow the deployment’s fallback or review policy.
An unverified information item SHOULD NOT be the sole basis for an automated
lifecycle action.

---
