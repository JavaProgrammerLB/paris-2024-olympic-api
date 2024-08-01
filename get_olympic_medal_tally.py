from datetime import datetime

def get_olympic_athletes(
) -> dict[str, any]:
    return {
        "last_updated": datetime.now().isoformat(),
    }