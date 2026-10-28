package fintech.policy

default allow = false

max_single_transaction_usd := 50000
max_crypto_allocation_percentage := 20

allow {
    input.investor.kyc_status == "VERIFIED"
    input.investor.kyc_tier >= 2
    input.transaction.amount_usd <= max_single_transaction_usd
    not is_exposure_limit_exceeded
    is_asset_allowlisted
}

is_exposure_limit_exceeded {
    new_crypto_pct := (input.portfolio.current_crypto_usd + input.transaction.amount_usd) / (input.portfolio.total_valuation_usd + input.transaction.amount_usd) * 100
    new_crypto_pct > max_crypto_allocation_percentage
}

is_asset_allowlisted {
    allowed_assets := {"USDC", "WBTC", "WETH", "GOLD_RWA", "GOV_T_BILL"}
    allowed_assets[input.transaction.asset_symbol]
}
