# Pillbox Engine

## Initial Setup
If it is the first time you're setting up the app follow these steps

**Install the requirements**

    $: pip install -r requirements.txt

**Setup the database**

    $: python manage.py syncdb
    $: python manage.py migrate

## Run the app

    $: python manage.py runserver


## Sync DailyMed data

To sync all xml headers from DailyMed

    $: python manage.py syncspl products

To sync OSDF information

    $: python manage.py syncspl pills

To sync everything

    $: python manage.py syncspl all
