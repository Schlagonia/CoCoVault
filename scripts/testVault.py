from pathlib import Path
import click

from brownie import Vault, Token, BeefMaster, YakAttack, PTPLifez, SingleJoe, StrategyLib, accounts, config, network, project, web3
from eth_utils import is_checksum_address
from brownie.network.gas.strategies import LinearScalingStrategy


#Variables
vault = Vault.at('0xDecdE3D0e1367155b62DCD497B0A967D6aa41Afd')
acct = accounts.at('0xaa9F4EB6273904CC609bdB06e7Df9f26Ed223Ff9', force=True)

beefVault = '0xEbdf71f56BB3ae1D145a4121d0DDCa5ABEA7a946'
gas_strategy = LinearScalingStrategy("30 gwei", "100 gwei", 1.1)
beef = BeefMaster.at('0x19284d07aab8Fa6B8C9B29F9Bc3f101b2ad5f661')
yak = YakAttack.at('0x9F1a3536d7B4f27e0e20bc6d9a55588a1a00bf9C')
pp = PTPLifez.at('0x541dCb7b9F340D6b311034D33581563213de11cF')
joe = SingleJoe.at('0x5D95e05E208CB11aa42A90287A75fe610564896B')

usdc = Token.at('0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664')

param = { 'from': acct, 'gas_price': gas_strategy }

def main():
    print(f"You are using the '{network.show_active()}' network")
    #dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    dev = acct
    print(f"You are using: 'dev' [{dev.address}]")

    shares = vault.balanceOf(acct.address)
    print('Vault USDC balance: ', usdc.balanceOf(vault.address))
    print('Beef Strategy usdc balance: ', beef.estimatedTotalAssets())
    print('Yak Strategy usdc balance: ', yak.estimatedTotalAssets())
    print('PTP assets :', joe.estimatedTotalAssets())
    print('Acct usdc: ', usdc.balanceOf(acct.address))
    print('Account cvUSDC: ', vault.balanceOf(acct.address))

    tx = vault.withdraw(shares, param);
    print('Funds withdrawn')
    print('Vault USDC balance: ', usdc.balanceOf(vault.address))
    print('Beef Strategy usdc balance: ', beef.estimatedTotalAssets())
    print('Yak Strategy usdc balance: ', yak.estimatedTotalAssets())
    print('PTP assets :', joe.estimatedTotalAssets())
    print('Acct usdc: ', usdc.balanceOf(acct.address))
    print('Account cvUSDC: ', vault.balanceOf(acct.address))

    usdc.approve(vault.address, 100000000000, param)

    vault.deposit(60000000, param);
    print('Deposited into vault. Current acct cv balance: ', vault.balanceOf(acct.address))
    
    print('Vault USDC balance: ', usdc.balanceOf(vault.address))
    print('Beef Strategy usdc balance: ', beef.estimatedTotalAssets())
    print('Yak Strategy usdc balance: ', yak.estimatedTotalAssets())
    print('PTP assets :', joe.estimatedTotalAssets())
    print('Acct usdc: ', usdc.balanceOf(acct.address))
    print('Account cvUSDC: ', vault.balanceOf(acct.address))
    
    joe.harvest(param)

    print('Vault USDC balance: ', usdc.balanceOf(vault.address))
    print('Beef Strategy usdc balance: ', beef.estimatedTotalAssets())
    print('Yak Strategy usdc balance: ', yak.estimatedTotalAssets())
    print('PTP assets :', joe.estimatedTotalAssets())
    print('Acct usdc: ', usdc.balanceOf(acct.address))
    print('Account cvUSDC: ', vault.balanceOf(acct.address))

    shares = vault.balanceOf(acct.address)
    print('Vault USDC balance: ', usdc.balanceOf(vault.address))
    print('Beef Strategy usdc balance: ', beef.estimatedTotalAssets())
    print('Yak Strategy usdc balance: ', yak.estimatedTotalAssets())
    print('PTP assets :', joe.estimatedTotalAssets())
    print('Acct usdc: ', usdc.balanceOf(acct.address))
    print('Account cvUSDC: ', vault.balanceOf(acct.address))
    
    tx = vault.withdraw(10000000, param);
    print('Funds withdrawn')
    print('Vault USDC balance: ', usdc.balanceOf(vault.address))
    print('Beef Strategy usdc balance: ', beef.estimatedTotalAssets())
    print('Yak Strategy usdc balance: ', yak.estimatedTotalAssets())
    print('PTP assets :', joe.estimatedTotalAssets())
    print('Acct usdc: ', usdc.balanceOf(acct.address))
    print('Account cvUSDC: ', vault.balanceOf(acct.address))

    #joe.harvest(param)

    print('Vault USDC balance: ', usdc.balanceOf(vault.address))
    print('Beef Strategy usdc balance: ', beef.estimatedTotalAssets())
    print('Yak Strategy usdc balance: ', yak.estimatedTotalAssets())
    print('PTP assets :', joe.estimatedTotalAssets())
    print('Acct usdc: ', usdc.balanceOf(acct.address))
    print('Account cvUSDC: ', vault.balanceOf(acct.address))