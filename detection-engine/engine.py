def analyze_log(log):
    severity = log.get("severity", "info")

    if severity.lower() in ["high", "critical"]:
        return {
            "alert": True,
            "message": "Suspicious activity detected"
        }

    return {
        "alert": False
    }
