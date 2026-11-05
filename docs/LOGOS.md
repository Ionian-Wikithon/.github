# Logo sources and credits

Retrieved on 5 November 2026. The institutional marks identify the documented organizing collaboration. Wikimedia and Wikipedia appear separately in the resources section and link to their own sites. No mark is incorporated into the original Ionian Wikithon wiki-code identity.

## NMSLab

- Source: [Ionian University's 2024 Wikithon announcement](https://di.ionio.gr/gr/news/30613/) and its [official poster PDF](https://ionio.gr/download.php?f=30000-30999/IU-nf-30613-93979-gr.pdf).
- Asset: [originals/nmslab.png](../assets/affiliations/originals/nmslab.png).
- Credit: NMSLab / Ionian University. An individual logo designer is not identified in the poster.
- Handling: the PDF contains a 3543 x 5010 raster poster. The logo was extracted at its native resolution from the rectangle `left=2040, top=4175, width=760, height=220` and saved as PNG. There is no redrawing, recoloring, retouching or shape change.
- Status: institutional identifying mark. No separate open-content license is stated in the poster; this repository does not assign one to it.

The laboratory's standalone host timed out during retrieval. The university-published poster provides the original source for the displayed mark.

## Department of Informatics, Ionian University

- Source: the inline logo SVG in [the department's official website header](https://di.ionio.gr/en/), paired with the colors in its [official stylesheet](https://di.ionio.gr/scripts/di.css).
- Asset: [originals/department.svg](../assets/affiliations/originals/department.svg).
- Credit: Department of Informatics, Ionian University. An individual logo designer is not identified on the page.
- Handling: the inline SVG is saved unchanged. The display panel embeds its original CSS declarations: `.path1 { fill: #9C0101; }` and `.path2 { fill: #143259; }`. Its geometry and original colors are preserved.
- Status: institutional identifying mark. No separate open-content license is stated on the source page; this repository does not assign one to it.

## Wikimedia Community User Group Greece

- Source: [Wikimedia Commons file description](https://commons.wikimedia.org/wiki/File:Wikimedia_Community_User_Group_Greece.svg).
- Asset: [originals/wikimedia-greece.svg](../assets/affiliations/originals/wikimedia-greece.svg).
- Credit: Wikimedia Foundation logo and trademark, adapted for the user group by [Exec8](https://commons.wikimedia.org/wiki/User:Exec8).
- Copyright status: the Commons description marks the file as public domain because it is ineligible for copyright. Wikimedia trademark restrictions remain applicable.
- Handling: original SVG unchanged; displayed proportionally on a white surround.

## Wikimedia

- Source: [Wikimedia Commons file description](https://commons.wikimedia.org/wiki/File:Wikimedia-logo.svg).
- Asset: [originals/wikimedia.svg](../assets/affiliations/originals/wikimedia.svg).
- Credit: logo originally designed by Neolux; SVG by Zscout370 with modifications by Dbenbenn.
- Copyright status: public domain according to the Commons description. Wikimedia trademark restrictions remain applicable.
- Handling: original SVG unchanged; displayed proportionally on a white surround.

## Wikipedia

- Source: [Wikimedia Commons file description](https://commons.wikimedia.org/wiki/File:Wikipedia-logo-v2.svg).
- Asset: [originals/wikipedia.svg](../assets/affiliations/originals/wikipedia.svg).
- Credit: Wikimedia; version 1 by Nohat, based on the concept by Paullusmagnus.
- License: [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Wikimedia trademark restrictions remain applicable.
- Handling: original SVG unchanged; displayed proportionally on a white surround. The profile includes a visible credit, license link and original-file link.

## Display and maintenance

The [manifest](../assets/affiliations/manifest.json) records source URLs, attribution, modifications and SHA-256 checksums. Each displayed panel embeds the source artwork as a data URI inside a white SVG surface, using `preserveAspectRatio="xMidYMid meet"`. The white surround keeps black details and lettering visible in GitHub's dark theme. It is separate from the logo artwork.

The panels contain accessible titles and descriptions, load without third-party image services, and keep each mark's original proportions. The department panel also embeds the source website's original CSS fills, which would otherwise be lost when extracting its inline SVG. No recoloring is used to match the archive's green palette.

To regenerate the display panels after reviewing any source update:

```sh
python3 scripts/build-logo-panels.py
```

The script uses Python's standard library, validates every source checksum and regenerates the five panel SVGs. If replacing an original, review its source and rights, update its manifest entry and checksum, rebuild, then inspect desktop and mobile rendering in both themes. Do not run formatters or optimizers over the preserved third-party originals.

The [Wikimedia trademark policy](https://foundation.wikimedia.org/wiki/Policy:Trademark_policy) distinguishes linking to Wikimedia sites, truthful references and uses requiring permission. The displayed Wikimedia and Wikipedia marks link to their respective sites. This repository does not grant trademark rights or relicense the institutional marks, and the logos do not establish any affiliation beyond the relationships documented in the profile.
