def detect_intent(user_input: str) -> str:
    """
    Detects user intent based on simple keyword matching.
    Returns one of:
    - greeting
    - product_inquiry
    - high_intent
    """

    text = user_input.lower()

    greeting_keywords = ["hi", "hello", "hey", "good morning", "good evening"]
    pricing_keywords = ["price", "pricing", "cost", "plan", "subscription", "features"]
    high_intent_keywords = [
        "sign up",
        "signup",
        "subscribe",
        "start",
        "try",
        "buy",
        "get started",
        "use pro",
        "want to try"
    ]

    if any(word in text for word in greeting_keywords):
        return "greeting"

    if any(word in text for word in high_intent_keywords):
        return "high_intent"

    if any(word in text for word in pricing_keywords):
        return "product_inquiry"

    # Default fallback
    return "product_inquiry"
