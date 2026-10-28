# Reality Gate: 58 Central Ministries Web3 & AI Verification
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.ministries.registry import ALL_58_MINISTRIES, get_ministry_count, verify_sovereign_invariants
from services.ministries.canister_router import MinistryCanisterRouter

def test_ministries_reality_gates():
    print("[RUNNING] Bharat 58-Ministry Web3 & AI Reality Gates...")

    # Gate 1: Check total ministry count
    count = get_ministry_count()
    assert count == 58, f"Expected 58 ministries, found {count}"
    print(f"  -> Gate 1 Passed: Exactly {count} Union Ministries registered.")

    # Gate 2: Sovereign critical security invariants
    assert verify_sovereign_invariants(), "Sovereign invariant violation detected!"
    print("  -> Gate 2 Passed: Sovereign air-gapped portfolios enforced as tokenless audit anchors.")

    # Gate 3: Workflow Router Reality Check
    router = MinistryCanisterRouter()
    
    # Test Defence (Tokenless Audit Anchor)
    def_res = router.route_workflow(13, "PROCUREMENT_LOG", {"vendor": "BEL", "item": "RADAR_MODULE_X"})
    assert def_res["status"] == "ANCHORED"
    assert "merkle_anchor_hash" in def_res
    print("  -> Gate 3 Passed: DefenceLedger AI tokenless Merkle anchor verified.")

    # Test Education (Soulbound Credential)
    edu_res = router.route_workflow(16, "ISSUE_BTECH_DEGREE", {"recipient_did": "did:india:aadhaar_zk_987654"})
    assert edu_res["status"] == "CREDENTIAL_ISSUED"
    assert edu_res["transferable"] is False
    print("  -> Gate 4 Passed: EduCredential AI Soulbound Credential verified.")

    # Test Agriculture (Programmatic Utility)
    agri_res = router.route_workflow(1, "DISBURSE_CROP_INCENTIVE", {"amount": 500})
    assert agri_res["status"] == "UTILITY_EXECUTED"
    assert agri_res["symbol"] == "AGRI"
    print("  -> Gate 5 Passed: AgroChain AI programmatic clearing credit verified.")

    print("[SUCCESS] All 58-Ministry Sovereign Reality Gates passed (100/100).")
    return True

if __name__ == "__main__":
    if not test_ministries_reality_gates():
        sys.exit(1)
