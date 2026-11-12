import time

from openai import AzureOpenAI, RateLimitError

from app.core.config import settings


client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version=settings.AZURE_OPENAI_API_VERSION,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    # Handle throttling here with short bounded waits instead of the SDK's
    # long automatic retry delays, which can exceed the web worker timeout.
    max_retries=0,
    timeout=90.0
)

EMBEDDING_BATCH_SIZE = 16
MAX_RATE_LIMIT_RETRIES = 4


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """Generate embeddings in batches to reduce Azure API request volume."""
    all_embeddings = []

    for start in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        batch = texts[start:start + EMBEDDING_BATCH_SIZE]

        for attempt in range(MAX_RATE_LIMIT_RETRIES + 1):
            try:
                response = client.embeddings.create(
                    model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
                    input=batch
                )

                # The API returns an index for each input; preserve input order.
                ordered = sorted(response.data, key=lambda item: item.index)
                all_embeddings.extend(item.embedding for item in ordered)
                break

            except RateLimitError:
                if attempt >= MAX_RATE_LIMIT_RETRIES:
                    raise

                # Bounded exponential backoff: 2, 4, 8, then 10 seconds.
                time.sleep(min(2 ** (attempt + 1), 10))

    return all_embeddings


def generate_embedding(text: str) -> list[float]:
    """Backward-compatible single-text helper."""
    return generate_embeddings([text])[0]
