"""Standards catalog, product profiles and planning lead times.

Lead times are planning assumptions in weeks (low, high) for a first-of-kind
product with a prepared design and a booked lab. They are not quotes. Edit
them for your lab, your NRTL and your product maturity; everything else in
the planner is derived from this file.
"""

# Phases run in this order. Phases in the same "stage" run in parallel.
PHASES = [
    {"id": "plan", "name": "Plan, hazard analysis, design review", "stage": 1},
    {"id": "precomp", "name": "Pre-compliance testing (in-house or lab)", "stage": 2},
    {"id": "component", "name": "Component and cell certifications", "stage": 3},
    {"id": "safety", "name": "Product / system safety", "stage": 4},
    {"id": "emc", "name": "EMC and radio", "stage": 4},
    {"id": "grid", "name": "Grid interconnection", "stage": 4},
    {"id": "fusa", "name": "Functional safety and cybersecurity", "stage": 4},
    {"id": "listing", "name": "Listing, factory inspection, technical file", "stage": 5},
    {"id": "site", "name": "Installation code / AHJ approval", "stage": 6},
]

# id: (title, phase, (low, high) weeks, markets)
STANDARDS = {
    "HARA": ("Hazard analysis and risk assessment (ISO 12100 method)", "plan", (2, 4), {"us", "eu"}),
    "PRECOMP": ("Pre-compliance safety and EMC screening", "precomp", (4, 8), {"us", "eu"}),

    # batteries
    "UN38.3": ("UN 38.3 lithium battery transport tests", "component", (4, 8), {"us", "eu"}),
    "UL1973": ("UL 1973 batteries for stationary and motive auxiliary power", "component", (10, 16), {"us"}),
    "IEC62619": ("IEC 62619 secondary lithium cells and batteries, industrial", "component", (8, 14), {"eu"}),
    "IEC62133-2": ("IEC 62133-2 portable lithium cells and batteries", "component", (6, 10), {"us", "eu"}),
    "UL9540A": ("UL 9540A thermal runaway fire propagation test method", "component", (12, 24), {"us"}),
    "EUBATT": ("EU Battery Regulation 2023/1542 conformity, labelling, due diligence", "listing", (4, 10), {"eu"}),

    # system safety
    "UL9540": ("UL 9540 energy storage systems and equipment", "safety", (12, 20), {"us"}),
    "UL2877": ("UL 2877 outline of investigation, medium-voltage power supplies", "safety", (16, 30), {"us"}),
    "IEC62477-1": ("IEC 62477-1 safety of power electronic converter systems", "safety", (8, 12), {"eu"}),
    "UL62368": ("IEC/UL 62368-1 audio/video, ICT equipment safety", "safety", (6, 10), {"us", "eu"}),
    "UL2202": ("UL 2202 electric vehicle charging system equipment", "safety", (12, 20), {"us"}),
    "UL2594": ("UL 2594 electric vehicle supply equipment", "safety", (8, 12), {"us"}),
    "UL9741": ("UL 9741 bidirectional EV charging system equipment", "safety", (12, 20), {"us"}),
    "IEC61851": ("IEC 61851-1 EV conductive charging systems", "safety", (8, 14), {"eu"}),
    "ISO10218": ("ISO 10218-1/-2:2025 industrial robots and robot applications", "safety", (8, 16), {"us", "eu"}),
    "UL1740": ("UL 1740 robots and robotic equipment (with NFPA 79)", "safety", (10, 16), {"us"}),
    "IEC60204-1": ("IEC 60204-1 electrical equipment of machines", "safety", (4, 8), {"eu"}),
    "R15.08": ("ANSI/A3 R15.08-1/-2 industrial mobile robots", "safety", (8, 14), {"us"}),
    "ISO3691-4": ("ISO 3691-4 driverless industrial trucks", "safety", (8, 14), {"eu"}),
    "UL3100": ("UL 3100 automated mobile platforms", "safety", (10, 16), {"us"}),
    "ISO13482": ("ISO 13482 personal care robots", "safety", (8, 14), {"us", "eu"}),
    "UL3300": ("UL 3300 service, communication, information, education and entertainment robots", "safety", (10, 16), {"us"}),
    "MACHREG": ("EU Machinery Regulation 2023/1230 (applies from 20 Jan 2027)", "listing", (6, 12), {"eu"}),
    "LVD": ("EU Low Voltage Directive 2014/35/EU technical file", "listing", (3, 6), {"eu"}),

    # EMC and radio
    "FCC15B": ("FCC Part 15 Subpart B unintentional radiators", "emc", (2, 4), {"us"}),
    "FCC15C": ("FCC Part 15 Subpart C intentional radiators (radio modules)", "emc", (4, 8), {"us"}),
    "EUEMC": ("EU EMC Directive 2014/30/EU (EN 61000-6-x / product family)", "emc", (4, 6), {"eu"}),
    "RED": ("EU Radio Equipment Directive 2014/53/EU incl. delegated cyber act", "emc", (6, 10), {"eu"}),

    # grid
    "UL1741SB": ("UL 1741 SB grid support, tested to IEEE 1547.1-2020", "grid", (8, 16), {"us"}),
    "IEEE1547": ("IEEE 1547-2018 interconnection requirements and utility settings", "grid", (2, 6), {"us"}),
    "EN50549": ("EN 50549-1/-2 generating plant connection to distribution networks", "grid", (8, 14), {"eu"}),

    # functional safety and cyber
    "ISO13849": ("ISO 13849-1/-2 safety functions: PL calculation and validation", "fusa", (6, 12), {"us", "eu"}),
    "UL1998": ("UL 1998 / UL 60730-1 Annex H software for safety controls", "fusa", (8, 16), {"us", "eu"}),
    "IEC62443": ("IEC 62443-4-1/-4-2 secure development and component security", "fusa", (8, 16), {"us", "eu"}),
    "UL2941": ("UL 2941 cybersecurity for DER and inverter-based resources", "fusa", (6, 12), {"us"}),

    # listing and site
    "LISTING": ("NRTL listing, initial production inspection, follow-up service", "listing", (2, 6), {"us"}),
    "CEFILE": ("CE technical file and EU Declaration of Conformity", "listing", (2, 4), {"eu"}),
    "NFPA855": ("NFPA 855 / IFC siting, AHJ plan review and fire marshal sign-off", "site", (4, 12), {"us"}),
    "NEC": ("NEC (NFPA 70) installation, field inspection, utility interconnection agreement", "site", (4, 12), {"us"}),
}

# Product types: base standards plus optional ones switched on by flags.
PRODUCTS = {
    "mv-sst": {
        "label": "Medium-voltage solid-state transformer / power supply (e.g. MV AC to 800 VDC)",
        "base": ["HARA", "PRECOMP", "UL2877", "IEC62477-1", "FCC15B", "EUEMC", "UL1998", "IEC62443",
                 "LISTING", "CEFILE", "LVD", "NEC"],
        "options": {"grid_export": ["UL1741SB", "IEEE1547", "UL2941", "EN50549"],
                    "battery": ["UN38.3", "UL1973", "IEC62619", "UL9540A", "UL9540", "EUBATT"],
                    "wireless": ["FCC15C", "RED"]},
    },
    "bess": {
        "label": "Battery energy storage system",
        "base": ["HARA", "PRECOMP", "UN38.3", "UL1973", "IEC62619", "UL9540A", "UL9540", "IEC62477-1",
                 "FCC15B", "EUEMC", "UL1998", "IEC62443", "LISTING", "CEFILE", "LVD", "EUBATT", "NFPA855", "NEC"],
        "options": {"grid_export": ["UL1741SB", "IEEE1547", "UL2941", "EN50549"],
                    "wireless": ["FCC15C", "RED"]},
    },
    "ev-charger": {
        "label": "EV charger / EVSE",
        "base": ["HARA", "PRECOMP", "UL2202", "UL2594", "IEC61851", "FCC15B", "EUEMC", "UL1998",
                 "IEC62443", "LISTING", "CEFILE", "LVD", "NEC"],
        "options": {"grid_export": ["UL9741", "UL1741SB", "IEEE1547", "UL2941", "EN50549"],
                    "wireless": ["FCC15C", "RED"]},
    },
    "industrial-robot": {
        "label": "Industrial robot or robot cell (incl. cobot applications)",
        "base": ["HARA", "PRECOMP", "ISO10218", "UL1740", "IEC60204-1", "ISO13849", "FCC15B", "EUEMC",
                 "LISTING", "CEFILE", "MACHREG"],
        "options": {"battery": ["UN38.3", "IEC62133-2"], "wireless": ["FCC15C", "RED"],
                    "software_safety": ["UL1998"], "connected": ["IEC62443"]},
    },
    "mobile-robot": {
        "label": "Industrial mobile robot / AMR / AGV",
        "base": ["HARA", "PRECOMP", "R15.08", "ISO3691-4", "UL3100", "IEC60204-1", "ISO13849", "UN38.3",
                 "IEC62133-2", "FCC15B", "FCC15C", "EUEMC", "RED", "LISTING", "CEFILE", "MACHREG"],
        "options": {"software_safety": ["UL1998"], "connected": ["IEC62443"]},
    },
    "service-robot": {
        "label": "Service / personal care / humanoid robot in public or home settings",
        "base": ["HARA", "PRECOMP", "ISO13482", "UL3300", "ISO13849", "UN38.3", "IEC62133-2", "UL62368",
                 "FCC15B", "FCC15C", "EUEMC", "RED", "LISTING", "CEFILE", "MACHREG"],
        "options": {"software_safety": ["UL1998"], "connected": ["IEC62443"]},
    },
    "consumer-electronics": {
        "label": "Consumer / ICT electronics with lithium battery",
        "base": ["HARA", "PRECOMP", "UL62368", "UN38.3", "IEC62133-2", "FCC15B", "EUEMC", "LISTING",
                 "CEFILE", "LVD"],
        "options": {"wireless": ["FCC15C", "RED"], "connected": ["IEC62443"]},
    },
}

OPTION_FLAGS = ["grid_export", "battery", "wireless", "software_safety", "connected"]
