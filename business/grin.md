---
title: grin
date: 2018-08-09 11:51:23
categories: [项目分析]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 源码详细](#2-源码详细)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://github.com/mimblewimble/grin/blob/master/doc/build.md (构建说明)
* http://www.grinmint.com/pages/index.html (grin的矿池)
* http://www.grinmint.com/explorer/ (浏览器)

```bash
git clone https://github.com/mimblewimble/grin

.                    52087 
./core               11054  # 核心cuckoo-cycle算法,区块定义
./wallet             8588 
./servers            6928 
./chain              5789 
./p2p                3900 
./src                3748 
./store              3308 
./api                2770 
./keychain           2082 
./pool               1829 
./util               1086 
./config             1005 
./.idea              0 
./.hooks             0 
./.git               0 
./doc                0 
```

```bash
# 编译

sudo apt-get install build-essential cmake git libgit2-dev clang libncurses5-dev libncursesw5-dev zlib1g-dev pkg-config libssl-dev llvm -y

cd /mnt/disk1/linux/reference/refer/grin
cargo build --release

# 调试版本
cargo build

# 调试代码
use std::io;

let mut input = String::new();

match io::stdin().read_line(&mut input) {
	Ok(n) => {
	}
	Err(error) => println!("error: {}", error),
};

```


<a id="markdown-2-源码详细" name="2-源码详细"></a>
# 2. 源码详细


* min_edge_bits
* base_edge_bits
* proofsize

网络|min空间变量|base空间变量|验证数变量
-|-|-|-
AutomatedTesting|AUTOMATED_TESTING_MIN_EDGE_BITS(9)|AUTOMATED_TESTING_MIN_EDGE_BITS(9)|AUTOMATED_TESTING_PROOF_SIZE(4)
UserTesting|USER_TESTING_MIN_EDGE_BITS(15)|USER_TESTING_MIN_EDGE_BITS(15)|USER_TESTING_PROOF_SIZE(42)
Testnet1|USER_TESTING_MIN_EDGE_BITS(15)|USER_TESTING_MIN_EDGE_BITS(15)|PROOFSIZE(42)
Testnet2|SECOND_POW_EDGE_BITS(29)|BASE_EDGE_BITS(24)|PROOFSIZE(42)
Testnet3|SECOND_POW_EDGE_BITS(29)|BASE_EDGE_BITS(24)|PROOFSIZE(42)
Testnet4|SECOND_POW_EDGE_BITS(29)|BASE_EDGE_BITS(24)|PROOFSIZE(42)
Mainnet|SECOND_POW_EDGE_BITS(29)|BASE_EDGE_BITS(24)|PROOFSIZE(42)

* coinbase_maturity

网络|coinbase_maturity
-|-
AutomatedTesting|AUTOMATED_TESTING_COINBASE_MATURITY(3)
UserTesting|USER_TESTING_COINBASE_MATURITY(3)
Testnet1|COINBASE_MATURITY(1440) DAY_HEIGHT
Testnet2|COINBASE_MATURITY(1440) DAY_HEIGHT
Testnet3|COINBASE_MATURITY(1440) DAY_HEIGHT
Testnet4|COINBASE_MATURITY(1440) DAY_HEIGHT
Mainnet|COINBASE_MATURITY(1440) DAY_HEIGHT


* initial_block_difficulty

网络|initial_block_difficulty
-|-
AutomatedTesting|TESTING_INITIAL_DIFFICULTY(1)
UserTesting|TESTING_INITIAL_DIFFICULTY(1)
Testnet1|TESTING_INITIAL_DIFFICULTY(1)
Testnet2|TESTNET2_INITIAL_DIFFICULTY(1000)
Testnet3|TESTNET3_INITIAL_DIFFICULTY(30000)
Testnet4|TESTNET4_INITIAL_DIFFICULTY(1_000 * UNIT_DIFFICULTY)
Mainnet|INITIAL_DIFFICULTY(1_000_000 * UNIT_DIFFICULTY)

* initial_graph_weight

网络|initial_graph_weight
-|-
AutomatedTesting|TESTING_INITIAL_GRAPH_WEIGHT(1)
UserTesting|TESTING_INITIAL_GRAPH_WEIGHT(1)
Testnet1|TESTING_INITIAL_GRAPH_WEIGHT(1)
Testnet2|TESTING_INITIAL_GRAPH_WEIGHT(1)
Testnet3|TESTING_INITIAL_GRAPH_WEIGHT(1)
Testnet4|graph_weight(SECOND_POW_EDGE_BITS) (1856)
Mainnet|graph_weight(SECOND_POW_EDGE_BITS) (1856)

```rust
pub fn graph_weight(edge_bits: u8) -> u64 {
	(2 << (edge_bits - global::base_edge_bits()) as u64) * (edge_bits as u64)
}

(2 << (29 - 24)) * 29 = 1856
```

* cut_through_horizon

网络|cut_through_horizon
-|-
AutomatedTesting|TESTING_CUT_THROUGH_HORIZON(70)
UserTesting|TESTING_CUT_THROUGH_HORIZON(70)
Testnet1|CUT_THROUGH_HORIZON(10080) WEEK_HEIGHT
Testnet2|CUT_THROUGH_HORIZON(10080) WEEK_HEIGHT
Testnet3|CUT_THROUGH_HORIZON(10080) WEEK_HEIGHT
Testnet4|CUT_THROUGH_HORIZON(10080) WEEK_HEIGHT
Mainnet|CUT_THROUGH_HORIZON(10080) WEEK_HEIGHT

* state_sync_threshold


```bash
# 难度调整 
Digishield  和 GravityWave  , 与ZCash类似

# 生成区块(难度)
main -> real_main -> server_command -> start_server -> start_server_tui -> Server::start -> start_stratum_server -> run_loop -> get_block -> build_block

# 测试挖矿?
main -> real_main -> server_command -> start_server -> start_server_tui -> Server::start -> start_test_miner -> run_loop -> inner_mining_loop

```

指令
```bash
# 开启
./target/debug/grin server run


```
