import decimal
from dataclasses import dataclass
from typing import Optional, List


@dataclass()
class BlockHeaderSchema:
    block: int
    timestamp: int


@dataclass()
class ParticipantSchema:
    address: str
    amount: decimal.Decimal


@dataclass()
class TransactionSchema:
    transactionId: str
    amount: decimal.Decimal
    fee: decimal.Decimal
    inputs: List[ParticipantSchema]
    outputs: List[ParticipantSchema]
    timestamp: int
    token: Optional[str] = None


@dataclass()
class BlockSchema:
    headers: BlockHeaderSchema
    transactions: List[TransactionSchema]
