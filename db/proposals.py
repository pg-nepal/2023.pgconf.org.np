import sqlalchemy as sa

from db.base import Base


class Proposals(Base):
    __tablename__ = "proposals"
    __table_args__ = {
        "comment": "listing proposals",
    }

    pk = sa.Column(
        sa.Integer,
        autoincrement=True,
        primary_key=True,
        comment="Primary key of the proposal",
    )

    # Contact Information
    firstname = sa.Column(
        sa.String(256), nullable=True, comment="First name of the person"
    )
    lastname = sa.Column(
        sa.String(256), nullable=True, comment="Last name of the person"
    )
    email = sa.Column(
        sa.String(256), nullable=True, comment="Affiliation of the person"
    )
    job = sa.Column(sa.String(256), nullable=True, comment="Job of the person")
    affiliation = sa.Column(
        sa.String(256), nullable=True, comment="Address of the person"
    )
    country = sa.Column(
        sa.String(256), nullable=True, comment="Country of the person"
        )
    phonenum = sa.Column(
        sa.String(10), nullable=True, comment="Phone number of the person"
    )

    # Session Details
    session_title = sa.Column(
        sa.String(100), nullable=True, comment="Title of the session"
    )
    session_type = sa.Column(
        sa.String(100), nullable=True, comment="Type of the session"
    )
    abstract = sa.Column(
        sa.String(1000), nullable=True, comment="Abstract of the person's session"
    )
    learning_objective = sa.Column(
        sa.String(256), nullable=True, comment="Learning objective for audience"
    )
