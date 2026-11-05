"""Frame attributed source logos without altering their colors or proportions."""

import base64
import hashlib
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets' / 'affiliations'


def build_panels() -> None:
    manifest = json.loads((ASSETS / 'manifest.json').read_text())
    for asset in manifest['assets']:
        original = (ASSETS / 'originals' / asset['file']).read_bytes()
        if hashlib.sha256(original).hexdigest() != asset['sha256']:
            raise ValueError(f"Source checksum changed for {asset['id']}")
        content = original
        if 'svgStyle' in asset:
            # Inline SVGs rely on the official site's stylesheet for their colors.
            svg = original.decode()
            end = svg.index('>') + 1
            content = (svg[:end] + '<style>' + asset['svgStyle'] + '</style>' + svg[end:]).encode()
        payload = base64.b64encode(content).decode('ascii')
        title = html.escape(asset['label'])
        description = html.escape('Original identifying logo. Source and attribution: ' + asset['sourcePage'])
        panel = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" '
            'role="img" aria-labelledby="title description">'
            f'<title id="title">{title}</title>'
            f'<desc id="description">{description}</desc>'
            '<path fill="#FFFFFF" d="M0 0h300v180H0z"/>'
            '<image x="26" y="22" width="248" height="136" '
            'preserveAspectRatio="xMidYMid meet" '
            f'href="data:{asset["mime"]};base64,{payload}"/>'
            '</svg>\n'
        )
        (ASSETS / f"{asset['id']}.svg").write_text(panel)
        print(f"Prepared {asset['id']}: verified source, unchanged proportions")


if __name__ == '__main__':
    build_panels()
