from source.database import connect

import hashlib
import os
import sys


def calculate_hash(migration_name):
    with open(f'migrations/{migration_name}') as file:
        migration_script = file.read()
    return hashlib.md5(migration_script.encode('utf-8')).hexdigest(), migration_script


def create_versioning_table(connection):
    connection.execute(
        '''
        create table if not exists migration (
            name varchar(200) not null primary key,
            hash varchar(50) not null,
            date timestamp
        )
        '''
    )


def get_migrations_executed(connection):
    return (
        connection
        .select('migration')
        .fields('name', 'hash', 'date')
        .order_by('name')
        .execute()
    )


def get_migrations_status(migration_name, migrations_executed):
    pending = False
    if migration_name not in migrations_executed:
        print(f'Script {migration_name} was not executed')
        pending = True
    else:
        migration = migrations_executed[migration_name]
        migration_date = migration.get('date')
        migration_hash, migration_script = calculate_hash(migration_name)
        if migration_hash == migration.get('hash'):
            print(f'Script {migration_name} was run on {migration_date}')
        else:
            print(f'Script {migration_name} was run on {migration_date}, however the file was modified')
            pending = True
    return pending


def information():
    print('python3 database.py migrations_execute | migrations_status')


def migrations_execute():
    migrations_pending = migrations_status()
    if migrations_pending:
        print('Executing pending migrations')
        with connect() as connection:
            migrations_executed = get_migrations_executed(connection)
            migrations_executed = {migration.get('name'): migration for migration in migrations_executed}
            migrations = os.listdir('migrations')
            migrations.sort()
            migrations = [migration for migration in migrations if migration not in migrations_executed]
            migrations_run(connection, migrations)
    else:
        print('Database already updated')


def migrations_run(connection, migrations_pending):
    print('Running migrations')
    for migration_name in migrations_pending:
        print(f'Running: {migration_name}')
        migration_hash, migration_script = calculate_hash(migration_name)
        connection.execute(migration_script, skip_load_query=True)
        (
            connection
            .insert('migration')
            .set('name', migration_name)
            .set('hash', migration_hash)
            .set('date', 'current_timestamp', True)
            .execute()
        )


def migrations_status():
    with connect() as connection:
        create_versioning_table(connection)
        migrations_executed = get_migrations_executed(connection)
        migrations_executed = {migration.get('name'): migration for migration in migrations_executed}
        migrations_names = os.listdir('migrations')
        migrations_names.sort()
        pending = False
        for migration_name in migrations_names:
            pending = get_migrations_status(migration_name, migrations_executed) or pending
    return pending


def main():
    if len(sys.argv) < 2:
        information()
    elif sys.argv[1] == 'migrations_execute':
        migrations_execute()
    elif sys.argv[1] == 'migrations_status':
        migrations_status()
    else:
        information()


if __name__ == '__main__':
    main()
