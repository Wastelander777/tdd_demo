from behave import given, then, when

from src.usecase.persist_max_temperature import PersistMaxTemperature


@given("an invalid input record")
def step_impl(context):
    context.use_case = PersistMaxTemperature()


@when("persisting the maximum temperature")
def step_impl(context):
    context.use_case.persist()


@then("it rejects the input as not valid")
def step_impl(context):
    assert isinstance(context.exception, ValidationError
