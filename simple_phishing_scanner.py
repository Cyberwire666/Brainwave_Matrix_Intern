import re
import requests
from urllib.parse import urlparse

# ========== SETTINGS ==========
API_KEY = 'AIzaSyB9UidRQWU0psFbrgXKw4VSmBbyepGjBVQ'  # Replace with your actual API key

# ========== MANUAL PHISHING FEATURES ==========
suspicious_keywords = ['login', 'verify', 'update', 'secure', 'account', 'bank', 'signin', 'password', 'confirm']
suspicious_extensions = ['.ru', '.cn', '.xyz', '.top', '.tk', '.pw']
shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 'cutt.ly', 'ow.ly', 't.co', 'shorte.st', 'adf.ly']

# ========== COLORS ==========
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

# ========== URL EXPANDER ==========
def expand_url(url):
    """Expands shortened URLs to their final destination."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.url != url:
            print(f"{Colors.YELLOW}↪ Expanded URL: {response.url}{Colors.RESET}")
        return response.url
    except requests.RequestException:
        return url

# ========== MANUAL CHECK ==========
def manual_check(url):
    reasons = []

    if len(url) > 75:
        reasons.append("Link is too long")
    if any(char in url for char in ['@', '=', '%', '&', '+']):
        reasons.append("Suspicious symbol in URL")
    if any(service in url for service in shorteners):
        reasons.append("Shortened URL (URL shortener detected)")
    if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url):
        reasons.append("IP address used instead of domain")
    if url.startswith('http://'):
        reasons.append("Not using HTTPS")
    if any(url.endswith(ext) or ext in url for ext in suspicious_extensions):
        reasons.append("Suspicious domain extension detected")
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        reasons.append("Suspicious keyword found in URL")

    if reasons:
        return True, reasons
    return False, ["No suspicious patterns detected (manual rules)"]

# ========== GOOGLE SAFE BROWSING ==========
def google_safe_browsing_check(url):
    api_url = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}'
    payload = {
        "client": {"clientId": "phishing-scanner", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    try:
        response = requests.post(api_url, json=payload, timeout=10)
        result = response.json()
        if "matches" in result:
            return True, f"{Colors.RED}⚠️ Google Safe Browsing flagged this URL as dangerous.{Colors.RESET}"
        else:
            return False, f"{Colors.GREEN}✅ This URL is safe (Google Safe Browsing).{Colors.RESET}"
    except Exception as e:
        return False, f"{Colors.YELLOW}⚠️ Error when connecting to Google Safe Browsing: {e}{Colors.RESET}"

# ========== MAIN LOGIC ==========
def main():
    url = input("🔗 Enter the URL to check: ").strip()

    # Expand shortened URLs first
    expanded_url = expand_url(url)
    parsed = urlparse(expanded_url)
    domain = parsed.netloc if parsed.netloc else expanded_url

    print(f"\n{Colors.BOLD}{Colors.CYAN}🔍 Scanning URL:{Colors.RESET} {domain}\n")

    # Manual phishing detection
    manual_result, manual_reasons = manual_check(expanded_url)
    print(f"{Colors.BOLD}--- Manual Check Results ---{Colors.RESET}")
    if manual_result:
        print(f"{Colors.RED}⚠️ Suspicious indicators found:{Colors.RESET}")
        for reason in manual_reasons:
            print(f"   - {Colors.YELLOW}{reason}{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}✅ {manual_reasons[0]}{Colors.RESET}")

    # Google Safe Browsing API check
    print(f"\n{Colors.BOLD}--- Google Safe Browsing Check ---{Colors.RESET}")
    google_result, google_reason = google_safe_browsing_check(expanded_url)
    print(google_reason)

    # Final report
    print(f"\n{Colors.BOLD}{Colors.CYAN}--- Final Report ---{Colors.RESET}")
    if manual_result or google_result:
        print(f"{Colors.RED}❌ This URL is NOT safe! Avoid opening it.{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}✅ This URL appears safe according to all checks.{Colors.RESET}\n")

if __name__ == '__main__':
    main()
