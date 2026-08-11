import pandas as pd

def get_trade_statistics_df():
    data = {
        "Year": [2023, 2023, 2024, 2024, 2025, 2025, 2026],
        "MEA Category": ["Basel (Plastic)", "Basel (E-Waste)", "Basel (Plastic)", "Montreal (ODS)", "Basel (E-Waste)", "Montreal (ODS)", "Basel (Plastic)"],
        "HS Code": ["3915.10", "8549.21", "3915.90", "2903.42", "8549.39", "2903.77", "3915.20"],
        "Volume (Tonnes)": [42500, 12800, 38900, 4200, 15400, 3900, 18200],
        "Declared Value (USD)": [18200000, 34500000, 15800000, 9800000, 41000000, 8900000, 7800000],
        "Anomaly Risk Score": [78.4, 88.1, 42.0, 91.5, 84.0, 35.2, 82.6],
        "Flagged Action": ["Physical Inspection", "Container Hold", "Cleared", "JAS Confiscation", "Container Hold", "Cleared", "Physical Inspection"]
    }
    return pd.DataFrame(data)

def get_malaysia_port_locations():
    ports = [
        {"port": "Port Klang (Westports/Northport)", "lat": 2.9999, "lon": 101.3928, "state": "Selangor", "risk_level": "High", "anomalies": 142},
        {"port": "Port of Tanjung Pelepas (PTP)", "lat": 1.3620, "lon": 103.5510, "state": "Johor", "risk_level": "Medium", "anomalies": 89},
        {"port": "Penang Port (Butterworth)", "lat": 5.3942, "lon": 100.3664, "state": "Penang", "risk_level": "High", "anomalies": 112},
        {"port": "Kuantan Port", "lat": 3.9733, "lon": 103.4278, "state": "Pahang", "risk_level": "Low", "anomalies": 24},
        {"port": "Bintulu Port", "lat": 3.2538, "lon": 113.0722, "state": "Sarawak", "risk_level": "Medium", "anomalies": 45},
        {"port": "Sepanggar Bay Container Port", "lat": 6.0822, "lon": 116.1264, "state": "Sabah", "risk_level": "Low", "anomalies": 18}
    ]
    return pd.DataFrame(ports)

def get_open_data_news():
    return [
        {
            "date": "2026-06-14",
            "agency": "JKDM / JAS",
            "title": "12 Containers of Contaminated Plastic Scrap Detained at Port Klang",
            "summary": "Customs officers flagged declared 'Polyethylene Flakes' using SENTINEL ML scan. Physical check revealed unsorted municipal plastic waste.",
            "mea": "Basel Convention",
            "hs_code": "3915.10"
        },
        {
            "date": "2026-05-28",
            "agency": "JAS",
            "title": "Illegal Import of Unregistered R-22 ODS Refrigerants Intercepted in Johor",
            "summary": "Chemical analysis verified mislabeled gas cylinders shipped under standard industrial coolant HS codes.",
            "mea": "Montreal Protocol",
            "hs_code": "2903.42"
        },
        {
            "date": "2026-04-10",
            "agency": "PERHILITAN",
            "title": "Seizure of Illegal Rosewood Shipment Attempting Export via Penang Port",
            "summary": "Cross-border trade anomalies flagged timber weight density discrepancies against standard declarations.",
            "mea": "CITES Framework",
            "hs_code": "4403.49"
        }
    ]

def get_faq_items():
    return [
        {
            "q": "What is SENTINEL and who operates it?",
            "a": "SENTINEL is an inter-agency AI trade intelligence engine operated jointly by JKDM, JAS, MITI, and PERHILITAN to detect trade anomalies under international MEA agreements."
        },
        {
            "q": "How does the machine learning inference model detect anomalies?",
            "a": "Models like Isolation Forest examine unit-price-to-weight ratios, declared volume density, origin risk indices, and historical importer profile deviations."
        },
        {
            "q": "Why are some raw .joblib model binaries restricted to Admin view?",
            "a": "To preserve model security, prevent adversarial evasion by illegal trade syndicates, and ensure strict governance over algorithm weights."
        }
    ]