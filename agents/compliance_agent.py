from schemas.compliance import ComplianceReport

MIN_LENGTH = 50

BANNED_WORDS = [
    "gratis",
    "100% garantizado",
    "sin riesgo"
]


def validate_content(
    instagram_post: str,
    facebook_post: str,
    linkedin_post: str
) -> ComplianceReport:

    feedback = []

    posts = {
        "Instagram": instagram_post,
        "Facebook": facebook_post,
        "LinkedIn": linkedin_post
    }

    for platform, post in posts.items():

        # Check 1: Missing content
        if not post or not post.strip():
            feedback.append(f"{platform} post is missing.")
            continue

        # Check 2: Minimum length
        if len(post.strip()) < MIN_LENGTH:
            feedback.append(
                f"{platform} post is too short "
                f"(minimum {MIN_LENGTH} characters)."
            )

        # Check 3: Restricted words
        lower_post = post.lower()

        for word in BANNED_WORDS:
            if word.lower() in lower_post:
                feedback.append(
                    f"{platform} post contains restricted term: '{word}'."
                )

    return ComplianceReport(
        approved=len(feedback) == 0,
        feedback=feedback
    )