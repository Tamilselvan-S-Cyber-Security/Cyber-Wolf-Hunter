#!/usr/bin/env python3
"""
Quick demonstration of Cyber Wolf Hunter - One-line vulnerability scanning
"""

from cyber_wolf_hunter import wolfhunter

def main():
    print("Cyber Wolf Hunter - One-Line Vulnerability Scanner")
    print("=" * 60)
    
    # The main interface - just one line to create and use the scanner
    wolf = wolfhunter("httpbin.org", thread=50)
    
    print("Performing comprehensive vulnerability scan...")
    
    # Run the scan
    results = wolf.scan()
    
    # Generate HTML report
    report_path = wolf.generate_report("vulnerability_report.html")
    
    # Get summary
    summary = wolf.get_summary()
    
    print("\nSCAN COMPLETED!")
    print(f"Target: {summary['target']}")
    print(f"Vulnerabilities Found: {summary['total_vulnerabilities']}")
    print(f"High Risk: {summary['high_risk']}")
    print(f"Medium Risk: {summary['medium_risk']}")
    print(f"Low Risk: {summary['low_risk']}")
    print(f"Duration: {summary['scan_duration']} seconds")
    print(f"HTML Report: {report_path}")
    
    return 0

if __name__ == "__main__":
    main()