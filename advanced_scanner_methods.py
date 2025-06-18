"""
Advanced scanner methods extension for Cyber Wolf Hunter
"""

def add_advanced_methods_to_scanner(scanner_class):
    """Add advanced scanning methods to the VulnerabilityScanner class"""
    
    def check_sql_injection_advanced(self, target_url):
        """Advanced SQL injection detection with extended payloads"""
        import urllib.parse
        vulnerabilities = self.check_sql_injection(target_url)
        
        advanced_payloads = [
            "'; WAITFOR DELAY '00:00:05'--",
            "'; SELECT BENCHMARK(5000000,MD5(1))--",
            "' UNION SELECT user,password FROM mysql.user--"
        ]
        
        test_params = ['id', 'user', 'search', 'q', 'username', 'email', 'page']
        
        for param in test_params:
            for payload in advanced_payloads:
                try:
                    test_url = f"{target_url}?{param}={urllib.parse.quote(payload)}"
                    response = self.session.get(test_url, timeout=10)
                    
                    advanced_errors = [
                        'mysql_error', 'Warning: mysql', 'MySQLSyntaxErrorException',
                        'postgresql query failed', 'sqlite error', 'oracle error'
                    ]
                    
                    for error in advanced_errors:
                        if error.lower() in response.text.lower():
                            vulnerabilities.append({
                                'type': 'SQL Injection Advanced',
                                'severity': 'High',
                                'risk_level': 'high',
                                'url': test_url,
                                'payload': payload,
                                'parameter': param,
                                'description': f'Advanced SQL injection detected in {param}',
                                'evidence': error,
                                'recommendation': 'Implement parameterized queries immediately'
                            })
                            break
                            
                except Exception:
                    continue
        
        return vulnerabilities
    
    def check_xss_advanced(self, target_url):
        """Advanced XSS detection"""
        import urllib.parse
        vulnerabilities = self.check_xss(target_url)
        
        advanced_xss = [
            '<svg/onload=alert(/XSS/)>',
            '<img src=x onerror=alert(/XSS/)>',
            '<iframe src="javascript:alert(/XSS/)">',
            '<details open ontoggle=alert(/XSS/)>'
        ]
        
        test_params = ['q', 'search', 'query', 'input', 'comment', 'message', 'name']
        
        for param in test_params:
            for payload in advanced_xss:
                try:
                    test_url = f"{target_url}?{param}={urllib.parse.quote(payload)}"
                    response = self.session.get(test_url, timeout=10)
                    
                    if payload in response.text:
                        vulnerabilities.append({
                            'type': 'XSS Advanced',
                            'severity': 'High',
                            'risk_level': 'high',
                            'url': test_url,
                            'payload': payload,
                            'parameter': param,
                            'description': f'Advanced XSS vulnerability in {param}',
                            'evidence': 'Advanced payload reflected',
                            'recommendation': 'Implement CSP and output encoding'
                        })
                        break
                        
                except Exception:
                    continue
        
        return vulnerabilities
    
    def check_nosql_injection(self, target_url):
        """NoSQL injection detection"""
        import urllib.parse
        vulnerabilities = []
        
        nosql_payloads = [
            '{"$gt":""}',
            '{"$ne":""}',
            '{"$regex":".*"}',
            '[$ne]=1'
        ]
        
        test_params = ['user', 'username', 'email', 'id', 'search']
        
        for param in test_params:
            for payload in nosql_payloads:
                try:
                    test_url = f"{target_url}?{param}={urllib.parse.quote(payload)}"
                    response = self.session.get(test_url, timeout=10)
                    
                    nosql_errors = ['mongodb', 'mongo error', 'bson', 'couchdb', 'nosql']
                    
                    for error in nosql_errors:
                        if error.lower() in response.text.lower():
                            vulnerabilities.append({
                                'type': 'NoSQL Injection',
                                'severity': 'High',
                                'risk_level': 'high',
                                'url': test_url,
                                'payload': payload,
                                'parameter': param,
                                'description': f'NoSQL injection in {param}',
                                'evidence': error,
                                'recommendation': 'Use parameterized NoSQL queries'
                            })
                            break
                            
                except Exception:
                    continue
        
        return vulnerabilities
    
    # Add methods to the class
    scanner_class.check_sql_injection_advanced = check_sql_injection_advanced
    scanner_class.check_xss_advanced = check_xss_advanced
    scanner_class.check_nosql_injection = check_nosql_injection
    
    # Add placeholder methods for compatibility
    scanner_class.check_directory_traversal_advanced = lambda self, url: self.check_directory_traversal(url)
    scanner_class.check_csrf_advanced = lambda self, url: self.check_csrf(url)
    scanner_class.check_info_disclosure_advanced = lambda self, url: self.check_info_disclosure(url)
    scanner_class.check_security_headers_advanced = lambda self, url: self.check_security_headers(url)
    scanner_class.check_ssl_config_advanced = lambda self, url: self.check_ssl_config(url)
    scanner_class.check_directory_enum_advanced = lambda self, url: self.check_directory_enum(url)
    scanner_class.check_file_upload_advanced = lambda self, url: self.check_file_upload(url)
    scanner_class.check_cookie_security_advanced = lambda self, url: self.check_cookie_security(url)
    scanner_class.check_auth_bypass_advanced = lambda self, url: self.check_auth_bypass(url)
    scanner_class.check_command_injection_advanced = lambda self, url: self.check_command_injection(url)
    scanner_class.check_ldap_injection_advanced = lambda self, url: self.check_ldap_injection(url)
    scanner_class.check_xxe_injection = lambda self, url: []
    scanner_class.check_ssrf = lambda self, url: []
    scanner_class.check_deserialization = lambda self, url: []
    scanner_class.check_security_misconfig = lambda self, url: []
    
    return scanner_class