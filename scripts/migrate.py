from pathlib import Path
import click

from brownie import (
    Vault,
    Token,
    BeefMaster,
    YakAttack,
    JoeFoSho,
    PTPLifez,
    SingleJoe,
    StrategyLib,
    accounts,
    config,
    network,
    project,
    web3,
)
from eth_utils import is_checksum_address
from brownie.network.gas.strategies import LinearScalingStrategy

#Variables
acct = accounts.add('privKey')
gas_strategy = LinearScalingStrategy("30 gwei", "50 gwei", 1.1)
param = { 'from': acct, 'gas_price': gas_strategy }

#tokens
usdc = '0x2791bca1f2de4661ed88a30c99a7a9449aa84174'
dai = '0x8f3cf7ad23cd3cadbd9735aff958023239c6a063'
weth = '0x7ceb23fd6bc0add59e62ac25578270cff1b9f619'
wbtc = '0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6'
wmatic = '0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270'

#vaults
usdcVault = ''
daiVault = ''
wethVault = ''
wbtcVault = '0x5fa039aFc64dABC8B219b6E85749faD3939D8564'
wmaticVault = ''

#Variables
### THESE VARIABLES NEED TO BE UPDATED
vault = Vault.at(usdcVault)
token = Token.at(usdc)
old = Strategy.at('')
### THESE VARIABLES NEED TO BE UPDATED

def main():

    print("Vault USDC balance: ", token.balanceOf(vault.address))
    print("Old Strategy balance: ", old.estimatedTotalAssets())
    print("Acct usdc: ", token.balanceOf(acct.address))
    print("Account cvUSDC: ", vault.balanceOf(acct.address))
    
    new = Strategy.deploy(
        vault.address, 
        # Parameters
        param
    )
    
    print("Strategy Deployed: ", new.address)
    
    vault.migrateStrategy(old, new, param)

    tx = new.harvest(param)
    print(tx.events)

    print("Vault USDC balance: ", token.balanceOf(vault.address))
    print("Old Strategy balance: ", old.estimatedTotalAssets())
    print("New Strat Balance: ", new.estimatedTotalAssets())
    print("Acct usdc: ", token.balanceOf(acct.address))
    print("Account cvUSDC: ", vault.balanceOf(acct.address))
