from fastapi import APIRouter

from . import search
from . import offers
from . import upsell
from . import rules
from . import verify


router = APIRouter(
    prefix='/content',
    tags=['content']
)

router.include_router(search.router)
router.include_router(offers.router)
# router.include_router(upsell.router)
# router.include_router(rules.router)
# router.include_router(verify.router)
# router.include_router(offers.router)
# router.include_router(offers.router)