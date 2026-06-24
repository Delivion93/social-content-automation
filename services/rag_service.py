from pathlib import Path


def load_rules() -> dict:

    return {

        "instagram":
            Path(
                "rag/normas_instagram.txt"
            ).read_text(
                encoding="utf-8"
            ),

        "facebook":
            Path(
                "rag/normas_facebook.txt"
            ).read_text(
                encoding="utf-8"
            ),

        "linkedin":
            Path(
                "rag/normas_linkedin.txt"
            ).read_text(
                encoding="utf-8"
            )
    }