# Certification path: Battery energy storage system

Markets: EU/US · Options: none

Planned duration: **38-78 weeks** (9-18 months) from design freeze.

## Standards map

| Phase | Standard | Weeks |
|---|---|---|
| Plan, hazard analysis, design review | Hazard analysis and risk assessment (ISO 12100 method) | 2-4 |
| Pre-compliance testing (in-house or lab) | Pre-compliance safety and EMC screening | 4-8 |
| Component and cell certifications | UN 38.3 lithium battery transport tests | 4-8 |
| Component and cell certifications | UL 1973 batteries for stationary and motive auxiliary power | 10-16 |
| Component and cell certifications | IEC 62619 secondary lithium cells and batteries, industrial | 8-14 |
| Component and cell certifications | UL 9540A thermal runaway fire propagation test method | 12-24 |
| Product / system safety | UL 9540 energy storage systems and equipment | 12-20 |
| Product / system safety | IEC 62477-1 safety of power electronic converter systems | 8-12 |
| EMC and radio | FCC Part 15 Subpart B unintentional radiators | 2-4 |
| EMC and radio | EU EMC Directive 2014/30/EU (EN 61000-6-x / product family) | 4-6 |
| Functional safety and cybersecurity | UL 1998 / UL 60730-1 Annex H software for safety controls | 8-16 |
| Functional safety and cybersecurity | IEC 62443-4-1/-4-2 secure development and component security | 8-16 |
| Listing, factory inspection, technical file | NRTL listing, initial production inspection, follow-up service | 2-6 |
| Listing, factory inspection, technical file | CE technical file and EU Declaration of Conformity | 2-4 |
| Listing, factory inspection, technical file | EU Low Voltage Directive 2014/35/EU technical file | 3-6 |
| Listing, factory inspection, technical file | EU Battery Regulation 2023/1542 conformity, labelling, due diligence | 4-10 |
| Installation code / AHJ approval | NFPA 855 / IFC siting, AHJ plan review and fire marshal sign-off | 4-12 |
| Installation code / AHJ approval | NEC (NFPA 70) installation, field inspection, utility interconnection agreement | 4-12 |

## Test sequence

1. **Plan, hazard analysis, design review**: starts week 0-0
2. **Pre-compliance testing (in-house or lab)**: starts week 2-4
3. **Component and cell certifications**: starts week 6-12
4. **Product / system safety + EMC and radio + Functional safety and cybersecurity** (in parallel): starts week 18-36
5. **Listing, factory inspection, technical file**: starts week 30-56
6. **Installation code / AHJ approval**: starts week 34-66

## Long poles

- Hazard analysis and risk assessment (ISO 12100 method) (2-4 wk)
- Pre-compliance safety and EMC screening (4-8 wk)
- UL 9540A thermal runaway fire propagation test method (12-24 wk)
- UL 9540 energy storage systems and equipment (12-20 wk)
- EU Battery Regulation 2023/1542 conformity, labelling, due diligence (4-10 wk)
- NFPA 855 / IFC siting, AHJ plan review and fire marshal sign-off (4-12 wk)
- NEC (NFPA 70) installation, field inspection, utility interconnection agreement (4-12 wk)

## Timeline

```
Plan, hazard analysis, design revi |#--                                                         |
Pre-compliance testing (in-house o | ###-----                                                   |
Component and cell certifications  |    #########--------------                                 |
Product / system safety            |             #########---------------------                 |
EMC and radio                      |             ###----------------                            |
Functional safety and cybersecurit |             ######---------------------                    |
Listing, factory inspection, techn |                       ###------------------------          |
Installation code / AHJ approval   |                          ###-------------------------------|
                                    0 wk                                                  78 wk
# = optimistic duration, - = added time in the pessimistic case
```

_Lead times are planning assumptions for a first-of-kind product with lab slots booked. Edit `cert_path/catalog.py` for your NRTL, lab capacity and design maturity. Applicability of each standard depends on the final design and intended use._
