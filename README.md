
# Set up


1. Clone locally

        git clone --recurse-submodules -j8 https://github.com/Impact-Africa-Network/ian-content-hub.git

2. Create and activate virtual environment (Use `pipenv`)

        pipenv --python 3.10

        pipenv shell
        
        pipenv install

3. Setup Database and Database User

        psql

        > create database ian_cms;

        > create role ian with password 'ian';

        > alter role ian with login;

        > grant all on database ian_cms to ian;


4. Rename `example.env` to `.env` and populate the values appropriately.

        mv example.env .env
        
        
5. Setup submodules

This Project relies on the following submodules:
        
   `ian_account` - https://github.com/Impact-Africa-Network/ian-account (branch: `feat/ian-cms`)
   
   `ian_auth`   - https://github.com/Impact-Africa-Network/ian_auth.     (branch: `feat/ian-cms`)

        
 i. Initialize submodules
 
        git submodule init
        
 ii. Fetch and update submodules
 
        git submodule update --remote --recursive
        
        
 iii. Check out to the respective branches
 
        cd src/ian_auth
        
        git checkout feat/ian-cms
        
        
        cd src/ian_account
        
        git checkout feat/ian-cms

6. Run migrations

        ./manage.py makemigrations

        ./manage.py migrate