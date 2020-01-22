echo "Package version updated? (y/n)"
read confirmation

if [ "$confirmation" = "y" ];
then
  python3 setup.py sdist bdist_wheel
  python3 -m twine upload dist/*
else
  echo "\n\033[0;31mPlease update version!\033[0m"
  exit 1
fi