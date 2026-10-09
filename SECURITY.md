# Security Policy

This repository provides reproducible **research materials** and saved model artifacts; it is not a hosted application, clinical diagnostic service or medical device.

## Reporting a vulnerability

Please do **not** disclose credentials, access tokens, sensitive records or detailed security exploits in public GitHub Issues or pull requests.

If private vulnerability reporting is enabled, use the repository's **Security → Advisories → Report a vulnerability** option. Otherwise, request a private contact channel through the repository owner's GitHub profile before sharing sensitive details.

## Scope

Relevant reports include exposed secrets, unsafe deserialisation or dependency use, malicious file-handling behavior and unintended disclosure of non-public data. Saved `.joblib` models must be treated as trusted artifacts; do not load unverified files from third parties.

There is no deployment with guaranteed support or security service-level agreement. A security repair that could affect scientific output will be described and reviewed explicitly rather than silently changing the frozen results.
