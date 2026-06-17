# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: AssetCheckout
import sys, datetime as dt
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Asset:
    id: str
    name: str
    status: str = "available"  # available, checked_out, returned
    condition: str = "good"   # good, damaged

@dataclass
class CheckoutRecord:
    asset_id: str
    recipient_name: str
    checkout_date: dt.date
    return_date: Optional[dt.date] = None
    status: str = "checked_out"  # checked_out, returned

def get_demo_assets() -> list[Asset]:
    return [
        Asset("LAPTOP-001", "MacBook Pro M2"),
        Asset("MONITOR-005", "Dell UltraSharp 27"),
        Asset("KEYBOARD-MECH", "Keychron K2"),
    ]

def get_demo_recipients() -> list[str]:
    return ["Иванов И.И.", "Петров П.П.", "Сидоров С.С."]

if __name__ == "__main__":
    assets = get_demo_assets()
    recipients = get_demo_recipients()
    
    # Демонстрация выдачи одного актива
    if assets:
        asset = assets[0]
        record = CheckoutRecord(
            asset_id=asset.id,
            recipient_name=recipients[0],
            checkout_date=dt.date.today(),
        )
        
        print(f"Ассет {asset.name} ({asset.status}) выдан пользователю {record.recipient_name}")
        print(f"Дата выдачи: {record.checkout_date}, Статус записи: {record.status}")
