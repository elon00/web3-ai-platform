-- PostgreSQL 16 HA Authoritative Ledger Schema
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TYPE chain_environment AS ENUM (
    'SOLANA_MAINNET', 'ARBITRUM_ONE', 'BASE_L2', 'ALGORAND_MAINNET', 'STELLAR_PUBLIC', 'INTERNET_COMPUTER'
);

CREATE TYPE transaction_lifecycle_state AS ENUM (
    'INITIALIZED', 'POLICY_CHECK_PENDING', 'POLICY_APPROVED', 'POLICY_REJECTED',
    'SUBMITTED_TO_CHAIN', 'INCLUDED_PENDING_FINALITY', 'FINALIZED_CONFIRMED',
    'RECONCILED', 'FAILED_EXHAUSTED', 'REORG_DETECTED_REVERTED'
);

CREATE TABLE investors (
    investor_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    kyc_status_code VARCHAR(32) NOT NULL DEFAULT 'UNVERIFIED',
    kyc_tier_level INT NOT NULL DEFAULT 0,
    jurisdiction_country_iso VARCHAR(2) NOT NULL,
    risk_profile_category VARCHAR(32) NOT NULL DEFAULT 'MODERATE',
    is_account_suspended BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE investor_wallets (
    wallet_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    investor_id UUID NOT NULL REFERENCES investors(investor_id) ON DELETE RESTRICT,
    chain chain_environment NOT NULL,
    public_address VARCHAR(128) NOT NULL,
    is_primary_signing_address BOOLEAN NOT NULL DEFAULT FALSE,
    linked_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (chain, public_address)
);

CREATE TABLE authoritative_vault_positions (
    position_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    investor_id UUID NOT NULL REFERENCES investors(investor_id),
    chain chain_environment NOT NULL,
    application_domain VARCHAR(64) NOT NULL,
    instrument_category_id INT NOT NULL,
    contract_or_program_address VARCHAR(128) NOT NULL,
    token_mint_address VARCHAR(128) NOT NULL,
    principal_amount_base_units NUMERIC(38, 0) NOT NULL,
    accrued_yield_base_units NUMERIC(38, 0) NOT NULL DEFAULT 0,
    lockup_starts_at TIMESTAMPTZ NOT NULL,
    maturity_due_at TIMESTAMPTZ,
    status VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    last_onchain_sync_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE financial_transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    idempotency_key VARCHAR(128) NOT NULL UNIQUE,
    investor_id UUID NOT NULL REFERENCES investors(investor_id),
    chain chain_environment NOT NULL,
    tx_hash VARCHAR(128) UNIQUE,
    block_number BIGINT,
    lifecycle_state transaction_lifecycle_state NOT NULL DEFAULT 'INITIALIZED',
    source_address VARCHAR(128) NOT NULL,
    destination_address VARCHAR(128) NOT NULL,
    asset_identifier VARCHAR(128) NOT NULL,
    amount_base_units NUMERIC(38, 0) NOT NULL,
    network_fee_base_units NUMERIC(38, 0),
    initiated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    finalized_at TIMESTAMPTZ,
    reconciled_at TIMESTAMPTZ
);
