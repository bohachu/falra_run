echo First, you need to modify version at setup.py
rm dist/*.whl
python3 setup.py bdist_wheel
echo bohachu password left_up_four_times_123
python3 -m twine upload dist/*
