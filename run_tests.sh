# Test the python program
python3.8 test_klarg.py --some-number 10 --not-number 1a --number-no-args 

# Remove __pycache__ folder (for some reason, __pycache__ folders deeply annoy me)
rm -rfv __pycache__

# Signal done
echo "Done."