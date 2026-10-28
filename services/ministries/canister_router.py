# ICP Canister Router for Bharat 58-Ministry Web3 & AI Workflows
import hashlib
import time
from .registry import ALL_58_MINISTRIES

class MinistryCanisterRouter:
    def __init__(self):
        self.registry = ALL_58_MINISTRIES

    def route_workflow(self, ministry_id: int, action: str, payload: dict):
        if ministry_id not in self.registry:
            return {"error": f"Invalid Ministry ID {ministry_id}", "status": "REJECTED"}

        ministry = self.registry[ministry_id]
        
        # Check Token Strategy constraints
        if ministry.token_strategy == "TOKENLESS_AUDIT_ANCHOR":
            payload_str = str(payload).encode('utf-8')
            anchor_hash = hashlib.sha256(payload_str).hexdigest()
            return {
                "status": "ANCHORED",
                "ministry": ministry.ministry_name,
                "project": ministry.project_name,
                "canister_id": ministry.canister_id,
                "action": action,
                "merkle_anchor_hash": anchor_hash,
                "timestamp": int(time.time()),
                "token_transferred": 0
            }
        elif ministry.token_strategy == "SOULBOUND_CREDENTIAL":
            recipient = payload.get("recipient_did", "did:india:unknown")
            cert_id = hashlib.sha256(f"{recipient}:{action}:{time.time()}".encode('utf-8')).hexdigest()
            return {
                "status": "CREDENTIAL_ISSUED",
                "ministry": ministry.ministry_name,
                "project": ministry.project_name,
                "canister_id": ministry.canister_id,
                "credential_id": f"urn:bharat:sbt:{cert_id[:16]}",
                "recipient_did": recipient,
                "transferable": False,
                "revocable": True
            }
        elif ministry.token_strategy == "PROGRAMMATIC_UTILITY":
            amount = payload.get("amount", 0)
            return {
                "status": "UTILITY_EXECUTED",
                "ministry": ministry.ministry_name,
                "project": ministry.project_name,
                "canister_id": ministry.canister_id,
                "symbol": ministry.token_symbol,
                "settlement_chain": ministry.primary_chain,
                "amount": amount
            }
