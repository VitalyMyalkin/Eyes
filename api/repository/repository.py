from sqlalchemy import select
from pydantic import BaseModel, ConfigDict
from datetime import datetime

from Eyes.api.database.database import BaseOrm, async_session_maker

from Eyes.modules.email_modules import duolingo, gravatar, imgur, protonmail, bitmoji, x, github, mailru, ig
from Eyes.lib.maileye import decomp, regex_check


class MailModel(BaseModel):

    id: int
    email: str
    name: str
    domain: str
    protonmail: str
    mailru: str
    duolingo: str
    gravatar: str
    imgur: str
    ig: str
    github: str
    x: str
    bitmoji: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class MailRepository:
    @classmethod
    async def add_mail(cls, email) -> BaseOrm:

        regex_check(email)
        name, domain = decomp(email)

        new_mail = BaseOrm()
        new_mail.email = email
        new_mail.name = name
        new_mail.domain = domain
        new_mail.protonmail = await protonmail.protonmail(email)
        new_mail.mailru = await mailru.mailru(email)
        new_mail.duolingo = await duolingo.duolingo(email)
        new_mail.gravatar = await gravatar.gravatar(email)
        new_mail.imgur = await imgur.imgur(email)
        new_mail.ig = await ig.instagram(email)
        new_mail.github = await github.github(email)
        new_mail.x = await x.x(email)
        new_mail.bitmoji = await bitmoji.bitmoji(email)

        async with async_session_maker() as session:
            session.add(new_mail)
            await session.flush()
            await session.commit()
            return new_mail

    @classmethod
    async def get_mails(cls) -> list[MailModel]:
        async with async_session_maker() as session:
            query = select(BaseOrm)
            result = await session.execute(query)
            data = result.scalars().all()
            mails = [MailModel.model_validate(mail_model) for mail_model in data]
            return mails
