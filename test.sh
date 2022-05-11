# sudo apt-get install python3-venv -y
# python3 -m venv venv

# source venv/bin/activate

# pip3 install -r requirements.txt
# python3 -m pytest --cov --cov-config=.coveragerc --cov-report term-missing --cov-report xml:coverage.xml --junitxml junit.xml

python3 -m venv venv

ls -l

source venv/bin/activate

declare -a directories=("service_1" "service_2" "service_3" "service_4")

for dir in "${directories[@]}"

do

    cd ${dir}

    pip3 install -r testing.txt

    python3 -m pytest --cov=application

    cd ..

done