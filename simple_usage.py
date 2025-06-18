#!/usr/bin/env python3
"""
Simple demonstration of the one-line usage for Cyber Wolf Hunter
"""

from cyber_wolf_hunter import wolfhunter

# One-line vulnerability scanner usage
wolf = wolfhunter("example.com", thread=100)
results = wolf.scan()
wolf.generate_report("report.html")

print(f"Scan completed! Found {wolf.get_summary()['total_vulnerabilities']} vulnerabilities")
print(f"Report saved to: report.html")