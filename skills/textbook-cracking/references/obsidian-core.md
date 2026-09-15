<!--
GENERATED FILE — DO NOT EDIT
contract-version: 1.0.0
source: _shared/obsidian-core/obsidian-core.md
source-sha256: 535aed51410b5e478645c91450b2e889214946f085c8db920ead22f30e6d52e8
Regenerate with: python3 _shared/obsidian-core/sync_obsidian_core.py sync
-->

# Compact Obsidian Authoring Core

## Purpose and precedence

Use this contract whenever the Skill creates or updates Obsidian artifacts. It is package-local and has no runtime dependency on another Skill.

Apply rules in this order:

1. Explicit user instructions.
2. The current Skill's domain-specific rules and templates.
3. This compact Core.
4. General Markdown conventions.

More-specific domain rules may override this Core. Never discard a domain requirement merely to make files stylistically uniform.

## Properties

- YAML frontmatter starts on the first line and is bounded by `---`.
- Prefer flat properties. Keep the type of each property consistent across the Vault.
- Use ISO dates: `YYYY-MM-DD`; use ISO date-times when time is required.
- Use `tags`, `aliases`, and `cssclasses`, not singular variants.
- Prefer block lists when values may contain punctuation.
- Quote strings containing YAML-special characters.
- Quote wikilinks stored as property values: `related: "[[Other Note]]"`.
- Preserve unknown user-authored properties during updates.

## Links and embeds

- Use `[[Note]]`, `[[Note#Heading]]`, and `[[Note#^block-id]]` for Vault content.
- Use `[label](https://example.com)` for external URLs.
- Use `![[Note]]`, `![[image.png|300]]`, and `![[document.pdf#page=3]]` for embeds.
- Do not create speculative wikilinks to pages the workflow does not intend to create.
- Prefer stable note names or paths that remain valid when the Vault is moved.

## Callouts, math, and diagrams

- Use native Callouts such as `abstract`, `info`, `note`, `tip`, `warning`, `question`, `success`, `failure`, `danger`, `bug`, and `example`.
- Use one Callout per meaningful idea; do not turn every paragraph into a Callout.
- Use `$...$` for inline math and `$$` on separate lines for block math.
- Inside a Callout, prefix every formula line, including blank lines and delimiters, with `>`.
- Use Mermaid only when relationships or sequences are clearer visually than in prose.

## Safe updates and ownership

1. Read the complete existing file before editing it.
2. Make the narrowest change that satisfies the workflow.
3. Preserve user-authored prose, unknown frontmatter, comments, and unsupported extensions.
4. Never replace an entire mixed-ownership note merely to update one generated section.
5. When repeated Agent updates share a note with user writing, use stable namespaced regions:

```html
<!-- agent-managed:start id="<domain>:<stable-id>" -->
...generated content...
<!-- agent-managed:end -->
```

Replace only the matching region. Content outside it remains byte-for-byte unchanged unless the user explicitly asks otherwise.

## Verification

After writing:

1. Parse or structurally inspect YAML, JSON, or Canvas data as applicable.
2. Confirm required properties and template sections exist.
3. Confirm no unresolved template placeholders remain.
4. Confirm internal links and embeds use valid Obsidian syntax.
5. Confirm managed-region IDs are unique and markers are balanced.
6. If Obsidian CLI or another safe renderer is already available, use it for optional rendering verification; absence of that tool must not make static files invalid.

## Optional enhancements

Obsidian Bases, JSON Canvas, Obsidian CLI, MCP integrations, and Dataview are enhancements, not requirements for basic correctness. A Skill must still produce useful static Markdown when optional capabilities are unavailable, unless its documented domain purpose explicitly requires one of them.

