# Data Dictionary

## Basic Information
| Field | Description | Example |
|-------|-------------|---------|
| fdc_id | Unique identifier in the Food Data Central database | 169097 |
| name | Full food item name | "Oranges, raw, all commercial varieties" |
| name3 | Shortened food name | "Oranges" |
| data_type | Source database type | "sr_legacy_food" |
| data_db_name | Database name | "Standard Release (Common)" |

## Serving Information
| Field | Description | Unit |
|-------|-------------|------|
| commonserving | Default serving reference | "wt1" |
| commondesc | Description of common serving | "1 cup, sections" |
| commonweight | Weight of common serving | grams |
| servingsizes | JSON string containing various serving size options | various |

## Macronutrients
| Field | Description | Unit |
|-------|-------------|------|
| ENERC_KCAL | Energy | kcal/100g |
| WATER | Water content | g/100g |
| FAT | Total fat | g/100g |
| PROCNT | Protein content | g/100g |
| CHOCDF | Total carbohydrates | g/100g |
| FIBTG | Total dietary fiber | g/100g |
| SUGAR | Total sugars | g/100g |
| NetCarb | Net carbohydrates (CHOCDF - FIBTG) | g/100g |

## Minerals
| Field | Description | Unit |
|-------|-------------|------|
| CA | Calcium | mg/100g |
| FE | Iron | mg/100g |
| K | Potassium | mg/100g |
| MG | Magnesium | mg/100g |
| P | Phosphorus | mg/100g |
| NA | Sodium | mg/100g |
| ZN | Zinc | mg/100g |
| SE | Selenium | μg/100g |

## Vitamins
| Field | Description | Unit |
|-------|-------------|------|
| VITA_RAE | Vitamin A (Retinol Activity Equivalent) | μg/100g |
| VITC | Vitamin C | mg/100g |
| THIA | Thiamin (B1) | mg/100g |
| RIBF | Riboflavin (B2) | mg/100g |
| NIA | Niacin (B3) | mg/100g |
| VITB6A | Vitamin B6 | mg/100g |
| FOL | Total Folate | μg/100g |
| VITB12 | Vitamin B12 | μg/100g |
| TOCPHA | Vitamin E (alpha-tocopherol) | mg/100g |
| VITD | Vitamin D | μg/100g |

## Fatty Acids
| Field | Description | Unit |
|-------|-------------|------|
| FASAT | Saturated fatty acids | g/100g |
| FAMS | Monounsaturated fatty acids | g/100g |
| FAPU | Polyunsaturated fatty acids | g/100g |
| Omega3 | Omega-3 fatty acids | g/100g |
| Omega6 | Omega-6 fatty acids | g/100g |
| Om3Om6Ratio | Omega-3:Omega-6 ratio | ratio |

## Amino Acids
| Field | Description | Unit |
|-------|-------------|------|
| TRP_G | Tryptophan | mg/100g |
| THR_G | Threonine | mg/100g |
| ILE_G | Isoleucine | mg/100g |
| LEU_G | Leucine | mg/100g |
| LYS_G | Lysine | mg/100g |
| MET_G | Methionine | mg/100g |
| PHE_G | Phenylalanine | mg/100g |

Note: Null values in the data indicate that the measurement is either not applicable or not available for that particular food item.
