from fastapi import FastAPI
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from configs.environment import get_environment_variables
from configs.graphql import get_graphql_context
from metadata.tags import Tags
from models.base_model import init
from schemas.graphql.mutation import Mutation
from schemas.graphql.query import Query

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)

# Add Routers


# GraphQL Schema and Application Instance
schema = Schema(query=Query, mutation=Mutation)
graphql = GraphQLRouter(
    schema,
    graphiql=env.DEBUG_MODE,
    context_getter=get_graphql_context,
)

# Integrate GraphQL Application to the Core one
app.include_router(
    graphql,
    prefix="/graphql",
    include_in_schema=False,
)

# Initialise Data Model Attributes
init()
