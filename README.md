# Original Power BI assets — publication note

The source project contains three real `.pbix` reports: a faculty report, a facilities report and an administration report. Their screenshots appear under `../assets/` and the corresponding business decisions are documented in `../docs/`.

The original `.pbix` files are **not included in the public-ready package** because they contain embedded data models and original remote-artifact identifiers. Before uploading the files to GitHub, perform a publication and privacy review, confirm source-data rights, open and validate all visuals in Power BI Desktop and correct the aggregation/axis issues described in `../docs/09-provenance-and-limitations.md`.

The portable, independently reproducible implementation is located in `../demo/`, and the interactive lightweight showcase is located in `../site/`. Neither claims to be a Power BI deployment.
