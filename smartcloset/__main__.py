from fastmsa.core import FastMsa, AbstractConfig
from fastmsa.api import init_app

class MyConfig(AbstractConfig):
    def get_db_url(self):
        return "sqlite://"

def init_routes(msa: FastMsa, app: FastAPI):
    from smartcloset.routes import clothing

msa = FastMsa(MyConfig()))
init_app(msa, init_routes)
msa.run()
