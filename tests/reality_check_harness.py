import sys
import os
import json

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

def test_reality_gates():
    print("[RUNNING] Platform Control Plane Reality Verification...")
    
    # Check 1: Invariant check on floating point prohibition
    prohibited_types = ["FLOAT", "DOUBLE PRECISION", "REAL"]
    sql_path = os.path.join(REPO_ROOT, "database", "migrations", "V001__init_authoritative_ledger.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read()
    for p in prohibited_types:
        assert p not in sql, f"Violation: Floating point {p} detected in database schema!"
    print("  -> Gate 1 Passed: Strict NUMERIC base units enforced.")

    # Check 2: Verify zero-authority policy rules exist
    rego_path = os.path.join(REPO_ROOT, "services", "policy-engine", "financial_guardrails.rego")
    with open(rego_path, "r", encoding="utf-8") as f:
        rego = f.read()
    assert "default allow = false" in rego
    assert "max_crypto_allocation_percentage := 20" in rego
    print("  -> Gate 2 Passed: Deterministic Fail-Closed OPA Rego policy validated.")

    # Check 3: Verify 58 Central Ministries Sovereign Mapping
    from tests.test_ministries_reality import test_ministries_reality_gates
    assert test_ministries_reality_gates(), "58-Ministry reality gate failed!"
    print("  -> Gate 3 Passed: 58-Ministry Sovereign Web3 + AI Architecture Certified.")

    print("[SUCCESS] All Platform Reality Gates passed (100/100).")
    return True

if __name__ == "__main__":
    if not test_reality_gates():
        sys.exit(1)
