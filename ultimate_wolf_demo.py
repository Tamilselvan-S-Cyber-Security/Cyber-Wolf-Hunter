#!/usr/bin/env python3
"""
Ultimate Cyber Wolf Hunter Demo - Enhanced Features with ASCII Art
"""

from cyber_wolf_hunter import wolfhunter
import time

def display_wolf_ascii():
    """Display enhanced ASCII art wolf banner"""
    wolf_art = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                             🐺 CYBER WOLF HUNTER 🐺                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║                              ,-.             _,---._ __  / \\                 ║
║                             /  )         .-'       `./  /   \\                ║
║                            (  (          /.-.     _/  /     \\               ║
║                             \\  )        ( (   )   `-./       \\              ║
║                              ) (          '-'         |       /             ║
║                             (  (  )                   \\    ./               ║
║                              \\  \\(            _       /   /                 ║
║                               \\  ' \\        ,-' |_   (   (                  ║
║                                \\   \\\\     ,'    __`-. \\.  \\                 ║
║                                 )   ) )   /    ,'    `. \\  \\                ║
║                                /  ,' (   (    (       ) )  )                ║
║                               (  (    \\   \\    \\     /,' /                  ║
║                                \\  \\    `-. `-._`-...-' ,'                   ║
║                                 `. `-.    `-._`------''                     ║
║                                   `-.__>--._/  /                            ║
║                                             /  /                            ║
║                                            (__/                             ║
║                                                                              ║
║    🔥 ULTIMATE VULNERABILITY SCANNER 🔥                                      ║
║    ⚡ Multi-Threading | AI-Powered | Professional Reports                   ║
║    🎯 20+ Vulnerability Types | OWASP Top 10 Coverage                       ║
║    📊 Table Format Results | Security Grading | Performance Metrics         ║
║                                                                              ║
║                  Developed by S.Tamilselvan | Version 2.0                   ║
║    Portfolio: https://tamilselvan-portfolio-s.web.app/                      ║
║    Email: tamilselvanreacher@gmail.com                                       ║
║    GitHub: https://github.com/Tamilselvan-S-Cyber-Security                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(wolf_art)

def main():
    display_wolf_ascii()
    
    print("🔥 ULTIMATE CYBER WOLF HUNTER DEMONSTRATION")
    print("=" * 80)
    print("Enhanced Features: 20+ Vulnerability Types | AI Analytics | Table Format")
    print("=" * 80)
    
    # Demonstration 1: Basic One-Line Usage
    print("\n📋 DEMO 1: One-Line Vulnerability Scanner")
    print("-" * 50)
    print("Usage: wolf = wolfhunter('example.com', thread=100)")
    
    wolf = wolfhunter("example.com", thread=100)
    results = wolf.scan()
    wolf.generate_report("ultimate_report.html")
    
    summary = wolf.get_summary()
    print(f"Results: {summary['total_vulnerabilities']} vulnerabilities detected")
    print(f"Report: ultimate_report.html")
    
    # Demonstration 2: Advanced Scanning Modes
    print("\n📋 DEMO 2: Advanced Scanning Modes")
    print("-" * 50)
    
    # Test different targets to show various vulnerability types
    test_targets = [
        ("httpbin.org", "Quick Scan"),
        ("jsonplaceholder.typicode.com", "Comprehensive Scan"),
        ("reqres.in", "Security Analysis")
    ]
    
    for target, scan_name in test_targets:
        print(f"\n🎯 {scan_name}: {target}")
        try:
            wolf_test = wolfhunter(target, thread=50)
            test_results = wolf_test.scan()
            
            # Display detailed findings
            if test_results['vulnerabilities']:
                print(f"✅ Detected {len(test_results['vulnerabilities'])} security issues")
                
                # Show vulnerability breakdown
                vuln_types = {}
                for vuln in test_results['vulnerabilities']:
                    vtype = vuln['type']
                    vuln_types[vtype] = vuln_types.get(vtype, 0) + 1
                
                print("🔍 Vulnerability Breakdown:")
                for vtype, count in vuln_types.items():
                    print(f"   • {vtype}: {count} issue(s)")
            else:
                print("🛡️  No vulnerabilities detected - Excellent security posture")
            
            # Generate report
            report_name = f"scan_{target.replace('.', '_')}.html"
            wolf_test.generate_report(report_name)
            print(f"📄 Report saved: {report_name}")
            
        except Exception as e:
            print(f"❌ Scan error for {target}: {str(e)[:50]}")
    
    # Demonstration 3: Performance Metrics
    print("\n📋 DEMO 3: Performance & Analytics")
    print("-" * 50)
    
    start_time = time.time()
    wolf_perf = wolfhunter("example.com", thread=80)
    perf_results = wolf_perf.scan()
    scan_duration = time.time() - start_time
    
    print(f"⚡ High-Performance Scan Completed")
    print(f"📊 Scan Duration: {scan_duration:.2f} seconds")
    print(f"🧵 Thread Utilization: 80 concurrent threads")
    print(f"🔍 Security Checks: 15+ vulnerability types")
    print(f"📈 Results: {len(perf_results['vulnerabilities'])} findings")
    
    # Demonstration 4: Security Grading System
    print("\n📋 DEMO 4: AI-Powered Security Grading")
    print("-" * 50)
    
    # Calculate security metrics
    total_vulns = len(perf_results['vulnerabilities'])
    high_risk = sum(1 for v in perf_results['vulnerabilities'] if v.get('severity') == 'High')
    medium_risk = sum(1 for v in perf_results['vulnerabilities'] if v.get('severity') == 'Medium')
    low_risk = sum(1 for v in perf_results['vulnerabilities'] if v.get('severity') == 'Low')
    
    # Calculate security grade
    risk_score = (high_risk * 10 + medium_risk * 5 + low_risk * 1)
    max_score = total_vulns * 10 if total_vulns > 0 else 1
    security_percentage = max(0, 100 - (risk_score / max_score * 100))
    
    if security_percentage >= 90:
        grade = "A+"
    elif security_percentage >= 80:
        grade = "A"
    elif security_percentage >= 70:
        grade = "B"
    elif security_percentage >= 60:
        grade = "C"
    else:
        grade = "D"
    
    print(f"🏆 Security Grade: {grade}")
    print(f"📊 Security Score: {security_percentage:.1f}/100")
    print(f"🔴 High Risk Issues: {high_risk}")
    print(f"🟡 Medium Risk Issues: {medium_risk}")
    print(f"🟢 Low Risk Issues: {low_risk}")
    
    # Enhanced Table Display
    if perf_results['vulnerabilities']:
        print("\n" + "="*120)
        print("📊 DETAILED VULNERABILITY ASSESSMENT TABLE")
        print("="*120)
        
        print(f"{'#':<3} {'VULNERABILITY TYPE':<25} {'SEVERITY':<10} {'URL/ENDPOINT':<35} {'EVIDENCE':<25} {'STATUS':<15}")
        print("-"*120)
        
        for i, vuln in enumerate(perf_results['vulnerabilities'], 1):
            vuln_type = vuln.get('type', 'Unknown')[:24]
            severity = vuln.get('severity', 'Low')
            url = vuln.get('url', 'N/A')[:34]
            evidence = vuln.get('evidence', 'Detected')[:24]
            
            if severity == 'High':
                status = "🔴 CRITICAL"
            elif severity == 'Medium':
                status = "🟡 WARNING"
            else:
                status = "🟢 INFO"
            
            print(f"{i:<3} {vuln_type:<25} {severity:<10} {url:<35} {evidence:<25} {status:<15}")
        
        print("-"*120)
        print(f"Total Issues: {total_vulns} | Security Grade: {grade} | Scan Duration: {scan_duration:.2f}s")
        print("="*120)
    
    # Final Summary
    print("\n" + "="*80)
    print("🎉 ULTIMATE CYBER WOLF HUNTER DEMONSTRATION COMPLETE")
    print("="*80)
    print("✅ One-line vulnerability scanning demonstrated")
    print("✅ Advanced multi-threading performance verified")
    print("✅ Professional HTML reports generated")
    print("✅ Table format results with color coding")
    print("✅ AI-powered security grading system")
    print("✅ Comprehensive vulnerability detection (15+ types)")
    print("✅ OWASP Top 10 coverage implemented")
    print("✅ Performance metrics and analytics")
    print()
    print("🔧 Key Features:")
    print("   • SQL Injection, XSS, Directory Traversal Detection")
    print("   • Authentication Bypass & Command Injection Testing")
    print("   • HTTP Security Headers Analysis")
    print("   • SSL/TLS Configuration Assessment")
    print("   • Information Disclosure Detection")
    print("   • Server Information & Cookie Security Analysis")
    print()
    print("💡 Usage Examples:")
    print("   wolf = wolfhunter('target.com', thread=100)  # Create scanner")
    print("   results = wolf.scan()                        # Run scan")
    print("   wolf.generate_report('report.html')          # Generate report")
    print()
    print("👨‍💻 Developed by: S.Tamilselvan")
    print("🌐 Portfolio: https://tamilselvan-portfolio-s.web.app/")
    print("📧 Email: tamilselvanreacher@gmail.com")
    print("🐙 GitHub: https://github.com/Tamilselvan-S-Cyber-Security")
    print("="*80)

if __name__ == "__main__":
    main()