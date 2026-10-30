"""Write cite.ris and cite.bib beside every page, from the same fields as the page's citation line."""

import os


def _fields(page, config):
    cite = config["extra"]["citation"]
    return {
        "title": cite["site_title"] if page.is_homepage else page.title,
        "site": cite["site_title"],
        "family": cite["author_family"],
        "given": cite["author_given"],
        "date": str(page.meta.get("date") or cite["date"]),
        "url": page.canonical_url,
    }


def on_post_page(output, page, config):
    f = _fields(page, config)
    out_dir = os.path.join(config["site_dir"], page.url)
    os.makedirs(out_dir, exist_ok=True)
    ris = [
        "TY  - ELEC",
        f"TI  - {f['title']}",
        f"AU  - {f['family']}, {f['given']}",
        f"PY  - {f['date'][:4]}",
        f"DA  - {f['date'].replace('-', '/')}",
        f"T2  - {f['site']}",
        f"UR  - {f['url']}",
        "LA  - en",
        "ER  - ",
    ]
    with open(os.path.join(out_dir, "cite.ris"), "w", encoding="utf-8") as fh:
        fh.write("\r\n".join(ris) + "\r\n")
    key = "smithies" + f["date"][:4] + (page.url.strip("/").replace("-", "").replace("/", "") or "mechanism")
    bib = (
        f"@online{{{key},\n"
        f"  author       = {{{f['family']}, {f['given']}}},\n"
        f"  title        = {{{f['title']}}},\n"
        + ("" if page.is_homepage else f"  organization = {{{f['site']}}},\n")
        + f"  date         = {{{f['date']}}},\n"
        f"  url          = {{{f['url']}}},\n"
        "}\n"
    )
    with open(os.path.join(out_dir, "cite.bib"), "w", encoding="utf-8") as fh:
        fh.write(bib)
    return output
