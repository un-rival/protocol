import { setWorldConstructor, setDefaultTimeout } from '@cucumber/cucumber'
import {deployContract, MockProvider, solidity} from 'ethereum-waffle';
import {use} from "chai";
import DomainContract from "../../../artifacts/contracts/Domain.sol/Domain.json";
import { Domain } from "../../../typechain-types";
import {Wallet} from "ethers";



use(solidity);

setDefaultTimeout(20 * 1000);

class DomainWorld {
  public owner: string
  public wallets: Wallet[]
  public kyct: Domain | undefined
  public ready: boolean = false
  private _initialized: Promise<boolean>

  constructor() {
    this.wallets = new MockProvider().getWallets();
    this.owner = this.wallets[0].address

    const that = this
    this._initialized = new Promise(async (resolve, reject) => {
        try {
            this.kyct = (await deployContract(that.wallets[0], DomainContract, ["KYC Token"])) as Domain;

        that.ready = true
        resolve(true)
      }catch (err) {
        reject(err)
      }
    })
  }

}

setWorldConstructor(DomainWorld);
 
