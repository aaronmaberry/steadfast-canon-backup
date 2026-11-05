if __name__ == "__main__":
    only = set(sys.argv[1:])
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
        for name, (html, alpha) in B.items():
            if only and name not in only:
                continue
            f = G / "html" / f"l04-{name}.html"; f.write_text(html)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(100)
            pg.screenshot(path=str(OUT / f"{name}.png"), omit_background=alpha)
        b.close()
    print("rendered", len(B) if not only else len(only), "boards")
