import db


def main():
    db.base.Base.metadata.create_all(bind=db.engine, checkfirst=True)


if __name__ == "__main__":
    main()
