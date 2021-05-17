"""FastMSA App Configuration."""

from fastmsa.config import FastMSA


class Config(FastMSA):
    """여기에 변경할 설정을 추가합니다.

    설정 가능한 모든 항목들은 `FastMSA` 클래스 정의를 참고하세요.
    """

    title = "Smartorder"
    allow_external_event = True

    def get_api_port(self) -> int:
        return 5001

    @property
    def uow(self):
        from fastmsa.uow import SqlAlchemyUnitOfWork, RepoMakerDict
        from fastmsa.repo import SqlAlchemyRepository
        from smartorder.domain.aggregates import Product

        repo_maker: RepoMakerDict = {
            Product: lambda session: SqlAlchemyRepository(Product, session)
        }

        return SqlAlchemyUnitOfWork([Product], repo_maker=repo_maker)

    def get_db_url(self) -> str:
        """SqlAlchemy 에서 사용 가능한 형식의 DB URL을 리턴합니다.

        다음처럼 OS 환경변수를 이용할 수도 있씁니다.

        if self.mode == "prod":
            db_host = os.environ.get("DB_HOST", "localhost")
            db_user = os.environ.get("DB_USER", "postgres")
            db_pass = os.environ.get("DB_PASS", "password")
            db_name = os.environ.get("DB_NAME", db_user)
            return f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"
        else:
            return f"sqlite://"
        """
        # TODO: 메모리 DB 대신 실제 DB URL로 변경하세요.
        return "sqlite://"