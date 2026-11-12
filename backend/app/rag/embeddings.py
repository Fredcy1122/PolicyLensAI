import time

from openai import AzureOpenAI, RateLimitError

from app.core.config import settings


client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version=settings.AZURE_OPENAI_API_VERSION,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    max_retries=0,
    timeout=90.0
)

# Each API request processes multiple chunks.
EMBEDDING_BATCH_SIZE = 32
MAX_RATE_LIMIT_RETRIES = 3


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """Generate embeddings in batches with Azure rate-limit handling."""

    if not texts:
        return []

    all_embeddings = []

    for start in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        batch = texts[start:start + EMBEDDING_BATCH_SIZE]

        for attempt in range(MAX_RATE_LIMIT_RETRIES + 1):
            try:
                response = client.embeddings.create(
                    model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
                    input=batch
                )

                ordered = sorted(
                    response.data,
                    key=lambda item: item.index
                )

                all_embeddings.extend(
                    item.embedding for item in ordered
                )

                break

            except RateLimitError as exc:

                if attempt >= MAX_RATE_LIMIT_RETRIES:
                    raise

                # Respect Azure's retry instructions.
                headers = (
                    exc.response.headers
                    if exc.response is not None
                    else {}
                )

                retry_after_ms = headers.get("retry-after-ms")
                retry_after = headers.get("retry-after")

                if retry_after_ms:
                    wait_seconds = float(retry_after_ms) / 1000
                elif retry_after:
                    wait_seconds = float(retry_after)
                else:
                    # Azure's current error message specifies 60 seconds.
                    wait_seconds = 60

                wait_seconds = max(1, min(wait_seconds, 180))

                print(
                    f"Azure embedding rate limit reached. "
                    f"Retrying in {wait_seconds} seconds. "
                    f"Attempt {attempt + 1}/{MAX_RATE_LIMIT_RETRIES}"
                )

                time.sleep(wait_seconds)

    return all_embeddings


def generate_embedding(text: str) -> list[float]:
    """Generate an embedding for a single text."""
    return generate_embeddings([text])[0]
