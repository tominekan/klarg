# Test normal klarg functions
echo "--------------- Testing Normal Klarg Functions ---------------"
echo ""
echo ""
python3.8 test_klarg.py --some-number 10 --not-number 1a --number-no-args  -n
echo ""
echo ""

# Test klarg.command functions
echo "--------------- Testing klarg.command functions ---------------"
echo ""
echo ""
python3.8 test_klarg_command.py --this-should-not-work test --some-number 10 --not-number 1a --number-no-args  -n
echo ""
echo ""

echo "--------------- End Tests ---------------"
# Remove __pycache__ folder (for some reason, __pycache__ folders deeply annoy me)
rm -rfv __pycache__

# Signal done
echo "Done."