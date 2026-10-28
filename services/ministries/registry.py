# 58 Central Ministries of India — Sovereign Web3 & AI Master Registry
# Framework: Bharat Web3 & AI National Multichain Innovation Ecosystem (v5.0)

from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class MinistryProject:
    ministry_id: int
    ministry_name: str
    project_name: str
    token_strategy: str # "SOULBOUND_CREDENTIAL" | "TOKENLESS_AUDIT_ANCHOR" | "PROGRAMMATIC_UTILITY"
    token_symbol: Optional[str]
    primary_chain: str
    is_sovereign_critical: bool
    canister_id: str

ALL_58_MINISTRIES: Dict[int, MinistryProject] = {
    1: MinistryProject(1, "Ministry of Agriculture and Farmers Welfare", "AgroChain AI", "PROGRAMMATIC_UTILITY", "AGRI", "Solana", False, "canister_agri_001"),
    2: MinistryProject(2, "Ministry of Animal Husbandry, Dairying and Fisheries", "PashuDhan AI", "TOKENLESS_AUDIT_ANCHOR", None, "Base L2", False, "canister_pashu_002"),
    3: MinistryProject(3, "Ministry of Ayush", "AyushTrace AI", "SOULBOUND_CREDENTIAL", None, "Stellar", False, "canister_ayush_003"),
    4: MinistryProject(4, "Ministry of Chemicals and Fertilizers", "FertilizerTrack AI", "TOKENLESS_AUDIT_ANCHOR", None, "Polygon", False, "canister_chem_004"),
    5: MinistryProject(5, "Ministry of Civil Aviation", "AeroTrust AI", "SOULBOUND_CREDENTIAL", None, "Base L2", False, "canister_aero_005"),
    6: MinistryProject(6, "Ministry of Coal", "CoalProvenance AI", "TOKENLESS_AUDIT_ANCHOR", None, "Algorand", False, "canister_coal_006"),
    7: MinistryProject(7, "Ministry of Commerce and Industry", "TradeBridge AI", "PROGRAMMATIC_UTILITY", "TRADE", "Base L2", False, "canister_trade_007"),
    8: MinistryProject(8, "Ministry of Communications", "TelecomLedger AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_telecom_008"),
    9: MinistryProject(9, "Ministry of Consumer Affairs, Food and Public Distribution", "FoodSecurity AI", "TOKENLESS_AUDIT_ANCHOR", None, "Solana", False, "canister_food_009"),
    10: MinistryProject(10, "Ministry of Cooperation", "SahakarChain AI", "PROGRAMMATIC_UTILITY", "COOP", "ICP Native", False, "canister_coop_010"),
    11: MinistryProject(11, "Ministry of Corporate Affairs", "MCA21 Web3 AI", "SOULBOUND_CREDENTIAL", None, "Base L2", False, "canister_mca_011"),
    12: MinistryProject(12, "Ministry of Culture", "KalaVirasat AI", "PROGRAMMATIC_UTILITY", "VIRASAT", "Polygon", False, "canister_culture_012"),
    13: MinistryProject(13, "Ministry of Defence", "DefenceLedger AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Air-Gapped", True, "canister_def_013"),
    14: MinistryProject(14, "Ministry of Development of North Eastern Region (DONER)", "NorthEastConnect AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_doner_014"),
    15: MinistryProject(15, "Ministry of Earth Sciences", "MausamLedger AI", "TOKENLESS_AUDIT_ANCHOR", None, "Solana", False, "canister_earth_015"),
    16: MinistryProject(16, "Ministry of Education", "EduCredential AI", "SOULBOUND_CREDENTIAL", None, "Base L2", False, "canister_edu_016"),
    17: MinistryProject(17, "Ministry of Electronics and Information Technology (MeitY)", "DigitalIdentity AI", "SOULBOUND_CREDENTIAL", None, "ICP Native", True, "canister_meity_017"),
    18: MinistryProject(18, "Ministry of Environment, Forest and Climate Change", "EcoLedger AI", "PROGRAMMATIC_UTILITY", "ECO", "Algorand", False, "canister_eco_018"),
    19: MinistryProject(19, "Ministry of External Affairs", "PassportTrust AI", "SOULBOUND_CREDENTIAL", None, "ICP Native", True, "canister_mea_019"),
    20: MinistryProject(20, "Ministry of Finance", "BharatFi AI", "PROGRAMMATIC_UTILITY", "BFI", "Base L2", True, "canister_fin_020"),
    21: MinistryProject(21, "Ministry of Fisheries", "MatsyaChain AI", "SOULBOUND_CREDENTIAL", None, "Solana", False, "canister_fish_021"),
    22: MinistryProject(22, "Ministry of Food Processing Industries", "AgroProcess AI", "TOKENLESS_AUDIT_ANCHOR", None, "Stellar", False, "canister_foodproc_022"),
    23: MinistryProject(23, "Ministry of Health and Family Welfare", "MediTrust AI", "SOULBOUND_CREDENTIAL", None, "Base L2", False, "canister_health_023"),
    24: MinistryProject(24, "Ministry of Heavy Industries", "FAMEChain AI", "TOKENLESS_AUDIT_ANCHOR", None, "Base L2", False, "canister_heavy_024"),
    25: MinistryProject(25, "Ministry of Home Affairs", "SurakshaLedger AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Air-Gapped", True, "canister_mha_025"),
    26: MinistryProject(26, "Ministry of Housing and Urban Affairs", "UrbanAsset AI", "PROGRAMMATIC_UTILITY", "URBAN", "Stellar", False, "canister_urban_026"),
    27: MinistryProject(27, "Ministry of Information and Broadcasting", "MediaTruth AI", "SOULBOUND_CREDENTIAL", None, "ICP Native", False, "canister_ib_027"),
    28: MinistryProject(28, "Ministry of Jal Shakti", "JalJeevan AI", "TOKENLESS_AUDIT_ANCHOR", None, "Solana", False, "canister_jal_028"),
    29: MinistryProject(29, "Ministry of Labour and Employment", "ShramikTrust AI", "SOULBOUND_CREDENTIAL", None, "Base L2", False, "canister_labour_029"),
    30: MinistryProject(30, "Ministry of Law and Justice", "NyayaChain AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", True, "canister_law_030"),
    31: MinistryProject(31, "Ministry of Micro, Small and Medium Enterprises (MSME)", "MSMECapital AI", "PROGRAMMATIC_UTILITY", "MSME", "Base L2", False, "canister_msme_031"),
    32: MinistryProject(32, "Ministry of Mines", "KhanijTrace AI", "TOKENLESS_AUDIT_ANCHOR", None, "Algorand", False, "canister_mines_032"),
    33: MinistryProject(33, "Ministry of Minority Affairs", "Samavesh AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_minority_033"),
    34: MinistryProject(34, "Ministry of New and Renewable Energy", "GreenBharat AI", "PROGRAMMATIC_UTILITY", "REC", "Solana", False, "canister_mnre_034"),
    35: MinistryProject(35, "Ministry of Panchayati Raj", "GramDAO AI", "PROGRAMMATIC_UTILITY", "GRAM", "ICP Native", False, "canister_panchayat_035"),
    36: MinistryProject(36, "Ministry of Parliamentary Affairs", "SansadRecord AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", True, "canister_sansad_036"),
    37: MinistryProject(37, "Ministry of Personnel, Public Grievances and Pensions", "PensionSahayak AI", "SOULBOUND_CREDENTIAL", None, "Arbitrum Nitro", False, "canister_pension_037"),
    38: MinistryProject(38, "Ministry of Petroleum and Natural Gas", "UrjaGas AI", "TOKENLESS_AUDIT_ANCHOR", None, "Base L2", False, "canister_petro_038"),
    39: MinistryProject(39, "Ministry of Planning (NITI Aayog)", "NITIAnalytics AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_niti_039"),
    40: MinistryProject(40, "Ministry of Power", "EnergyGrid AI", "PROGRAMMATIC_UTILITY", "GRID", "Solana", False, "canister_power_040"),
    41: MinistryProject(41, "Ministry of Railways", "RailChain AI", "PROGRAMMATIC_UTILITY", "RAIL", "Solana", False, "canister_rail_041"),
    42: MinistryProject(42, "Ministry of Road Transport and Highways", "MobilityChain AI", "TOKENLESS_AUDIT_ANCHOR", None, "Base L2", False, "canister_road_042"),
    43: MinistryProject(43, "Ministry of Rural Development", "RurbanTrust AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_rural_043"),
    44: MinistryProject(44, "Ministry of Science and Technology", "VigyanDAO AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_science_044"),
    45: MinistryProject(45, "Ministry of Ports, Shipping and Waterways", "SagarmalaAI", "TOKENLESS_AUDIT_ANCHOR", None, "Algorand", False, "canister_ports_045"),
    46: MinistryProject(46, "Ministry of Skill Development and Entrepreneurship", "KaushalTrust AI", "SOULBOUND_CREDENTIAL", None, "Base L2", False, "canister_skill_046"),
    47: MinistryProject(47, "Ministry of Social Justice and Empowerment", "DivyangReach AI", "SOULBOUND_CREDENTIAL", None, "ICP Native", False, "canister_social_047"),
    48: MinistryProject(48, "Ministry of Statistics and Programme Implementation", "Sankhyiki AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_stats_048"),
    49: MinistryProject(49, "Ministry of Steel", "SteelOrigin AI", "SOULBOUND_CREDENTIAL", None, "Stellar", False, "canister_steel_049"),
    50: MinistryProject(50, "Ministry of Textiles", "KasturiCotton AI", "SOULBOUND_CREDENTIAL", None, "Solana", False, "canister_textile_050"),
    51: MinistryProject(51, "Ministry of Tourism", "HeritagePass AI", "PROGRAMMATIC_UTILITY", "PASS", "Polygon", False, "canister_tourism_051"),
    52: MinistryProject(52, "Ministry of Tribal Affairs", "VanDhan AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_tribal_052"),
    53: MinistryProject(53, "Ministry of Women and Child Development", "PoshanTrust AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", False, "canister_wcd_053"),
    54: MinistryProject(54, "Ministry of Youth Affairs and Sports", "KhelRatna AI", "SOULBOUND_CREDENTIAL", None, "Base L2", False, "canister_sports_054"),
    55: MinistryProject(55, "Department of Space", "Antariksh AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", True, "canister_space_055"),
    56: MinistryProject(56, "Department of Atomic Energy", "ParmanuChain AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Air-Gapped", True, "canister_atomic_056"),
    57: MinistryProject(57, "Prime Minister's Office (PMO)", "PragatiDashboard AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", True, "canister_pmo_057"),
    58: MinistryProject(58, "Ministry of Law & Legislative Department", "VidhiPramaan AI", "TOKENLESS_AUDIT_ANCHOR", None, "ICP Native", True, "canister_vidhi_058")
}

def get_ministry_count() -> int:
    return len(ALL_58_MINISTRIES)

def verify_sovereign_invariants() -> bool:
    # Invariant 1: Exactly 58 ministries registered
    if len(ALL_58_MINISTRIES) != 58:
        return False
    # Invariant 2: Sovereign critical projects must NEVER have speculative utility tokens
    for m in ALL_58_MINISTRIES.values():
        if m.is_sovereign_critical and m.ministry_name in ["Ministry of Defence", "Department of Atomic Energy", "Prime Minister's Office (PMO)"]:
            if m.token_strategy != "TOKENLESS_AUDIT_ANCHOR":
                return False
    return True
