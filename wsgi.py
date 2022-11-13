#!/user/bin/env python
from app import create_app, db, models, forms


app = create_app()


@app.shell_context_processor
def get_context():
    return dict(app=app, db=db, m=models, f=forms)


if __name__ == "__main__":
    app.run()
