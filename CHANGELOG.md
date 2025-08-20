# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2024-08-20

### Added
- Historical event indexers for blockchain data analysis
  - `CurveIndexer`: Index bonding curve events (CREATE, BUY, SELL, SYNC, LOCK, LISTED)
  - `DexIndexer`: Index DEX swap events with automatic pool discovery from V3 factory
- `parseMon()` utility function for converting MON amounts to wei
- `get_block_number()` method for both indexers
- Extended transaction parameters in `BuyParams` and `SellParams`:
  - `nonce`: Custom transaction nonce
  - `gas`: Gas limit override
  - `gas_price`: Gas price override

### Changed
- Improved import structure - all main classes now available from top-level `nadfun_sdk`
- Enhanced DexIndexer to automatically find pools from token addresses via V3 factory
- Updated all examples to use `parseMon()` for amount conversions
- Reorganized example files into subdirectories (`trade/`, `stream/`)

### Fixed
- Token filter in CurveIndexer now correctly pads addresses to 32 bytes
- Import consistency across all example files
- Environment variable validation in examples

### Removed
- Deprecated `RECIPIENT` environment variable from examples (now optional)

## [0.1.0] - 2024-08-19

### Added
- Initial release of Nad.fun Python SDK
- Core trading functionality with `Trade` class
- Token operations with `Token` class
- Real-time event streaming with WebSocket support
  - `CurveStream`: Monitor bonding curve events
  - `DexStream`: Monitor DEX swap events
- Type-safe interfaces with TypedDict
- Comprehensive examples for all features
- Full async/await support
- MIT License