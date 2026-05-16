# Bound connector action gate

This playbook hardens Adventures workflows against stale, sparse, or partially hydrated connector manifests.

## Scope

Use this gate whenever a turn, skill step, or project playbook stage clearly requires a bound external app connector such as Canva, GitHub, Google Drive, Adobe Photoshop, or a future external app connector.

## Required gate

At the connector action boundary, refresh the relevant connector namespace before selecting tools or declaring tools unavailable.

Examples:

- Canva task: refresh `/Canva`.
- GitHub API task: refresh `/GitHub`.
- Google Drive or Slides task: refresh `/Google Drive`.
- Photoshop task: refresh `/Adobe Photoshop`.

If the namespace is not known from the task, list top-level resources once, identify the connector namespace, then refresh that namespace directly.

## Anti-sparsity rule

A sparse or partial tool list is provisional until the connector namespace has been refreshed at the point of use.

Do not explain missing tools as product impossibility, connector limitation, user binding failure, or unsupported workflow from a stale or non-refreshed manifest.

If a needed action is still missing after namespace refresh, report only the observed refreshed connector state:

- the exact connector namespace refreshed;
- the exact action sought;
- the exact absence or tool error;
- what this proves: the action is not exposed in the refreshed connector namespace;
- what this does not prove: product incapability, user-binding failure, or URL/resource incompatibility unless separately evidenced.

## Required ledger fields

When this gate is used inside a longer playbook run, record:

- `connector_namespace_refreshed`;
- `connector_action_sought`;
- `connector_refresh_result`;
- `connector_action_result`;
- `connector_unavailability_claim_basis` when any absence is reported.

## Recovery rule

If another route or session proves the connector action exists or succeeds, treat that as stronger evidence than an earlier stale manifest. Refresh the relevant namespace again before making any further capability claim.
