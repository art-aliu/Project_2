#!/bin/bash
# python3 -m venv venv

# ls -l

# source venv/bin/activate

# declare -a directories=("service_1" "service_2" "service_3" "service_4")

# for dir in "${directories[@]}"

# do

#     cd ${dir}

#     pip3 install -r requirements.txt

#     python3 -m pytest --cov=application

#     cd ..

# done

#!/bin/bash
declare -a directories=("service_1" "service_2" "service_3" "service_4")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python3 -m pytest --cov=application --cov-report=xml --junitxml=junit/test-results.xml
  deactivate
  cd ..
done
