#!/usr/bin/env python3
"""
Final Usage Example - Cyber Wolf Hunter with Enhanced Features
One-line command for comprehensive vulnerability scanning with table results
"""

from cyber_wolf_hunter import wolfhunter

# Simple one-line usage as requested
wolf = wolfhunter("example.com", thread=100)
results = wolf.scan()
wolf.generate_report("security_report.html")

print(f"\nScan Summary: {wolf.get_summary()['total_vulnerabilities']} vulnerabilities found")
print(f"Detailed report saved to: security_report.html")