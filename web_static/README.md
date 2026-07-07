# AirBnB clone - Web static

Static HTML/CSS prototypes of the AirBnB clone front-end.

Each step builds on the previous one:

- `0-index.html`: header and footer, inline styling
- `1-index.html`: same layout, `style` tag in the `head`
- `2-index.html`: same layout, external CSS files
- `3-index.html`: zoning (fonts, colors, logo, favicon)
- `4-index.html`: filters box with a Search button
- `5-index.html`: locations and amenities filters
- `6-index.html`: dropdown popovers on the filters
- `7-index.html`: places section with search results
- `8-index.html`: detailed place cards (price, info, owner, description)

Styles live in `styles/`, images in `images/`. No JavaScript, no `id`
selectors, no `!important`.

## Running it

From this directory, start a local server:

```
python -m http.server 8000
```

(Windows without a `python` alias: `py -3 -m http.server 8000`)

Then open `http://localhost:8000/<file>`, e.g.
`http://localhost:8000/8-index.html`, swapping the number for any task
(0 through 8).

Alternatively, since these are static files with no JavaScript and only
relative paths, you can open any `*-index.html` file directly in a browser
(double-click it, or open via `file://`). If styling looks off that way,
use the server method instead.
