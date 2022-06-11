from behave import *
from unrival_serverless import gen_key, read, create_domain

@given('a public key')
def step_impl(context):
    key = gen_key()
    context.public_key = key

@when('the holder of this public key creates a domain')
def step_impl(context):
    domain = create_domain(
        context.public_key
    )
    context.domain = domain

@then(u'a child of this domain has the name {name}')
def step_impl(context, name):
    raise NotImplementedError(u'STEP: Then the child owner has one entity, the address of which is the public key used to create this domain')


@then(u'{promise} is a promise made by this child')
def step_impl(context, promise):
    name_child_promises = context.name_child.get_promises()
    name_child_promise_strings = map(lambda promise_address: read(promise_address))
    context.name_child = next((child for child in context.children if promise in name_child_promise_strings), None)


@then(u'the child owner has one entity, the address of which is the public key used to create this domain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the child owner has one entity, the address of which is the public key used to create this domain')

@then(u'this domain has no name')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then this domain has no name')


@then(u'this domain has no parents')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then this domain has no parents')



@then(u'"I will keep any promise I make." is a promise made by this domain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "I will keep any promise I make." is a promise made by this domain')


@then(u'"If one of my ancestors makes a promise, then I also make that promise." is a promise made by this domain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "If one of my ancestors makes a promise, then I also make that promise." is a promise made by this domain')

@given(u'a child domain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a child domain')


@given(u'a domain has one stakeholder')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a domain has one stakeholder')
