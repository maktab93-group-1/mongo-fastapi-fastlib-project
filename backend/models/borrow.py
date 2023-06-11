from typing import Optional
from datetime import date


class BorrowModel:
    book_id: Optional[str]
    user_id: Optional[str]
    borrowed_at: Optional[date]
    return_date: Optional[date]