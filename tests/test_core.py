"""Tests for core module"""

import pytest
from prompt_injection_payloads.core import PayloadDatabase


def test_singleton():
    db1 = PayloadDatabase()
    db2 = PayloadDatabase()
    assert db1 is db2


def test_load_data():
    db = PayloadDatabase()
    data = db.load()
    assert "version" in data
    assert "categories" in data


def test_get_categories():
    db = PayloadDatabase()
    categories = db.get_categories()
    assert len(categories) > 0
    assert "role-hijacking" in categories


def test_get_all_payloads():
    db = PayloadDatabase()
    payloads = db.get_all_payloads()
    assert len(payloads) > 0
    assert all("id" in p for p in payloads)


def test_filter_by_category():
    db = PayloadDatabase()
    payloads = db.filter_by_category("role-hijacking")
    assert len(payloads) > 0
    assert all(p["category_id"] == "role-hijacking" for p in payloads)


def test_filter_by_severity():
    db = PayloadDatabase()
    payloads = db.filter_by_severity("high")
    assert len(payloads) > 0
    assert all(p["severity"] == "high" for p in payloads)


def test_search():
    db = PayloadDatabase()
    payloads = db.search("DAN")
    assert len(payloads) > 0


def test_get_payload_by_id():
    db = PayloadDatabase()
    payload = db.get_payload_by_id("rh-001")
    assert payload is not None
    assert payload["id"] == "rh-001"


def test_get_payload_by_invalid_id():
    db = PayloadDatabase()
    payload = db.get_payload_by_id("invalid-id")
    assert payload is None


def test_get_random_payload():
    db = PayloadDatabase()
    payload = db.get_random_payload()
    assert payload is not None
    assert "id" in payload


def test_get_random_payload_by_category():
    db = PayloadDatabase()
    payload = db.get_random_payload("jailbreak")
    assert payload is not None
    assert payload["category_id"] == "jailbreak"
