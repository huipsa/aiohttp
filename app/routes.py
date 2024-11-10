from aiohttp import web
from app.models import Ad
from app.database import db_session
from app.schemas import AdCreateSchema, AdUpdateSchema, AdResponseSchema
from pydantic import ValidationError


async def create_ad(request):
    try:
        data = await request.json()
        ad_data = AdCreateSchema(**data)
    except ValidationError as e:
        return web.json_response({"error": e.errors()}, status=400)

    new_ad = Ad(
        title=ad_data.title,
        description=ad_data.description,
        owner=ad_data.owner
    )
    db_session.add(new_ad)
    db_session.commit()

    return web.json_response({"message": "Объявление создано", "ad_id": new_ad.id}, status=201)


async def get_ad(request):
    ad_id = request.match_info.get('id')
    ad = db_session.query(Ad).filter(Ad.id == ad_id).first()

    if not ad:
        return web.json_response({"error": "Объявление не найдено"}, status=404)

    ad_response = AdResponseSchema(
        id=ad.id,
        title=ad.title,
        description=ad.description,
        owner=ad.owner,
        created_at=ad.created_at.isoformat()
    )

    return web.json_response(ad_response.dict())


async def update_ad(request):
    ad_id = request.match_info.get('id')
    ad = db_session.query(Ad).filter(Ad.id == ad_id).first()

    if not ad:
        return web.json_response({"error": "Объявление не найдено"}, status=404)

    try:
        data = await request.json()
        update_data = AdUpdateSchema(**data)
    except ValidationError as e:
        return web.json_response({"error": e.errors()}, status=400)

    if update_data.title:
        ad.title = update_data.title
    if update_data.description:
        ad.description = update_data.description

    db_session.commit()

    return web.json_response({"message": "Объявление обновлено"}, status=200)


async def delete_ad(request):
    ad_id = request.match_info.get('id')
    ad = db_session.query(Ad).filter(Ad.id == ad_id).first()

    if not ad:
        return web.json_response({"error": "Объявление не найдено"}, status=404)

    db_session.delete(ad)
    db_session.commit()

    return web.json_response({"message": "Объявление удалено"}, status=200)


def setup_routes(app):
    app.router.add_post('/ads', create_ad)
    app.router.add_get('/ads/{id}', get_ad)
    app.router.add_put('/ads/{id}', update_ad)
    app.router.add_delete('/ads/{id}', delete_ad)
