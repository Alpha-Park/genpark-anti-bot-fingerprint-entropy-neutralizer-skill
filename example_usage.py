import json
from client import AntiBotFingerprintEntropyNeutralizer

def main():
    neutralizer = AntiBotFingerprintEntropyNeutralizer()
    current_probe = {
        "navigator_webdriver": True,
        "userAgent": "HeadlessChrome/128.0.0.0",
        "platform": "Linux x86_64"
    }
    result = neutralizer.audit_and_generate_overrides(current_probe, target_platform="windows_chrome")
    print("Fingerprint Neutralization Result:")
    print(json.dumps(result, indent=2))
    assert result["recommended_injections"]["navigator.webdriver"] is False
    assert "RTX 4080" in result["recommended_injections"]["webgl_renderer"]
    print("Anti-bot neutralizer verification: PASS")

if __name__ == "__main__":
    main()
