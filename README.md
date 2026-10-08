# cert-path-planner

Answers the first question every hardware program asks the compliance lead: which standards apply, in what order do we test, and how long until we can ship?

Pick a product type and target markets, switch on the scope that applies (grid export, battery, radio, safety software, connectivity), and it returns:

- a **standards map** grouped by phase
- the **test sequence**, with which phases can run in parallel
- the **long poles** that set the schedule
- a **timeline** with an optimistic and a pessimistic case, as markdown and CSV for your project tool

## Product types

| Key | Product |
|---|---|
| `mv-sst` | Medium-voltage solid-state transformer / power supply (e.g. MV AC to 800 VDC for data centers) |
| `bess` | Battery energy storage system |
| `ev-charger` | EV charger / EVSE, optionally bidirectional |
| `industrial-robot` | Industrial robot or robot cell, including cobot applications |
| `mobile-robot` | Industrial mobile robot / AMR / AGV |
| `service-robot` | Service, personal care or humanoid robot in public or home settings |
| `consumer-electronics` | Consumer / ICT electronics with a lithium battery |

Markets: `us`, `eu` or both. Options: `grid_export`, `battery`, `wireless`, `software_safety`, `connected`.

## Example

```
pip install -e .
cert-path mv-sst --markets us --option grid_export --csv plan.csv
```

```
# Certification path: Medium-voltage solid-state transformer / power supply (e.g. MV AC to 800 VDC)

Planned duration: 28-60 weeks (6-14 months) from design freeze.

| Phase | Standard | Weeks |
| Product / system safety | UL 2877 outline of investigation, medium-voltage power supplies | 16-30 |
| Grid interconnection | UL 1741 SB grid support, tested to IEEE 1547.1-2020 | 8-16 |
| Functional safety and cybersecurity | UL 1998 / UL 60730-1 Annex H software for safety controls | 8-16 |
...

Plan, hazard analysis, design revi |##--                                                        |
Pre-compliance testing (in-house o |  ####------                                                |
Product / system safety            |      ################--------------------                  |
Grid interconnection               |      ########--------------                                |
Listing, factory inspection, techn |                      ##------------------------            |
Installation code / AHJ approval   |                        ####--------------------------------|
```

Full example outputs for an MV SST, a US/EU BESS and a US/EU mobile robot are in [`examples/`](examples/).

## How the timeline is built

Phases run in stages: plan, then pre-compliance, then component certifications, then system safety, EMC, grid and functional safety in parallel, then listing and factory inspection, then site approval. Each phase lasts as long as its slowest standard. That is a deliberate simplification. Real programs overlap stages and get blocked by things a table cannot see: a failed 9540A run, a lab slot that moves, a utility that changes its source requirements document.

## Editing the catalog

Every standard, its phase, its lead time and its markets live in [`cert_path/catalog.py`](cert_path/catalog.py). The lead times are planning assumptions for a first-of-kind product with lab slots already booked. They are not quotes. Change them to match your NRTL, your lab capacity and how mature your design is, and the plan updates.

## What it does not do

It does not decide applicability for you. Whether UL 1741 SB applies to an SST, or whether a robot application falls under the EU Machinery Regulation, depends on the final design and intended use. Treat the output as the first draft of a certification plan that an engineer then defends.

## Tests

```
pip install pytest
pytest
```

## License

MIT. Built by [Tsadi Shvo](https://www.linkedin.com/in/tsadishvo/), product safety and compliance for robotics, EV/BESS and power electronics.
