# Notes

## Adding some data:

    $ python manage.py shell

and:

    from expenses.models import Expense
    o = Expense()
    o.date="2016-11-25"
    o.amount=1.12
    o.title="Gum"
    o.save()
    print(o.id)

    for i in range(10):
        o = Expense(date="2017-02-{:02}".format(i+1), amount=1.2*i, title="expense #123{}".format(i))
        o.save()

## Querying Data

    $ python manage.py shell_plus

and:

    for o in Expense.objects.all():
        print(o.id, o.title, o.amount)
    o = Expense.objects.get(id=6)
    o.amount
