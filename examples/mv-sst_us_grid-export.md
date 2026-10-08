# Certification path: Medium-voltage solid-state transformer / power supply (e.g. MV AC to 800 VDC)

Markets: US · Options: grid_export

Planned duration: **28-60 weeks** (6-14 months) from design freeze.

## Standards map

| Phase | Standard | Weeks |
|---|---|---|
| Plan, hazard analysis, design review | Hazard analysis and risk assessment (ISO 12100 method) | 2-4 |
| Pre-compliance testing (in-house or lab) | Pre-compliance safety and EMC screening | 4-8 |
| Product / system safety | UL 2877 outline of investigation, medium-voltage power supplies | 16-30 |
| EMC and radio | FCC Part 15 Subpart B unintentional radiators | 2-4 |
| Grid interconnection | UL 1741 SB grid support, tested to IEEE 1547.1-2020 | 8-16 |
| Grid interconnection | IEEE 1547-2018 interconnection requirements and utility settings | 2-6 |
| Functional safety and cybersecurity | UL 1998 / UL 60730-1 Annex H software for safety controls | 8-16 |
| Functional safety and cybersecurity | IEC 62443-4-1/-4-2 secure development and component security | 8-16 |
| Functional safety and cybersecurity | UL 2941 cybersecurity for DER and inverter-based resources | 6-12 |
| Listing, factory inspection, technical file | NRTL listing, initial production inspection, follow-up service | 2-6 |
| Installation code / AHJ approval | NEC (NFPA 70) installation, field inspection, utility interconnection agreement | 4-12 |

## Test sequence

1. **Plan, hazard analysis, design review**: starts week 0-0
2. **Pre-compliance testing (in-house or lab)**: starts week 2-4
3. **Product / system safety + EMC and radio + Grid interconnection + Functional safety and cybersecurity** (in parallel): starts week 6-12
4. **Listing, factory inspection, technical file**: starts week 22-42
5. **Installation code / AHJ approval**: starts week 24-48

## Long poles

- Hazard analysis and risk assessment (ISO 12100 method) (2-4 wk)
- Pre-compliance safety and EMC screening (4-8 wk)
- UL 2877 outline of investigation, medium-voltage power supplies (16-30 wk)
- NRTL listing, initial production inspection, follow-up service (2-6 wk)
- NEC (NFPA 70) installation, field inspection, utility interconnection agreement (4-12 wk)

## Timeline

```
Plan, hazard analysis, design revi |##--                                                        |
Pre-compliance testing (in-house o |  ####------                                                |
Product / system safety            |      ################--------------------                  |
EMC and radio                      |      ##--------                                            |
Grid interconnection               |      ########--------------                                |
Functional safety and cybersecurit |      ########--------------                                |
Listing, factory inspection, techn |                      ##------------------------            |
Installation code / AHJ approval   |                        ####--------------------------------|
                                    0 wk                                                  60 wk
# = optimistic duration, - = added time in the pessimistic case
```

_Lead times are planning assumptions for a first-of-kind product with lab slots booked. Edit `cert_path/catalog.py` for your NRTL, lab capacity and design maturity. Applicability of each standard depends on the final design and intended use._
