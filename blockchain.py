#! /usr/bin/env python		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]



import doctest
import hashlib
import keyword
import random


DEBUG_MODE = False
if DEBUG_MODE:
    pdb.set_trace()

RESERVED = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield']
KEYWORDS = keyword.kwlist


class BlockEntry():
    entryID = -1
    previousEntryID = 0
    previousEntryHash = ""

    def __init__(self, previousEntryHash, genesis = False):
        if genesis:
            self.entryID = 0
            self.previousEntryID = None
        else:
            self.previousEntryHash = previousEntryHash
            


class Transaction(BlockEntry):
    transactionID = BlockEntry.entryID
    previousTransactionID = BlockEntry.previousEntryID
    previousTransactionHash = BlockEntry.previousEntryHash

    def __init__(self, previousTransactionHash, genesis = False):
        if genesis:
            self.transactionID = 0
            self.previousTransactionID = None
        else:
            self.previousTransactionHash = previousTransactionHash
            

class Block():
    blockID = -1
    previousBlockID = 0
    previousBlockHash = ""
    genesisBlockEntry = BlockEntry.entryID
    blockEntryList = {0: []}

    def __init__(self, previousBlockHash, genesis = False):
        if genesis:
            self.blockID = 0
            self.previousBlockID = None
            self.genesisBlockEntry = BlockEntry(genesis = True)
            self.blockEntryList = {0: self.genesisBlockEntry}
        else:
            self.previousBlockHash = previousBlockHash

    def isGenesis(self):
        if self.blockID == 0:
            return True
        else:
            return False

    def blockSize(self):
        return len(self.blockEntryList)

    def calculatePreviousEntryHash(self):
        previousEntryID = self.blockSize() - 1
        previousEntryHash = hashlib.sha512()
        previousEntryHash.update( str(self.blockEntryList[ previousEntryID ]).encode('utf-8') )
        return previousEntryHash.hexdigest()

    def addEntry(self):
        nextEntryID = self.blockSize()
        self.entryList[nextEntryID] = BlockEntry(self.calculatePreviousEntryHash(), genesis = False)


class ExchangeBlock(Block):
    blockID = -1
    previousBlockID = 0
    previousBlockHash = ""
    genesisTransaction = Transaction.transactionID
    transactionList = {0: []}

    def __init__(self, previousBlockHash, genesis = False):
        if genesis:
            self.blockID = 0
            self.previousBlockID = None
            self.genesisTransaction = Transaction(genesis = True)
            self.transactionList = {0: self.genesisTransaction}
        else:
            self.previousBlockHash = previousBlockHash

    def isGenesis(self):
        if self.blockID == 0:
            return True
        else:
            return False

    def blockSize(self):
        return len(self.transactionList)

    def calculatePreviousTransactionHash(self):
        previousEntryID = self.blockSize() - 1
        previousEntryHash = hashlib.sha512()
        previousEntryHash.update( str(self.transactionList[ previousEntryID ]).encode('utf-8') )
        return previousEntryHash.hexdigest()

    def addTransaction(self):
        nextTransactionID = self.blockSize()
        self.transactionList[nextTransactionID] = Transaction(self.calculatePreviousTransactionHash(), genesis = False)


class BlockChain():
    blockChainName = ""
    genesisBlock = Block.blockID
    blockList = {0: []}

    def __init__(self, blockChainName):
        self.blockChainName = blockChainName
        self.genesisBlock = Block(None, genesis = True)
        self.blockList = {0: self.genesisBlock}

    def blockChainSize(self):
        return len(self.blockList)
    
    def calculatePreviousBlockHash(self):
        previousBlockID = self.blockChainSize() - 1
        previousBlockHash = hashlib.sha512()
        previousBlockHash.update( str(self.blockList[ previousBlockID ]).encode('utf-8') )
        return previousBlockHash.hexdigest()

    def addBlock(self):
        nextBlockID = self.blockChainSize()
        self.blockList[nextBlockID] = Block(self.calculatePreviousBlockHash(), genesis = False)
        

class ExchangeChain(BlockChain):
    ExchangeChainName = BlockChain.blockChainName
    genesisExchangeBlock = ExchangeBlock.blockID
    exchangeBlockList = BlockChain.blockList

    def __init__(self, ExchangeChainName):
        self.ExchangeChainName = ExchangeChainName
        self.genesisExchangeBlock = ExchangeBlock(None, genesis = True)
        self.exchangeBlockList = {0: self.genesisExchangeBlock}

    def blockChainSize(self):
        return len(self.exchangeBlockList)
    
    def calculatePreviousBlockHash(self):
        previousBlockID = self.blockChainSize() - 1
        previousBlockHash = hashlib.sha512()
        previousBlockHash.update( str(self.exchangeBlockList[ previousBlockID ]).encode('utf-8') )
        return previousBlockHash.hexdigest()

    def addBlock(self):
        nextBlockID = self.blockChainSize()
        self.exchangeBlockList[nextBlockID] = ExchangeBlock(self.calculatePreviousBlockHash(), genesis = False)    
        

        
