from openai import AzureOpenAI

from app.core.config import (
    settings
)

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version=settings.AZURE_OPENAI_API_VERSION,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
)


def generate_embedding(
    text: str
):

    response = client.embeddings.create(
        model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=text
    )

    return (
        response.data[0]
        .embedding
    )