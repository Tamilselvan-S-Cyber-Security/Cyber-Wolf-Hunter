#!/usr/bin/env python3
"""
Cyber Wolf Hunter - Example Usage
Comprehensive Website Vulnerability Scanner

Developed by: S.Tamilselvan
Portfolio: https://tamilselvan-portfolio-s.web.app/
Email: tamilselvanreacher@gmail.com
GitHub: https://github.com/Tamilselvan-S-Cyber-Security
"""

from cyber_wolf_hunter import wolfhunter
import sys
import time

def main():
    """
    Example usage of Cyber Wolf Hunter vulnerability scanner
    """
    print("🐺" + "="*60 + "🐺")
    print("          CYBER WOLF HUNTER - EXAMPLE USAGE")
    print("    Comprehensive Website Vulnerability Scanner")
    print("="*64)
    print()
    
    # Example 1: Basic scan with default threads
    print("📋 Example 1: Basic Vulnerability Scan")
    print("-" * 40)
    
    try:
        # Create scanner instance - this is the main interface
        wolf = wolfhunter("httpbin.org", thread=20)
        
        # Perform comprehensive vulnerability scan
        print("🚀 Starting vulnerability assessment...")
        results = wolf.scan()
        
        # Generate HTML report
        print("\n📊 Generating detailed HTML report...")
        report_path = wolf.generate_report("example_report.html")
        
        # Display summary
        summary = wolf.get_summary()
        print("\n" + "="*50)
        print("📈 SCAN SUMMARY")
        print("="*50)
        print(f"🎯 Target: {summary['target']}")
        print(f"🔍 Total Vulnerabilities: {summary['total_vulnerabilities']}")
        print(f"🚨 High Risk: {summary['high_risk']}")
        print(f"⚠️  Medium Risk: {summary['medium_risk']}")
        print(f"ℹ️  Low Risk: {summary['low_risk']}")
        print(f"⏱️  Scan Duration: {summary['scan_duration']} seconds")
        print(f"📄 Report: {report_path}")
        print("="*50)
        
    except Exception as e:
        print(f"❌ Error during scan: {str(e)}")
        return 1
    
    print()
    print("=" * 64)
    
    # Example 2: High-performance scan with maximum threads
    print("📋 Example 2: High-Performance Scan")
    print("-" * 40)
    
    try:
        # High-performance scan with 100 threads
        wolf_fast = wolfhunter("example.com", thread=100)
        
        print("⚡ Starting high-performance scan with 100 threads...")
        start_time = time.time()
        
        # Quick connectivity test
        if not wolf_fast._test_connectivity():
            print("⚠️  Target example.com is not accessible - this is expected for demo")
        else:
            results_fast = wolf_fast.scan()
            report_path_fast = wolf_fast.generate_report("fast_scan_report.html")
            
            print(f"⚡ High-performance scan completed in {time.time() - start_time:.2f} seconds")
            print(f"📄 Report saved to: {report_path_fast}")
        
    except Exception as e:
        print(f"ℹ️  Demo scan (expected): {str(e)}")
    
    print()
    print("=" * 64)
    
    # Example 3: Multiple target scanning
    print("📋 Example 3: Multiple Target Assessment")
    print("-" * 40)
    
    # List of demo targets (some may not be accessible)
    targets = [
        "httpbin.org",
        "jsonplaceholder.typicode.com", 
        "reqres.in"
    ]
    
    for i, target in enumerate(targets, 1):
        print(f"\n🎯 Scanning target {i}/{len(targets)}: {target}")
        try:
            wolf_multi = wolfhunter(target, thread=10)
            
            # Quick scan
            results = wolf_multi.scan()
            summary = wolf_multi.get_summary()
            
            # Generate report with unique filename
            report_filename = f"scan_report_{target.replace('.', '_')}.html"
            wolf_multi.generate_report(report_filename)
            
            print(f"✅ Found {summary['total_vulnerabilities']} vulnerabilities")
            print(f"📄 Report: {report_filename}")
            
        except Exception as e:
            print(f"❌ Scan failed for {target}: {str(e)}")
            continue
    
    print()
    print("=" * 64)
    print("🎉 EXAMPLES COMPLETED SUCCESSFULLY!")
    print()
    print("💡 Key Features Demonstrated:")
    print("   • One-line scanner instantiation")
    print("   • Multi-threaded vulnerability detection")
    print("   • Professional HTML report generation")
    print("   • Comprehensive security assessment")
    print("   • Multiple vulnerability types detection")
    print()
    print("🔧 Advanced Usage Tips:")
    print("   • Adjust thread count based on target capacity")
    print("   • Use lower threads (10-20) for smaller sites")
    print("   • Use higher threads (50-100) for robust targets")
    print("   • Always respect target's robots.txt and terms")
    print()
    print("👨‍💻 Developed by: S.Tamilselvan")
    print("🌐 Portfolio: https://tamilselvan-portfolio-s.web.app/")
    print("📧 Email: tamilselvanreacher@gmail.com")
    print("🐙 GitHub: https://github.com/Tamilselvan-S-Cyber-Security")
    print("🐺" + "="*60 + "🐺")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
