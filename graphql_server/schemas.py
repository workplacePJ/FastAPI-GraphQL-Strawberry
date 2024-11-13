import strawberry

@strawberry.type
class Task:
    id: int
    content: str
    is_done: bool = False
  
@strawberry.input
class UpdateTaskInput:
    content: str | None = None
    is_done: bool | None = None
  
@strawberry.input
class PaginationInput:
    offset: int
    limit: int
