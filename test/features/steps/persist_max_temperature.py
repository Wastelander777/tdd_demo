from behave import *

from src.data_generator.data_generator import DataGenerator
from src.usecase.persist_max_temperature import PersistMaxTemperature
from src.validator.validator import ValidationError


@given("an invalid input record")
def step_impl(context):
    context.use_case = PersistMaxTemperature()
    context.bad_temperature = "123"
    context.bad_timestamp = 123
    context.exception = None


@when("persisting the maximum temperature")
def step_impl(context):
    try:
        context.use_case.persist(context.bad_timestamp, context.bad_temperature)
    except ValidationError as ve:
        context.exception = ve


@then("it rejects the input as not valid")
def step_impl(context):
    assert isinstance(
        context.exception, ValidationError
    ), f"Expected ValidationError but got {type(context.exception)}"
