"""Core data loading and filtering logic"""

import json
import random
from pathlib import Path
from typing import Dict, List, Optional


class PayloadDatabase:
    _instance = None
    _data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load(self) -> Dict:
        if self._data is None:
            data_file = Path(__file__).parent / "data" / "payloads.json"
            with open(data_file, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        return self._data

    def get_categories(self) -> List[str]:
        data = self.load()
        return list(data.get("categories", {}).keys())

    def get_all_payloads(self) -> List[Dict]:
        data = self.load()
        payloads = []
        for category_id, category_data in data.get("categories", {}).items():
            for payload in category_data.get("payloads", []):
                payload["category_id"] = category_id
                payload["category_name"] = category_data.get("name", category_id)
                payloads.append(payload)
        return payloads

    def filter_by_category(self, category: str) -> List[Dict]:
        data = self.load()
        category_data = data.get("categories", {}).get(category, {})
        payloads = []
        for payload in category_data.get("payloads", []):
            payload["category_id"] = category
            payload["category_name"] = category_data.get("name", category)
            payloads.append(payload)
        return payloads

    def filter_by_severity(self, severity: str) -> List[Dict]:
        all_payloads = self.get_all_payloads()
        return [p for p in all_payloads if p.get("severity") == severity]

    def search(self, keyword: str, fields: Optional[List[str]] = None) -> List[Dict]:
        if fields is None:
            fields = ["name", "description", "tags"]

        all_payloads = self.get_all_payloads()
        keyword_lower = keyword.lower()
        results = []

        for payload in all_payloads:
            for field in fields:
                value = payload.get(field, "")
                if isinstance(value, list):
                    if any(keyword_lower in str(v).lower() for v in value):
                        results.append(payload)
                        break
                elif keyword_lower in str(value).lower():
                    results.append(payload)
                    break

        return results

    def get_payload_by_id(self, payload_id: str) -> Optional[Dict]:
        all_payloads = self.get_all_payloads()
        for payload in all_payloads:
            if payload.get("id") == payload_id:
                return payload
        return None

    def get_random_payload(self, category: Optional[str] = None) -> Optional[Dict]:
        if category:
            payloads = self.filter_by_category(category)
        else:
            payloads = self.get_all_payloads()

        return random.choice(payloads) if payloads else None
