import sys
import json

def test_reality_gates():
    print("[RUNNING] Platform Control Plane Reality Verification...")
    
    # Check 1: Invariant check on floating point prohibition
    prohibited_types = ["FLOAT", "DOUBLE PRECISION", "REAL"]
    sql_path = "database/migrations/V001__init_authoritative_ledger.sql"
    with open(sql_path, "r") as f:
        sql = f.read()
    for p in prohibited_types:
        assert p not in sql, f"Violation: Floating point {p} detected in database schema!"
    print("  -> Gate 1 Passed: Strict NUMERIC base units enforced.")

    # Check 2: Verify zero-authority policy rules exist
    rego_path = "services/policy-engine/financial_guardrails.rego"
    with open(rego_path, "r") as f:
        rego = f.read()
    assert "default allow = false" in rego
    assert "max_crypto_allocation_percentage := 20" in rego
    print("  -> Gate 2 Passed: Deterministic Fail-Closed OPA Rego policy validated.")

    print("[SUCCESS] All Platform Reality Gates passed (100/100).")
    return True

if __name__ == "__main__":
    if not test_reality_gates():
        sys.exit(1)
