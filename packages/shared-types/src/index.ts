import { z } from 'zod';

export const ChainEnvironmentEnum = z.enum([
  'SOLANA_MAINNET',
  'ARBITRUM_ONE',
  'BASE_L2',
  'ALGORAND_MAINNET',
  'STELLAR_PUBLIC',
  'INTERNET_COMPUTER'
]);
export type ChainEnvironment = z.infer<typeof ChainEnvironmentEnum>;

export const InvestmentInstrumentEnum = z.enum([
  'AUTO_SWEEP_SAVINGS', 'FIXED_DEPOSIT', 'RECURRING_DEPOSIT',
  'PPF_PROXY', 'NPS_TRUST', 'POST_OFFICE_SCHEME', 'SSY_SCSS_ANNUITY',
  'LIQUID_FUNDS', 'INDEX_FUNDS_ETFS', 'ACTIVE_SIP', 'ELSS_TAX_SAVER',
  'GOVERNMENT_SECURITIES', 'CORPORATE_BONDS', 'IPO_EQUITY',
  'PHYSICAL_GOLD_SILVER', 'REITS_INVITS', 'FRACTIONAL_REAL_ESTATE',
  'INTERNATIONAL_ETFS_CRYPTO'
]);
export type InvestmentInstrument = z.infer<typeof InvestmentInstrumentEnum>;

export const AIRecommendationSchema = z.object({
  recommendationId: z.string().uuid(),
  modelVersion: z.string(),
  investorId: z.string().uuid(),
  instrument: InvestmentInstrumentEnum,
  targetAction: z.enum(['DEPOSIT', 'WITHDRAW', 'SWEEP', 'REBALANCE', 'HOLD']),
  proposedAmountBaseUnits: z.string().regex(/^[0-9]+$/),
  confidenceScore: z.number().min(0).max(1),
  riskProfileMatch: z.boolean(),
  explanation: z.string(),
  signature: z.string()
});
export type AIRecommendation = z.infer<typeof AIRecommendationSchema>;
