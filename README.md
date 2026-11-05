# Ionian Wikithon organization profile

This repository publishes the public profile of [Ionian Wikithon](https://github.com/Ionian-Wikithon). The visitor-facing document is [profile/README.md](profile/README.md).

The visual identity uses an original `[[W]]` mark, a forest-green palette and an editorial layout. It connects open knowledge, computer science and community without using institutional or Wikimedia logos.

## Files

```text
profile/README.md              Public organization Overview
assets/brand/logo.svg          Editable original wiki-code mark
assets/brand/banner.svg        Desktop header for light themes
assets/brand/banner-dark.svg   Desktop header for dark themes
assets/brand/banner-mobile.svg Mobile header for light themes
assets/brand/banner-mobile-dark.svg
                              Mobile header for dark themes
docs/SOURCES.md                Historical evidence and editorial decisions
README.md                      Maintenance and publication guidance
```

There is no build system, package installation or runtime service. GitHub renders the Markdown and SVG files directly.

## Maintain the profile

- Edit public-facing copy in `profile/README.md`. Keep the opening short and use native Markdown headings and links.
- Verify historical additions against original university announcements or Wikimedia event documentation. Record important evidence and limitations in [docs/SOURCES.md](docs/SOURCES.md).
- Feature a repository only after confirming it is public. Use its exact name, a direct link, its learning purpose and its current maintenance status. Replace the introductory publishing section when public workshop or software collections become available.
- Add each future edition as a short dated entry in the journey, with a reliable reference. A proposal or announcement alone does not prove completion or an outcome.
- Keep private repository names, source code, unpublished plans and personal participant details out of the public profile.
- Do not add organization-wide default community-policy files casually: special files in a public `.github` repository can apply to other repositories. This repository's maintenance notes do not replace individual projects' contribution policies.

## Visual identity

| Role                         | Color     |
| ---------------------------- | --------- |
| Primary text and mark        | `#123D2A` |
| Brand green                  | `#26734D` |
| Accent, used sparingly       | `#69A84F` |
| Light header surface         | `#F7FAF7` |
| Light secondary surface      | `#EAF1E8` |
| Dark-theme header surface    | `#E5EFE4` |
| Dark-theme secondary surface | `#D9E7D7` |
| Secondary text               | `#435E4B` |

Dark-mode artwork uses a muted sage surface rather than a predominantly black image. GitHub's own theme controls the surrounding text and page. A `<picture>` selects the desktop or mobile composition and the appropriate theme variant; the ordinary desktop image remains the fallback.

SVGs use a `viewBox`, local system-font fallbacks, basic paths and accessible titles and descriptions. They contain no scripts, external fonts, animations, embedded raster imagery or third-party logo assets. Keep all variants synchronized when changing copy or geometry. The mark remains editable and is not presented as an institution's or Wikimedia's trademark.

Profile image URLs point to this public repository's raw files so they work on both the repository page and the organization Overview. Asset documentation links use relative repository paths. If the default branch or asset paths change, update all four image URLs together.

## Review and publish

Before publishing, check the actual GitHub-rendered profile at desktop and phone widths, in light and dark themes. Confirm that the selected header remains readable, every internal anchor resolves, SVGs load, and public links work while signed out. Relative links in the root README must resolve from this repository.

Members of the organization may have a different Overview view; inspect the public view to confirm what visitors see. GitHub's [organization-profile documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile) explains the special repository and `profile/README.md` path.

Visitors may suggest corrections through issues or pull requests. Trusted maintainers with write access may commit directly. All maintainer commits must be GPG-signed with their own identity; never bypass a signing failure.

From a clean checkout on `main`, synchronize before editing:

```sh
git pull --ff-only origin main
```

After reviewing the source and rendered changes:

```sh
git diff --check
git add -- profile/README.md
git diff --cached
git commit -S -m 'Clarify the organization profile'
git verify-commit HEAD
git push origin main
```

Stage other changed assets or source notes explicitly when needed. Never force-push. Publishing the default branch of this public `.github` repository updates the organization's public Overview; it does not deploy any separate application or change other repositories' visibility.
