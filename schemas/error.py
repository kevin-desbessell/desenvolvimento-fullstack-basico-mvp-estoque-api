from pydantic import BaseModel, Field


class ErrorSchema(BaseModel):
    """Schema padrão para mensagens de erro retornadas pela API."""
    message: str = Field(
        "Ocorreu um erro na requisição.",
        description="Mensagem descritiva do erro retornado pela API."
    )